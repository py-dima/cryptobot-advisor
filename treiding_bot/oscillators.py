import time
from typing import Dict

from tradingview_ta import TA_Handler, Interval

from send_mes_tg import send_telegram_message

def get_oscillators_data(symbol: str):
    handler = TA_Handler(
        symbol=symbol,
        screener="Crypto",
        exchange="BINANCE",
        interval=Interval.INTERVAL_1_MINUTE
    )

    analysis = handler.get_analysis()
    return analysis.oscillators

def print_oscillator_info(symbol: str, oscillators: Dict):
    line = (f"{symbol}\r\n"
            f"ADX: {oscillators['COMPUTE']['ADX']}\r\n"
            f"AO: {oscillators['COMPUTE']['AO']}\r\n"
            f"BBP: {oscillators['COMPUTE']['BBP']}\r\n"
            f"CCI: {oscillators['COMPUTE']['CCI']}\r\n"
            f"MACD: {oscillators['COMPUTE']['MACD']}\r\n"
            f"Mom: {oscillators['COMPUTE']['Mom']}\r\n"
            f"RSI: {oscillators['COMPUTE']['RSI']}\r\n"
            f"Stochastic %k: {oscillators['COMPUTE']['STOCH.K']}\r\n"
            f"Stoch.RSI: {oscillators['COMPUTE']['UO']}\r\n"
            f"W%R: {oscillators['COMPUTE']['W%R']}\r\n\r\n"
            f"Загальна рекомендація осциляторів: {oscillators['RECOMMENDATION']}\r\n"
            f"Сигнали на покупку: {oscillators['BUY']}\r\n"
            f"Нейстральні сигнали: {oscillators['NEUTRAL']}\r\n"
            f"Сигнали на продаж: {oscillators['SELL']}\r\n")
    return line

if __name__ == "__main__":
    symbol = "BTCUSDT"
    while True:
        # Виправлено ім'я змінної (osccillators_data -> oscillators_data)
        oscillators_data = get_oscillators_data(symbol=symbol)
        recommendation = oscillators_data['RECOMMENDATION']
        print(recommendation)

        if 'STRONG' in recommendation:
            # Передається правильна змінна (oscillators_data замість oscillators)
            report = print_oscillator_info(symbol=symbol, oscillators=oscillators_data)
            
            # Додаємо рекомендацію до вже існуючого звіту
            if recommendation == 'STRONG_BUY':
                report += f"\r\n\r\nКупляй!"
            elif recommendation == 'STRONG_SELL':
                report += f"\r\n\r\nПродавай!"

            send_telegram_message(message=report)
            print(report)

        time.sleep(60)