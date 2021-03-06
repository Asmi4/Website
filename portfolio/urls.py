from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('blog/', blog.views.allblogs,name='allblogs'),
    path('', jobs.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
