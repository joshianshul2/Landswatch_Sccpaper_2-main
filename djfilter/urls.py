from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import *
# from django.views.generic import TemplateView
from django.conf.urls import url
from django.urls import reverse
from core import views
# from core.views import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import path
# from socialcustom.views import SomeTableView

a='?title_contains=Texas&view_count_min=&view_count_max=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres='

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index,name = 'login'),
    path('login', views.Login),
    #url(r'^success$', views.success),
    path('show/', views.show,name='show'),
    path('show3/', views.show3,name='show3'),
    path('testrishu', views.testrishu,name='testrishu'),
    path('gcsv', views.psg),
    path('show/bahu.jpg', views.rks,name='rks'),
    path('bahu.jpg', views.rks2,name='rks2'),
    path('desp', views.desp,name='desp'),
    path('AlertTODO', views.AlertTODO,name='AlertTODO'),
    path('RatioDetailsTemp', views.RatioDetailsTemp,name='RatioDetailsTemp'),
    path('delete', views.delete,name='delete'),
    path('logout', views.logout,name='logout'),

    path('csv',views.getfile),

    path('disp/<int:id>/',views.disp,name = 'disp'),

    #url(r'^Alert$', views.Alert),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
