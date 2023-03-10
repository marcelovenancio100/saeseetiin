from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('user/', include('user.urls')),
    path('home/', include('home.urls')),
    path('brand/', include('brand.urls')),
    path('model/', include('model.urls')),
    path('group/', include('group.urls')),
    path('situation/', include('situation.urls')),
    path('collection/', include('collection.urls')),
    path('item/', include('item.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug Toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
