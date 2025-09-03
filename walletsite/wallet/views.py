from decimal import Decimal, InvalidOperation
from django.contrib.auth import get_user_model
from django.db import transaction as db_transaction
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Wallet, Transaction
from .serializers import UserSerializer, WalletSerializer, TransactionSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all().order_by('id')
    serializer_class = UserSerializer


@swagger_auto_schema(
    method='post',
    operation_description="Update wallet balance by crediting or debiting money",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['user_id', 'amount', 'transaction_type'],
        properties={
            'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
            'amount': openapi.Schema(type=openapi.TYPE_STRING, description='Amount to credit/debit'),
            'transaction_type': openapi.Schema(type=openapi.TYPE_STRING, enum=['credit', 'debit'], description='Type of transaction'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Transaction description'),
        }
    ),
    responses={
        200: WalletSerializer,
        400: 'Bad Request - Invalid data or insufficient balance',
        404: 'User not found'
    }
)
@api_view(['POST'])
def wallet_update(request):
    user_id = request.data.get('user_id')
    amount = request.data.get('amount')
    transaction_type = request.data.get('transaction_type')  # 'credit' or 'debit'
    description = request.data.get('description', '')

    if user_id is None or amount is None or transaction_type not in [Transaction.CREDIT, Transaction.DEBIT]:
        return Response({'detail': 'user_id, amount and valid transaction_type are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        amount = Decimal(str(amount))
    except (InvalidOperation, TypeError, ValueError):
        return Response({'detail': 'amount must be a valid decimal.'}, status=status.HTTP_400_BAD_REQUEST)

    if amount <= 0:
        return Response({'detail': 'amount must be greater than zero.'}, status=status.HTTP_400_BAD_REQUEST)

    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=user_id)
    except user_model.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    with db_transaction.atomic():
        wallet, _ = Wallet.objects.select_for_update().get_or_create(user=user)

        if transaction_type == Transaction.DEBIT and wallet.balance < amount:
            return Response({'detail': 'Insufficient balance.'}, status=status.HTTP_400_BAD_REQUEST)

        if transaction_type == Transaction.CREDIT:
            wallet.balance += amount
        else:
            wallet.balance -= amount
        wallet.save()

        Transaction.objects.create(
            user=user,
            amount=amount,
            transaction_type=transaction_type,
            description=description,
        )

    return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)


class UserTransactionsAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transaction.objects.filter(user_id=user_id).order_by('-created_at')
