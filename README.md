# Wagtail 360° virtual tours

An admin interface to choose google street view imagery and display an embedded virtual tour.

Powered by [google maps Javascript API](https://developers.google.com/maps/documentation/javascript) and [Wagtail CMS](https://wagtail.org/)

![Alt text](docs/screenshot.jpg?raw=true "Title")

## Installation

### Install the package

```bash
pip install wagtail-360
```

### Then add `wagtail_360` to your installed apps

```bash
INSTALLED_APPS = [
    # ...
    "wagtail_360",
    # ...
]
```

## Usage

Add 2 page models.

### The Tour Index Page

This represents a virtual tour and is the parent page for each Panorama in this tour.

```python
from wagtail_360.abstract_models import AbstractTour

class TourPage(AbstractTour, Page):
    subpage_types = ["PanoramaPage"]
    content_panels = Page.content_panels + [AbstractTour.panels]
```

### The Panorama Page Model

This represents a single panorama and is used as a child page of a TourPage.

```python
from wagtail_360.abstract_models import AbstractPanorama

class PanoramaPage(AbstractPanorama):
    parent_page_types = ["TourPage"]
    content_panels = Page.content_panels + AbstractPanorama.panels
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Configuration

Set the configuration in your settings.py file

A google maps API key is required. You can generate one at <https://developers.google.com/maps/documentation/javascript>

The service isn't free but there's a generous free tier available.

```python
GOOGLE_MAPS_API_KEY = "your-google-maps-api-key"
```

*If you don't set the key the panorama images will still display but will be in developer mode.*

## Build a virtual tour

[User docs](./docs/contribute.md)

## Contributing

If you would like to suggest an improvement to the package [contributions](docs/contrubute.md) are welcome

## Issues

If you find an issue please consider [raising and issue](https://github.com/nickmoreton/wagtail-360/issues)
