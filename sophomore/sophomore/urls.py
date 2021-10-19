from django.contrib import admin
from django.urls import path, include,re_path
# from apps.rbac.views import MyObtainTokenPairView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken import views as api_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
    # 具体定义详见 [Swagger/OpenAPI 规范](https://swagger.io/specification/#infoObject "Swagger/OpenAPI 规范")
    info=openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    # public 表示文档完全公开, 无需针对用户鉴权
    public=True,
    # 可以传递 drf 的 BasePermission
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rest-auth/', include('rest_auth.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-spec'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('personal/', include(('personal.urls', 'personal'), namespace='personal')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('rbac/', include('rbac.urls')),

]


# 如果是调式状态
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns