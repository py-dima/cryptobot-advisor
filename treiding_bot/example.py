from tradingview_ta import TA_Handler, Interval

SYMBOL = "LTCUSDT"

handler = TA_Handler(symbol=SYMBOL,
                     screener="Crypto",
                     exchange='MEXC',
                     interval=Interval.INTERVAL_1_MINUTE)

print(handler.get_analysis().summary)