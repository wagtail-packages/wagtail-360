from django import forms
from django.conf import settings
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


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
                f"https://maps.googleapis.com/maps/api/js?key={getattr(settings, 'GOOGLE_MAPS_API_KEY', '')}",
                "wagtail_360/admin/js/street_view.min.js",
            )


class ReadOnlyFieldPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldPanel, self).__init__(*args, **kwargs)
        self.widget = forms.TextInput(
            attrs={"readonly": "readonly", "placeholder": "read only"}
        )
