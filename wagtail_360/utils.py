from django.conf import settings


def google_maps_api_key():
    if hasattr(settings, "GOOGLE_MAPS_API_KEY"):
        return settings.GOOGLE_MAPS_API_KEY
    return ""
