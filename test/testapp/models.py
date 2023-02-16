from wagtail.models import Page

from wagtail_360.abstract_models import AbstractPanorama, AbstractTour


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["tours"] = TourPage.objects.all()
        return context


class TourPage(AbstractTour, Page):
    subpage_types = ["test_testapp.PanoramaPage"]
    content_panels = Page.content_panels + AbstractTour.panels

    def get_context(self, request, *args, **kwargs):
        context = super(AbstractTour, self).get_context(request, *args, **kwargs)
        context["panoramas"] = self.get_panoramas()
        context["api_key"] = self.get_maps_api_key()
        return context


class PanoramaPage(AbstractPanorama, Page):
    parent_page_types = ["test_testapp.TourPage"]
    content_panels = Page.content_panels + AbstractPanorama.panels

    def serve_preview(self, request, mode_name):
        parent = self.get_parent()
        return parent.serve(request, mode_name)
