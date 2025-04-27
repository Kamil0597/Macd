# MACD Calculator

Projekt napisany w języku python do analizowania danych cen kursów akcji za pomocą wskaźnika **MACD** (Moving Average Convergence Divergence) oraz **SIGNAL**.
Aplikacja identyfikuje sygnały kupna i sprzedaży na podstawie przecięć **MACD** i **SIGNAL**.

## Funkcjonalności

- Wczytywanie danych giełdowych z pliku CSV (np. ceny akcji).
- Obliczanie wskaźnika MACD oraz linii SIGNAL.
- Wykrywanie punktów przecięcia MACD i SIGNAL (sygnały kupna/sprzedaży).
- Rysowanie wykresów cen akcji oraz wykresów MACD i SIGNAL z zaznaczonymi punktami kupna/sprzedaży.
- Symulowanie handlu akcjami na podstawie wykrytych sygnałów kupna i sprzedaży.
- Śledzenie i wykres historii stanu portfela po każdej transakcji.


## Wymagania

Aby uruchomić projekt, musisz mieć zainstalowane następujące biblioteki:

- `pandas`
- `matplotlib`

Możesz je zainstalować za pomocą polecenia:

```bash
pip install pandas matplotlib
```

## Przykładowe dane

W projekcie znajdują się przykładowe pliki `.csv` z historycznymi danymi giełdowymi dla kilku spółek:

- **AMZN.csv** — Amazon
- **DELL.csv** — Dell Technologies
- **INTC.csv** — Intel
- **META.csv** — Meta Platforms
- **TSLA.csv** — Tesla
- **cdr_d.csv** — CD Projekt

Domyślnie wczytywany jest plik **AMZN.csv** (Amazon).

Plik można uruchomić za pomocą będąc w folderze pliku:
```bash
python main.py
```

#Wynik

Kod zwraca trzy wykresy:
- Wykres cen
- Wykres z zaznaczonymi punktami kupna i sprzedaży
- Wykres ilości pieniędzy w portfelu po każdej transakcji.
