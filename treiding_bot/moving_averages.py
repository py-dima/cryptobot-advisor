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
    line = (f"{symbol}\r\n"
            f"EMA10: {moving_averages['COMPUTE']['EMA10']}\r\n"
            f"SMA10: {moving_averages['COMPUTE']['SMA10']}\r\n"
            f"EMA20: {moving_averages['COMPUTE']['EMA20']}\r\n"
            f"SMA20: {moving_averages['COMPUTE']['SMA20']}\r\n"
            f"EMA30: {moving_averages['COMPUTE']['EMA30']}\r\n"
            f"SMA30: {moving_averages['COMPUTE']['SMA30']}\r\n"
            f"EMA50: {moving_averages['COMPUTE']['EMA50']}\r\n"
            f"SMA50: {moving_averages['COMPUTE']['SMA50']}\r\n"
            f"EMA100: {moving_averages['COMPUTE']['EMA100']}\r\n"
            f"SMA100: {moving_averages['COMPUTE']['SMA100']}\r\n"
            f"EMA200: {moving_averages['COMPUTE']['EMA200']}\r\n"
            f"SMA200: {moving_averages['COMPUTE']['SMA200']}\r\n"
            f"Ichimoku: {moving_averages['COMPUTE']['Ichimoku']}\r\n"
            f"VWMA: {moving_averages['COMPUTE']['VWMA']}\r\n"
            f"HullMA: {moving_averages['COMPUTE']['HullMA']}\r\n\r\n"
            f"Загальна рекомендація MA: {moving_averages['RECOMMENDATION']}\r\n"
            f"Сигнали на покупку: {moving_averages['BUY']}\r\n"
            f"Нейстральні сигнали: {moving_averages['NEUTRAL']}\r\n"
            f"Сигнали на продаж: {moving_averages['SELL']}\r\n")
    return line

if __name__ == "__main__":
    symbol = "BTCUSDT"
    while True:
        moving_averages_data = get_moving_averages_data(symbol=symbol)
        recommendation = moving_averages_data['RECOMMENDATION']
        print(recommendation)

        if 'STRONG' in recommendation:
            # Формування звіту
            report = print_moving_averages_info(symbol=symbol, moving_averages=moving_averages_data)
            
            if recommendation == 'STRONG_BUY':
                report = f"\r\n\r\nКупляй!\r\n{report}"
            elif recommendation == 'STRONG_SELL':
                report = f"\r\n\r\nПродавай!\r\n{report}"
                
            send_telegram_message(message=report)
            print(report)

        time.sleep(60)