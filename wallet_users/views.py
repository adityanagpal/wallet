from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User, Wallet, Transactions
from .serializers import UserSerializer,WalletCreateSerializer, WalletStatusSerializer, TransactionsSerializer


# Create your views here.
d = {"name":"aditya", "govt_id":"12345"}
d = {"name":"PhonePe", "user":1}

class UserView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the user items for given requested user
        '''
        user = User.objects.filter(govt_id=(request.GET.get("govt_id")))
        # http://127.0.0.1:8000/wallet/users/?govt_id=12345
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the user with given  data
        '''
        data = {
            'name': request.data.get('name'),
            'govt_id': request.data.get('govt_id')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletView(APIView):

    def get(self, request, *args, **kwargs):
        wallet = Wallet.objects.get(id=(request.GET.get("wallet_id")))
        serializer = WalletCreateSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the user with given  data
        '''
        data = {
            'name': request.data.get('name'),
            'user': request.data.get('user')
        }
        serializer = WalletCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WalletStatusView(APIView):


    def get(self, request, *args, **kwargs):
        '''
        Status of wallet by Id
        '''
        wallet = Wallet.objects.filter(id=(request.GET.get("wallet_id"))).first()
        if wallet is None:
            return Response({"error":"does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = WalletStatusSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'id': request.data.get('wallet_id'),
            'active': request.data.get('active')
        }
        d = {
            "wallet_id": 1,
            "active": "true"
        }
        if data['active'].lower() not in ['true','false','0','1']:
            return Response({"error": "pass value as true,false,0,1"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            wallet = Wallet.objects.get(id=int(data['id']))
            wallet.active = True if data['active'].lower() in ['true',1,'1'] else False
            wallet.save()
            serializer = WalletStatusSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error":f"error {e} in updating request"},status=status.HTTP_400_BAD_REQUEST)

class TransactionsView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        Status of wallet by Id
        '''

        transactions = Transactions.objects.filter(user=(request.GET.get("user_id")),wallet=(request.GET.get("wallet_id")))

        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the transactions with given  data
        d = {"user":1, "wallet":1, "credit":1000}
        '''
        data = request.data
        try:
            wallet = Wallet.objects.get(id=int(data['wallet']))
            if not wallet.active:
                return Response({"error": "wallet is not active"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error":"wallet is invalid"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            User.objects.get(id=int(data['user']))
        except:
            return Response({"error":"user is invalid"}, status=status.HTTP_400_BAD_REQUEST)
        if 'debit' in data and 'credit' in data:
            if int(data['debit'])!=0 and int(data['credit'])!=0:
                return Response({"error":"debit and credit one must be zero or not passed"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TransactionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletBalanceView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        Status of wallet by Id
        '''
        user_id = (request.GET.get("user_id"))
        wallet_id = (request.GET.get("wallet_id"))
        transactions = Transactions.objects.filter(user=user_id,wallet=wallet_id)
        try:
            debit = sum([i.debit for i in transactions])
            credit = sum([i.credit for i in transactions])
            return Response({"user_id": user_id, "wallet_id": wallet_id, "balance": credit - debit},
                            status=status.HTTP_200_OK)
        except:
            return Response({"error":"No transaction found"}, status=status.HTTP_400_BAD_REQUEST)








