from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'opencv_webapp'
# html에서 :으로 넘길 때 여기 앱네임으로 간다는 의미

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
