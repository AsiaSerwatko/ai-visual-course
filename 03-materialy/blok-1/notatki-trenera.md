# Blok 1. Fundamenty – notatki trenera

Czas: 3 h (2 h 50 min zajęć + 10 min przerwy). Grupa do 12 osób.

## Cel bloku

Po bloku uczestnik:

- wyjaśnia, dlaczego ten sam prompt daje różne wyniki i do czego służy seed,
- dobiera narzędzie do zadania (obraz, wideo, edycja, audio),
- opisuje kadr językiem fotografa (plan, kąt, ogniskowa, światło, kompozycja),
- ma moodboard kampanii NORDA i 3 słowa stylu + 3 słowa antystylu.

## Przygotowanie przed zajęciami

- [ ] Deck bloku 1 otwarty, tryb prezentacji przetestowany
- [ ] Zalogowane konta: Midjourney (plan z trybem Fast), Flow, Kling, Firefly
- [ ] Notebook [`seed-i-losowosc.ipynb`](seed-i-losowosc.ipynb) uruchomiony wcześniej – obrazy zapisane w folderze `wyniki/` na wypadek braku sieci
- [ ] 6 reklam do analizy kadru (własne zrzuty ekranu z kampanii; nie wrzucać ich do narzędzi AI)
- [ ] Folder wspólny lub tablica Miro z sekcją „Moodboardy” i miejscem dla każdego uczestnika
- [ ] Wydrukowany lub wysłany brief NORDA ([`brief-NORDA-i-projekt-koncowy.md`](../brief-NORDA-i-projekt-koncowy.md))
- [ ] Lista obecności, ankieta wstępna (poziom doświadczenia z AI 1–5)

## Scenariusz

### 0:00–0:15 Otwarcie (slajdy 1–4)

- Przedstaw się w 1 minucie: doświadczenie, 1 realny projekt z AI.
- Runda: imię, rola, czego najbardziej chcesz się nauczyć (maks. 20 s na osobę).
- Kontrakt: telefony wyciszone, pytania w każdej chwili, prace uczestników zostają w grupie.
- Pokaż efekt końcowy kursu: spot i kreacje z poprzedniej edycji lub przygotowany przykład NORDA.
- Przedstaw brief NORDA. Podkreśl: **cały kurs to jedna kampania**, każdy blok dokłada element.

**Komunikat kluczowy:** „Nie uczymy się klikania w narzędzia. Uczymy się podejmować decyzje wizualne, a narzędzia je wykonują.”

### 0:15–0:45 Jak działa generowanie (slajdy 5–10)

Wyjaśnienie modelu dyfuzyjnego bez matematyki:

1. Model był trenowany na parach obraz + opis. Nauczył się, jak „odszumiać” obraz w kierunku opisu.
2. Generowanie zaczyna się od losowego szumu. Model w kilkunastu–kilkudziesięciu krokach usuwa szum, kierując się promptem.
3. **Seed** to liczba, z której powstaje ten startowy szum. Ten sam prompt + ten sam seed + te same ustawienia = ten sam (lub bardzo podobny) obraz.
4. Inny seed = inny punkt startu = inna kompozycja, mimo tego samego promptu.

**Pokaz (notebook, eksperyment 1):** ten sam prompt, 4 seedy. Zapytaj grupę: „Który obraz jest poprawny?” Odpowiedź: każdy, bo prompt ich nie rozróżnia. Wniosek: im mniej decyzji w prompcie, tym więcej decyduje los.

**Pokaz (notebook, eksperyment 2):** stały seed, zmiana jednego elementu (światło). Wniosek: przy stałym seedzie zmiana promptu daje kontrolowaną zmianę – podstawa iterowania.

**Uwaga merytoryczna:** w narzędziach z interfejsem (Midjourney, Flow) seed jest zwykle ukryty lub ma ograniczone działanie. Dlatego pokazujemy go w notebooku, gdzie mamy pełną kontrolę.

**Pytania, które padają:**

- *„Czy AI kopiuje obrazy z internetu?”* – Model nie przechowuje obrazów jak baza danych; uczy się wzorców. Może jednak odtworzyć bardzo znane obrazy, postacie i style – stąd ryzyka prawne (blok 5).
- *„Dlaczego dłonie i napisy wychodzą źle?”* – To trudne struktury o wielu poprawnych wariantach; nowsze modele radzą sobie lepiej, ale kontrola jakości nadal jest obowiązkowa (blok 3).

### 0:45–1:15 Mapa narzędzi (slajdy 11–15)

Pokaż tabelę narzędzi. Dla każdego: do czego, mocne strony, ograniczenia, koszt, licencja.

| Zadanie | Narzędzie | Kiedy wybrać |
| --- | --- | --- |
| Obraz – estetyka, styl | Midjourney | kampanie wizerunkowe, moodboardy |
| Obraz – edycja, bezpieczeństwo licencji | Adobe Firefly + Photoshop | praca z realnym produktem, klienci korporacyjni |
| Obraz – edycja poleceniem, tekst w obrazie | Gemini (Nano Banana), GPT Image, Ideogram | szybkie warianty, napisy |
| Wideo z obrazu | Kling, Veo (Flow), Runway | ujęcia do spotów |
| Montaż | DaVinci Resolve, CapCut, Runway | składanie spotu |
| Audio | ElevenLabs (lektor), Suno (muzyka) | ścieżka dźwiękowa |
| Automatyzacja, API | fal.ai, Replicate, Gemini API | duże wolumeny, własne workflow |

**Kryteria wyboru (zapisz na flipcharcie):** jakość → kontrola → licencja → prywatność → koszt.

**Ćwiczenie 5 min:** w parach przypiszcie narzędzie do 4 zadań NORDA (moodboard, baner z puszką, ujęcie z parą nad kubkiem, lektor). Omówienie: nie ma jednej poprawnej odpowiedzi, liczy się uzasadnienie.

**Aktualizacja:** ceny i nazwy modeli zmieniają się co kilka tygodni. Przed każdą edycją sprawdź slajd z narzędziami.

### 1:15–1:25 Przerwa

### 1:25–2:05 Język obrazu (slajdy 16–22)

Kolejno: plany, kąt kamery, ogniskowa, głębia ostrości, światło, kompozycja. Na każdym slajdzie 1 pojęcie + 2 przykłady + odpowiednik w prompcie po angielsku.

**Ćwiczenie „opisz kadr” (20 min):**

1. Pokaż 6 reklam po kolei (po 2–3 min).
2. Uczestnicy zapisują opis kadru: plan, kąt, ogniskowa, światło, kompozycja, nastrój.
3. Losowo 2 osoby czytają opis, grupa ocenia, czy da się z niego odtworzyć kadr.

**Wniosek:** dobry prompt to opis, z którego fotograf mógłby zrobić zdjęcie. Przymiotniki typu „piękny, niesamowity, 8k” niewiele dają.

### 2:05–2:45 Ćwiczenie: moodboard NORDA (slajdy 23–24)

1. Uczestnicy startują od promptu bazowego (biblioteka promptów, P1.1).
2. Każdy generuje 12–16 obrazów, zmieniając po jednym elemencie (miejsce, światło, kadr).
3. Wybiera 4 najlepsze i zapisuje przy każdym jedno zdanie: dlaczego pasuje do briefu.
4. Wrzuca do folderu wspólnego / Miro.

**Rola trenera:** chodź po sali (lub sprawdzaj ekrany w pokojach). Najczęstsze interwencje:

- uczestnik losuje bez zmiany promptu → „Co konkretnie chcesz zmienić?”
- prompt to lista przymiotników → „Gdzie stoi kamera? Skąd pada światło?”
- wybór „bo ładne” → „Które słowo z briefu ten obraz realizuje?”

**Koszt:** 16 obrazów w Midjourney to ok. 16 min Fast GPU na osobę (Basic ma ok. 200 obrazów/mies.). Uczestnicy na Basic mogą wykorzystać ok. 8% miesięcznego limitu.

### 2:45–3:00 Prezentacje i zadanie domowe (slajdy 25–26)

- 3 osoby pokazują moodboard (po 3 min). Feedback: co jest spójne, co odstaje od briefu.
- Zadanie domowe: 3 słowa stylu i 3 słowa antystylu dopisane do briefu.
- Zapowiedź bloku 2: „Z moodboardu robimy kampanię”.

## Plan awaryjny

| Problem | Rozwiązanie |
| --- | --- |
| Midjourney nie działa / kolejka | Moodboard w Firefly lub Gemini; Midjourney w domu |
| Uczestnik bez konta | Praca w parze z inną osobą |
| Brak sieci | Pokaz z gotowych wyników notebooka (`wyniki/`), ćwiczenie „opisz kadr” rozszerzone do 35 min |
| Grupa zaawansowana | Dodatkowo: parametry --sref, --s, --chaos w Midjourney |
| Grupa bardzo początkująca | Skrócić mapę narzędzi do 15 min, wydłużyć moodboard |

## Materiały bloku

- Deck: Blok 1 – Fundamenty (Slides)
- Notebook: [`seed-i-losowosc.ipynb`](seed-i-losowosc.ipynb)
- Biblioteka promptów: [`biblioteka-promptow.md`](../biblioteka-promptow.md), sekcja Blok 1
- Brief: [`brief-NORDA-i-projekt-koncowy.md`](../brief-NORDA-i-projekt-koncowy.md)
