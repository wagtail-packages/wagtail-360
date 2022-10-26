from django.test import TestCase

from wagtail_360.forms import PanoramaForm
from wagtail_360.test.factories import test_page_factory
from wagtail_360.test.models import PanoramaPage, TourPage


class TestForms(TestCase):
    def setUp(self):
        self.home_page, self.tour_page, self.panorama_page = test_page_factory()

    def test_panorama_form(self):
        # existing page
        form = self.panorama_page.get_edit_handler().get_form_class()(
            instance=self.panorama_page
        )
        self.assertIsInstance(form, PanoramaForm)
        self.assertEqual(form.initial["lat"], 50)
        self.assertEqual(form.initial["lng"], 60)
        self.assertEqual(form.initial["heading"], 70)
        self.assertEqual(form.initial["elevation"], 80)
        self.assertEqual(form.initial["zoom_level"], 3)
        self.assertEqual(form.initial["panorama_id"], "1")

        # new tour page
        tour = TourPage(
            title="Tour",
            maps_url="https://www.example.com/maps/place/1+Main+St,+New+York,+",
            lat=123,
            lng=-456,
            heading=789,
            elevation=0,
            zoom_level=1,
        )
        self.home_page.add_child(instance=tour)
        tour.save_revision().publish()

        # new panorama page, no child pages
        panorama = PanoramaPage(
            title="Panorama Page",
            panorama_id="2",  # set by javascript
        )
        form = self.panorama_page.get_edit_handler().get_form_class()(
            instance=panorama, parent_page=tour
        )
        # should inherit from parent
        self.assertIsInstance(form, PanoramaForm)
        self.assertEqual(form.initial["lat"], 123)
        self.assertEqual(form.initial["lng"], -456)
        self.assertEqual(form.initial["heading"], 789)
        self.assertEqual(form.initial["elevation"], 0)
        self.assertEqual(form.initial["zoom_level"], 1)

        # save with expected values
        panorama.lat = 123
        panorama.lng = -456
        panorama.heading = 789
        panorama.elevation = 0
        panorama.zoom_level = 1
        tour.add_child(instance=panorama)
        panorama.save_revision().publish()

        # update the panorama page values
        panorama.lat = 123123
        panorama.lng = -456456
        panorama.heading = 789789
        panorama.elevation = 2
        panorama.zoom_level = 3

        panorama.save_revision().publish()

        # new panorama page, with sibling pages
        panorama_2 = PanoramaPage(
            title="Panorama Page 2",
            panorama_id="3",  # set by javascript
        )

        form = self.panorama_page.get_edit_handler().get_form_class()(
            instance=panorama_2, parent_page=tour
        )
        # should inherit from last sibling (panorama)
        self.assertIsInstance(form, PanoramaForm)
        self.assertEqual(form.initial["lat"], 123123)
        self.assertEqual(form.initial["lng"], -456456)
        self.assertEqual(form.initial["heading"], 789789)
        self.assertEqual(form.initial["elevation"], 2)
        self.assertEqual(form.initial["zoom_level"], 3)
