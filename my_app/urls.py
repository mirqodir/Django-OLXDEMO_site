from django.urls import path
from .views import IndexPageView,AboutPageView,ContactPageView,GlassesPageView,ShopPageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [


			path('',IndexPageView.as_view(),name='index'),
			path('about/',AboutPageView.as_view(),name='about'),
			path('contact/',ContactPageView.as_view(),name='contact'),
			path('glasses/',GlassesPageView,name='glasses'),
			path('shop/',ShopPageView.as_view(),name='shop'),
			# path("test/",testpageview,name="test")

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)