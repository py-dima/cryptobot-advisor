import time
from typing import Dict
from tradingview_ta import TA_Handler, Interval
from send_mes_tg import send_telegram_message

def get_moving_averages_data(symbol: str):
    handler = TA_Handler(
        symbol=symbol,
        screener="Crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_MINUTE
    )
    analysis = handler.get_analysis()
    return analysis.moving_averages

def print_moving_averages_info(symbol: str, moving_averages: Dict):
    line = (f"🔮 **Монета**: {symbol}\n\n"
            f"📊 **EMA10**: {moving_averages['COMPUTE']['EMA10']}\n"
            f"📊 **SMA10**: {moving_averages['COMPUTE']['SMA10']}\n"
            f"📊 **EMA20**: {moving_averages['COMPUTE']['EMA20']}\n"
            f"📊 **SMA20**: {moving_averages['COMPUTE']['SMA20']}\n"
            f"📊 **EMA30**: {moving_averages['COMPUTE']['EMA30']}\n"
            f"📊 **SMA30**: {moving_averages['COMPUTE']['SMA30']}\n"
            f"📊 **EMA50**: {moving_averages['COMPUTE']['EMA50']}\n"
            f"📊 **SMA50**: {moving_averages['COMPUTE']['SMA50']}\n"
            f"📊 **EMA100**: {moving_averages['COMPUTE']['EMA100']}\n"
            f"📊 **SMA100**: {moving_averages['COMPUTE']['SMA100']}\n"
            f"📊 **EMA200**: {moving_averages['COMPUTE']['EMA200']}\n"
            f"📊 **SMA200**: {moving_averages['COMPUTE']['SMA200']}\n"
            f"🌫️ **Ichimoku**: {moving_averages['COMPUTE']['Ichimoku']}\n"
            f"📈 **VWMA**: {moving_averages['COMPUTE']['VWMA']}\n"
            f"🏁 **HullMA**: {moving_averages['COMPUTE']['HullMA']}\n\n"
            f"⚡ **Загальна рекомендація MA**: {moving_averages['RECOMMENDATION']}\n"
            f"🟢 **Сигнали на покупку**: {moving_averages['BUY']}\n"
            f"⚪ **Нейтральні сигнали**: {moving_averages['NEUTRAL']}\n"
            f"🔴 **Сигнали на продаж**: {moving_averages['SELL']}\n")
    return line

def get_user_input():
    return input("Введіть символ монети (наприклад, BTCUSDT): ")

if __name__ == "__main__":
    symbol = get_user_input()
    while True:
        moving_averages_data = get_moving_averages_data(symbol=symbol)
        recommendation = moving_averages_data['RECOMMENDATION']
        print(recommendation)

        if 'STRONG' in recommendation:
            report = print_moving_averages_info(symbol=symbol, moving_averages=moving_averages_data)
            
            if recommendation == 'STRONG_BUY':
                report = f"🚀 **Купляй!**\n{report}"
            elif recommendation == 'STRONG_SELL':
                report = f"🔻 **Продавай!**\n{report}"
                
            send_telegram_message(message=report)
            print(report)

        time.sleep(60)
