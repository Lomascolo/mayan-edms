from __future__ import unicode_literals

from django.test import TestCase

from ..models import Organization

from .literals import TEST_ORGANIZATION_LABEL, TEST_ORGANIZATION_EDITED_LABEL


class OrganizationTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(
            label=TEST_ORGANIZATION_LABEL
        )

    def test_basic(self):
        queryset = Organization.objects.get_for_now()

        self.assertEqual(queryset.exists(), True)