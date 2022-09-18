from wagtail.admin.forms import WagtailAdminPageForm


class PanoramaForm(WagtailAdminPageForm):
    def __init__(self, data=None, files=None, parent_page=None, *args, **kwargs):
        super(PanoramaForm, self).__init__(data, files, parent_page, *args, **kwargs)
        if not self.instance.id:
            self.initial.update(self.parent_page.initial_panorama_data())
