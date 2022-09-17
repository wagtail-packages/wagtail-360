from django import forms
from django.conf import settings
from wagtail.admin.panels import MultiFieldPanel, PanelGroup, Panel, FieldPanel


def google_street_view_api_key():
    if hasattr(settings, "GOOGLE_STREET_VIEW_API_KEY"):
        return settings.GOOGLE_STREET_VIEW_API_KEY
    return ""


class TourPanel(MultiFieldPanel):
    class BoundPanel(MultiFieldPanel.BoundPanel):
        template_name = "wagtail_360/admin/panels/tour_panel.html"
        heading = "360 Tour"

        class Media:
            js = ("wagtail_360/admin/js/parse_url.js",)


class PanoramaPanel(MultiFieldPanel):
    class BoundPanel(MultiFieldPanel.BoundPanel):
        template_name = "wagtail_360/admin/panels/panorama_panel.html"

        class Media:
            css = {"all": ("wagtail_360/admin/css/panorama_panel.css",)}
            js = (
                f"https://maps.googleapis.com/maps/api/js?key={google_street_view_api_key()}",
                "wagtail_360/admin/js/street_view.js",
            )


class ReadOnlyFieldPanel(FieldPanel):
    def __init__(self, field_name, **kwargs):
        super().__init__(field_name)
        self.widget = forms.TextInput(
            attrs={"readonly": "readonly", "placeholder": "read only"}
        )
