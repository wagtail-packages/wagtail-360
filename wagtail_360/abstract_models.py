from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect
from wagtail.admin.panels import FieldPanel, FieldRowPanel, HelpPanel
from wagtail.fields import RichTextField

from wagtail_360.forms import PanoramaForm

from .panels import PanoramaPanel, ReadOnlyFieldPanel, TourPanel


class AbstractTour(models.Model):
    class Meta:
        abstract = True
        verbose_name = "AbstractTour"
        verbose_name_plural = "AbstractTours"

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

    panels = [
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

    def is_previewable(self):
        return self.get_panoramas().exists()

    def get_panoramas(self):
        return self.get_children().specific().all()

    @staticmethod
    def get_maps_api_key():
        if hasattr(settings, "GOOGLE_MAPS_API_KEY"):
            return settings.GOOGLE_MAPS_API_KEY
        return ""

    def initial_panorama_data(self):
        """
        Get the initial data for the panorama. It needs to start somewhere.

        Returns:
            dict: A dictionary of initial data for the tour page or the last panorama created.
        """
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


class AbstractPanorama(models.Model):
    class Meta:
        abstract = True
        verbose_name = "AbstractPanorama"
        verbose_name_plural = "AbstractPanoramas"

    panorama_id = models.CharField(max_length=255)
    lat = models.FloatField(verbose_name="Latitude")
    lng = models.FloatField(verbose_name="Longitude")
    heading = models.FloatField(verbose_name="Direction/Rotation")
    elevation = models.FloatField(verbose_name="Elevation/Pitch")
    zoom_level = models.FloatField(verbose_name="Zoom In/Out")
    body = RichTextField(blank=True)

    base_form_class = PanoramaForm

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

    def is_previewable(self):
        return False

    def serve(self, *args, **kwargs):
        # redirect to the parent page, setting the panorama_id in the url
        return HttpResponseRedirect(
            self.get_parent().get_url() + "?panorama=" + self.panorama_id
        )
