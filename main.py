import json
from datetime import date
from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("turkish-holidays")

# Load data once at startup
with open("holidays.json", "r", encoding="utf-8") as f:
    holidays_data = json.load(f)

with open("birthdays.json", "r", encoding="utf-8") as f:
    birthdays_data = json.load(f)


@mcp.tool()
def get_current_date() -> dict:
    """Get today's date in DD.MM.YYYY format."""
    today = date.today()
    return {"current_date": today.strftime("%d.%m.%Y")}


@mcp.resource("data://birthdays")
def get_all_birthdays() -> dict:
    """Get all birthdays with their details."""
    return {"birthdays": birthdays_data}


@mcp.resource("data://holidays")
def get_all_holidays() -> dict:
    """Get all holidays with their details."""
    return {"holidays": holidays_data}


@mcp.resource("data://holidays/{epoch}")
def get_holiday_by_epoch(epoch: str) -> dict:
    """Get holiday details for a specific epoch timestamp."""
    epoch_int = int(epoch)
    
    for holiday in holidays_data:
        if holiday["date"] == epoch_int:
            return {
                "title": holiday["title"],
                "date": holiday["date"],
                "localeDateString": holiday["localeDateString"]
            }
    
    return {"error": "No holiday found for this epoch", "epoch": epoch_int}


@mcp.tool()
def is_holiday(date_input: str) -> dict:
    """
    Check if a specific date is a holiday in Turkey.
    
    Args:
        date_input: Date in DD.MM.YYYY format (e.g., "01.01.2025")
    """
    for holiday in holidays_data:
        if holiday["localeDateString"] == date_input:
            return {
                "is_holiday": True, 
                "holiday_name": holiday["title"],
                "date": holiday["date"],
                "localeDateString": holiday["localeDateString"]
            }
    
    return {"is_holiday": False, "date_checked": date_input}


if __name__ == "__main__":
    mcp.run(transport="stdio")