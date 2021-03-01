from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume),
    path('projects', views.projects),
    path('saralu', views.saralu)
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
# above static code is only for debug mode