from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Index,name="index"),
    path('upload/',views.Upload,name="upload"),
    path('download/',views.download,name="download")
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)