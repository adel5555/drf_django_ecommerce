from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from E_com.product import views

router = DefaultRouter()
router.register(r"category", views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api_schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api_schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
