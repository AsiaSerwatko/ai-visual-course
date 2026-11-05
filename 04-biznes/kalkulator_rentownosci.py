"""Kalkulator rentowności jednej edycji kursu „Grafika i wideo AI dla marketingu”.

Uruchomienie:  python kalkulator_rentownosci.py
Zmień założenia w słowniku ZALOZENIA i uruchom ponownie. Wszystkie kwoty netto w PLN.
Wymaga tylko Pythona 3.8+ (bez dodatkowych pakietów).
"""

ZALOZENIA = {
    # Ceny (netto za osobę)
    "warianty_cen": {
        "Online 16 h, bez narzędzi": {"cena": 2290, "narzedzia": False, "projekt": False},
        "Online 16 h + narzędzia (rekomendowany)": {"cena": 2690, "narzedzia": True, "projekt": False},
        "Online 20 h + narzędzia + projekt": {"cena": 3190, "narzedzia": True, "projekt": True},
    },
    # Koszty zmienne na uczestnika
    "narzedzia_na_osobe": 200,          # pakiet rekomendowany ok. 50 USD x 4,0 PLN
    "oplata_platnicza_proc": 0.015,     # bramka płatności / obsługa faktur
    "materialy_certyfikat_na_osobe": 30,
    "konsultacja_projektu_h_na_osobe": 1,
    # Koszty stałe edycji
    "stawka_trenera_h": 250,
    "godziny_zajec": 16,
    "aktualizacja_materialow_h": 4,     # ceny i narzędzia zmieniają się co kilka tygodni
    "koordynacja_h": 20,
    "stawka_koordynatora_h": 120,
    "platforma_lms_zoom": 400,
    "marketing_edycji": 3000,
    # Koszt jednorazowy (amortyzowany)
    "opracowanie_materialow_h": 80,
    "konta_trenera_na_rozwoj": 1000,
    "liczba_edycji_amortyzacji": 6,
}


def koszt_staly(z, projekt):
    # Projekt końcowy to praca własna uczestnika; konsultacje liczone w kosztach zmiennych.
    trener = (z["godziny_zajec"] + z["aktualizacja_materialow_h"]) * z["stawka_trenera_h"]
    koordynacja = z["koordynacja_h"] * z["stawka_koordynatora_h"]
    amortyzacja = (z["opracowanie_materialow_h"] * z["stawka_trenera_h"] + z["konta_trenera_na_rozwoj"]) / z["liczba_edycji_amortyzacji"]
    return trener + koordynacja + z["platforma_lms_zoom"] + z["marketing_edycji"] + amortyzacja


def koszt_zmienny(z, wariant):
    k = wariant["cena"] * z["oplata_platnicza_proc"] + z["materialy_certyfikat_na_osobe"]
    if wariant["narzedzia"]:
        k += z["narzedzia_na_osobe"]
    if wariant["projekt"]:
        k += z["konsultacja_projektu_h_na_osobe"] * z["stawka_trenera_h"]
    return k


def raport(z=ZALOZENIA, grupy=(6, 9, 12)):
    print("Kalkulacja jednej edycji (PLN netto)\n")
    for nazwa, w in z["warianty_cen"].items():
        ks = koszt_staly(z, w["projekt"])
        kz = koszt_zmienny(z, w)
        marza_jedn = w["cena"] - kz
        prog = ks / marza_jedn
        print(f"== {nazwa}: {w['cena']} zł/os.")
        print(f"   koszty stałe edycji: {ks:,.0f} zł | koszt zmienny/os.: {kz:,.0f} zł | marża/os.: {marza_jedn:,.0f} zł")
        print(f"   próg rentowności: {prog:.1f} os. (min. {int(-(-prog // 1))} uczestników)")
        for n in grupy:
            przychod = n * w["cena"]
            zysk = przychod - ks - n * kz
            print(f"   {n:>2} os.: przychód {przychod:>7,.0f} | zysk {zysk:>7,.0f} | marża {zysk / przychod:>5.0%}")
        print()


if __name__ == "__main__":
    raport()
