import asyncio
from fastmcp import Client
import json

client = Client("main.py")

async def check_holiday(date):
    async with client:
        result = await client.call_tool("is_holiday", {"date_input": date})
        holiday_info = json.loads(result[0].text)
        print(json.dumps(holiday_info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(check_holiday("01.01.2025")