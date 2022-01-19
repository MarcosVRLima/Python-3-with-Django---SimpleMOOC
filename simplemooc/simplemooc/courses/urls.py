from django.urls import path
from simplemooc.courses.views import coursePageView, detailsPageView, enrollmentPageView

urlpatterns = [
    path('', coursePageView, name='index'),
    path('<slug:slug>/', detailsPageView, name='details'),
    path('<slug:slug>/inscricao/', enrollmentPageView, name='enrollment'),
]