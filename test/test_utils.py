from django.test import TestCase, override_settings

from wagtail_360.utils import google_maps_api_key


class TestMethods(TestCase):
    def test_google_maps_api_key(self):
        self.assertEqual(google_maps_api_key(), "")

    @override_settings(GOOGLE_MAPS_API_KEY="test")
    def test_google_maps_api_key_with_setting(self):
        self.assertEqual(google_maps_api_key(), "test")
