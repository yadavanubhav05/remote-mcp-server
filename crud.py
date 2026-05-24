from db import get_db
from models import UserCreate, TransactionCreate, TransactionUpdate, TransactionFilter


# ----------------------------
# Create user
# ----------------------------
async def create_user(user: UserCreate):
    db = await get_db()

    cursor = await db.execute(
        """
        INSERT INTO users (username, email)
        VALUES (?, ?)
        """,
        (user.username, user.email)
    )

    await db.commit()
    user_id = cursor.lastrowid
    await db.close()

    return {"message": "User created", "user_id": user_id}


# ----------------------------
# Add transaction
# ----------------------------
async def add_transaction(txn: TransactionCreate):
    db = await get_db()

    cursor = await db.execute(
        """
        INSERT INTO transactions
        (user_id, amount, type, category, note, txn_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            txn.user_id,
            txn.amount,
            txn.type,
            txn.category,
            txn.note,
            txn.txn_date
        )
    )

    await db.commit()
    txn_id = cursor.lastrowid
    await db.close()

    return {"message": "Transaction added", "transaction_id": txn_id}


# ----------------------------
# List transactions
# ----------------------------
async def list_transactions(filters: TransactionFilter):
    db = await get_db()

    query = """
    SELECT id, amount, type, category, note, txn_date
    FROM transactions
    WHERE user_id = ?
    """

    params = [filters.user_id]

    if filters.start_date:
        query += " AND txn_date >= ?"
        params.append(filters.start_date)

    if filters.end_date:
        query += " AND txn_date <= ?"
        params.append(filters.end_date)

    if filters.type:
        query += " AND type = ?"
        params.append(filters.type)

    if filters.category:
        query += " AND category = ?"
        params.append(filters.category)

    cursor = await db.execute(query, params)
    rows = await cursor.fetchall()
    await db.close()

    return rows


# ----------------------------
# Update transaction
# ----------------------------
async def update_transaction(txn_id: int, update_data: TransactionUpdate):
    db = await get_db()

    fields = []
    values = []

    if update_data.amount is not None:
        fields.append("amount = ?")
        values.append(update_data.amount)

    if update_data.category is not None:
        fields.append("category = ?")
        values.append(update_data.category)

    if update_data.note is not None:
        fields.append("note = ?")
        values.append(update_data.note)

    if update_data.txn_date is not None:
        fields.append("txn_date = ?")
        values.append(update_data.txn_date)

    if not fields:
        return {"message": "Nothing to update"}

    query = f"""
    UPDATE transactions
    SET {", ".join(fields)},
        updated_at = CURRENT_TIMESTAMP
    WHERE id = ?
    """

    values.append(txn_id)

    await db.execute(query, values)
    await db.commit()
    await db.close()

    return {"message": "Transaction updated"}


# ----------------------------
# Delete transaction
# ----------------------------
async def delete_transaction(txn_id: int):
    db = await get_db()

    await db.execute(
        """
        DELETE FROM transactions
        WHERE id = ?
        """,
        (txn_id,)
    )

    await db.commit()
    await db.close()

    return {"message": "Transaction deleted"}