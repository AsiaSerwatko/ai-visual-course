# Harmonogram wdrożenia

Od decyzji o uruchomieniu do pierwszej edycji: **12 tygodni**. Pilotaż w tygodniu 10, wnioski i poprawki w tygodniach 11–12. Daty na wykresie są przykładowe (start: styczeń 2027).

```mermaid
gantt
    title Wdrożenie kursu – 12 tygodni
    dateFormat  YYYY-MM-DD
    axisFormat  tydz. %W
    section Przygotowanie
    Walidacja popytu (ankieta, 10 rozmów)     :a1, 2027-01-04, 14d
    Rekrutacja trenera                        :a2, 2027-01-11, 21d
    section Program i materiały
    Finalizacja programu i efektów uczenia    :b1, after a1, 7d
    Materiały bloków 2–5                      :b2, after b1, 28d
    Przegląd prawny bloku 5                   :b3, after b1, 14d
    Próba generalna z trenerem                :b4, after b2, 3d
    section Sprzedaż
    Strona kursu, regulamin, płatności        :c1, after b1, 10d
    Kampania i zapisy na pilotaż              :c2, after c1, 28d
    Decyzja go/no go (min. 8 os.)             :milestone, m1, after c2, 0d
    section Realizacja
    Pilotaż                                   :d1, 2027-03-08, 5d
    Ewaluacja i poprawki                      :d2, after d1, 14d
```

## Kamienie milowe

| Tydzień | Kamień milowy | Kryterium akceptacji |
| --- | --- | --- |
| 2 | Popyt potwierdzony | min. 30 odpowiedzi w ankiecie, 10 rozmów, min. 40% deklaruje zainteresowanie w przedziale 2 000–3 000 zł |
| 4 | Trener zakontraktowany | lekcja próbna oceniona min. 4/5 |
| 7 | Materiały gotowe | prezentacje, notatki trenera, prompty dla 5 bloków; przegląd prawny bloku 5 |
| 8 | Sprzedaż uruchomiona | strona, regulamin, płatności, formularz zapisu |
| 9 | Go/no go | min. 8 opłaconych miejsc 10 dni przed startem |
| 10 | Pilotaż zrealizowany | frekwencja min. 80% |
| 12 | Wersja 1.0 | poprawki po ewaluacji, cennik regularny |

## RACI

| Zadanie | Koordynator | Trener | Marketing | Prawnik / księgowość |
| --- | --- | --- | --- | --- |
| Analiza potrzeb | A/R | C | C | |
| Program i efekty uczenia | A | R | | |
| Materiały | A | R | | C (blok 5) |
| Cennik, budżet | A/R | | C | C |
| Regulamin, umowy | A | | | R |
| Kampania, zapisy | A | C | R | |
| Logistyka edycji | A/R | I | | |
| Prowadzenie zajęć | I | A/R | | |
| Ewaluacja | A/R | C | I | |

R – realizuje, A – odpowiada, C – konsultowany, I – informowany.
