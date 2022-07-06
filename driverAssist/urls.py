from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='DriverAssist'),
    path('navigation', views.navigation, name='Navigation'),
    path('students', views.students, name='Students'),
    path('signin', views.signin, name='Signin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
