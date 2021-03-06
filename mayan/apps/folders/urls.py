from __future__ import unicode_literals

from django.conf.urls import url

from .api_views import (
    APIDocumentFolderListView, APIFolderDocumentListView,
    APIFolderDocumentView, APIFolderListView, APIFolderView
)
from .views import (
    DocumentAddToFolderView, DocumentFolderListView,
    DocumentRemoveFromFolderView, FolderCreateView, FolderDeleteView,
    FolderDetailView, FolderEditView, FolderListView,
)

urlpatterns = [
    url(r'^list/$', FolderListView.as_view(), name='folder_list'),
    url(r'^create/$', FolderCreateView.as_view(), name='folder_create'),
    url(r'^(?P<pk>\d+)/edit/$', FolderEditView.as_view(), name='folder_edit'),
    url(
        r'^(?P<pk>\d+)/delete/$', FolderDeleteView.as_view(),
        name='folder_delete'
    ),
    url(r'^(?P<pk>\d+)/$', FolderDetailView.as_view(), name='folder_view'),

    url(
        r'^document/(?P<pk>\d+)/folder/add/$',
        DocumentAddToFolderView.as_view(), name='folder_add_document'
    ),
    url(
        r'^document/multiple/folder/add/$', DocumentAddToFolderView.as_view(),
        name='folder_add_multiple_documents'
    ),
    url(
        r'^document/(?P<pk>\d+)/folder/remove/$',
        DocumentRemoveFromFolderView.as_view(), name='document_folder_remove'
    ),
    url(
        r'^document/multiple/folder/remove/$',
        DocumentRemoveFromFolderView.as_view(),
        name='multiple_document_folder_remove'
    ),
    url(
        r'^document/(?P<pk>\d+)/folder/list/$',
        DocumentFolderListView.as_view(), name='document_folder_list'
    ),
]

api_urls = [
    url(
        r'^folders/(?P<folder_pk>[0-9]+)/documents/(?P<pk>[0-9]+)/$',
        APIFolderDocumentView.as_view(), name='folder-document'
    ),
    url(
        r'^folders/(?P<pk>[0-9]+)/documents/$',
        APIFolderDocumentListView.as_view(), name='folder-document-list'
    ),
    url(
        r'^folders/(?P<pk>[0-9]+)/$', APIFolderView.as_view(),
        name='folder-detail'
    ),
    url(r'^folders/$', APIFolderListView.as_view(), name='folder-list'),
    url(
        r'^document/(?P<pk>[0-9]+)/folders/$',
        APIDocumentFolderListView.as_view(), name='document-folder-list'
    ),
]
