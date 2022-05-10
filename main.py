import asyncio
from pytgcalls import idle
from driver.veez import call_py, STRING5, STRING4, STRING3, STRING2, STRING1
async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
