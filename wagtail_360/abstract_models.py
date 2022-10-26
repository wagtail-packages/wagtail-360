from django.db import models
from django.http import HttpResponseRedirect
from wagtail.admin.panels import FieldPanel, FieldRowPanel, HelpPanel
from wagtail.core.fields import RichTextField
from wagtail.models import Page

from wagtail_360.forms import PanoramaForm
from wagtail_360.utils import google_maps_api_key

from .panels import PanoramaPanel, ReadOnlyFieldPanel, TourPanel


class BaseTour(models.Model):
    maps_url = models.TextField(
        help_text="""Copy a Google Maps Street View URL and paste it here.
        It's values will be used as a starting point for the first panorama.""",
        verbose_name="Google Maps Street View URL",
    )
    lat = models.FloatField(verbose_name="Latitude")
    lng = models.FloatField(verbose_name="Longitude")
    heading = models.FloatField(verbose_name="Direction/Rotation")
    elevation = models.FloatField(verbose_name="Elevation/Pitch")
    zoom_level = models.FloatField(verbose_name="Zoom In/Out")

    class Meta:
        abstract = True


class Tour(BaseTour, Page):
    class Meta:
        abstract = True
        verbose_name = "Tour"
        verbose_name_plural = "Tours"

    content_panels = [
        TourPanel(
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
    ]

    def get_panoramas(self):
        return self.get_children().specific().all()

    def get_context(self, request, *args, **kwargs):
        context = super(Tour, self).get_context(request, *args, **kwargs)
        context["panoramas"] = self.get_panoramas()
        context["api_key"] = google_maps_api_key()
        return context

    def initial_panorama_data(self):
        data = {}
        last_child_page = self.get_children().specific().last()
        if last_child_page:
            data["lat"] = last_child_page.lat
            data["lng"] = last_child_page.lng
            data["heading"] = last_child_page.heading
            data["elevation"] = last_child_page.elevation
            data["zoom_level"] = last_child_page.zoom_level
        else:
            data["lat"] = self.lat
            data["lng"] = self.lng
            data["heading"] = self.heading
            data["elevation"] = self.elevation
            data["zoom_level"] = self.zoom_level

        return data


class BasePanorama(models.Model):
    panorama_id = models.CharField(max_length=255)
    lat = models.FloatField(verbose_name="Latitude")
    lng = models.FloatField(verbose_name="Longitude")
    heading = models.FloatField(verbose_name="Direction/Rotation")
    elevation = models.FloatField(verbose_name="Elevation/Pitch")
    zoom_level = models.FloatField(verbose_name="Zoom In/Out")
    body = RichTextField(blank=True)

    class Meta:
        abstract = True


class Panorama(BasePanorama, Page):
    class Meta:
        abstract = True
        verbose_name = "Panorama"
        verbose_name_plural = "Panoramas"

    parent_page_types = [
        # intentionally left blank
        # to remind you to set this in your own models
        # e.g. parent_page_types = ["test.TourPage"]
    ]

    base_form_class = PanoramaForm

    content_panels = [
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

    def serve(self, *args, **kwargs):
        # redirect to the parent page, setting the panorama_id in the url
        return HttpResponseRedirect(
            self.get_parent().get_url() + "?panorama=" + self.panorama_id
        )
