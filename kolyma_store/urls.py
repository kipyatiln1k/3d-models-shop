"""kolyma_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from shop.views import MdlListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('', MdlListView.as_view(), name='home'),
    path('models/', include(('mdls.urls', 'mdls'))),
    path('tasks/', include(('tasks.urls', 'tasks'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('feedback/', include(('sendemail.urls', 'sendemail'))),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

