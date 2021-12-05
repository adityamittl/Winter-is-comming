from django.contrib import admin
from django.urls import path,include
from blog.views import blog,send,dash
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('chat/',include('chat.urls')),
    path('', include('auth0login.urls')),
    path('blog',blog,name='blog'),
    path('send',send),
    path('',dash),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
