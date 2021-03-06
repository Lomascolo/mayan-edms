from __future__ import unicode_literals

from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from acls import ModelPermission
from acls.permissions import permission_acl_edit, permission_acl_view
from common import (
    MayanAppConfig, menu_facet, menu_main, menu_multi_item, menu_object,
    menu_sidebar
)
from rest_api.classes import APIEndPoint

from .links import (
    link_cabinet_list, link_document_cabinet_list,
    link_document_cabinet_remove, link_cabinet_add_document,
    link_cabinet_add_multiple_documents, link_cabinet_child_add,
    link_cabinet_create, link_cabinet_delete, link_cabinet_edit,
    link_cabinet_view, link_custom_acl_list,
    link_multiple_document_cabinet_remove
)
from .menus import menu_cabinets
from .permissions import (
    permission_cabinet_add_document, permission_cabinet_delete,
    permission_cabinet_edit, permission_cabinet_remove_document,
    permission_cabinet_view
)


class CabinetsApp(MayanAppConfig):
    has_tests = True
    name = 'cabinets'
    verbose_name = _('Cabinets')

    def ready(self):
        super(CabinetsApp, self).ready()

        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )

        DocumentCabinet = self.get_model('DocumentCabinet')
        Cabinet = self.get_model('Cabinet')

        APIEndPoint(app=self, version_string='1')

        Document.add_to_class(
            'document_cabinets',
            lambda document: DocumentCabinet.objects.filter(documents=document)
        )

        ModelPermission.register(
            model=Document, permissions=(
                permission_cabinet_add_document,
                permission_cabinet_remove_document
            )
        )

        ModelPermission.register(
            model=Cabinet, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_cabinet_delete, permission_cabinet_edit,
                permission_cabinet_view
            )
        )

        menu_facet.bind_links(
            links=(link_document_cabinet_list,), sources=(Document,)
        )

        menu_cabinets.bind_links(
            links=(
                link_cabinet_list, link_cabinet_create
            )
        )

        menu_main.bind_links(links=(menu_cabinets,), position=98)

        menu_multi_item.bind_links(
            links=(
                link_cabinet_add_multiple_documents,
                link_multiple_document_cabinet_remove
            ), sources=(Document,)
        )
        menu_object.bind_links(
            links=(
                link_cabinet_view,
            ), sources=(DocumentCabinet, )
        )
        menu_object.bind_links(
            links=(
                link_cabinet_view, link_cabinet_edit,
                link_custom_acl_list, link_cabinet_delete
            ), sources=(Cabinet,)
        )
        menu_sidebar.bind_links(
            links=(link_cabinet_child_add,), sources=(Cabinet,)
        )
        menu_sidebar.bind_links(
            links=(link_cabinet_add_document, link_document_cabinet_remove),
            sources=(
                'cabinets:document_cabinet_list',
                'cabinets:cabinet_add_document',
                'cabinets:document_cabinet_remove'
            )
        )
