from django.urls import path
from django.http import JsonResponse
from .views import UserListAPIView, wallet_update, UserTransactionsAPIView

def api_test(request):
    return JsonResponse({'status': 'API is working!', 'message': 'Django Wallet API is running correctly'})

urlpatterns = [
	path('test/', api_test, name='api-test'),
	path('users/', UserListAPIView.as_view(), name='users-list'),
	path('wallet/update/', wallet_update, name='wallet-update'),
	path('transactions/<int:user_id>/', UserTransactionsAPIView.as_view(), name='user-transactions'),
]
