# Projekt Dashboardu Analizy Danych

## Opis
Projekt polega na przygotowaniu interaktywnego dashboardu do analizy danych na podstawie danych zawartych w pliku `messy_data.csv`.

## Etapy Pracy

### 1. Wstępna Analiza Danych i Czyszczenie
   -  Usuwanie duplikatów.
   - Identyfikacja i obsługa wartości odstających.
   - Zapewnienie spójności danych.
   - Obsługa brakujących danych.
   - Dostosowanie skali wartości.
   - Inne czynności wstępnej analizy danych.

### 2. Wizualizacja Rozkładu Zmiennych i Zależności
   - Rozkład zmiennych.
   - Zależność ceny od innych zmiennych.
   - Liczebność kategorii.

### 3. Budowa Modelu Regresji
   - Budowa modelu regresji ceny od pozostałych zmiennych.
   - Selekcja istotnych zmiennych eliminacją wsteczną lub selekcją postępującą.

### 4. Wizualizacja Modelu Regresji

### 5. Tworzenie Dashboardu
   - Implementacja dashboardu z powyższymi wizualizacjami.
   - Dodanie możliwości zmiany parametrów wykresów przez użytkownika, np. wybór zmiennej do analizy.

### W projekcie utworzono następujące katalogi:
- `messy_data.csv`: zawiera pliki z danymi.
- `proj_s20468.ipynb`: zawiera skrypty Pythona odpowiedzialne za przetwarzanie danych, wizualizację, budowę modelu regresji i tworzenie dashboardu.
- `dashboard.py`: zawiera skrypty Pythona odpowiedzialne za uruchomienie streamlit dashboardu.
- `PAD_praca_domowa.docx`: zawiera treść zadania
- `README.md`: plik zawierający instrukcje dotyczące projektu.

## Wymagania
- Python 3.9
- Pakiety Pythona: pandas, numpy, matplotlib, seaborn, plotly, streamlit, statsmodels

## Uruchomienie
1. Sklonuj repozytorium na swój lokalny komputer.
2. Zainstaluj wymagane pakiety Pythona za pomocą polecenia `pip install ...`.
3. Uruchom skrypty z katalogu `proj_s20468.ipynb` zgodnie z kolejnością opisaną w sekcji "Etapy Pracy".
4. Uruchom dashboard streamlit z katalogu `dashboard.py` za pomocą polecenia `streamlit run dashboard.py`.

## Autor
Autor: Siarhei Vilchuk
