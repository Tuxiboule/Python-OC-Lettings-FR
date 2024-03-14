from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from lettings.views import index as index_lettings
from lettings.views import letting
from profiles.views import index as index_profile
from profiles.views import profile

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'


def trigger_error(request):
    u_cant_divide_dis = 1 / 0
    print(u_cant_divide_dis)


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', index_lettings, name='lettings'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', index_profile, name='profiles'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
