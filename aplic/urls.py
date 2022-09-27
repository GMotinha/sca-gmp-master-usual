from django.urls import path

from aplic.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
