from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from documents.views import AvaliacaoViewSet, PlanilhaViewSet
from users.views import ClientViewSet

userRouter = DefaultRouter()
userRouter.register(r'', ClientViewSet, basename='cliente')

avaliacaoRouter = DefaultRouter()
avaliacaoRouter.register(r'', AvaliacaoViewSet, basename='avaliacao')

planilhaRouter = DefaultRouter()
planilhaRouter.register(r'', PlanilhaViewSet, basename='planilha')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(userRouter.urls)),
    path('api/planilhas/', include(planilhaRouter.urls)),
    path('api/avaliacoes/', include(avaliacaoRouter.urls))
]
