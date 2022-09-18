from wagtail.models import Page

from wagtail_360.test.models import HomePage, PanoramaPage, TourPage


def test_page_factory():
    root = Page.objects.get(id=1)

    home_page = HomePage(title="Home")
    root.add_child(instance=home_page)
    home_page.save_revision().publish()

    tour_page = TourPage(
        title="Tour",
        maps_url="https://www.example.com/maps/place/1+Main+St,+New+York,+",
        lat=10,
        lng=-20,
        heading=30,
        elevation=40,
        zoom_level=5,
    )
    home_page.add_child(instance=tour_page)
    tour_page.save_revision().publish()

    panorama_page = PanoramaPage(
        title="Panorama",
        panorama_id="1",
        lat=50,
        lng=60,
        heading=70,
        elevation=80,
        zoom_level=3,
    )
    tour_page.add_child(instance=panorama_page)
    panorama_page.save_revision().publish()

    return home_page, tour_page, panorama_page
