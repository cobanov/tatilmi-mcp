# Turkish Holidays & Birthdays MCP Server

A **Model Context Protocol (MCP)** server for Turkish holidays and birthdays.

## Features

- Check if a date is a Turkish holiday
- Get current date
- Access holiday and birthday data via resources

## Installation

```bash
git clone <repository-url>
cd tatilmi-mcp
uv sync
```

## Usage

**Run the server:**

```bash
python main.py
```

**Test with client:**

```bash
python client.py  # Edit client.py to uncomment desired tests
```

## Tools

- `get_current_date()` - Returns today's date in DD.MM.YYYY format
- `is_holiday(date_input)` - Check if date is a Turkish holiday

## Resources

- `data://birthdays` - All birthday records
- `data://holidays` - All holidays
- `data://holidays/{epoch}` - Holiday by timestamp

## Data Files

- `data/holidays.json` - Turkish holidays with timestamps
- `data/birthdays.json` - Birthday records with timestamps

## Dependencies

- Python 3.13+
- fastmcp >= 2.8.1
