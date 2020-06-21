import pandas as pd
import AlgoTrader as at

path = \
    r'c:\Users\cmamon\Documents\GitHub\bigdikfactory\GeneticAlgo\Collectors\bitcoin_4h.csv'
data = pd.read_csv(path)

min_indicator = at.signals.Min(10, 3, 10, 3)
max_indicator = at.indicators.Max(10, 3, 10, 3)

min_signal = min_indicator(data)
max_features = max_indicator(data)

min_indicator.plot_candles(data, w='4h', plot_width=1500, plot_height=800)
min_indicator.plot_features()

# max_indicator.plot_candles(data, w='4h', fig=min_indicator.axis)
# max_indicator.plot_features()

min_indicator.show()

print('done')