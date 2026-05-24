import asyncio
from analytics import (
    get_summary,
    get_category_summary,
    get_daily_summary,
    get_monthly_summary
)


async def main():

    user_id = 1

    print("Overall summary:")
    print(await get_summary(user_id))

    print("\nCategory summary:")
    print(await get_category_summary(user_id))

    print("\nDaily summary:")
    print(await get_daily_summary(user_id))

    print("\nMonthly summary:")
    print(await get_monthly_summary(user_id))


if __name__ == "__main__":
    asyncio.run(main())