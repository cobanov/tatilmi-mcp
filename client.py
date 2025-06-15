import asyncio
from fastmcp import Client
import json

client = Client("main.py")

async def check_holiday(date):
    async with client:
        result = await client.call_tool("is_holiday", {"date_input": date})
        holiday_info = json.loads(result[0].text)
        print(json.dumps(holiday_info, indent=2, ensure_ascii=False))

async def get_current_date():
    async with client:
        result = await client.call_tool("get_current_date")
        date_info = json.loads(result[0].text)
        print(json.dumps(date_info, indent=2, ensure_ascii=False))

async def get_all_birthdays():
    async with client:
        result = await client.read_resource("data://birthdays")
        birthdays_info = json.loads(result[0].text)
        print(json.dumps(birthdays_info, indent=2, ensure_ascii=False))

async def get_holiday_by_epoch(epoch: int):
    async with client:
        result = await client.read_resource(f"data://holidays/{epoch}")
        holiday_info = json.loads(result[0].text)
        print(json.dumps(holiday_info, indent=2, ensure_ascii=False))

async def get_all_holidays():
    async with client:
        result = await client.read_resource("data://holidays")
        holidays_info = json.loads(result[0].text)
        print(json.dumps(holidays_info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    # Test different functions
    # asyncio.run(check_holiday("01.01.2025"))
    # asyncio.run(get_current_date())
    # asyncio.run(get_all_birthdays())
    # asyncio.run(get_all_holidays())
    # asyncio.run(get_holiday_by_epoch(1735689600))