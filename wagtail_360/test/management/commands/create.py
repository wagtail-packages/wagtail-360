from django.core.management.base import BaseCommand
from wagtail.models import Page

from wagtail_360.test.models import PanoramaPage, TourPage


class TourPageFactory:
    def __init__(self, parent=None, **kwargs):
        data = {key: value for key, value in kwargs.items()}
        self.page = TourPage(**data)
        if not parent:
            self.parent = Page.objects.get(title="Welcome to your new Wagtail site!")
        else:
            self.parent = parent

    def create(self):
        self.parent.add_child(instance=self.page)
        self.page.save_revision().publish()
        return self.page


class PanoramaPageFactory:
    def __init__(self, parent=None, **kwargs):
        if not parent:
            raise Exception("Parent page is required")
        data = {key: value for key, value in kwargs.items()}
        self.page = PanoramaPage(**data)

    def create(self):
        self.parent.add_child(instance=self.page)
        self.page.save_revision().publish()
        return self.page


class Command(BaseCommand):
    help = "Create test pages"

    def handle(self, *args, **options):
        factory = TourPageFactory(
            title="Restaurant",
            maps_url="https://www.google.com/maps/place/Bullocks+Bistro+and+bar/@52.2681251,-2.146122,3a,90y,187.54h,82.95t/data=!3m8!1e1!3m6!1sAF1QipN3_M3OONDMhBcz6leUfD5PvDWFwb__RvMVSeh8!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipN3_M3OONDMhBcz6leUfD5PvDWFwb__RvMVSeh8%3Dw203-h100-k-no-pi-20-ya1.5714489-ro-0-fo100!7i13312!8i6656!4m7!3m6!1s0x0:0x65d2e616db4b051b!8m2!3d52.2680933!4d-2.1461253!14m1!1BCgIgARICCAI",  # noqa
            lat=52.2681251,
            lng=-2.146122,
            heading=187.54,
            elevation=-7.049999999999997,
            zoom_level=0.0,
        ).create()
        self.stdout.write(self.style.SUCCESS(f"{factory}: Tour page created"))

        factory = PanoramaPageFactory(
            title="Bullocks Bistro and Bar",
            panorama_id="1",
        )

        factory = TourPageFactory(
            title="Cinema",
            maps_url="https://www.google.com/maps/place/Regal+Cinema+Evesham/@52.0910322,-1.9399386,3a,90y,187.44h,82.41t/data=!3m7!1e1!3m5!1sAF1QipOWRhBbSIYaMVqY2TD-Kb1Ydx_SjvvqHc81a1VV!2e10!3e11!7i13312!8i6656!4m7!3m6!1s0x0:0x540b84f32ae5f6ab!8m2!3d52.090865!4d-1.939927!14m1!1BCgIgARICCAI",  # noqa
            lat=52.0910322,
            lng=-1.9399386,
            heading=187.44,
            elevation=-7.590000000000003,
            zoom_level=0.0,
        )
        # .create()
        # self.stdout.write(self.style.SUCCESS(f'{factory}: Tour page created'))

        factory = TourPageFactory(
            title="Wedding Venue",
            maps_url="https://www.google.com/maps/place/Manor+Hill+House+Weddings/@52.3187606,-2.1181237,3a,75y,105.32h,92.93t/data=!3m6!1e1!3m4!1sAF1QipMIWi6q30ZF40Kg_s32nSQeCwMjpU-n5lxNSVUj!2e10!7i8000!8i4000!4m7!3m6!1s0x0:0x99ab2060fe09039b!8m2!3d52.3184969!4d-2.1174893!14m1!1BCgIgARICCAI",  # noqa
            lat=52.3187606,
            lng=-2.1181237,
            heading=105.32,
            elevation=2.930000000000007,
            zoom_level=-1.0,
        )
        # .create()
        # self.stdout.write(self.style.SUCCESS(f'{factory}: Tour page created'))
