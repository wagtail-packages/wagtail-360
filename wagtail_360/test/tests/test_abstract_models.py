from django.test import TestCase

from wagtail_360.abstract_models import Panorama, Tour


class TestAbstractModels(TestCase):
    def test_tour_abstract_models(self):
        # attributes
        with self.assertRaises(AttributeError):
            Tour.parent_page_types
        self.assertTrue(hasattr(Tour, "lat"))
        self.assertTrue(hasattr(Tour, "lng"))
        self.assertTrue(hasattr(Tour, "heading"))
        self.assertTrue(hasattr(Tour, "elevation"))
        self.assertTrue(hasattr(Tour, "zoom_level"))

        # methods
        self.assertTrue(callable(Tour.initial_panorama_data))
        self.assertTrue(callable(Tour.get_context))
        self.assertTrue(callable(Tour.get_panoramas))

        # meta
        self.assertEqual(Tour._meta.abstract, True)
        self.assertEqual(Tour._meta.verbose_name, "Tour")
        self.assertEqual(Tour._meta.verbose_name_plural, "Tours")

    def test_panorama_abstract_models(self):
        # attributes
        self.assertTrue(Panorama.parent_page_types == [])
        self.assertTrue(hasattr(Panorama, "panorama_id"))
        self.assertTrue(hasattr(Panorama, "lat"))
        self.assertTrue(hasattr(Panorama, "lng"))
        self.assertTrue(hasattr(Panorama, "heading"))
        self.assertTrue(hasattr(Panorama, "elevation"))
        self.assertTrue(hasattr(Panorama, "zoom_level"))
        self.assertTrue(hasattr(Panorama, "body"))

        # methods
        self.assertTrue(callable(Panorama.serve))
