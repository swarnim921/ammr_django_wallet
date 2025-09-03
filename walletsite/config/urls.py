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

def api_docs(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Wallet API Documentation</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .endpoint { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .method { font-weight: bold; color: #007bff; }
            .url { font-family: monospace; background: #e9ecef; padding: 2px 5px; }
        </style>
    </head>
    <body>
        <h1>Django Wallet API Documentation</h1>
        <p>Simple API documentation for testing endpoints.</p>
        
        <div class="endpoint">
            <div class="method">GET</div>
            <div class="url">/api/test/</div>
            <p>Test endpoint to verify API is working</p>
        </div>
        
        <div class="endpoint">
            <div class="method">GET</div>
            <div class="url">/api/users/</div>
            <p>Get all users in the system</p>
        </div>
        
        <div class="endpoint">
            <div class="method">POST</div>
            <div class="url">/api/wallet/update/</div>
            <p>Update wallet balance (credit/debit money)</p>
            <p><strong>Body:</strong> {"user_id": 1, "amount": "100.50", "transaction_type": "credit", "description": "Deposit"}</p>
        </div>
        
        <div class="endpoint">
            <div class="method">GET</div>
            <div class="url">/api/transactions/{user_id}/</div>
            <p>Get all transactions for a specific user</p>
        </div>
        
        <h2>Test with curl:</h2>
        <pre>
# Test API
curl https://ammr-django-wallet.onrender.com/api/test/

# Credit money
curl -X POST https://ammr-django-wallet.onrender.com/api/wallet/update/ \\
  -H "Content-Type: application/json" \\
  -d '{"user_id": 1, "amount": "100.00", "transaction_type": "credit", "description": "Test deposit"}'
        </pre>
    </body>
    </html>
    """
    from django.http import HttpResponse
    return HttpResponse(html)

# Simplified Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Wallet API",
        default_version='v1',
        description="API documentation for Wallet service",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path('api/', include('wallet.urls')),
    ],
)

urlpatterns = [
    path('', root_view, name='root'),
    path('health/', health_check, name='health'),
    path('docs/', api_docs, name='api-docs'),
    path('admin/', admin.site.urls),
    path('api/', include('wallet.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
