from db import get_db


# ----------------------------
# Overall summary
# ----------------------------
async def get_summary(user_id: int):
    db = await get_db()

    # total expenses
    cursor = await db.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE user_id = ?
        AND type = 'expense'
    """, (user_id,))
    total_expense = (await cursor.fetchone())[0]

    # total credits
    cursor = await db.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE user_id = ?
        AND type = 'credit'
    """, (user_id,))
    total_credit = (await cursor.fetchone())[0]

    balance = total_credit - total_expense

    await db.close()

    return {
        "total_expense": total_expense,
        "total_credit": total_credit,
        "balance": balance
    }


# ----------------------------
# Category-wise expense summary
# ----------------------------
async def get_category_summary(user_id: int):
    db = await get_db()

    cursor = await db.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE user_id = ?
        AND type = 'expense'
        GROUP BY category
    """, (user_id,))

    rows = await cursor.fetchall()
    await db.close()

    return rows


# ----------------------------
# Daily trend summary
# ----------------------------
async def get_daily_summary(user_id: int):
    db = await get_db()

    cursor = await db.execute("""
        SELECT txn_date, SUM(amount)
        FROM transactions
        WHERE user_id = ?
        AND type = 'expense'
        GROUP BY txn_date
        ORDER BY txn_date
    """, (user_id,))

    rows = await cursor.fetchall()
    await db.close()

    return rows


# ----------------------------
# Monthly summary
# ----------------------------
async def get_monthly_summary(user_id: int):
    db = await get_db()

    cursor = await db.execute("""
        SELECT strftime('%Y-%m', txn_date) as month,
               SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END),
               SUM(CASE WHEN type = 'credit' THEN amount ELSE 0 END)
        FROM transactions
        WHERE user_id = ?
        GROUP BY month
        ORDER BY month
    """, (user_id,))

    rows = await cursor.fetchall()
    await db.close()

    return rows