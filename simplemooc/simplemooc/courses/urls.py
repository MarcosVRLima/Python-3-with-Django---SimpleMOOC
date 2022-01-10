from django.urls import path
from simplemooc.courses.views import coursePageView, detailsPageView

urlpatterns = [
    path('', coursePageView, name='index'),
    path('<slug:slug>/', detailsPageView, name='details'),
]