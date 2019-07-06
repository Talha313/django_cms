from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class WebAPP(CMSApp):
    app_name = "webapp"  # must match the application namespace
    name = "My Webapp"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["mysite.apps.webapp.urls"] # replace this with the path to your application's URLs module

