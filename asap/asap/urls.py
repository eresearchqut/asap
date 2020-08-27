from django.conf.urls import include
from django.urls import re_path
from django.views.generic import RedirectView

urlpatterns = [
    # Any custom URLs go here before we include the TRRF urls
    re_path(r'^$', RedirectView.as_view(url='router/', permanent=False)),
    re_path(r'', include('rdrf.urls')),
]
