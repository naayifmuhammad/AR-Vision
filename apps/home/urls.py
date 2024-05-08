from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name='home'),
    path('upload_material/', views.upload_material, name="upload_material"),
    path('fetch_uploaded/', views.fetch_uploaded, name='fetch_uploaded'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

