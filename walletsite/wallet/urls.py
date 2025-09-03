from django.urls import path
from .views import UserListAPIView, wallet_update, UserTransactionsAPIView

urlpatterns = [
	path('users/', UserListAPIView.as_view(), name='users-list'),
	path('wallet/update/', wallet_update, name='wallet-update'),
	path('transactions/<int:user_id>/', UserTransactionsAPIView.as_view(), name='user-transactions'),
]
