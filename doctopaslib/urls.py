from django.contrib import admin
from django.urls import include,path
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('management.urls')),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('agenda/', include('agenda.urls')),
]
