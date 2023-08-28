from rest_framework import serializers
from .models import User, Wallet, Transactions

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','name','govt_id')



class WalletStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id','active')

class WalletCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id','name','user')

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ('id','user', 'wallet','debit','credit','transaction_time')



