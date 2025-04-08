import asyncio
from huqt_oracle_client import AdvancedTrader
import time

class MyTrader(AdvancedTrader):
    def __init__(self, account, api_key, url, secure = True):
        super().__init__(account, api_key, url, secure)

    def handle_md_update(self, data):
        print(data)
    
    def handle_open_orders_update(self, data):
        print(data)
    
    def handle_positions_update(self, data):
        print(data)
    
    def handle_fill_update(self, data):
        print(data)
    
    def handle_recent_fills(self, data):
        print(data)
    
    def handle_exchange_status_update(self, data):
        print(data)
    
async def listen(t: MyTrader):
    await t.listen()

async def trade(t: MyTrader):
    while True:
        await asyncio.sleep(1)
    
async def main():
    ACCOUNT = ""
    API_KEY = ""
    EXCHANGE_URL = ""
    t = MyTrader(ACCOUNT, API_KEY, EXCHANGE_URL, secure=True)
    listener_task = asyncio.create_task(listen(t))
    trade_task = asyncio.create_task(trade(t))
    await asyncio.gather(listener_task, trade_task)
if __name__ == '__main__':
    asyncio.run(main())
    # main()