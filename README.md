# TON Scraper
Python script that parses the TON to USD exchange rate

Follow these steps to run main.py and set up the necessary dependencies:

### Step 1: Install Dependencies

You will need to install the necessary dependencies for the script to run. You can do this using pip:

```bash
pip install -r requirements.txt
```

### Step 2: Setting Up .env File

Create a .env file in the same directory as your main.py file. This file will contain the necessary parameters for the script to run. Here are the parameters you need to include:

.env
```
MARKET_TOKEN=""
BOT_TOKEN=""
CHAT_ID=""
```

- MARKET_TOKEN: This is your Market API token from [CoinMarketCap](https://coinmarketcap.com/).
- BOT_TOKEN: This is your Telegram bot token.
- CHAT_ID: This is the ID of the chat where the bot will send the message.


### Step 3: Running the Script

After setting up the dependencies and the .env file, you can now run the script:

```bash
python main.py
```

That's it!