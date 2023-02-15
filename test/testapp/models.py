from wagtail.models import Page

from wagtail_360.abstract_models import Panorama, Tour


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["tours"] = TourPage.objects.all()
        return context


class TourPage(Tour):
    subpage_types = ["test_testapp.PanoramaPage"]
    content_panels = Page.content_panels + Tour.content_panels


class PanoramaPage(Panorama):
    parent_page_types = ["test_testapp.TourPage"]
    content_panels = Page.content_panels + Panorama.content_panels

    def serve_preview(self, request, mode_name):
        parent = self.get_parent()
        return parent.serve(request, mode_name)
