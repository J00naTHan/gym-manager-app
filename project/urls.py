from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import ClientViewSet

router = DefaultRouter()
router.register(r'clientes', ClientViewSet, basename='cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
