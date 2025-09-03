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
from django.http import JsonResponse, HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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

def assignment_info(request):
    """Special endpoint for assignment submission with CORS headers"""
    data = {
        'project_name': 'Django Wallet API',
        'description': 'A complete REST API for wallet management system',
        'status': 'active',
        'endpoints': {
            'test': 'https://ammr-django-wallet.onrender.com/api/test/',
            'users': 'https://ammr-django-wallet.onrender.com/api/users/',
            'wallet_update': 'https://ammr-django-wallet.onrender.com/api/wallet/update/',
            'transactions': 'https://ammr-django-wallet.onrender.com/api/transactions/{user_id}/',
            'documentation': 'https://ammr-django-wallet.onrender.com/docs/',
            'swagger': 'https://ammr-django-wallet.onrender.com/swagger/'
        },
        'features': [
            'User Management',
            'Wallet Balance Tracking', 
            'Transaction History',
            'Credit/Debit Operations',
            'RESTful API Design',
            'JSON Response Format',
            'Error Handling',
            'CORS Enabled'
        ],
        'technology_stack': [
            'Django 4.2.23',
            'Django REST Framework',
            'PostgreSQL',
            'Swagger Documentation',
            'CORS Headers'
        ]
    }
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

def api_docs(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Wallet API Documentation</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f8f9fa; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .endpoint { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #007bff; }
            .method { font-weight: bold; color: #007bff; display: inline-block; min-width: 60px; }
            .url { font-family: monospace; background: #e9ecef; padding: 2px 5px; border-radius: 3px; }
            .success { color: #28a745; }
            .info { color: #17a2b8; }
            pre { background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }
            .header { text-align: center; margin-bottom: 30px; }
            .status { display: inline-block; padding: 5px 10px; background: #28a745; color: white; border-radius: 15px; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Django Wallet API Documentation</h1>
                <p class="status">API Status: ACTIVE</p>
                <p>Complete REST API for wallet management system</p>
            </div>
            
            <h2>Available Endpoints</h2>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/api/test/</div>
                <p>Test endpoint to verify API is working</p>
                <p class="success">✅ Returns API status and available endpoints</p>
            </div>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/api/users/</div>
                <p>Get all users in the system</p>
                <p class="success">✅ Returns list of all registered users</p>
            </div>
            
            <div class="endpoint">
                <div class="method">POST</div>
                <div class="url">/api/wallet/update/</div>
                <p>Update wallet balance (credit/debit money)</p>
                <p><strong>Body:</strong> {"user_id": 1, "amount": "100.50", "transaction_type": "credit", "description": "Deposit"}</p>
                <p class="success">✅ Updates wallet balance and creates transaction record</p>
            </div>
            
            <div class="endpoint">
                <div class="method">GET</div>
                <div class="url">/api/transactions/{user_id}/</div>
                <p>Get all transactions for a specific user</p>
                <p class="success">✅ Returns transaction history for the specified user</p>
            </div>
            
            <h2>API Testing Examples</h2>
            <pre>
# Test API Status
curl https://ammr-django-wallet.onrender.com/api/test/

# Get All Users
curl https://ammr-django-wallet.onrender.com/api/users/

# Credit Money to User
curl -X POST https://ammr-django-wallet.onrender.com/api/wallet/update/ \\
  -H "Content-Type: application/json" \\
  -d '{"user_id": 1, "amount": "100.00", "transaction_type": "credit", "description": "Test deposit"}'

# Get User Transactions
curl https://ammr-django-wallet.onrender.com/api/transactions/1/
            </pre>
            
            <h2>API Features</h2>
            <ul>
                <li>✅ User Management</li>
                <li>✅ Wallet Balance Tracking</li>
                <li>✅ Transaction History</li>
                <li>✅ Credit/Debit Operations</li>
                <li>✅ RESTful API Design</li>
                <li>✅ JSON Response Format</li>
                <li>✅ Error Handling</li>
                <li>✅ CORS Enabled</li>
            </ul>
        </div>
    </body>
    </html>
    """
    from django.http import HttpResponse
    response = HttpResponse(html)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Simplified Swagger configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Django Wallet API",
        default_version='v1',
        description="Complete REST API for wallet management system with user management, balance tracking, and transaction history",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path('api/', include('wallet.urls')),
    ],
)

# Custom Swagger view with CORS headers
@csrf_exempt
def swagger_view(request, *args, **kwargs):
    """Custom Swagger view with CORS headers"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Wallet API - Interactive Documentation</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { 
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
                margin: 0; 
                padding: 0; 
                background: #f5f5f5;
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem;
                text-align: center;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }
            .endpoint {
                background: white;
                border-radius: 8px;
                margin: 1rem 0;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                overflow: hidden;
            }
            .endpoint-header {
                padding: 1rem;
                border-bottom: 1px solid #eee;
                display: flex;
                align-items: center;
                gap: 1rem;
            }
            .method {
                padding: 0.5rem 1rem;
                border-radius: 4px;
                font-weight: bold;
                font-size: 0.9rem;
                text-transform: uppercase;
            }
            .method.get { background: #61affe; color: white; }
            .method.post { background: #49cc90; color: white; }
            .method.put { background: #fca130; color: white; }
            .method.delete { background: #f93e3e; color: white; }
            .url {
                font-family: monospace;
                font-size: 1.1rem;
                color: #333;
            }
            .endpoint-body {
                padding: 1rem;
            }
            .description {
                color: #666;
                margin-bottom: 1rem;
            }
            .try-it {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 1rem;
                margin-top: 1rem;
            }
            .try-it h4 {
                margin-top: 0;
                color: #495057;
            }
            .try-it button {
                background: #007bff;
                color: white;
                border: none;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                cursor: pointer;
                margin-right: 0.5rem;
            }
            .try-it button:hover {
                background: #0056b3;
            }
            .response {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 1rem;
                margin-top: 1rem;
                font-family: monospace;
                white-space: pre-wrap;
                display: none;
            }
            .status {
                display: inline-block;
                padding: 0.25rem 0.5rem;
                border-radius: 4px;
                font-size: 0.8rem;
                font-weight: bold;
                margin-left: 0.5rem;
            }
            .status.success { background: #d4edda; color: #155724; }
            .status.error { background: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Django Wallet API</h1>
            <p>Interactive API Documentation</p>
        </div>
        
        <div class="container">
            <div class="endpoint">
                <div class="endpoint-header">
                    <span class="method get">GET</span>
                    <span class="url">/api/test/</span>
                    <span class="status success">Active</span>
                </div>
                <div class="endpoint-body">
                    <div class="description">
                        Test endpoint to verify API is working and get available endpoints.
                    </div>
                    <div class="try-it">
                        <h4>Try it out:</h4>
                        <button onclick="testEndpoint('/api/test/', 'GET')">Test API</button>
                        <div class="response" id="response-test"></div>
                    </div>
                </div>
            </div>

            <div class="endpoint">
                <div class="endpoint-header">
                    <span class="method get">GET</span>
                    <span class="url">/api/users/</span>
                    <span class="status success">Active</span>
                </div>
                <div class="endpoint-body">
                    <div class="description">
                        Get all users in the system.
                    </div>
                    <div class="try-it">
                        <h4>Try it out:</h4>
                        <button onclick="testEndpoint('/api/users/', 'GET')">Get Users</button>
                        <div class="response" id="response-users"></div>
                    </div>
                </div>
            </div>

            <div class="endpoint">
                <div class="endpoint-header">
                    <span class="method post">POST</span>
                    <span class="url">/api/wallet/update/</span>
                    <span class="status success">Active</span>
                </div>
                <div class="endpoint-body">
                    <div class="description">
                        Update wallet balance (credit/debit money).<br>
                        <strong>Body:</strong> {"user_id": 1, "amount": "100.50", "transaction_type": "credit", "description": "Deposit"}
                    </div>
                    <div class="try-it">
                        <h4>Try it out:</h4>
                        <button onclick="testWalletUpdate()">Credit Money</button>
                        <button onclick="testWalletDebit()">Debit Money</button>
                        <div class="response" id="response-wallet"></div>
                    </div>
                </div>
            </div>

            <div class="endpoint">
                <div class="endpoint-header">
                    <span class="method get">GET</span>
                    <span class="url">/api/transactions/{user_id}/</span>
                    <span class="status success">Active</span>
                </div>
                <div class="endpoint-body">
                    <div class="description">
                        Get all transactions for a specific user.
                    </div>
                    <div class="try-it">
                        <h4>Try it out:</h4>
                        <input type="number" id="user-id" placeholder="User ID" value="1" style="padding: 0.5rem; margin-right: 0.5rem;">
                        <button onclick="testTransactions()">Get Transactions</button>
                        <div class="response" id="response-transactions"></div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            const BASE_URL = 'https://ammr-django-wallet.onrender.com';
            
            async function testEndpoint(endpoint, method) {
                const responseDiv = document.getElementById('response-' + endpoint.split('/')[2]);
                responseDiv.style.display = 'block';
                responseDiv.textContent = 'Loading...';
                
                try {
                    const response = await fetch(BASE_URL + endpoint);
                    const data = await response.json();
                    responseDiv.textContent = JSON.stringify(data, null, 2);
                } catch (error) {
                    responseDiv.textContent = 'Error: ' + error.message;
                }
            }
            
            async function testWalletUpdate() {
                const responseDiv = document.getElementById('response-wallet');
                responseDiv.style.display = 'block';
                responseDiv.textContent = 'Loading...';
                
                try {
                    const response = await fetch(BASE_URL + '/api/wallet/update/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            user_id: 1,
                            amount: "100.00",
                            transaction_type: "credit",
                            description: "Test deposit"
                        })
                    });
                    const data = await response.json();
                    responseDiv.textContent = JSON.stringify(data, null, 2);
                } catch (error) {
                    responseDiv.textContent = 'Error: ' + error.message;
                }
            }
            
            async function testWalletDebit() {
                const responseDiv = document.getElementById('response-wallet');
                responseDiv.style.display = 'block';
                responseDiv.textContent = 'Loading...';
                
                try {
                    const response = await fetch(BASE_URL + '/api/wallet/update/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            user_id: 1,
                            amount: "50.00",
                            transaction_type: "debit",
                            description: "Test withdrawal"
                        })
                    });
                    const data = await response.json();
                    responseDiv.textContent = JSON.stringify(data, null, 2);
                } catch (error) {
                    responseDiv.textContent = 'Error: ' + error.message;
                }
            }
            
            async function testTransactions() {
                const userId = document.getElementById('user-id').value;
                const responseDiv = document.getElementById('response-transactions');
                responseDiv.style.display = 'block';
                responseDiv.textContent = 'Loading...';
                
                try {
                    const response = await fetch(BASE_URL + '/api/transactions/' + userId + '/');
                    const data = await response.json();
                    responseDiv.textContent = JSON.stringify(data, null, 2);
                } catch (error) {
                    responseDiv.textContent = 'Error: ' + error.message;
                }
            }
        </script>
    </body>
    </html>
    """
    response = HttpResponse(html)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@csrf_exempt
def redoc_view(request, *args, **kwargs):
    """Custom ReDoc view with CORS headers"""
    response = schema_view.with_ui('redoc', cache_timeout=0)(request, *args, **kwargs)
    if hasattr(response, 'content'):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

urlpatterns = [
    path('', root_view, name='root'),
    path('health/', health_check, name='health'),
    path('assignment/', assignment_info, name='assignment-info'),
    path('docs/', api_docs, name='api-docs'),
    path('admin/', admin.site.urls),
    path('api/', include('wallet.urls')),
    path('swagger/', swagger_view, name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', redoc_view, name='schema-redoc'),
]
