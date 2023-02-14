from wagtail.models import Page

from wagtail_360.abstract_models import Panorama, Tour


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["tours"] = TourPage.objects.all()
        return context


class TourPage(Tour, Page):
    subpage_types = ["test_testapp.PanoramaPage"]
    content_panels = Page.content_panels + Tour.content_panels


class PanoramaPage(Panorama, Page):
    parent_page_types = ["test_testapp.TourPage"]
    content_panels = Page.content_panels + Panorama.content_panels
