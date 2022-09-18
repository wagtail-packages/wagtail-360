from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect
from wagtail.admin.panels import FieldPanel, FieldRowPanel, HelpPanel
from wagtail.models import Page
from wagtail.core.fields import RichTextField

from .forms import PanoramaForm
from .panels import PanoramaPanel, TourPanel, ReadOnlyFieldPanel


def google_street_view_api_key():
    if hasattr(settings, "GOOGLE_STREET_VIEW_API_KEY"):
        return settings.GOOGLE_STREET_VIEW_API_KEY
    return ""


class Tour(Page):
    maps_url = models.TextField(
        help_text="Copy a Google Maps Street View URL and paste it here. It's values will be used as a starting point for the first panorama.",
        verbose_name="Google Maps Street View URL",
    )
    lat = models.FloatField(verbose_name="Latitude")
    lng = models.FloatField(verbose_name="Longitude")
    heading = models.FloatField(verbose_name="Direction/Rotation")
    elevation = models.FloatField(verbose_name="Elevation/Pitch")
    zoom_level = models.FloatField(verbose_name="Zoom In/Out")

    panels = TourPanel(
        [
            FieldPanel("maps_url"),
            FieldRowPanel(
                [
                    ReadOnlyFieldPanel("lat"),
                    ReadOnlyFieldPanel("lng"),
                ],
            ),
            FieldRowPanel(
                [
                    ReadOnlyFieldPanel("heading"),
                    ReadOnlyFieldPanel("elevation"),
                    ReadOnlyFieldPanel("zoom_level"),
                ],
            ),
        ],
        heading="Generate Initial Panorama Data",
    )

    def get_panoramas(self):
        return self.get_children().specific().all()

    def get_context(self, request, *args, **kwargs):
        context = super(Tour, self).get_context(request, *args, **kwargs)
        context["panoramas"] = self.get_panoramas()
        context["api_key"] = google_street_view_api_key()
        return context

    class Meta:
        abstract = True


class Panorama(Page):
    panorama_id = models.CharField(
        max_length=255,
    )
    lat = models.FloatField(verbose_name="Latitude")
    lng = models.FloatField(verbose_name="Longitude")
    heading = models.FloatField(verbose_name="Direction/Rotation")
    elevation = models.FloatField(verbose_name="Elevation/Pitch")
    zoom_level = models.FloatField(verbose_name="Zoom In/Out")
    body = RichTextField(blank=True)

    base_form_class = PanoramaForm

    class Meta:
        abstract = True

    # needs to be implemented in a child class
    parent_page_types = []

    template = "wagtail_360/panorama_page.html"

    preview_modes = []

    panels = [
        PanoramaPanel(
            [
                HelpPanel("""initial data is taken from last tour panorama"""),
                ReadOnlyFieldPanel("panorama_id"),
                FieldRowPanel(
                    [
                        ReadOnlyFieldPanel("lat"),
                        ReadOnlyFieldPanel("lng"),
                    ]
                ),
                FieldRowPanel(
                    [
                        ReadOnlyFieldPanel("heading"),
                        ReadOnlyFieldPanel("elevation"),
                        ReadOnlyFieldPanel("zoom_level"),
                    ]
                ),
            ],
            heading="Choose and position a panorama.",
        ),
        FieldPanel("body"),
    ]

    # def get_context(self, request, *args, **kwargs):
    # context = super(Panorama, self).get_context(request, *args, **kwargs)
    # context["panorama_title"] = self.title
    # context["panorama_id"] = self.panorama_id
    # context["lat"] = self.lat
    # context["lng"] = self.lng
    # context["heading"] = self.heading
    # context["elevation"] = self.elevation
    # context["zoom_level"] = self.zoom_level
    # return context

    def serve(self, *args, **kwargs):
        # redirect to the parent page
        return HttpResponseRedirect(
            self.get_parent().get_url() + "?panorama=" + self.panorama_id
        )
