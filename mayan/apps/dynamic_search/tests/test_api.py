from __future__ import unicode_literals

from json import loads

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import override_settings

from documents.models import DocumentType
from documents.search import document_search
from documents.tests import TEST_DOCUMENT_TYPE, TEST_SMALL_DOCUMENT_PATH
from rest_api.tests import BaseAPITestCase
from user_management.tests import (
    TEST_ADMIN_EMAIL, TEST_ADMIN_PASSWORD, TEST_ADMIN_USERNAME
)


@override_settings(OCR_AUTO_OCR=False)
class SearchAPITestCase(BaseAPITestCase):
    def setUp(self):
        super(SearchAPITestCase, self).setUp()

        self.admin_user = get_user_model().objects.create_superuser(
            username=TEST_ADMIN_USERNAME, email=TEST_ADMIN_EMAIL,
            password=TEST_ADMIN_PASSWORD
        )

        self.client.login(
            username=TEST_ADMIN_USERNAME, password=TEST_ADMIN_PASSWORD
        )

    def test_search(self):
        document_type = DocumentType.objects.create(
            label=TEST_DOCUMENT_TYPE
        )

        with open(TEST_SMALL_DOCUMENT_PATH) as file_object:
            document = document_type.new_document(
                file_object=file_object,
            )

        response = self.client.get(
            '{}?q={}'.format(
                reverse(
                    'rest_api:search-view', args=(
                        document_search.get_full_name(),
                    )
                ), document.label
            )
        )

        content = loads(response.content)
        self.assertEqual(content['results'][0]['label'], document.label)
        self.assertEqual(content['count'], 1)
