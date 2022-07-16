from django.urls import path
from .views import HomePageView, AboutPageView, CatalogPageView, ContactPageView, LoginPageView, SignupPageView, CartPageView

urlpatterns =[
    path('', HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('catalog/', CatalogPageView.as_view(),name='catalog'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('registration/login/', LoginPageView.as_view(),name='login'),
    path('signup/', SignupPageView.as_view(),name='signup'),
    path('cart/', CartPageView.as_view(),name='cart'),
]
