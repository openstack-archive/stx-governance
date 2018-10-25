#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Report on the current list of projects"""

import copy
from docutils import nodes
from docutils.parsers import rst
from docutils import statemachine
import os
from sphinx.util import logging
from sphinx.util.nodes import nested_parse_with_titles
import yaml
import yamlordereddictloader


LOG = logging.getLogger(__name__)

IRC_LOG_URL_BASE = 'http://eavesdrop.openstack.org/irclogs/%23'

_projects_yaml = {}


def _get_project_data():
    """Return a copy of the project data."""
    return copy.deepcopy(_projects_yaml)


def _load_project_file(filename='reference/tsc/projects.yaml'):
    with open(filename, 'r', encoding='utf-8') as f:
        return yaml.load(
            f.read(),
            Loader=yamlordereddictloader.Loader,
        )


def _project_to_rst(name, info):

    if 'service' in info:
        title = "{0} ({1})".format(name.title(), info['service'])
    elif name == 'I18n':
        title = name
    else:
        title = name.title()

    yield '.. _project-%s:' % _slugify(name)
    yield ''
    yield '=' * len(title)
    yield title
    yield '=' * len(title)
    yield ''
    yield ':Home Page: ' + info.get('url', '')
    tl = info.get('tl', {'name': '', 'irc': '', 'email': ''})
    yield ':Technical Lead: %(name)s (``%(irc)s``) <%(email)s>' % tl
    pl = info.get('pl', {'name': '', 'irc': '', 'email': ''})
    yield ':Project Lead: %(name)s (``%(irc)s``) <%(email)s>' % pl
    irc_channel = info.get('irc-channel')
    if irc_channel:
        yield ':IRC Channel: `#%s <%s%s>`__' % (
            irc_channel, IRC_LOG_URL_BASE, irc_channel)
    service = info.get('service')
    if service:
        yield ':Service: ' + service
    yield ''
    mission = info.get('mission', '').rstrip()
    if mission:
        yield "Mission"
        yield '-------'
        yield ''
        yield mission
        yield ''
    yield 'Deliverables'
    yield '------------'
    yield ''
    deliverables = info.get('deliverables', [])
    if deliverables:
        for repo_name, deliverable in deliverables.items():
            yield repo_name
            yield '~' * len(repo_name)
            yield ''
            yield ':Repositories: ' + ', '.join(
                ':repo:`%s`' % repo
                for repo in deliverable.get('repos', [])
            )
            yield ''
            tags = deliverable.get('tags', [])
            if tags:
                yield ':Tags:'
                yield ''
                for tag in tags:
                    yield '  - :ref:`tag-%s`' % tag
                yield ''
    else:
        yield 'None'
    yield ''


def _slugify(name):
    """Convert name to slug form for references."""
    return name.lower().replace(' ', '-')


def _write_project_pages(app):
    all_projects = _get_project_data()
    files = []
    for project, info in all_projects.items():
        LOG.info("project: %s" % project)
        slug = _slugify(project)
        filename = 'reference/tsc/projects/%s.rst' % slug
        LOG.info('generating project page for %s' % project)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(_project_to_rst(project, info)))
        files.append(filename)
    return files


class ProjectListDirective(rst.Directive):

    has_content = False

    def run(self):
        all_projects = _get_project_data()

        # Build the view of the data to be parsed for rendering.
        result = statemachine.ViewList()
        for project_name in sorted(all_projects.keys()):
            project_info = all_projects[project_name]
            for line in _project_to_rst(project_name, project_info):
                result.append(line, '<' + __name__ + '>')

        # Parse what we have into a new section.
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


def setup(app):
    global _projects_yaml

    LOG.info('loading projects extension')
    app.add_directive('projectlist', ProjectListDirective)

    filename = os.path.abspath('reference/tsc/projects.yaml')
    LOG.info('reading %s' % filename)
    _projects_yaml = _load_project_file(filename)
    _write_project_pages(app)
