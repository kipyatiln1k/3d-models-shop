from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mdls.views import MdlDetailView

urlpatterns = [
    path('<int:pk>', MdlDetailView.as_view(), name='detail')
]