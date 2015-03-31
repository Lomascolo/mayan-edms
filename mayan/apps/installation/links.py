from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from .permissions import PERMISSION_INSTALLATION_DETAILS

link_menu_link = {'text': _('Installation details'), 'view': 'installation:namespace_list', 'icon': 'fa fa-flag', 'permissions': [PERMISSION_INSTALLATION_DETAILS]}
link_namespace_list = {'text': _('Installation property namespaces'), 'view': 'installation:namespace_list', 'famfam': 'layout', 'permissions': [PERMISSION_INSTALLATION_DETAILS]}
link_namespace_details = {'text': _('Details'), 'view': 'installation:namespace_details', 'args': 'object.id', 'famfam': 'layout_link', 'permissions': [PERMISSION_INSTALLATION_DETAILS]}
