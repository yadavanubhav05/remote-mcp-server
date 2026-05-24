from fastmcp import FastMCP
from datetime import date
from typing import Optional

from crud import (
    create_user,
    add_transaction,
    list_transactions,
    update_transaction,
    delete_transaction
)

from analytics import (
    get_summary,
    get_category_summary,
    get_daily_summary,
    get_monthly_summary
)

from models import (
    UserCreate,
    TransactionCreate,
    TransactionUpdate,
    TransactionFilter
)

from db import init_db


# Create MCP server
mcp = FastMCP("Expense Tracker Server")


# ----------------------------
# Initialize DB
# ----------------------------
@mcp.tool
async def initialize_database():
    """
    Initialize database tables
    """
    await init_db()
    return "Database initialized successfully"


# ----------------------------
# Create user
# ----------------------------
@mcp.tool
async def register_user(username: str, email: Optional[str] = None):
    """
    Register a new user
    """
    user = UserCreate(username=username, email=email)
    return await create_user(user)


# ----------------------------
# Add expense
# ----------------------------
@mcp.tool
async def add_expense(
    user_id: int,
    amount: float,
    category: str,
    note: Optional[str] = None,
    txn_date: Optional[str] = None
):
    """
    Add expense transaction
    """

    txn_date = txn_date or str(date.today())

    txn = TransactionCreate(
        user_id=user_id,
        amount=amount,
        type="expense",
        category=category,
        note=note,
        txn_date=txn_date
    )

    return await add_transaction(txn)


# ----------------------------
# Add credit
# ----------------------------
@mcp.tool
async def add_credit(
    user_id: int,
    amount: float,
    category: str,
    note: Optional[str] = None,
    txn_date: Optional[str] = None
):
    """
    Add credit transaction
    """

    txn_date = txn_date or str(date.today())

    txn = TransactionCreate(
        user_id=user_id,
        amount=amount,
        type="credit",
        category=category,
        note=note,
        txn_date=txn_date
    )

    return await add_transaction(txn)


# ----------------------------
# List transactions
# ----------------------------
@mcp.tool
async def get_transactions(
    user_id: int,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    txn_type: Optional[str] = None,
    category: Optional[str] = None
):
    """
    List transactions with filters
    """

    filters = TransactionFilter(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        type=txn_type,
        category=category
    )

    return await list_transactions(filters)


# ----------------------------
# Update transaction
# ----------------------------
@mcp.tool
async def edit_transaction(
    txn_id: int,
    amount: Optional[float] = None,
    category: Optional[str] = None,
    note: Optional[str] = None,
    txn_date: Optional[str] = None
):
    """
    Edit existing transaction
    """

    update_data = TransactionUpdate(
        amount=amount,
        category=category,
        note=note,
        txn_date=txn_date
    )

    return await update_transaction(txn_id, update_data)


# ----------------------------
# Delete transaction
# ----------------------------
@mcp.tool
async def remove_transaction(txn_id: int):
    """
    Delete transaction
    """
    return await delete_transaction(txn_id)


# ----------------------------
# Analytics
# ----------------------------
@mcp.tool
async def expense_summary(user_id: int):
    """
    Overall expense summary
    """
    return await get_summary(user_id)


@mcp.tool
async def category_summary(user_id: int):
    """
    Category-wise summary
    """
    return await get_category_summary(user_id)


@mcp.tool
async def daily_summary(user_id: int):
    """
    Daily expense trend
    """
    return await get_daily_summary(user_id)


@mcp.tool
async def monthly_summary(user_id: int):
    """
    Monthly summary
    """
    return await get_monthly_summary(user_id)


# ----------------------------
# Start MCP server
# ----------------------------
if __name__ == "__main__":
    mcp.run()