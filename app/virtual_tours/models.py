from wagtail.models import Page

from wagtail_360.models import Panorama, Tour


class TourPage(Tour):
    subpage_types = ["virtual_tours.PanoramaPage"]
    content_panels = Page.content_panels + [Tour.panels]

    template = "wagtail_360/tour_page.html"


class PanoramaPage(Panorama):
    parent_page_types = ["virtual_tours.TourPage"]
    content_panels = Page.content_panels + Panorama.panels
