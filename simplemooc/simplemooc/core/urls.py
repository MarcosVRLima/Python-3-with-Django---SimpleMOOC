from django.urls import path
from simplemooc.core.views import homePageView, contactPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('contato/', contactPageView, name='contact'),
]