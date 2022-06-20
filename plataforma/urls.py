from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trocasolidaria/', include('trocasolidaria.urls')),
    path('', RedirectView.as_view(url='/trocasolidaria/', permanent=True)),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)