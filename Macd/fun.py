import matplotlib.pyplot as plt


def open_file(data):
    Date = data['Data'].to_numpy()
    Open = data['Otwarcie'].to_numpy()
    High = data['Najwyzszy'].to_numpy()
    Low = data['Najnizszy'].to_numpy()
    Closed = data['Zamkniecie'].to_numpy()
    Volume = data['Wolumen'].to_numpy()

    return [Date, Open, High, Low, Closed, Volume]

def EMA(N, tab, i):
    alfa = 2 / (N + 1)
    sum = 0
    dziel = 0
    shift = max(0, i - N + 1)
    index = 0
    while index < N and i - index >= shift:
        sum += tab[i - index] * pow(1 - alfa, index)
        dziel += pow(1 - alfa, index)
        index += 1
    ema = sum / dziel
    return ema

def MACD(i, tab):
    EMA_12 = EMA(11, tab, i)
    EMA_26 = EMA(25, tab, i)
    return EMA_12 - EMA_26

def SIGNAL(i, MACD_tab):
    return EMA(8, MACD_tab, i)

def intersection_points(MACD_data, SIGNAL_data, N):
    buy = [[],[]]
    sell = [[],[]]
    MACD_up = True

    for i in range(N):
        if(MACD_up == True and MACD_data[i] < SIGNAL_data[i]):
            MACD_up = False
            sell[0].append(i + 33)
            sell[1].append(SIGNAL_data[i])
        elif(MACD_up == False and MACD_data[i] > SIGNAL_data[i]):
            MACD_up = True
            buy[0].append(i + 33)
            buy[1].append(SIGNAL_data[i])

    return buy, sell

def MACD_create_data(size, data_closed, start):
    new_data = []
    for i in range(start, size):
        value = MACD(i, data_closed)
        new_data.append(value)
    return new_data

def SIGNAL_create_data(size, data_closed, start):
    new_data = []
    for i in range(start, size):
        value = SIGNAL(i, data_closed)
        new_data.append(value)
    return new_data

def graph(x, y, x_macd, MACD_data, SIGNAL_data, buy, sell):

    plt.figure(figsize=(10, 6))  # Ustawienie rozmiaru wykresu
    plot_data(x, y, title='Cena zamknięcia akcji', xlabel='Data', ylabel='Cena', linestyle='-')
    plt.xlim(min(x_macd), max(x_macd))
    # Ustawienie rozmiaru wykresu
    plt.figure(figsize=(10, 6))

    # Wskaźnik MACD
    plot_data(x_macd, MACD_data, title='Wskaźnik MACD i Signal', xlabel='Data', ylabel='Wartość', linestyle='-',
              label='MACD')

    # Wskaźnik Signal
    plot_data(x_macd, SIGNAL_data,title='Wskaźnik MACD i Signal',  xlabel='Data', ylabel='Wartość', linestyle='-', color='r', label='Signal')

    plt.xlim(min(x_macd), max(x_macd))

    # Dodanie punktów kupna i sprzedaży
    plt.scatter(buy[0], buy[1], color='green', marker='o', label='punkty kupna', s = 80, zorder=3)
    plt.scatter(sell[0], sell[1], color='red', marker='^', label='punkty sprzedaży', s = 80, zorder=3)


    plt.legend()
    plt.show()


def plot_data(x, y, title='', xlabel='', ylabel='', linestyle='-', color='b', marker=None, label=None):
    plt.plot(x, y, linestyle=linestyle, color=color, marker=marker, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

def buy_sell(buy_sell_tab, gold):
    shares = 0
    wallet = []
    if buy_sell_tab[len(buy_sell_tab) - 1][0] == 'BUY':
        buy_sell_tab = buy_sell_tab[:len(buy_sell_tab) - 1]

    for elem in buy_sell_tab:
        if elem[0] == 'BUY':
            gold, shares = buy(gold, elem[1], shares)
        else:
            gold, shares = sell(gold, elem[1], shares)
            test(gold, elem[1], shares)
            wallet.append(gold)
    while shares > 0:
        gold += buy_sell_tab[len(buy_sell_tab) - 1][1]
        shares -= 1

    return gold, wallet

def test(gold, price, shares):
    gold2 = gold
    shares2 = shares
    while shares2 > 0:
        gold2 += price
        shares2 -= 1
    print(" gold :" + str(gold2))
def buy(gold, price, shares):
    while gold > price:
        shares += 1
        gold -= price
    return gold, shares
def sell(gold, price, shares):
    while shares > 0:
        shares -= 1
        gold += price
    return gold, shares

def plot_wallet(wallet):
    transaction_indices = range(len(wallet))
    plt.plot(transaction_indices, wallet, marker='o')
    plt.xlabel('Indeks transakcji')
    plt.ylabel('Ilosc pieniedzy')
    plt.title('Historia Portfela')
    plt.grid(True)
    plt.show()