from fastmcp import FastMCP
import random
import json

# Create MCP server
mcp = FastMCP("Simple Calculator Server")


# -------------------
# TOOL 1: Add numbers
# -------------------
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


# --------------------------
# TOOL 2: Random number tool
# --------------------------
@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random number within a range.

    Args:
        min_val: Minimum value
        max_val: Maximum value

    Returns:
        Random integer
    """
    return random.randint(min_val, max_val)


# --------------------
# RESOURCE: Server info
# --------------------
@mcp.resource("info://server", mime_type="application/json")
def server_info() -> str:
    """
    Get information about this server.
    """
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Anubhav"
    }

    return json.dumps(info, indent=2)


# ---------------------
# TOOL 3: Multiply
# ---------------------
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    """
    return a * b


# ---------------------
# TOOL 4: Subtract
# ---------------------
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract second number from first.
    """
    return a - b


# ---------------------
# Start remote server
# ---------------------
if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )