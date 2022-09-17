from wagtail.admin.forms import WagtailAdminPageForm


class PanoramaForm(WagtailAdminPageForm):
    def __init__(self, data=None, files=None, parent_page=None, *args, **kwargs):

        if not kwargs.get("instance").id:
            # only set these if it's a new page
            last_child = parent_page.get_children().last()
            if last_child:
                # found a child of panorama page so copy it's values
                # as a starting point
                last_child_specific = last_child.specific
                kwargs.update(
                    initial={
                        "lat": last_child_specific.lat,
                        "lng": last_child_specific.lng,
                        "heading": last_child_specific.heading,
                        "elevation": last_child_specific.elevation,
                        "zoom_level": last_child_specific.zoom_level,
                    }
                )
            else:
                # no child panorama pages so use the parent tour page
                # values as a starting point
                parent_specific = parent_page.specific
                kwargs.update(
                    initial={
                        "lat": parent_specific.lat,
                        "lng": parent_specific.lng,
                        "heading": parent_specific.heading,
                        "elevation": parent_specific.elevation,
                        "zoom_level": parent_specific.zoom_level,
                    }
                )

        super(PanoramaForm, self).__init__(data, files, parent_page, *args, **kwargs)
