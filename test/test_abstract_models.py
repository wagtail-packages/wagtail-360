from django.test import TestCase

from wagtail_360.abstract_models import AbstractPanorama, AbstractTour


class TestAbstractModels(TestCase):
    def test_abstract_models(self):
        # attributes
        with self.assertRaises(AttributeError):
            AbstractTour.parent_page_types
        self.assertTrue(hasattr(AbstractTour, "lat"))
        self.assertTrue(hasattr(AbstractTour, "lng"))
        self.assertTrue(hasattr(AbstractTour, "heading"))
        self.assertTrue(hasattr(AbstractTour, "elevation"))
        self.assertTrue(hasattr(AbstractTour, "zoom_level"))

        # methods
        self.assertTrue(callable(AbstractTour.initial_panorama_data))
        self.assertTrue(callable(AbstractTour.get_panoramas))

        # meta
        self.assertEqual(AbstractTour._meta.abstract, True)
        self.assertEqual(AbstractTour._meta.verbose_name, "AbstractTour")
        self.assertEqual(AbstractTour._meta.verbose_name_plural, "AbstractTours")

    def test_panorama_abstract_models(self):
        # attributes
        self.assertTrue(hasattr(AbstractPanorama, "panorama_id"))
        self.assertTrue(hasattr(AbstractPanorama, "lat"))
        self.assertTrue(hasattr(AbstractPanorama, "lng"))
        self.assertTrue(hasattr(AbstractPanorama, "heading"))
        self.assertTrue(hasattr(AbstractPanorama, "elevation"))
        self.assertTrue(hasattr(AbstractPanorama, "zoom_level"))
        self.assertTrue(hasattr(AbstractPanorama, "body"))

        # methods
        self.assertTrue(callable(AbstractPanorama.serve))
