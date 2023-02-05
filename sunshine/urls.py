from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import import_data

app_name = 'sunshine'

urlpatterns = [
    path('home',views.home ,name='home'),
     path('',views.index , name='index'),
     path('blogs',views.blogs, name='blogs'),
     path('post',views.post, name='post'),
     path('media',views.media, name='media'),
    path('import/', import_data, name='import_data'),
]   

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
