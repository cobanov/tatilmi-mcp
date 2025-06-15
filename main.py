import json
from datetime import date
from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("turkish-holidays")

# Load data once at startup
with open("tatiller.json", "r", encoding="utf-8") as f:
    holidays_data = json.load(f)

with open("dogumgunleri.json", "r", encoding="utf-8") as f:
    birthdays_data = json.load(f)


@mcp.tool()
def get_current_date() -> dict:
    """Get today's date in DD.MM.YYYY format."""
    today = date.today()
    return {"current_date": today.strftime("%d.%m.%Y")}


@mcp.tool()
def get_all_birthdays() -> dict:
    """Get all birthdays with their details."""
    return {"birthdays": birthdays_data}


@mcp.tool()
def is_holiday(date_input: str) -> dict:
    """
    Check if a specific date is a holiday in Turkey.
    
    Args:
        date_input: Date in DD.MM.YYYY format (e.g., "01.01.2025")
    """
    for holiday in holidays_data:
        if holiday["localeDateString"] == date_input:
            return {"is_holiday": True, "holiday_name": holiday["title"]}
    
    return {"is_holiday": False}


if __name__ == "__main__":
    mcp.run(transport="stdio")
