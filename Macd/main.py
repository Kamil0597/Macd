import pandas as pd

from fun import open_file, intersection_points, buy_sell, graph, MACD_create_data, SIGNAL_create_data, plot_wallet

if __name__ == '__main__':
    SIZE = 1000

    DATA = 0
    OPEN = 1
    HIGHER = 2
    LOWER = 3
    CLOSED = 4
    VOLUME = 5

    data = pd.read_csv('AMZN.csv')
    data = data[:SIZE]
    Date, Open, High, Low, Closed, Volume = open_file(data)

    x = list(range(SIZE))
    x_macd = x[25:]

    MACD_data = MACD_create_data(SIZE, Closed, 25)             # stworzenie MACD
    MACD_data_len = len(MACD_data)
    SIGNAL_data = SIGNAL_create_data(MACD_data_len, MACD_data, 8)       # stworzenie SIGNAL

    MACD_data = MACD_data[8:]
    buy, sell = intersection_points(MACD_data, SIGNAL_data, len(MACD_data)) # punkty sprzedaży i kupna akcji z MACD i SIGNAL

    x_macd = x_macd[8:]
    y = Closed
    graph(x, y, x_macd, MACD_data, SIGNAL_data, buy, sell)                     # stworzenie wykresów

    gold = 1000
    buy_sell_tab = []
    indexB = 0
    indexS = 0
    for i in range(33, SIZE):
        if indexB < len(buy[0]) and buy[0][indexB] == i:
            buy_sell_tab.append(('BUY', Closed[i]))            # Dodanie informacji o kupnie
            indexB += 1
        elif indexS < len(sell[0]) and sell[0][indexS] == i:
            buy_sell_tab.append(('SELL', Closed[i]))          # Dodanie informacji o sprzedaży
            indexS += 1

    gold, wallet = buy_sell(buy_sell_tab, gold)
    print("Ostateczny kapitał: ")
    print(gold)
    plot_wallet(wallet)