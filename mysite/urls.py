from django.urls import path, include
from django.contrib import admin
#from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #path('api/', include('blog.urls'))
    path('api/', include('django_rest.urls'))
]