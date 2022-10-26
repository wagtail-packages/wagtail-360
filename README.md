# Wagtail 360 virtual tour player

This app is an admin interface to choose google street view imagery and display an embedded virtual tour.

It's powered by google maps Javascript API and Wagtail CMS

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

You'll need to add 2 page models. Assuming the app is the default `home` app...

### The Tour Index Page

This is the parent page type for each Virtual Tour

```python
from wagtail_360.abstract_models import Tour

class TourPage(Tour):
    subpage_types = ["home.PanoramaPage"]
    content_panels = Page.content_panels + [Tour.panels]

    template = "home/tour_page.html"
```

### The Panorama Page

This is the Panorama page that is added as a child of the TourPage

```python
from wagtail_360.abstract_models import Panorama

class PanoramaPage(Panorama):
    parent_page_types = ["home.TourPage"]
    content_panels = Page.content_panels + Panorama.panels
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Build a virtual tour

### Tour Page

1. Search for a business on google maps. E.g. [Aquatics & Reptiles Worcester](https://www.google.com/maps/place/Aquatics+%26+Reptiles/@52.187041,-2.234878,15z/data=!4m5!3m4!1s0x0:0x87d71961c90b1709!8m2!3d52.187041!4d-2.234878)

2. On the left scroll down to the Street View & 360 images and click in the picture icon.

3. Click around to find a suitable starting view. [Try this link](https://www.google.com/maps/place/Aquatics+%26+Reptiles/@52.1870119,-2.234866,3a,75y,334.08h,91.65t/data=!3m7!1e1!3m5!1sAF1QipMOrPzw37q0zV2sRnLBG43s9F4dJmf1XX2zyyxv!2e10!3e13!7i13312!8i6656!4m7!3m6!1s0x0:0x87d71961c90b1709!8m2!3d52.187041!4d-2.234878!14m1!1BCgIgARICCAI)

4. Copy the url from the browser address bar. Or use this:

    ```text
    https://www.google.com/maps/place/Aquatics+%26+Reptiles/@52.1870119,-2.234866,3a,75y,334.08h,91.65t/data=!3m7!1e1!3m5!1sAF1QipMOrPzw37q0zV2sRnLBG43s9F4dJmf1XX2zyyxv!2e10!3e13!7i13312!8i6656!4m7!3m6!1s0x0:0x87d71961c90b1709!8m2!3d52.187041!4d-2.234878!14m1!1BCgIgARICCAI
    ```

5. In the Wagtail admin create a new **Tour Page** and paste in the url you copied. You should see that the url is valid and the maps data has been extracted to the correct fields. **Now give the page a title and save it.**

### Panorama Page

1. View the Tour Page and create a new child page, the only one available is the Panorama Page so you should see the edit page. The initial panorama view will be copied over from the Tour Page fields.
2. Click around to set the view you like. As you do that the page fields will be updated with new values. You can: **Move to a new place using the arrows** | **Spin the parorama around to find the best view** | **Zoom in or out** | **Set the elevation**
3. Give the view a title and save the page.
4. Add another panorama child page. This time the initial view will be the same view you set on the previous panorama.
5. Repeat steps 1 - 4 until you have all the views you need.
6. Use live preview to see the virtual tour with menu navigation.

## Developer setup

### Install the package in editable mode

Activate your virtual environment and run the following commands.

```bash
pip install -e ".[testing]"
make migrate
make load
```

Run the testing app.

```bash
make run
```

## Frontend

If you wish to alter the css or javascript.

```bash
nvm use
npm install
npm run build
```
