import time

from tradingview_ta import TA_Handler

from send_mes_tg import send_telegram_message

def get_analisis_summary(symbol: str):
    handler = TA_Handler(symbol=symbol,
                     screener="Crypto",
                     exchange='MEXC',
                     interval="1m")
    analysis = handler.get_analysis()
    return analysis.summary

if __name__ == "__main__":
    symbol = "LTCUSDT"
    while True:
        anasysis_summary = get_analisis_summary(symbol=symbol)
        recomendation = anasysis_summary['RECOMMENDATION']
        print(recomendation)
        if 'STRONG' in recomendation:
            report = f'{symbol}'
            if recomendation == 'STRONG_BUY':
                report += '\r\nBuy'
            elif recomendation == 'STRONG_SELL':
                report += '\r\nSell'
            print(report)
            send_telegram_message(message=report)
        time.sleep(60)