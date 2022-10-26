from django import forms
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from wagtail_360.utils import google_maps_api_key


class TourPanel(MultiFieldPanel):
    class BoundPanel(MultiFieldPanel.BoundPanel):
        template_name = "wagtail_360/admin/panels/tour_panel.html"
        heading = "360 Tour"

        class Media:
            js = ("wagtail_360/admin/js/parse_url.min.js",)


class PanoramaPanel(MultiFieldPanel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class BoundPanel(MultiFieldPanel.BoundPanel):
        template_name = "wagtail_360/admin/panels/panorama_panel.html"

        class Media:
            css = {"all": ("wagtail_360/admin/css/panorama_panel.css",)}
            js = (
                f"https://maps.googleapis.com/maps/api/js?key={google_maps_api_key()}",
                "wagtail_360/admin/js/street_view.min.js",
            )


class ReadOnlyFieldPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldPanel, self).__init__(*args, **kwargs)
        self.widget = forms.TextInput(
            attrs={"readonly": "readonly", "placeholder": "read only"}
        )
