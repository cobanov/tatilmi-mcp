# Turkish Holidays & Birthdays MCP Server

A simple **Model Context Protocol (MCP)** server that provides tools for checking Turkish holidays and managing birthday information.

## 🚀 Features

- **Current Date**: Get today's date in Turkish format (DD.MM.YYYY)
- **Holiday Checker**: Check if any date is a Turkish public holiday
- **Birthday Manager**: Access all birthday records with details

## 📁 Project Structure

```
tatilmi-mcp/
├── main.py              # MCP server implementation
├── dogumgunleri.json    # Birthday data
├── tatiller.json        # Turkish holidays data
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd tatilmi-mcp
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Activate virtual environment**
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

## 🎯 Available Tools

### 1. `get_current_date()`

Returns today's date in Turkish format.

**Example Response:**

```json
{
  "current_date": "15.01.2025"
}
```

### 2. `get_all_birthdays()`

Returns all birthday records from the database.

**Example Response:**

```json
{
  "birthdays": [
    {
      "title": "Ahmet'in Doğum Günü",
      "date": 1736553600000,
      "localeDateString": "11.01.2025"
    }
  ]
}
```

### 3. `is_holiday(date_input: str)`

Checks if a specific date is a Turkish public holiday.

**Parameters:**

- `date_input`: Date in DD.MM.YYYY format

**Example Usage:**

```python
is_holiday("01.01.2025")  # New Year's Day
```

**Example Response:**

```json
{
  "is_holiday": true,
  "holiday_name": "Yılbaşı"
}
```

## 🏃‍♂️ Running the Server

```bash
python main.py
```

The server will start and listen for MCP protocol messages via stdio.

## 📊 Data Files

### `tatiller.json`

Contains Turkish public holidays with:

- `title`: Holiday name in Turkish
- `date`: Unix timestamp
- `localeDateString`: Formatted date (DD.MM.YYYY)

### `dogumgunleri.json`

Contains birthday records with:

- `title`: Person's birthday title
- `date`: Unix timestamp
- `localeDateString`: Formatted date (DD.MM.YYYY)

## 🔧 Dependencies

- **fastmcp**: MCP server framework
- **Python 3.8+**: Required Python version

## 📝 Usage Example

This MCP server can be integrated with any MCP-compatible client to:

1. **Check holidays** before scheduling events
2. **Get birthday reminders** for planning celebrations
3. **Retrieve current date** in Turkish format

## 🤝 Contributing

This is a tutorial project demonstrating MCP server implementation. Feel free to:

- Add more holidays
- Include additional birthday management features
- Extend with date calculation utilities

## 📄 License

This project is created for educational purposes.

---

**Perfect for learning MCP (Model Context Protocol) development!** 🎓
