# Expense Tracker MCP Server

An async **Expense Tracker backend** built with **FastMCP + SQLite + aiosqlite**, designed to work as an MCP server for AI agents (Claude, ChatGPT, MCP Inspector, Streamlit chatbot, etc.).

This project supports:

- Add expense
- Add credit/income
- Edit transactions
- Delete transactions
- Filter/list transactions
- Summarize expenses
- Category-wise analytics
- Daily trend analytics
- Monthly summaries

---

# Features

## Transaction Management

Users can:

- Log expenses
- Log credits/income (salary, refund, etc.)
- Edit existing transactions
- Delete transactions
- List transactions with filters

---

## Filters Supported

Transactions can be filtered by:

- Date range
- Transaction type (`expense` / `credit`)
- Category
- User

---

## Analytics

Built-in analytics include:

- Total expenses
- Total credits
- Balance
- Category-wise spending
- Daily spending trend
- Monthly summary

---

## Async Architecture

Built using async Python:

- `FastMCP`
- `aiosqlite`

Supports multiple users making requests concurrently.

---

## MCP Tools Exposed

| Tool | Description |
|---|---|
| `initialize_database` | Create DB tables |
| `register_user` | Register new user |
| `add_expense` | Add expense transaction |
| `add_credit` | Add income/credit |
| `get_transactions` | Filter/list transactions |
| `edit_transaction` | Update transaction |
| `remove_transaction` | Delete transaction |
| `expense_summary` | Overall summary |
| `category_summary` | Category analytics |
| `daily_summary` | Daily trend |
| `monthly_summary` | Monthly report |

---

# Project Structure

```text
expense-tracker/
│
├── db.py              # Database setup
├── models.py          # Pydantic models
├── crud.py            # CRUD operations
├── analytics.py       # Summary and analytics
├── mcp_server.py      # FastMCP server
├── app.py             # Streamlit UI (optional)
├── requirements.txt
├── pyproject.toml
├── README.md
```

---

# Database Schema

## Users table

Stores:

- user id
- username
- email
- created timestamp

---

## Transactions table

Stores:

- transaction id
- user id
- amount
- type (`expense` / `credit`)
- category
- note
- transaction date
- timestamps

---

# Installation

## Clone repo

```bash
git clone <repo-url>
cd remote-mcp-server
```

---

## Create environment

### Using uv

```bash
uv sync
```

---

### Or pip

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

---

# Run MCP Server

```bash
uv run mcp_server.py
```

or

```bash
python mcp_server.py
```

---

# Test with MCP Inspector

```bash
uv run fastmcp dev inspector
```

Use:

- Transport: `STDIO`
- Command:

```text
python
```

Arguments:

```text
mcp_server.py
```

---

# Deploy to FastMCP Cloud

Login:

```bash
uv run fastmcp login
```

Deploy:

```bash
uv run fastmcp deploy mcp_server.py
```

FastMCP returns a remote URL like:

```text
https://your-server.fastmcp.app/mcp
```

---

# Example MCP Usage

## Register user

```text
Register user:
username = anubhav
email = abc@gmail.com
```

---

## Add expense

```text
Add expense:
500
category = dining
note = with family
```

---

## Add credit

```text
Add credit:
50000
category = salary
```

---

## Summary

```text
Show my expense summary
```

Returns:

```json
{
  "total_expense": 5000,
  "total_credit": 50000,
  "balance": 45000
}
```

---

# Tech Stack

- Python
- FastMCP
- SQLite
- aiosqlite
- Pydantic
- Streamlit
- Plotly
- LangChain MCP Adapters

---

# Notes

## SQLite warning

SQLite works well for demo/local use.

For production, consider:

- Supabase
- Neon Postgres
- Turso

because cloud containers may reset local DB files.

---

# Future Improvements

- Authentication
- User login
- Budget alerts
- AI chatbot front-end
- Dashboard charts
- Recurring transactions
- Export to CSV/PDF

---

# Author

Built as a learning project for:

- MCP
- Async Python
- SQLite
- AI tool calling
- Streamlit integrations
