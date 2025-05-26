import views
from django.urls import path
from home.views import IndexView, AboutUsView, ContactUsView, GalleryView, BlogDetail
from home import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
     path('<int:pk>/', BlogDetail.as_view(), name='single_post'),
]



