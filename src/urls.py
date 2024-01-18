
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('book.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
]
urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)
