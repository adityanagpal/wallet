Create python virtual enviornment
cmd - virtualenv venv --python=python3
activate it by - source venv/bin/activate  or   venv/Scripts/activate

then install all requirements by

pip install -r requirements.txt

run - python manage.py makemigrations wallet_users
python manage.py migrate

then runserver by - python manage.py runserver

APIs
Create User - POST  http://127.0.0.1:8000/wallet/users  body = {"name":"Aditya" , "govt_id":"12345"}
get user details - http://127.0.0.1:8000/wallet/users?govt_id=12345

Create Wallet - POST http://127.0.0.1:8000/wallet/wallet  body = {"name":"PhonePe" , "user":1}  # id of above created user
get Wallet details - http://127.0.0.1:8000/wallet/wallet?wallet_id=1

get Wallet Status - http://127.0.0.1:8000/wallet/wallet_status?wallet_id=1
Change Wallet Status - POST http://127.0.0.1:8000/wallet/wallet_status  body = {"active":"true"}  # true, false, 0, 1

get Transactions - http://127.0.0.1:8000/wallet/transactions?wallet_id=1&user_id=1
Create Transactions - POST http://127.0.0.1:8000/wallet/transactions body = {"user":1, "wallet":1, "credit":1000}

get Balance - http://127.0.0.1:8000/wallet/wallet_balance?wallet_id=1&user_id=1


Assumptions -
1. A user can have multiple wallets
2. if wallet is inactive then transaction is not possible
3. all get calls have query params "&" seperated after ? 
4. All usecases are covered in above API calls that mentioned here

POST
Initialize my account for wallet
POST
Enable my wallet
GET
View my wallet balance
GET
View my wallet transactions
POST
Add virtual money to my wallet
POST
Use virtual money from my wallet
PATCH
Disable my wallet

