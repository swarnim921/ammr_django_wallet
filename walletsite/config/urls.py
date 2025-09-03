"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

def root_view(request):
    return JsonResponse({
        'message': 'Django Wallet API is running!',
        'status': 'healthy',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
            'swagger': '/swagger/',
            'users': '/api/users/',
            'wallet_update': '/api/wallet/update/',
            'transactions': '/api/transactions/<user_id>/'
        }
    })

def health_check(request):
    return JsonResponse({'status': 'ok', 'message': 'Health check passed'})

# Simplified Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Wallet API",
        default_version='v1',
        description="API documentation for Wallet service",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=None,  # Use current request URL
)

urlpatterns = [
    path('', root_view, name='root'),
    path('health/', health_check, name='health'),
    path('admin/', admin.site.urls),
    path('api/', include('wallet.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
