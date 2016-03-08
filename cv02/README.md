Cvičenie 2
==========

Riešenie prvého cvičenia odovzdávajte do **utorka 8.3. 23:59:59**.

Riešenie tohto cvičenia (úloha [Sudoku](#sudoku-3b)) odovzdávajte
do <del>**utorka 8.3. 23:59:59**</del> **štvrtka 10.3. 23:59:59**.

Všetky ukážkové a&nbsp;testovacie súbory k&nbsp;tomuto cvičeniu si môžete stiahnuť
ako jeden zip súbor
[cv02.zip](https://github.com/FMFI-UK-1-AIN-412/lpi/archive/cv02.zip).

## Odovzdanie cvičenia 1

Podľa návodu na [odovzdávanie riešení](../odovzdavanie.md) odovzdajte
riešenie prvého cvičenia. Riešenie odovzdajte do vetvy (branch) `cv01`
v&nbsp;adresári `cv01`.

Odovzdajte súbor `spy.txt` ktorý obsahuje „textovú“ verzia vstupu pre SAT solver
(s&nbsp;názvami premenných „GM“, „RM“ atď.) vrátane správne znegovaného tvrdenia,
ktoré chcete dokázať.

## <var>N</var>-queens

Pomocou SAT solvera vyriešte problém <var>N</var>-dám:

Máme šachovnicu rozmerov <code>N&times;N</code>. Na ňu chceme umiestniť `N` šachových dám
tak, aby sa navzájom neohrozovali. Ohrozovanie dám je v&nbsp;zmysle
štandardných šachových pravidiel:

-  žiadne dve dámy nemôžu byť v&nbsp;rovnakom riadku
-  žiadne dve dámy nemôžu byť v&nbsp;rovnakom stĺpci
-  žiadne dve dámy nemôžu byť na tej istej uhlopriečke

*Pomôcka*: Použite výrokové premenné `q_i_j`, <code>0 &le; i,j &lt; N</code>,
ktorých pravdivostná hodnota bude hovoriť, či je alebo nie je na pozícii `i,j`
umiestnená dáma.

*Pomôcka 2*: Pre SAT solver musíme premenné `q_i_j` zakódovať na čísla.
Keďže platí <code>0 &le; i, j &lt; N</code>, premennú `q_i_j` môžete zakódovať ako číslo
`N*i + j + 1`. **Napíšte si na to funkciu! Ideálne s&nbsp;názvom `q`. Jednoduchšie
sa vám budú opravovať chyby a&nbsp;ľahšie sa to číta / opravuje.**

*Pomôcka 3*: Nemusíme počítať počet dám. Stačí požadovať, že v&nbsp;každom riadku
musí byť nejaká dáma (určite nemôžu byť dve dámy v&nbsp;tom istom riadku, keďže ich
má byť `N`, musí byť v&nbsp;každom riadku práve jedna).

*Pomôcka 4*: Ostatné podmienky vyjadrujte vo forme jednoduchých implikácií:<br/>
<code>q_X_Y &rarr; &not;q_X_Z</code> pre <code>X,Y,Z &isin; &lt;0,N), Y&ne;Z</code>
(ak je v&nbsp;riadku `X` dáma na pozícii `Y`, tak nemôže byť iná dáma v&nbsp;tom istom
riadku), atď.

*Pomôcka 5*: V&nbsp;priečinku [examples/party](../examples/party) je ukážkový program
(c++ a&nbsp;python), ktorý môžete použiť ako kostru vášho riešenia.
V&nbsp;priečinku [examples/sat](../examples/sat) môžete nájsť knižnicu s&nbsp;dvoma
pomocnými triedami `DimacsWriter` a&nbsp;`SatSolver`, ktoré vám môžu uľahčiť prácu
so SAT solverom.

Riešenie implementujte ako triedu `NQueens`, ktorá má metódu `solve`. Metóda
`solve` má jediný argument `N` (číslo&nbsp;– počet dám) a&nbsp;vracia zoznam dvojíc čísel
(súradnice dám). Priložené testy by mali s&nbsp;vašou triedou zbehnúť!

## Sudoku (3b)

Implementujte triedu `SudokuSolver`, ktorá pomocou SAT solvera rieši sudoku.

Trieda musí mať metódu `solve`, ktorá ako jediný parameter dostane vstupné sudoku:
dvojrozmerné pole 9x9 čísel od 0 až 9, kde 0 znamená prázdne políčko. Metóda vráti ako výsledok
dvojrozmerné pole 9x9 čísel od 1 po 9 reprezentujúce (jedno možné) riešenie vstupného sudoku.

Ak zadanie sudoku nemá riešenie, metóda `solve` vráti dvojrozmerné pole (9×9) obsahujúce samé nuly.

Sudoku:

* štvorcová hracia plocha rozmerov 9x9 rozdelená na 9 podoblastí rozmerov 3×3
* cieľom je do každého políčka vpísať jednu z&nbsp;číslic 1 až 9

pričom musíme rešpektovať obmedzenia:

* v&nbsp;stĺpci sa nesmú číslice opakovať
* v&nbsp;riadku sa nesmú číslice opakovať
* v&nbsp;každej podoblasti 3x3 sa nesmú číslice opakovať

*Pomôcka*: Pomocou výrokovej premennej <code>s\_i\_j\_n</code> (<code>0
&le; i,j &le; 8</code>, <code>1 &le; n &le; 9</code>) môžeme zakódovať, že na
súradniciach <code>[i,j]</code> je vpísané číslo <code>n</code>.

*Pomôcka 2*: Samozrejme potrebuje zakódovať, že na každej pozícii má byť práve
jedno číslo (t.j. že tam bude aspoň jedno a&nbsp;že tam nebudú dve rôzne).

*Pomôcka 3*: Podmienky nedovoľujúce opakovanie číslic môžeme zapísať vo forme
implikácií: <code>s\_i\_j\_n -> -s\_k\_l\_n</code> pre vhodné indexy
<code>i,j,k,l</code> (spomeňte si, ako sme riešili problém <var>N</var>-dám).

*Pomôcka 4*: Pre SAT solver musíme výrokovologické premenné <code>s\_i\_j\_n</code>
zakódovať na čísla (od 1). <code>s\_i\_j\_n</code> môžeme zakódovať ako číslo
<code>9 * 9 * i + 9 * j + n</code>, kde <code>0 &le; i,j &le; 8</code>
a&nbsp;<code>1 &le; n &le; 9</code>.

*Pomôcka 5*: Opačná transformácia: SAT solver nám dá číslo <code>x</code>
a&nbsp;chceme vedieť pre aké <code>i, j, n</code> platí <code>x = s\_i\_j\_n</code>
(napríklad 728 je kód pre <code>s\_8\_8\_8</code>): keby sme nemali <code>n</code>
od 1, ale od 0 (teda rovnako ako súradnice), bolo by to vlastne to isté ako
zistiť cifry čísla <code>x</code> v&nbsp;deviatkovej sústave. Keďže `n` je od 1, ale
je na mieste 'jednotiek' (t.j. <code>n * 9<sup>0</sup></code>), stačí nám pred
celou operáciou od neho odčítať jedna (a&nbsp;potom zase pripočítať 1 k&nbsp;`n`).

## Technické detaily riešenia

Riešenie odovzdajte do vetvy `cv02` v&nbsp;adresári `cv02`.

### Python
Odovzdajte súbor `SudokuSolver.py`, v&nbsp;ktorom je implementovaná trieda `SudokuSolver`
obsahujúca metódu `solve`. Metóda `solve` má jediný argument: dvojrozmernú
maticu čísel (zoznam zoznamov čísel) a&nbsp;vracia rovnako dvojrozmernú maticu
čísel.

Program [`sudokuTest.py`](sudokuTest.py) musí korektne zbehnúť s&nbsp;vašou knižnicou
(súborom `SudokuSolver.py`, ktorý odovzdáte).

Ak chcete použiť knižnicu z&nbsp;[examples/sat](../examples/sat), nemusíte si ju
kopírovať do aktuálne adresára, stačí ak na začiatok svojej knižnice pridáte
```python
import sys
import os
sys.path[0:0] = [os.path.join(sys.path[0], '../examples/sat')]
```

### C++
Odovzdajte súbory `SudokuSolver.h` a&nbsp;`SudokuSolver.cpp`, v&nbsp;ktorých je implementovaná
trieda `SudokuSolver` ktorá obsahuje metódu `solve` s&nbsp;nasledovnou
deklaráciou:
```C++
std::vector<std::vector<int> > solve(const std::vector<std::vector<int> > &sudoku)
```

Program [`sudokuTest.cpp`](sudokuTest.cpp) musí byť skompilovateľný keď k&nbsp;nemu
priložíte vašu knižnicu.

###Java:
Odovzdajte súbor `SudokuSolver.java` obsahujúci triedu `SudokuSolver` s&nbsp;metódou `public static int[][] solve(int[][] sudoku)`.

Program [`SudokuTest.java`](SudokuTest.java) musí byť skompilovateľný, keď sa k
nemu priloží vaša knižnica.
