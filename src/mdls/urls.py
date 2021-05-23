from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mdls.views import MdlCreateView, MdlDetailView

urlpatterns = [
    path('<int:pk>', MdlDetailView.as_view(), name='detail'),
    path('create/', MdlCreateView.as_view(), name='create')
]