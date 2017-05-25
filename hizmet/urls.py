from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.anasayfa, name='anasayfa'),
    url(r'anasayfa', views.anasayfa, name='anasayfa'),
    url(r'hakkimizda', views.hakkimizda, name='hakkimizda'),
    url(r'urunler', views.urunler, name='urunler'),
    url(r'iletisim', views.iletisim, name='iletisim'),
]