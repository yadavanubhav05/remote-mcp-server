import asyncio
from datetime import date

from crud import create_user, add_transaction, list_transactions
from models import UserCreate, TransactionCreate, TransactionFilter


async def main():

    # create user
    user = await create_user(
        UserCreate(username="anubhav", email="test@gmail.com")
    )
    print(user)

    user_id = user["user_id"]

    # add expense
    txn = await add_transaction(
        TransactionCreate(
            user_id=user_id,
            amount=500,
            type="expense",
            category="dining",
            note="with family",
            txn_date=date.today()
        )
    )

    print(txn)

    # list
    rows = await list_transactions(
        TransactionFilter(user_id=user_id)
    )

    print(rows)


if __name__ == "__main__":
    asyncio.run(main())