# README for Trading Bot

## Project Description

This project is created to automate cryptocurrency analysis and send trading signals via Telegram. The scripts use the `tradingview_ta` library to retrieve technical analysis data from the TradingView platform.

### Key Features:

- General cryptocurrency analysis.
- Moving average (MA) analysis with recommendations.
- Generating reports and sending messages via Telegram.

## Requirements

1. Python 3.8+
2. Required libraries:
   - `tradingview_ta`
   - `requests` (for sending messages via Telegram)

Install dependencies:

```bash
pip install tradingview-ta requests
```

## Project Structure

```
trading_bot/
├── Summary.py            # Retrieves general analysis
├── example.py            # Basic usage example of TA_Handler
├── moving_averages.py    # Moving averages analysis
├── new_code.py           # Advanced user functionality
├── send_mes_tg.py        # Module for sending messages to Telegram
```

## Usage Instructions

### 1. General Analysis

The `Summary.py` file constantly monitors the specified cryptocurrency symbol and sends a message to Telegram when a strong buy or sell signal is detected.

Run the command:

```bash
python Summary.py
```

---

### 2. Basic Usage Example

The `example.py` file demonstrates basic usage of the `tradingview_ta` library to retrieve an analysis summary.

Run the command:

```bash
python example.py
```

---

### 3. Moving Averages Analysis

The `moving_averages.py` file generates a detailed report on moving averages and sends it to Telegram if the recommendation has a strong signal.

Run the command:

```bash
python moving_averages.py
```

---

### 4. Advanced Functionality

The `new_code.py` file allows the user to manually input a coin symbol, after which the bot will analyze its moving averages and send the data to Telegram.

Run the command:

```bash
python new_code.py
```

## Telegram Setup

1. Create a bot via [BotFather](https://t.me/BotFather) on Telegram.
2. Get the access token.
3. Add the token and your user ID in the `.env` file:

```python
TELEGRAM_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
```

## Disclaimer

- The script is created for educational purposes. The author is not responsible for any damages associated with the use of this code.

## Contact

If you have any questions or suggestions, feel free to contact via email: [[dimazaluzhets@gmail.com](mailto:dimazaluzhets@gmail.com)].
