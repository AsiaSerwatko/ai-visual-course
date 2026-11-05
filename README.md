# Grafika i wideo AI dla marketingu - projekt kursu

Kompletny projekt kursu szkoleniowego: od analizy potrzeb, przez program i materiały, po model cenowy, plan wdrożenia i ewaluację. Repozytorium jest częścią mojego portfolio jako **IT Training Coordinator**.

> **Stan:** listopad 2026 · ceny narzędzi i rynku zweryfikowane w październiku 2026

## W skrócie

| | |
| --- | --- |
| Grupa docelowa | marketingowcy, social media managerowie, właściciele małych firm |
| Format | online na żywo, 16 h w 5 blokach + opcjonalny projekt końcowy (4 h) |
| Wielkość grupy | 8–12 osób na trenera |
| Efekt dla uczestnika | gotowa kampania do portfolio: moodboard, kreacje w 4 formatach, spot 15 s, checklista zgodności z AI Act |
| Rekomendowana cena | **2 690 zł netto/os.** (z pakietem narzędzi na miesiąc) |
| Próg rentowności | 6 uczestników na edycję; rekomendowane minimum uruchomienia: 8 |
| Marża przy 12 os. | ok. 46% |

## Problem, który rozwiązuje kurs

Generatywne AI weszło do codziennej pracy marketingu: 49% marketerów na świecie używa AI codziennie do tworzenia obrazów i wideo ([Canva / Morning Consult, 2025](https://emarketer.com/content/almost-majority-of-marketers-use-ai-create-images-videos)). Jednocześnie brak przeszkolenia zespołu to najczęściej wskazywana bariera wdrożenia (50% firm, [Botco.ai via MarTech](https://martech.org/73-of-marketers-now-using-generative-ai-tools/)). Narzędzia są złożone, wynik zależy od wiedzy o kadrze, świetle i kompozycji, a od 2 sierpnia 2026 dochodzą obowiązki oznaczania treści z AI Act. Kurs uczy robić to profesjonalnie, a nie generować „AI slop”.

Szczegóły: [analiza potrzeb i rynku](01-analiza-potrzeb/analiza-rynku.md).

## Zawartość repozytorium

| Folder | Co zawiera | Kompetencja koordynatora |
| --- | --- | --- |
| [01-analiza-potrzeb](01-analiza-potrzeb/) | uzasadnienie, persony, konkurencja i ceny rynkowe | analiza potrzeb szkoleniowych |
| [02-program](02-program/) | sylabus, efekty uczenia, scenariusze 5 bloków minuta po minucie | projektowanie programu |
| [03-materialy](03-materialy/) | brief kampanii, biblioteka promptów, notatki trenera i notebook do bloku 1 | przygotowanie materiałów |
| [04-biznes](04-biznes/) | cennik, budżet narzędzi, kalkulator rentowności | budżetowanie i wycena |
| [05-operacje](05-operacje/) | harmonogram wdrożenia, logistyka, profil trenera, rejestr ryzyk | organizacja i realizacja |
| [06-ewaluacja](06-ewaluacja/) | model Kirkpatricka, KPI, ankieta poszkoleniowa | ocena jakości i efektywności |
| [07-prawo](07-prawo/) | checklista zgodności: AI Act, wizerunek, prawa autorskie, licencje, umowa z klientem | zgodność i ryzyko prawne |
| [docs](docs/) | prezentacje (PDF) | materiały dydaktyczne |

## Jak korzystać

- Dokumenty to pliki Markdown, czytelne bezpośrednio na GitHubie.
- Kalkulator: `python 04-biznes/kalkulator_rentownosci.py` (Python 3.8+, bez dodatkowych pakietów). Założenia zmienia się w słowniku `ZALOZENIA`.
- Notebook bloku 1: Jupyter lub Google Colab. Działa w trybie demo bez klucza API; z kluczem fal.ai pokaz kosztuje poniżej 0,10 USD.

## Status prac

- [x] Analiza potrzeb, program, scenariusze wszystkich bloków
- [x] Model cenowy i kalkulacja rentowności
- [x] Plan wdrożenia, ewaluacja, checklista prawna
- [x] Materiały bloku 1: prezentacja, notatki trenera, notebook, prompty
- [ ] Materiały bloków 2–5 (prezentacje, notatki trenera, prompty)
- [ ] Pilotaż i wyniki ewaluacji

## Uwagi

- Marka NORDA w ćwiczeniach jest fikcyjna.
- Materiały powstały z wykorzystaniem narzędzi AI. Zostały zweryfikowane, a dane rynkowe opatrzone źródłami.
- Ceny narzędzi i usług zmieniają się często. Przed użyciem sprawdź aktualne cenniki.

## English summary

A complete design of a 16-hour live online course on AI-generated images and video for marketers: needs analysis, syllabus, minute-by-minute session plans, trainer notes, a Jupyter demo notebook, pricing strategy with a break-even calculator, rollout plan, risk register, Kirkpatrick-based evaluation, and an EU AI Act compliance checklist. Portfolio project for an IT Training Coordinator role. Content in Polish.

## Licencja

Treści: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl). Kod (`.py`, `.ipynb`): MIT. Szczegóły w [LICENSE.md](LICENSE.md).
