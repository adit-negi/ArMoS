from django.urls import path
from django.contrib import admin
from people.views import PersonListView, PersonCreateView, PersonUpdateView, homepage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', PersonListView.as_view(), name='person_list'),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('admin/', admin.site.urls),
    path('home/', homepage, name='homepage')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
