# trading-bot-example

First, make a virtual environment:
```bash
python -m venv venv
```
Then, activate the environment: 
```bash 
source venv/bin/activate
```
Or on Windows (Powershell):
```bash
venv\Scripts\activate
```

To install the package to easily make games, run the following:
```bash
pip install huqtoracleclient==0.4.0
```

To write a handler for events that are streamed from the exchange server, fill out these functions:
```python
def handle_md_update(self, data):
    ...
    
def handle_open_orders_update(self, data):
    ...

def handle_positions_update(self, data):
    ...

def handle_fill_update(self, data):
    ...

def handle_recent_fills(self, data):
    ...

def handle_exchange_status_update(self, data):
    ...
```

To send and cancel orders, call these functions:
```python
def submit_order(self, symbol: str, logging: str, size: int, price: int, side: OrderSide, tif: OrderTif) -> Response:
    
def cancel_order(self, order_id: str) -> Response:

def cancel_orders(self, order_ids: List[str]) -> ResponseList:
```

You are allowed to add some logging to your order submission - you can view the information you logged in your open orders. Please note that currently you are only allowed at most 100 characters of logging.

Important Notes:
* all prices are in cents (integer number of cents)
* the lower_bound and upper_bound are in floats, so that they can equal +-infinity
