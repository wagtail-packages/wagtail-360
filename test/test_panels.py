from django.test import TestCase
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtail_360.panels import PanoramaPanel, ReadOnlyFieldPanel, TourPanel


class TestTourPanel(TestCase):
    def test_tour_panel(self):
        class TestTourPanel(TourPanel):
            pass

        self.assertIsInstance(TestTourPanel(), MultiFieldPanel)

        bound_panel = TestTourPanel().BoundPanel
        self.assertEqual(
            bound_panel.template_name, "wagtail_360/admin/panels/tour_panel.html"
        )
        self.assertEqual(bound_panel.heading, "360 Tour")
        self.assertEqual(
            bound_panel.Media.js, ("wagtail_360/admin/js/parse_url.min.js",)
        )


class TestPanoramaPanel(TestCase):
    def test_panorama_panel(self):
        class TestPanoramaPanel(PanoramaPanel):
            pass

        self.assertIsInstance(TestPanoramaPanel(), MultiFieldPanel)

        bound_panel = TestPanoramaPanel().BoundPanel
        self.assertEqual(
            bound_panel.template_name, "wagtail_360/admin/panels/panorama_panel.html"
        )
        self.assertEqual(
            bound_panel.Media.css,
            {"all": ("wagtail_360/admin/css/panorama_panel.css",)},
        )
        self.assertIn(
            "https://maps.googleapis.com/maps/api/js?key=",
            bound_panel.Media.js[0],
        )
        self.assertIn(
            "wagtail_360/admin/js/street_view.min.js",
            bound_panel.Media.js[1],
        )


class TestReadOnlyFieldPanel(TestCase):
    def test_read_only_field_panel(self):
        read_only_field_panel = ReadOnlyFieldPanel("test_field")
        self.assertIsInstance(read_only_field_panel, FieldPanel)
        self.assertEqual(read_only_field_panel.widget.attrs["readonly"], "readonly")
        self.assertEqual(read_only_field_panel.widget.attrs["placeholder"], "read only")
