from django.urls import path
from .views import UserView, WalletView, WalletStatusView, TransactionsView, WalletBalanceView

urlpatterns = [
    path('users', UserView.as_view()),
    path('wallet', WalletView.as_view()),
    path('wallet_status', WalletStatusView.as_view()),
    path('transactions', TransactionsView.as_view()),
    path('wallet_balance', WalletBalanceView.as_view()),
]