from __future__ import unicode_literals

from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from acls import ModelPermission
from acls.links import link_acl_list
from acls.permissions import permission_acl_edit, permission_acl_view
from common import (
    MayanAppConfig, menu_facet, menu_main, menu_object, menu_sidebar,
    menu_multi_item
)
from navigation import SourceColumn
from rest_api.classes import APIEndPoint

from .links import (
    link_folder_list, link_document_folder_list, link_document_folder_remove,
    link_folder_add_document, link_folder_add_multiple_documents,
    link_folder_create, link_folder_delete,
    link_folder_edit, link_folder_view, link_multiple_document_folder_remove
)
from .menus import menu_folders
from .permissions import (
    permission_folder_add_document, permission_folder_delete,
    permission_folder_edit, permission_folder_remove_document,
    permission_folder_view
)


class FoldersApp(MayanAppConfig):
    has_tests = True
    name = 'folders'
    verbose_name = _('Folders')

    def ready(self):
        super(FoldersApp, self).ready()

        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )

        DocumentFolder = self.get_model('DocumentFolder')
        Folder = self.get_model('Folder')

        APIEndPoint(app=self, version_string='1')

        Document.add_to_class(
            'document_folders',
            lambda document: DocumentFolder.objects.filter(documents=document)
        )

        ModelPermission.register(
            model=Document, permissions=(
                permission_folder_add_document,
                permission_folder_remove_document
            )
        )

        ModelPermission.register(
            model=Folder, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_folder_delete, permission_folder_edit,
                permission_folder_view
            )
        )

        SourceColumn(
            source=Folder, label=_('Created'), attribute='datetime_created'
        )
        SourceColumn(
            source=Folder, label=_('Documents'),
            func=lambda context: context['object'].get_document_count(
                user=context['request'].user
            )
        )

        menu_facet.bind_links(
            links=(link_document_folder_list,), sources=(Document,)
        )

        menu_folders.bind_links(
            links=(
                link_folder_list, link_folder_create
            )
        )

        menu_main.bind_links(links=(menu_folders,), position=98)
        menu_multi_item.bind_links(
            links=(
                link_folder_add_multiple_documents,
                link_multiple_document_folder_remove
            ), sources=(Document,)
        )
        menu_object.bind_links(
            links=(
                link_folder_view,
            ), sources=(DocumentFolder, )
        )
        menu_object.bind_links(
            links=(
                link_folder_view, link_folder_edit, link_acl_list,
                link_folder_delete
            ), sources=(Folder,)
        )
        menu_sidebar.bind_links(
            links=(link_folder_add_document, link_document_folder_remove),
            sources=(
                'folders:document_folder_list', 'folders:folder_add_document',
                'folders:document_folder_remove'
            )
        )
