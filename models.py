from pydantic import BaseModel
from typing import Optional
from datetime import date


class UserCreate(BaseModel):
    username: str
    email: Optional[str] = None


class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    type: str          # expense / credit
    category: str
    note: Optional[str] = None
    txn_date: date


class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    category: Optional[str] = None
    note: Optional[str] = None
    txn_date: Optional[date] = None


class TransactionFilter(BaseModel):
    user_id: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    type: Optional[str] = None
    category: Optional[str] = None