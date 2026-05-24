from models import TransactionCreate
from datetime import date

txn = TransactionCreate(
    user_id=1,
    amount=500,
    type="expense",
    category="dining",
    note="with family",
    txn_date=date.today()
)

print(txn)