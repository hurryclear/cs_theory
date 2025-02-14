# Übersicht Noto

| Vorlesung                                                    | Inhalt                                                       |                                                              | in der Übung | für Klausur                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------ | -------------------------- |
| $-e^{iπ}$  "Algorithmen und Komplexität"                     |                                                              |                                                              |              |                            |
|                                                              | Komplexitätsklassen                                          |                                                              | ✔︎            | ⭐️                          |
|                                                              | Master-Theorem                                               | $T(n) = aT({n\over b})+g(n)$ mit  $g(n) = \theta(n^k)$ ,  $a≥1, b≥1$ <br />compare $a$ und $b^k$ | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | Laufzeit- und Speicherplatzkomplexität                       | Schleife und Rekursive                                       | ✔︎            | ⭐️⭐️                         |
| $\sum^{\infty}_{i=0}2^{-i}$  "Suchverfahren in Linearen Listen" | 习题还要练一下，暂时不写了，后面的内容更重要                 |                                                              |              |                            |
|                                                              | Sequenzielle Suche                                           | $C_{avg}={1\over n} \sum\limits_{i=1}^n i = {n+1\over 2} $$  |              |                            |
|                                                              | Binäre Suche                                                 | $C_{avg} = log_2n$                                           | ✔︎            | ⭐️                          |
|                                                              | Sprungsuche                                                  | optimale Weite: $m = \lfloor \sqrt{({a\over b})n}\rfloor$ <br />$C_{avg} = O(\sqrt n)$ (optimal) | ✔︎            | ⭐️                          |
|                                                              | Exponentielle Suche                                          | $i \leftarrow 2^i$                                           |              |                            |
|                                                              | Interpolationssuche                                          | $p = \lfloor u + \frac{x-L[u]}{L[v]-L[u]}(v-u)\rfloor$       | ✔︎            | ⭐️                          |
|                                                              |                                                              | $C_{avg}(n) = 1+log_2log_2n$                                 |              |                            |
|                                                              | Selbstorganisierende Listen                                  | **F**requency **C**ount-Regel, **T**ranspose-Regel, **M**ove-**T**o-**F**ront-Regel | ✔︎            | ⭐️                          |
|                                                              | Auswahlproblem (V102F41)                                     | teilt die Liste in zwei Teilliste mit piv Element, das normalerweise letztes Element gewählt in dieser Vorlesung<br />1. $L_<.length = i-1$ : $i$-kE ist piv<br />2. $L_<.length > i-1$ : $i$-kE ist in $L_<$<br />3. $L_<.lenth<i-1$ : $i$-kE ist in $L_<$, aber man muss $(i-1-L_<.length)$-kE Element in $L_>$ weiter suchen | ✔︎            | ⭐️⭐️⭐️⭐️⭐️                      |
| $\lfloor π\rfloor$  "Verkettete Listen, Stacks und Schlangen" |                                                              |                                                              |              |                            |
|                                                              | verkettete Listen                                            |                                                              |              |                            |
|                                                              | verkettete Listen mit head und tail                          |                                                              |              |                            |
|                                                              | Doppelt Verkettete Listen                                    |                                                              |              |                            |
|                                                              | Skip-Listen                                                  |                                                              |              |                            |
|                                                              | Stack(Stapel, Keller, LIFO-Liste)                            | ADT                                                          |              |                            |
|                                                              | Schlange (Vorrangwarteschlange)                              | ADT                                                          |              |                            |
| $\lceil π \rceil$  & $\sqrt{13^2-12^2}$  "Sortierverfahren"  |                                                              |                                                              |              |                            |
| $O(n^2)$                                                     | Selectionsort                                                |                                                              |              |                            |
| $O(n^2)$                                                     | Insertionsort ("Loch")                                       | $i\in[1,length)$<br />$j\in[i,0)$ , $j$ wird nicht immer bis 0 abzählen! loop geht nicht immer bis zum Ende | ✔︎            | ⭐️⭐️⭐️                        |
| $O(n^2)$                                                     | Bubblesort (i >1, j <i-1)                                    |                                                              | ✔︎            | ⭐️⭐️⭐️                        |
| $O(nlogn)$                                                   | Shellsort                                                    |                                                              |              |                            |
| $O(nlogn)$                                                   | Quicksort                                                    | piv, i und j                                                 | ✔︎            | ⭐️⭐️⭐️                        |
| $O(nlogn)$                                                   | Turniersortierung                                            |                                                              |              |                            |
| $O(nlogn)$                                                   | Heapsort                                                     | creat heap and heap sort                                     | ✔︎            | ⭐️⭐️⭐️                        |
| $O(nlogn)$                                                   | Mergesort (normal&natürlich)                                 | $inv(F), runs(F),las(F),rem(F)$ <br />$rem(F) = F.lenght - las(F)$ | ✔︎            | ⭐️⭐️⭐️                        |
| $O(n)$                                                       | Distribution Sort                                            |                                                              | ✔︎            |                            |
| $3!$ "Bäume"                                                 |                                                              |                                                              |              |                            |
|                                                              | Definition von Ordnung, Tiefe, Stufe, Höhe, Vollständigkeit  |                                                              | ✔︎            |                            |
|                                                              | Eigenschaften: strikt, ausgeglichen, vollständig, fast vollständig, die Höhe eines vollständigen binären Baumes | strikt: jede innere Knoten haben zwei Kindern                | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | **Binärbaum**: Ordnung = 2                                   |                                                              |              |                            |
|                                                              | ADT Spezifikation BINTREE                                    |                                                              | ✔︎            |                            |
|                                                              | Traversierung: WLR(preorder), LWR(inorder), LRW(postorder)   |                                                              | ✔︎            | ⭐️                          |
|                                                              | Algorithmus von Traversierung (please note iterative pseudocode, not really unterstand ) |                                                              |              | ⭐️⭐️⭐️<br />(schwer für mich) |
|                                                              |                                                              |                                                              |              | fü 17b),18                 |
|                                                              | Gefädelte Binärbäume                                         |                                                              |              |                            |
| 111~2~ "Binäre Suchbäume"                                    |                                                              |                                                              |              |                            |
|                                                              | Einfügen, Löschen von natürliche binäre Suchbäume            |                                                              | ✔︎            |                            |
|                                                              | Zugriffskosten von natürliche binäre Suchbäume               |                                                              |              |                            |
|                                                              | **AVL-Baum** (1-balancierte Binärbaum)                       |                                                              | ✔︎            |                            |
|                                                              | Rotation zur Rebalancierung (AVL-Einfügen, Löschen)          |                                                              | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | die Höhe von AVL-Baum                                        |                                                              |              |                            |
|                                                              | Fibonacci-Bäume                                              |                                                              |              |                            |
|                                                              | Gewichtsbalancierte Suchbäume                                |                                                              |              |                            |
|                                                              | Positionssuche                                               |                                                              |              |                            |
| 0 1 1 2 3 5 ? "Mehrwegbäume"                                 |                                                              |                                                              |              |                            |
|                                                              | **B-Bäume** (Def., Einfügen, )                               |                                                              | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | B-Bäume Löschen                                              |                                                              | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | B*-Bäume (Unterschied zwischen B-Baum)                       |                                                              |              |                            |
|                                                              | Digitale Suchbäume                                           |                                                              |              |                            |
|                                                              | m-ärer Tries                                                 |                                                              |              |                            |
|                                                              | PATRICIA-Tree, Präfix-bzw.Radix-Baum                         |                                                              |              |                            |
| $\sum^{2}_{n=0}{2 \choose n}2^n$  "Hashing"                  |                                                              |                                                              |              |                            |
|                                                              | offene Hash-Verfahren <br />$h_i(K_p) = (h_0(K_p) + f(i))$ mod $m, i = 1,2,...$ |                                                              | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              |                                                              |                                                              |              |                            |
| $\lfloor 4e \rfloor$ "Textsuche"                             |                                                              |                                                              |              |                            |
|                                                              | KMP (Knuth-Morris-Pratt)                                     |                                                              | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | BM (Boyer-Moore)                                             | $i \leftarrow i+j-last[c]$                                   | ✔︎            | ⭐️⭐️⭐️                        |
|                                                              | BM-Verbesserung                                              |                                                              |              |                            |
|                                                              | Rabin-Karp                                                   |                                                              |              |                            |
|                                                              | Invertierte Listen                                           |                                                              |              |                            |
|                                                              | Signatur-Dateien                                             |                                                              | ✔︎            |                            |
|                                                              | k-Mismatch-Suchproblem                                       |                                                              | ✔︎            |                            |
| ._ _ _ _ ._ _ _ _ "Suffixbäume&Suffixarray"                  |                                                              |                                                              |              |                            |
|                                                              |                                                              |                                                              |              |                            |
| ?Mg "Datenkompression"                                       |                                                              |                                                              |              |                            |
|                                                              | Burrows-Wheeler-Transformation                               |                                                              |              |                            |
|                                                              | Move-To-Front                                                |                                                              |              |                            |
|                                                              | Huffman-Codierung                                            |                                                              |              |                            |
|                                                              |                                                              |                                                              |              |                            |



# Algorithmen und Komplexität

## Komplexitätsklassen

- Besst Case, Average Case, Worst Case

- Obere Schranken, Untere Schranken, Exakte Schranken

  obere Schranken: Groß-Oh: $O()$ 

  untere Schranken: $\Omega()$ 

  exakte Schranke: $\Theta()$ 

  20Klausur (nicht verstehen)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230201155757441.png" alt="image-20230201155757441" style="zoom:30%;" />

Zusatzvideo davon: https://www.youtube.com/watch?v=dP5J938kEAM

- ==wichtige Wachstumsfunktionen:==
  $O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!)$ 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119104515650.png" alt="image-20230119104515650" style="zoom:40%;" />

Beispiel: (Geben Sie jeweilige Komplexitätsklassen als $O(f)$)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230104144007033.png" alt="image-20230104144007033" style="zoom:40%;" />

16Klausur_Komplexität 
wir haben nur $O()$ geübt, oder?

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202220836059.png" alt="image-20230202220836059" style="zoom:50%;" />

## Laufzeitkomplexität

1. O(1)

2. O(n)
   ```pseudocode
   procedure linear_search(list, value)
   	
   	for each item in the list
   		if match item == value
   			return the item's location
   		end if
   	end for
   	
   end
   ```

   $\color{blue}{线性查找，时间复杂度看的是worst-case，假设这个list有20个数，要找的数恰好在最后一个，那就是要找20次}$

3. O(n^2^)
   ```pseudocode
   procedure quadratKomplex(int n){
   	int sum = 0;
   	for(int i = 1; i <= n; i++){	// O(n)
   		for(int j = 1; j <= n; j++){	// O(n)
   			sum += i*j;		// O(1)
   		}
   	}
   	return sum;	// O(1)
   }
   ```

   Produktregel:

   T~1~(n) $\in$ O(n), T~2~(n) $\in$ O(n), T~3~ $\in$ O(1)
   dann ist T(n) $\in$ O(n * n * 1) = O(n^2^)

   Summenregel:

4. $O(logn)$
   ```pseudocode
   procedure logKomplex(int n){
   	for(int i = 1; i <= n; i = i*2){	// nicht i++, sondern i=i*2 --> 2^x = n --> x = logn
   		#doSomethingWithO(1)
   	}
   }
   ```

   

5. O(n^2^)
   ```pseudocode
   procedure asympDemo(int n){
   	int sum = 0;
   	// Teil 1 
   	for(int i = 1; i <= n; i++){
   		for(int j = 1; j <= n; j++){
   			sum += i*j;
   		}
   	}
   	// Teil 2
   	for(int i = 1; i <= n; i++){
   		sum += i;
   	}
   }
   ```

   Teil 1: O(n^2^)

   Teil 2: O(n)

   Insgesamt: O(n^2^)

## Speicherkomplexität

#### was zahlt zu der Speicherkomplexität?

- gespeichertes Programm -> nein
- Eingabe -> nein
- Ausgabe -> ja
- Arbeitsspeicher -> ja

就是计算在这段程序运行的过程中，需要存储多少的数据，特别要注意递归算法的空间复杂度，在现在所学的内容中，主要看递归时如何分解n大小的问题。但是还是不懂为什么在freiwillige uebung 中的 aufgabe3 b 的空间复杂度是 O(logn)

#### Beispiel

1. S(n) ?


   ```pseudocode
   merge_sort(Liste a)
   	if a <= 1
   	do
   		int mitte = a.length / 2
   		int 1 -> i <= mitte - 1		//?
   		int r -> i >= array.length - mitte - 1	//?
   		l = merge_sort(l)
   		r = merge_sort(r)
   		return verschmelze(l,r)
   ```

### Komplexere Beispiel

1. mergeSort

   ```pseudocode
   public static void mergeSort(int[] a, int[] temp, int min, int max){
   	if (!(min<max))	// 1
   		return;				// 1
   	int middle = (min + max) / 2;	// 1+1+1 (weil drei Schritte gebraucht wird: 1.+; 2./2; 3.=)
   	
   	mergeSort(a, temp, min, middle);	// T(n/2)
   	mergeSOrt(a, temp, middle+1, max);	// T(n/2)
   	
   	merge(a, temp, min, middle, max);	// n
   }
   ```

   - Zeile 6 und 7
     - warum ist mit T() gezeigt?
       weil es rekursive Methoden sind
     - warum ist T(n/2)
       weil die Größe der Problem wird halbiert, von min bis middle oder von middle+1 bis max
   - Zeile 9
     T(n) von merge ist schon gewusst, T(n) = O(n)
     deswegen ist n

   $T(n) = 1+1+(1+1+1)+T({n\over2})+T({n\over2})+n = 2T({n\over2}) + n$

   dann wenden wir das Mastertheorem an: 
   $a = 2, b = 2, k = 1 \Rightarrow a=b^k$
   dann gilt dafür der zweite Form: $T(n)=O(nlogn)$ 

2. zwei Schleife
   ```pseudocode
   procedure doSomething(n){
   	result = 0;		
   	
   	for(i = 0; i <= n, i++){	
   		power = 1;	
   		
   		for(j = 1; j <= i; j++)	
   			power *= x;	
   		
   		result += a[i] * power 3	// r = r + a * power
   	}
   }
   ```

   <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221026234447626.png" alt="image-20221026234447626" style="zoom:50%;" />

## Master-Theorem

### Definition

Das Mastertheorem ist ein allgemines Theorem zur Lösung von Funktionalgleichungen (Rekursionsgleichungen) der Form 
$T(n) = aT({n\over b})+g(n)$, $a ≥ 1, b ≥ 1$, welche die algorithmische Strategie "Divide-and-Conquer" beschreiben.

### Divide-and-Conquer

- Zerlege Gesamtproblem n in a gleich große Teilprobleme der Größe $n\over b$
- Für Zerlegung und Kombination der Teillösung entstehen jeweils Overhead-Kosten
  g(n) ist Overhead-Kosten

### Polynomialer Overhead

Annahme: g(n) sei polynominal, d.h. $g(n)= \theta(n^k)$ mit $a ≥1$ und $b ≥ 1$, dann gilt: 

$T(n) = aT({n\over b})+g(n)$ mit $g(n) = \theta(n^k)$ ,  $a≥1, b≥1$ 

$$T(n)= \begin{cases} \theta(n^k),&\text{falls $a < b^k$} \\ \theta(n^klogn),&\text{falls $a = b^k$} \\ \theta(n^{log_b(a)}),&\text{falls $a>b^k$} \end{cases}$$

Frage dazu: was ist mit k? kann k =0? k=1? 

**Antwort von ADS Team:**
k ist als reelle, positive Zahl in den Folien definiert.
D.h. k=1 und k=1/2 sind recht klar OK. Strikt genommen verlassen wir damit normale Polynome, aber die sind auch nicht notwendig hier.
k=0 ist eine sehr interessante Frage. Da 𝑛0=1n0=1 bedeutet k=0 Konstante extra Kosten für jeden Rekursionsaufruf.
Wir haben das bei recht vielen Algorithmen in der Analyse. z.B. für Binäre Suche. Dort haben wir es ja auch in der Vorlesung verwendet.
Also ist k=0 explizit erlaubt und wichtig!

### wann ist das Master-Theorem anwendbar?

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230104143824469.png" alt="image-20230104143824469" style="zoom:50%;" />

### Beweis des Mastertheorems

VI_Folie42-48

略

# Suchverfahren in Linearen Listen

| Suchverfahren               |                                                              | Kosten                                                       |      |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| Binäre Suche                | mid =  $l + \lfloor (l-r+1)/2 \rfloor$                       | C~min~(n) = 1<br/> C~max~(n) = $\lfloor log_2(n)\rfloor +1$ <br/>C~avg~(n) ≈ log~2~(n) für $n \rightarrow \infty$ |      |
| Sprungsuche                 | $m = \lfloor \sqrt{({a\over b})n}\rfloor$                    | $O(\sqrt n)$                                                 |      |
| Interpolationssuche         | $p = \lfloor u + \frac{x-L[u]}{L[v]-L[u]}(v-u)\rfloor$       | $C_{avg}(n) = 1+log_2log_2n$                                 |      |
| Selbstorganisierende Listen | **F**requency **C**ount-Regel, **T**ranspose-Regel, **M**ove-**T**o-**F**ront-Regel |                                                              |      |
| Auswahlproblem              | 1. $L_<.length = i-1$ : $i$-kE ist piv<br />2. $L_<.length > i-1$ : $i$-kE ist in $L_<$<br />3. $L_<.lenth<i-1$ : $i$-kE ist in $L_<$, aber man muss $(i-1-L_<.length)$-kE Element in $L_>$ weiter suchen |                                                              |      |

ASL: Average Search Length

## Lineare Listen

Eine Lineare Listen (der Länge n) ist eine endliche und geordnete(aber nicht bestimmt sortiert) Folge von n Elementen a~0~, a~1~,..., a~n-1~ des selben Typs, welche als L [a~0~, ..., a~n-1~] notiert wird. L.length notiert die Länge von L und L heißt leer, wenn die Liste kein Element enthält (n=0).

## Sequenzielle Suche

nach Element mit Schlüsselwert x

Die mittlere Anzahl von Schlüsselvergleichen bei erfolgreicher Sequentieller Suche in L beträgt:(ASL)

$$C_{avg}={1\over n} \sum\limits_{i=1}^n i = {n+1\over 2} $$

Hinweis:

$1\over n$ bedeutet, dass das gesuchte Element x gleich Wahrscheinlichkeit hat, sich an verschiedenen Platz zu befinden
falls das gesuchte Element x sich an der i-ten Stelle der Liste befindet, werden i-mal Vergleiche benötigt

## Binäre Suche (binary search)

Bedingung: Liste L ist (aufsteigend) **vorsortiert** 

Suche durch rekursive binäre Zerlegung

### Sucheverfahren

Suche $k$ in $i$ ... $j$ , dann mid = $i$ + $\lfloor (j-i+1)/2 \rfloor$  

$(j-i+1)$ ist die Länge des Intervalls 

```pseudocode
input: Liste L, Suchwert x
output: Position von x in L oder -1 (wenn x nicht in L)

if L is leer then		// x nicht in L
	return -1;
else 
	m <- floor(L.length/2);		// m ist Mitte von L
if x == L[m] then		// x wird in Position m gefunden
	return m;
if x < L[m] then		// suche x in links seite von L[m]
	return Suche erneurt in (Sub-)Liste von 0 bis m-1;(Tiefstellung meine ich)
if x > L[m] then		// suche x in rechts seite von L[m]
	return Suche erneurt in (Sub-)Liste von m+1 bis L.length-1;
```

### Kosten für erfolgreiche Suche

Matertheorem anwenden: a=1, b=2, k=0

C~min~(n) = 1 
C~max~(n) = $\lfloor log_2(n)\rfloor +1$ 
C~avg~(n) ≈ log~2~(n) für $n \rightarrow \infty$ 

? wie kommt die her: VII-F11 

## Sprungsuche 

!!!: 1. fängt von $i=1$ an？ 2.optimale Sprungsweite

### Vorbediungen

aufsteigend sortiert

keine Duplikate

alle Elemente in $L$ sind zufällig verteilt ==???== 

### Prinzip

L wird in Abschnitte fester Länge m unterteil.

### Einfache Sprungsuche*

Springe zu Positionen $i*m$ (für i = 1, 2,...) der Reihe nach. 
Warum fängt i von 1 an, nicht von 0 an? 

Sobald $x < L[im]$, kann $x$ nur im $i$-ten Abschnitt $(i-1) m ... im -1$ liegen; dieser Abschnitt wird sequenziell nach $x$ durchsucht.

i的范围: $\frac{L.length}m -1$ 

### Kosten I

$C_{avg}(n) = {1\over2}\lceil{n\over m}\rceil a + {1\over 2}mb $

- $\lceil{n\over m}\rceil$ Blöcke
- ${1\over2}\lceil{n\over m}\rceil a$    sucht richtigen Block wie in Sequentieller Suche, allerdings muss der erste Block nicht überprüft werden
- ${1\over 2}mb$ findt das korrekte Element in einem Block, wie Sequentieller Suche, allerdings ist das erste Element bereits verglichen.

### Kosten II - optimale Sprungsweite

$a,b:$ Sei $a$ bzw. $b$ die Kosten für einen <u>Sprung</u> bzw. einen <u>Vergleich</u> (normaleweise ${a\over b} = 1$), dann gilt:

$C_{avg}(n)={1\over2}\lceil{n\over m} \rceil a + {1\over2}mb$ 

**optimale Sprungsweite**: $m = \lfloor \sqrt{({a\over b})n}\rfloor$, dann ist Komlexität in $O(\sqrt{n})$ 

${d\over dm}C_{avg}(n) = \frac{b-an\over m^2}{2} \Rightarrow m^2 = {an\over b} \Rightarrow m = \sqrt{({a\over b}n)}$  

### Zwei-Ebenen-Sprungsuche

VII-F16

## Exponentielle Suche

### gilt für: 

die Länge eines sortierten Suchbereichs ist unbekannt

aufsteigend sortierte Liste

### Pseudocode

```pseudocode
i <- 1;
while x > L[i] do
	i <- 2*i;	//幂查找就是i是幂次方增长的
for j = floor(i/2); j < i; j++ do
	if L[j] == x then
		return j;
return -1;
```

### Erklärung

1. $i$从1开始以幂级数增长
   假设是2次方增长，$i$ = 1, 2, 4, 8 ,16 ,32...
2. $i$ 增加的前提是$x$比$L[i]$要大，直到找到比$x$要小的$L[i]$的$i$
3. 然后在$(i/2+1, i-1)$ 的范围内用顺序查找法查找

**Frage: 为什么要用这种方法，好处是什么**

## Interpolationssuche (interpolation search)

==!!!:wenn nicht gefunden, wie man für die letzte Schritt schreiben sollte.== 
	 L[15] < k, L[16] > k, then don't need to write p = ... , we can directly say "nicht gefunden"

​	 example: Pflichtserie2, freiwillige Übung2

*Please compare interpolation search with binary search*: 二分查找就是一只折半，下一个查找的位置永远都是之前查找范围的一半，或前或后。但是差值查找是当前查找范围的首位元素值和末位元素值在此范围内的比例关系来预测下一个查找位置。

Wann ist Interpolationssuche schnell? **einigermaßen gleichverteilt**

wir versuchen den Index von $x$ zu **verraten**

### gilt für: 

die Schlüsselwerte im betreffenden Bereich sind **einigermaßen gleichverteilt** (均匀分布)

### Vorgehensweise:

$p = \lfloor u + \frac{x-L[u]}{L[v]-L[u]}(v-u)\rfloor$ 

$[u,v]$ ist aktueller Suchbereich 

dann zerlege den Suchbereichs bei p und fahre rekursiv fort

#### Beispiel hilft zu verstehen

**插值查找**（**interpolation search**）实际上是二分查找的改良版。假设有这样一个数组 $[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]$，我们可以发现，每个相邻元素的差均为 10，满足**均匀分布**。如果要查找元素 70，我们首先可以计算数组中小于等于 70 的元素占所有元素的比例的期望值 $p = {70 - 0\over 90 - 0} = {7 \over 9}$，而数组的长度 n 我们知道等于 10，所以我们期望查找的索引值就为 $⌊n × p⌋ = 7$，对应的元素为 70，恰好就是我们要找的元素。这样，原本用二分法需要查找 3 次的用插值查找只用查找 1 次，大大提高了查找的效率。

### Pseudocode von Interpolationssuche

```pseudocode
input: Positionen u,v einer sortierten List L, gesuchtes Element x
output: Position von x in L oder -1 (wenn x nicht in L)

// define a function, which gets p
// u and v is first index and last index of the present list, at the very beginning u is 0
def int getSuchposition(int u, int v):
	return ⌊u + ((x-L[u]/(L[v]-L[u]))*(v-u)⌋;		// nächste Position p zugreifen
	
//define a function: interPol
def int interPol(int u, int v, int x):

	// wenn x < L[u], untere Schranke, oder x > L[v], obere Schranke, d.h. nicht gefunden
	// wir suchen x von u bis v, x muss darin sein, ansonst heißt es, dass es kein x existiert
	if x < L[u] or x > L[v] then
		return -1;
	
	// get p, which is the gussed next position
	p = getSuchposition(u,v);
	if L[p] == x then
		return p;
	if x > L[p] then		// x in rechter Teilliste
		// search in new range, call interPol
		return interPol(p+1, v, x);	// warum gibt's hier x?
	else		// x in linker Teilliste
		// search in new range, call interPol
		return interPol(u, p-1, x);
		
```

### Kosten

$C_{avg}(n) = 1+log_2log_2n$ 

## Selbstorganisierende Listen

- FC-Regel: Frequency count

- T-Regel: Transpose

  比较次数是找到这个元素需要的次数，基本上就顺序查找的次数，也就是这个元素所在的位置就是次数

  找到之后将这个元素和前面一个位置的元素交换

  需要注意的：**然后下一次寻找是基于前一次改变后的序列**

  freiwillige uebung 3.8 

  pflicht uebung 2.3

- MF-Regel: Move-to-Front 

  将要找的元素直接放在首位

  比较次数也是这个元素所在位置的数，因为通过顺序查找就是从前向后一个一个找

  **需要注意的是下一次寻找是基于前一次改变后的序列**

  freiwillge uebung 3.8

  pflicht uebung 2.3

**Beispiel aus freiwilliger Serie3**
Gegeben sei die Liste L = [9,8,7,6,5,4,3,2] 

a: Transpose, b: Move to Front

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202193132321.png" alt="image-20230202193132321" style="zoom:40%;" />

verkettete selbstorganisierende Listen (freiwillige Serie 3 aufgabe 8)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230203160246429.png" alt="image-20230203160246429" style="zoom:50%;" />

## Auswahlproblem

Suche das $i$ - kleinste Element in unsortierter Liste $L$ 

1. Pivot-Element p (z.B. letztes Element) 
2. Teile die Elemente von $L$ bezüglich $p$ in 2 Teillisten $L_<$ and $L_>$ (die Reihenfolge von $L_<$ und $L_>$ müssen von L einbehaltet werden)
3. Drei Fälle (läuft rekursiv)
   - falls $L_<.length = i-1$ , dann ist $p$ das $i$-kleinste Element
   - falls $L_<.length > i-1$ , dann suche weiter in $L_<$ 
   - falls $L_<.length < i-1$ , dann suche weiter in $L_>$ , aber bestimme das $(i-1-L_<.length)$-kleinste Element

Komplexität: $T(n) = T(n/2) + \Theta(n)$ , nach Mastertheorem: $\Theta(n)$ 

# Datenstrukturen V3

## Verkettete Listen

Listenanfang : head (Kopf, Anker) bezeichnet Zeiger : pointer

Listenende : "next" Zeiger ist *null-pointer* 

key, value, next

​	key: einzigartiger Bezeichner 
​	value: Wert, tatsächliches Element in Liste 
​	next: Zeiger

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119182400420.png" alt="image-20230119182400420" style="zoom:40%;" />

### Löschen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119182902902.png" alt="image-20230119182902902" style="zoom:50%;" />

Algorithmus zum Löschen

```pseudocode
input: Zeiger p (welcher auf das Element vor dem zu löschenden zeigt)

if(p != null AND p->next != null) then
	p->next <- (p->next)->next; // p->next = (p->next)->next; 从前面指向后面
```

### Suchen

```pseudocode
def search(x,L): 
	p <- L.head;
	while p->value != x do
		p <- p->next;
	return p;
```

### Liste mit Head - und Tail-Zeigern

einfügen von Dummy-Elementen und Tail-Zeigern

- head zeigt auf Dummy-Element und head->next zeigt auf erstes Listenelement
- tail zeigt auf weiteres Dummy-Element und tail->next zeigt auf letztes echtes Listenelement

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119183948522.png" alt="image-20230119183948522" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119184011584.png" alt="image-20230119184011584" style="zoom:50%;" />

### Doppelt Verkettete Listen

### Kosten

## Skip Listen

## Stacks

= Stapel = Keller = LIFO (Last In - First Out)

ADT : Abstrakter Daten Typ 
	- PUSH(S,x) : **füge** Element x zu S hinzu
	- POP(S) : **lösche** zuletzt hinzugefügtes Element von S
	- TOP(S) : **Zugriff** auf zuletzt hinzugefügtes Element von S

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119190644255.png" alt="image-20230119190644255" style="zoom:40%;" />

### Anwendungen

Uebung: freiwillige Uebung3.7

#### Wohlgeformte Klammerausdrücke

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119185106089.png" alt="image-20230119185106089" style="zoom:40%;" />

```pseudocode
Bei öffnender Klammer : speichere auf Stack (PUSH)
Bei schließender Klammer : entferne oberstes Stack-Element (POP)
Ein wgK liegt vor, wenn der Stack vor einem POP nie leer war, und er am Ende leer ist (EMPTY)
```

#### Berechnung von UPN-Ausdrücken

UPN: die umgekehrte polnische Notation(Postfixnotation). Hierbei werden zunächst die Operanden angegeben und danach der darauf anzuwendende Operator.

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119185714132.png" alt="image-20230119185714132" style="zoom:40%;" />

```pseudocode
1. Lese gegebenen UPN-Ausdruck von links nach rechts
2. Bei Zahl: speichere Zahl auf Stack
3. Bei m-stelligem Operator: nehme m Operanden vom Stack, führe Operation aus und lege Ergebnis auf Stack
```

## Schlangen

= Queue, FIFO-Schlange (First In -First Out), Warteschlange

Abstrakter Daten Typ: 

	- ENQUEUE (Q, x): füge Element x am Ende von Q ein 
	- DEQUEUE (Q) : lösche am längsten in Q verweilendes Element (erstes Element)
	- FRONT(Q) : Zugriff auf erstes Element in Q

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119190727358.png" alt="image-20230119190727358" style="zoom:40%;" />

### Vorrangwarteschlangen

= Priority Queues, Prioritätsschlange, Prioritätswarteschlange

Jedes Element erhält eine Priorität. Entfernt wird stets Element mit der höchsten Priorität

ADT: 

- INTSERT (P, x) : füge Element x in Schlange P ein 
- DELETE (P) : lösche Element mit der höchsten Priorität aus P 
- MIN (P) : Zugriff auf Element in P mi höchster Priorität

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230119191242980.png" alt="image-20230119191242980" style="zoom:40%;" />

# Sortierverfahren

| Sortierverfahren     | need to remember                                             | Kosten (Avg-Case) |
| -------------------- | ------------------------------------------------------------ | ----------------- |
| Selectionsort        |                                                              | $n^2$             |
| Insertionsort        | `for(i=1;i<length;i++)`<br />`while(j>0 && L[j-1]>temp)`     | $n^2$             |
| Bubblesort           | `for(i=length;i>1;i--)`<br />`for(j=0;j<i-1)`                | $n^2$             |
| Shellsort            | keine Ahnung                                                 |                   |
| Quicksort            | piv = $\lfloor (l+r)/2 \rfloor$<br />`if(i<=j)`<br />`while(i<=j)`<br />`qsort(L,l,j);qsort(L,i,r)` | $nlogn$           |
| Heapsort             | Max-Heap-Eigenschaft<br />                                   | $nlogn$           |
| Mergesort            | inv(L), runs(L), las(L), rem(L)=L.length-las(L)              | $nlogn$           |
| Distributionsort     | Fachverteilung                                               | $n$               |
| indirektes Sortieren | große Datensätze, linearer Zeitaufwand<br />erstellen Zeigerlist, wenn austauschen muss, tausch Zeiger |                   |
| externes Sortieren   | Lesen und Schreiben abwechselnd zwischen Bändern             |                   |



<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221222161925110.png" alt="image-20221222161925110" style="zoom:30%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221122102215217.png" alt="image-20221122102215217" style="zoom:30%;" />

## Einfache Sortierverfahren($O(n^2)$)

### Selectionsort

1. mit zwei Listen

```pseudocode
while(0 < L2.length) do 
	iMin <- 0; 
	for(i = 1; i < L2.length; i++) 
		if(L2[i]<L2[iMin]) then 
			iMin <- i; 
	L1.apprend(L2[iMin]); 
	L2.remove(L2[iMin]); 
```

Erklärung

```pseudocode
// Selectionsort mit 2 Listen
input: Leere Liste L1, unsortierte Liste L2
output: Liste L1 mit sortierten Elementen aus L2

// 1. suche das min-Element in L2 und gebe den Index von ihn zu iMin
while(0 < L2.length) do
	iMin <- 0;
	// for(i=0; i < L2.length; i++) do	// in der Vorlesungsfolie steht i=1
	for(i = 1; i < L2.length; i++)	// warum i fängt von 1 an? Denn wir haben i=0 als min eingesetzt !!! ganz wichtig!
		if(L2[i]<L2[iMin]) then
			iMin <- i;
			
// 2. apprend das aktuelle Element in L2 in L1
// apprend heißt: füge Element von hintern einer Liste ein
	L1.apprend(L2[iMin]);
	
// 3. lösche das Element
	L2.remove(L2[iMin]);
```

2. mit Array
   Wichtig: nur ein Array!!!

```pseudocode
for(i = 0; i < L.length-1; i++) do // 如果前面的元素都排好序了，只剩下最后一个，那肯定也是排好的，所以只要到倒数第二个就可以
	min <- i;
	for(j = i + 1; j < L.length; j++) do	// 找最小是要一个一个都比较过
		if(L[j] < L[min]) then
			min <- j;
	swap(L[min], L[i]);
```

Erklärung

```pseudocode
// Selectionsort mit Array

input: unsortierte Liste L
output: sortierte Liste L

// use this loop to ...
for(i = 0; i < L.length-1; i++) do
// i in loop just count to L.length-1, which not include L.length-1, cause the last element in the list don't need this loop to sort, but the inner loop will do it, if the last element is smaller or bigger, then should be already somewhere else through every inner loop when i++
	min <- i;  // assume that the i is min, and then compare with j
	
	// use this loop to search the min-element in the another part of this array
	for(j = i + 1; j < L.length; j++) do	// j begin from i+1 until L.length - 1
		// if find one element is smaller than min, which we assumed before
		// then let this j-element be min-element
		if(L[j] < L[min]) then
			min <- j;
			
	// after inner loop we find min-element and we need to exchange the place of min-	element with the i-element
	swap(L[min], L[i]);	// wo soll man diese Zeile schreiben? warum nicht in der Schleife?
	
	
	// Frage: i < L.length - 1 aber j < L.length
```



### Insertionsort

"Loch"

bei Klausur muss man wissen wie $i$ und $j$ läuft: $i \in [1, L.length)$ , $j > 0$ 

$j$ fängt immer von $i-1$ an, aber endet sich nicht immer gleich, es hängt davon ab, ob in Loop gehen kann, weil $j--$ nur in Loop!!! **SEHR WICHTIG**

```pseudocode
input: unsortierte Liste L
output: sortierte Liste L

for(i = 1; i < L.length; i++) do 
	temp <- L[i];
	j <- i;
	while(j > 0 && L[j-1] > temp) do 
		L[j] <- L[j-1];
		j--;
	L[j] <- temp;
```

Erklärung

```pseudocode
input: unsortierte Liste L
output: sortierte Liste L

// rechte Seite (unsortierte Seite)
// die Schleife von die rechte Liste, fange von 2. Element an bis letztes Element
for(i = 1; i < L.length; i++) do // warum fängt man von i=1 an? 这个算法的思想就是让当前的元素和它之前的元素比较，然后将当前元素插入适当的位置，如果从0开始，第一个元素之前没有元素了，它不能和其它元素比较，没有意义，所以从第二个元素开始
	// setze das Element, das sortiert werden wird, zu/in temp
	temp <- L[i];
	
	// linke Seite (sortierte Seite)
	// j fängt von i an bis 0, also jedes Mal j--
	j <- i;
	// nach links weiter suchen, bis das Element, das kleiner als L[i] ist
	while(j > 0 && L[j-1] > temp) do // j can only be until 1, but we have j-1, so the first element can get
		L[j] <- L[j-1];
		j--;
		
	// warum ist hier L[j] nicht L[j-1]?
	// der obige Kontroller hält bis ein Element, das kleiner als L[j], an
	L[j] <- temp;
	
	// linke Seite (sortierte Seite) andere Schreibweise
	j <- i - 1;
	while(j >= 0 && L[j] > temp) do 
		L[j+1] <- L[j];
		j--;
	L[j] <- temp;
	
```

### Bubblesort

I

```pseudocode
for (i = L.length; i > 1; i--) do	
	for (j = 0; j < i - 1; j++) do	
		if(L[j] > L[j + 1]) then
			swap(L[j], L[j + 1]);
```

Erklärung

```pseudocode
input: unsortierte Liste L
output: sortierte Liste L

// i heißt: wie viele unsortierte Elemente gibt's noch?
for (i = L.length; i > 1; i--) do	// i > 1: min of i is 2, it means i in [2, L.length], for in total L.length elements, we need L.length-1 times compare, L.lenth-2+1=L.length-1
	for (j = 0; j < i - 1; j++) do	// jede j heißt ein Durchgang, j fängt von 0 an bis i-2, 
		if(L[j] > L[j + 1]) then	// weil der Bereich von j 0 bis i-2 ist, ist j+1 bis i-1, es macht Sinn
			swap(L[j], L[j + 1]);
```

- 外层大循环用$i$ 来计数：$i$ 可以理解为未被排序的元素个数，总共就是$L.length$个，每一次外层大循环结束，就减1，就是意味着少了一个未被排序的数，因为每一次外层大循环结束，最大的元素或最小的元素就会到最后面，那i在哪里结束呢？总共$L.length$个元素，其实只需要排$L.length-1$个元素或者说次数，比如，有10个元素，当其他9个元素都排好序了，第10个元素自然也就排好了，所以说$i$数到（能取到）2就可以，因为这样$L.length$到2的次数是$L.length-1$次，也就是例子中10-1为9次 ，这种理解就是要注意：$i$的最大值理解为未排序元素的个数，$i$的最小值理解为总共只需要$L.length-1$次排序，$i>1$ 也就是$L.length-1$次（算头不算尾）
- 内层小循环用$j$ 来计数：可以记初始状态，也就是$i$为$L.length$的时候。

II mit Abbruchkontrolle V4-F19 （这是另一种写法，这种方法的特别之处在哪里？有什么优点吗？）

```pseudocode
input: unsortierte Liste L
output: sortierte Liste L

i <- L.length;
swapped <- True;
while(swapped) do
	swapped <- False;
		for(j = 0; j < i-1; j++) do
			if(L[j] > L[j+1]) then
				swap(L[j], L[j+1]);
				swapped <- True;
		i--;
```



III Java Code

```java
public class BubbleSort1 {

    public static int[] bubbleSort(int[] array){

        for(int i = array.length; i > 1; i--){
            for(int j = 0; j < i - 1; j++){
                if(array[j] > array[j + 1]){
                    swap(array, j, j+1);
                }
            }
        }

        return array;
    }


    public static void swap(int[] array, int i, int j){
        int temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }
}

package com.huojiang.ads1;

public class BubbleSortTest {

    public static void main(String[] args) {
        BubbleSort1 test = new BubbleSort1();

        int[] array1 = new int[6];
        array1[0] = 23;
        array1[1] = 12;
        array1[2] = 53;
        array1[3] = 3;
        array1[4] = 25;
        array1[5] = 8;

        int[] array2 = test.bubbleSort(array1);

        // System.out.println(array2); // output: [I@1540e19d


        for(int i = 0; i < array1.length; i++){
            System.out.println(test.bubbleSort(array1)[i]);
        }
    }
}
```



## Verbesserte Sortierverfahren ($nlogn$)

### Shellsort

V104F25 nicht verstanden

### Quicksort

Best-Case: $O(nlogn)$ 

Worst-Case: $O(n^2)$ 

1. 用$i$和$j$作为左右两个指标，$i$找出比$piv$大的元素，否则$i$一直增加，$j$找出比$piv$小的元素，否则$j$一直减，当$i$和$j$确定后，看看$i$是否还比$j$小，如果是的话，那就两个位置上的元素互换。循环此操作。循环停止的条件是$i>j$ 
2. condition of swap and the outer loop is $i<=j$ , when $i=j$ will also swap, which the same element swap with itself, and also continue the outer loop
3. Bei Aufgabe schreibt man Array, der sortiert wird

I. die Version von Vorlesung

```pseudocode
qsort(L, l, r){
	if(r < = l) return;
	i = l;
	j = r;
	piv <- L[floor((l+r)/2)];
	do{
		while(L[i] < piv){
			i++;
		}
		while(L[j] > piv){
			j--;
		}
		if(i <= j){
			swap(L, i, j);
			i++;
			j--;
		}
	}while(i <= j);
	qsort(L, l, j);
	qsort(L, i, r);
}
```

Erklärung

```pseudocode
qsort(L, l, r){
	if (r <= l) return; // r <= l(not one), heißt es gibt kein Element, dann ist Sortierung nicht notwendig // Conquer
	i = l;	// i als linker "Zeiger"
	j = r;	// j als rechter "Zeiger"
	piv <- L[floor((l+r)/2)];	//
	do{
		// if the element in position i smaller than piv, then i++
		// which actually means that find a element which greater than piv, so i can change this element after piv
		while(L[i] < piv){
			i++; 
		}
		while(L[j] > piv){
			j--;
		}
		// when the previous two loops stop, it means i find an element in i position greater than piv, and an element in j position smaller than piv, then i want to exchange them
		// but requirement for exchange is i <= j. Why i need this requirement? when will it happen i > j?
		if(i <= j){
			swap(L[i], L[j]);
			i++; j--;
		}
	} while (i <= j);	// while put here is different from front?
	
	qsort(L, l, j);
	qsort(L, i, r);
}
```

### Turniersortierung



### Heapsort (für Liste)

1. creat heap

   begin from the lowest and the most right child tree

   Max-Heap-Eigenschaft (MHE) zu erfüllen
   die Wurzel jeses Unterbaumes ist das größtes Element des Unterbaum (andere Wort: das größte Element jedes Unterbaumes befindet sich in dessen Wurzel)

2. sort heap

   die Wurzel des ganzen Baum mit das tiefste, rechstste Element austauschen, und dann ausgeben (das tiefste, rechstste Element mit ganz oberem wurzel Element austauschen)

   dann nochmal "creat heap"

#### MHE

das größte Element jedes Unterbaumes befindet sich in dessen Wurzel

wir sagen $L$ erfüllt die Max-Heap-Eigenschaft(MHE), wenn $L[\lfloor{i-1\over 2}\rfloor] ≥ L[i]$ für alle $1 ≤ i ≤ L.length - 1$ 

linkes Kind von $L[i]$ ist $L[2i+1]$ 

rechtes Kind von $L[i]$ ist $L[2i+2]$ 

Vaterknoten von $L[i]$ ist $L[\lfloor{i-1\over 2}\rfloor]$ 

#### Algorithmusskizze (Heapsort mit Max-Heap)

```pseudocode
while (H enthält mindestens einen Knoten) do
	Ausgabe des Wurzelelementes;	// Ausgabe größtes Element in H
	Ersetze Wurzelelements mit dem am weitesten rechts stehenden Element der untersten Baumebene;	// H hat nun einen Knoten weniger
	Wiederherstellen der Max-Heap-Eigenschaft in H;
```

#### Max-Heapify (create Heap)

```pseudocode
def void max-heapify(L, i):
	l <- 2i + 1; 
	r <- 2i + 2;
	if l < L.length and L[l] > L[i] then
		largest <- l;
	else
		largest <- i;
	if r < L.length and L[r] > L[largest] then
		largest <- r;
	if largest != i then
		swap(L[i], L[largest]);
		max-heapify(L, largest);
```

#### Build-Max-Heap (Heap sort)

```pseudocode
def void build-max-heap(L):
	for(i = floor(L.length/2) - 1) to 0 do
		max-heapify(L, i);
```

#### Heapsort mit Liste

```pseudocode
def void heapsort(L):
	build-max-heap(L);
	for(i = L.length - 1; i > 0; i--) do
		swap( L[0], L[i]);
		L.length--;
		max-heapify(L,0);
```

### Normales Mergesort

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221121170422076.png" alt="image-20221121170422076" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221121170317078.png" alt="image-20221121170317078" style="zoom:30%;" />

**was ist mit Speicherplatz- und Zeitlaufkomplexität???**

```pseudocode
nicht-rekursiv (aus Vorlesung ads1)

input: unsortierte Liste L
output: sortierte Liste L

for(k = 2; k < n; k *= 2) do
	for(i = 0; i + k <= n; i += k) do
		merge(L, i, i + k/2, min{i + k - 1, n-1});
merge(L, 0, k/2, n - 1);
```

```pseudocode
Rekursives Algorithmus I //V105F4
Merge-Sort von L[l...r]

intput: Liste L und Indizes l und r
output: Liste L, sortiert zwischen Indizes l und r

def mergesort(L, l, r):
	if r <= l then
		return;
	else
		m <- floor((l+r+1)/2;
		mergesort(L, l, m-1);
		mergesort(L, m, r);
		merge(L, l, m, r);
```

```pseudocode 
Rekursiver Algorithmus II	//V105F5

input: Liste L und Indizes l,m,r
output: L[l...m-1] und L[m...r] verschmelzt in L

def merge(L,l,m,r):
	j <- l, k <- m;
	for(i = 0; i <= r-l; i++) do 
		if(k > r or (j < m and L[j] <= L[k])) then
			B[i] <- L[j];
			j <- j+1;
		else
			B[i] <- L[k];
			k <- k+1;
	for(i = 0; i <= r-l; i++) do 
		L[l+i] <- B[i];
```

#### Laufzeit des Mergesorts

$C_{min} = C_{max} = C_{avg} = \Theta (n\cdot logn)$ 
$M_{min} = M_{max} = M_{avg} = \Theta(n\cdot logn)$ 

### Natürliches Mergesort

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221121170241070.png" alt="image-20221121170241070" style="zoom:40%;" />

##### $inv(L)$, $runs(L)$, $las(L)$, $rem(L)$ 

V105-F9

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221206092836777.png" alt="image-20221206092836777" style="zoom:30%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221206092901806.png" alt="image-20221206092901806" style="zoom:30%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221206092937625.png" alt="image-20221206092937625" style="zoom:30%;" />

##### Beispiel 

L~1~ = [3, 6, 5, 7, 9, 1, 8, 0, 2, 4], L~2~ = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]

- $inv(L)$: Zahl der Inversionen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221206095046045.png" alt="image-20221206095046045" style="zoom:30%;" />

L~1~: hinter 3 sind 1, 2, 0 kleiner als 3; hinter 6 sind 5, 1, 0, 2, 4 kleiner als 6; hinter 5 sind 1, 0, 2, 4 kleiner als 5; hinter 7 sind 1, 0, 2, 4 kleiner als 7; hinter 9 sind 1, 8, 0, 2, 4 kleiner als 9; hinter 1 sind 0 kleiner als 1; hinter 8 sind 0, 2, 4 kleiner als 8; hinter 0 ist keine Zahl kleiner; hinter 2 ist keine Zahl kleiner; hinter 4 ist keine Zahl kleiner. Also andere Schreibweise: (3:1/2/0) (6:5/1/0/2/4) (5:1/0/2/4) (7:1/0/2/4) (9:1/8/0/2/4) (1:0) (8:0/2/4). $inv(L_1)$ = 3 + 5 + 4 + 4 + 5 + 1 + 3 + 0 + 0 + 0 

- $runs(L)$: Anzahl von Runs

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221206094650125.png" alt="image-20221206094650125" style="zoom:30%;" />

照递增或递减分成几个Teilliste

- $las(L)$: Länge längster sortierter Teilliste

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221206100338861.png" alt="image-20221206100338861" style="zoom:30%;" />

$las(L)$ ist die Länge von längster run oder Teilliste von L, $las(L~1~)$ = 3, weil längste Teilliste ist [5, 7, 9]

- $rem(L)$: $L.length - las(L)$

$L.length - las(L)$ , $rem(L_1) =$10 - 3 = 7

#### Beispiel für Mergesort (normal und natürlich, nicht rekursiv)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120134552147.png" alt="image-20230120134552147" style="zoom:30%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120134634047.png" alt="image-20230120134634047" style="zoom:30%;" />

was ist mit rekursivem version?

## Untere Schranke allgemeiner Sortierverfahren

Jedes allgemeine Sortierverfahren benötigt sowohl im mittleren als auch im schlechtesten Fall **wenigstens** $\Omega(nlogn)$ Schlüsselvergleiche

Die maximale und die mittlere Tiefe eines Blattes in einem Binärbaum mit k Blättern ist wenigstens $log_2k$ 

## Spezielle Sortierverfahren $O(n)$ 

### Distributionsort

```pseudocode
Algorithmus-Idee

1. Streuen: Bestimmen der Häufigkeit des Vorkommens für jeden der m möglichen Schlüsselwerte (Speicherung in Hilfsliste COUNT[0...m]).
2. Bestimmung der akkumulierten Häufigkeiten in COUNT.
3. Sammeln: Überprüfen von i=0 bis m-1. Falls COUNT[i]>0 wird i-ter Schlüsselwert COUNT[i]-mal ausgegeben.
```

重点：Streuen und Sammeln

- Beispiel aus Vorlesung
  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230102221607559.png" alt="image-20230102221607559" style="zoom:30%;" />
  Kosten: 
  - Kostanten $C_1, C_2$
  - keine Duplikate: Streuen $C_1 \cdot n$, Sammeln $C_2 \cdot m$ 
  - mit $d$ Duplikaten: Streuen $C_1 \cdot n$, Sammeln $C_2(m+d)$
- Beispiel aus Zusatzvideo

#### Fachverteilen

Veralgemeinerung: Sortierung von $n k$-Tupeln $( (n_{11}, ... ,n_{1k}), ... ,(n_{n1},...n_{nk}) )$ gemäß lexikographischer Ordnung

Sortierung erfolgt in $k$ Schritten:

1. Sortierung nach letzter Stelle
2. Sortierung nach der vorletzten Stelle
3. ...
4. Sortierung nach der ersten Stelle

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230201152513215.png" alt="image-20230201152513215" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230201152650693.png" alt="image-20230201152650693" style="zoom:25%;" />

## Umgang mit großen Datensätzen

### Indirektes Sortieren

die Frage kommt aus 16Klausur: Welchen Sortieralgorithmus benutzt man bei großen Datenmengen, um lineare Kosten beim Bewegen der Datensätze zu haben? 

Kopieraufwand für jedes Sortierverfahren auf <u>lineare Kosten</u> beschränken.

**Methode:**
Anlegen einer Hilfsliste aus Zeigern auf das eigentliche Listenelement.

- Liste: *L*[0..*n* − 1], Zeigerliste: *Z*[0..*n* − 1] (Initialisierung *Z*[*i*] = *i*)
- Austausch: statt tauschen von *L*[*i*] und *L*[*j*] tauschen wir *Z*[*i*] und *Z*[*j*]

换指针不换元素

### Externes Sortieren

Externes Sortieren mit Bändern: Ausgeglichenes 2-Wege-Mergesort

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230201202305422.png" alt="image-20230201202305422" style="zoom:30%;" />

Lesen und Schreiben abwechselnd zwischen Bändern

Beispiel V105F24

### Verbesserungen beim Mergesort

- Ausgeglichenes k-Wege-Mergesort: 
  k-Wege-Aufteilen und k-Wege-Mischen mit 2k Bändern

- Replacement Selectionsort:
  – Nutzung von Auswahlbaum als Priority Queue beschränkter Größe r
  – gelesene Elemente kommen zunächst in die Priority Queue $Q$ (bis diese voll) 

  – Sei *x* das Minimum von $Q$:

  - falls *x* **größer gleich** letztes geschriebenes Element: schreibe *x* auf Band 
  - falls *x* **kleiner** als letztes geschriebenes Element: schreibe alle restlichen Elemente von $Q$ aufs Band und fülle $Q$ neu auf, beginnend mit x

  Bitte wend zu Beispiel (V105F26) 

# Bäume

orientierte Wurzelbäume

Ordnung: die maximale Anzahl an Kindern eines Knotens von B

Geordneter Baum

 Vollständigkeit

Binärbaum

## Eigenschaften 

### Ordnung

die Anzahl von maximale Kinder eines Knotens

### Tiefe, Stufe, Höhe

Tiefe: die Anzahl des Pfades von Knoten $v$ bis Wurzel
Stufe: von $0$ bis maximale Tiefe
Höhe: die Höhe von Knoten ist **Tiefe + 1**; die Höhe eines Baumes ist **maximale Tiefe + 1** 
**Ein Baum mit genau einem Knoten hat die Höhe 1 (nicht 0!)** 

**Tiefe und Stufe sind ähnlich** 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221222141445655.png" alt="image-20221222141445655" style="zoom:35%;" />

# Binärbaum

Ordnung = 2

## ADT Spezifikation BINTREE

CREATE(), EMPTY(B), ROOT(B), LEFT(B), RIGHT(B)

BUILD (B~l~, p, B~r~)

Klausur: Geben Sie zu den Bäumen (i) und (ii) an, durch welchen Ausdruck Sie jeweils gemäß ADT-Spezifikation BINTREE erzeugt werden. (根据树的结构给出ADT-Spezifikation的步骤)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120143213631.png" alt="image-20230120143213631" style="zoom:30%;" />

What if there is a Binary Tree and then ask you to give steps of building this tree with ADT?
Build from children tree!

## Eigenschaft

Wurzel ist auch innere Knoten

- vollständig (einfach full)

  (Ein Binärbaum mit Höhe k+1)  

- strikt  

  bezüglich innere Knoten

  alle **innere** (<u>*inkl. Wurzel</u>, aber nicht Blätter) **Knoten** haben linke und rechte Kinder
  Frage: wenn es nur ein Knoten gibt, ist dieses Baum strikt? wahrscheinlich nicht nach meiner Meinung

- ausgeglichen

  Ein Binärbaum der Höhe $k + 1$ (d.h. maximale Tiefe ist $k$ und Stufe ist von $0$ bis $k$)

  1. Blätter sind auf Stufe $k$ oder $k - 1$ (<u>叶子结点</u>都在<u>最后一级或倒数第二级</u>)
  2. alle Knoten auf Stufe $< k - 1 $ haben linke und rechte Kinder (所有从<u>倒数第三级开始</u>的结点都有左右孩子)

- fast vollständig

  fast vollständig, heißt noch nicht vollständig, aber "**fast**"

  vollständig ist auch natürlich fast vollständig

  字面理解：几乎满。那几乎满，就是还没满，那要达到满，必须从上到下，从左向右开始填

  Ein **ausgeglichener Binärbaum** B der Höhe $k + 1$ (d.h. maximale Tiefe ist $k$ und Stufe ist von $0$ bis $k$)

  Für alle Knoten $v$ auf Stufe $k - 1$: (es ist schwer diese drei Bedingungen zu verstehen, einfach zu verstehen durch die vorne Erklärung)

  1. wenn $v$ hat links und rechts Kinder (zwei nicht-leere Unterbäume) => alle andere Knoten auf derselbe Stufe befinden sich links von $v$ 
  2. wenn $v$ ein Blatt ist (kein Kinder) => alle 

  3. ...

- ähnlichkeit

  Zwei Binärbäume werden als ähnlich bezeichnet, wenn sie **dieselbe Struktur** besitzen.

- äquivalenz
  Zwei Binärbäume werden als äquivalent bezeichnet, wenn sie **ähnlich** sind und **dieselbe Information** enthalten.

- die Höhe eines vollständigen binären Baumes

  die Höhe eines vollständigen binären Baumes mit N Knoten beträgt $\log_2(N+1)$ 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130151711169.png" alt="image-20230130151711169" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130151808102.png" alt="image-20230130151808102" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130151739937.png" alt="image-20230130151739937" style="zoom:40%;" />

## Speicherung

1. <u>Verkettete</u> Speicherung

   <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120144850868.png" alt="image-20230120144850868" style="zoom:50%;" />

   <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130160247384.png" alt="image-20230130160247384" style="zoom:40%;" />

   - Freispeicherverwaltung der Struktur wird von der Speicherverwaltung der Programmiersprache übernommen.

2. <u>Feldbaum</u>-Darstellung 

   - Simulation einer dynamischen Struktur in einem statischen Feld
   - Element jedes Knotens <u>sequentiell</u> in Liste *ELEM* gespeichert
   - <u>Index des linken und rechten Kindes</u> in *LCHILD* und *RCHILD*

    - *LCHILD* und *RCHILD* sind −1 wenn kein Kind vorhanden
    - statische Speicherplatzzuordnung, explizite Freispeicherverwaltung

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120144908814.png" alt="image-20230120144908814" style="zoom:30%;" />

3. <u>Sequentielle</u> Speicherung in Liste L 
   - Wurzelelement *w* in *L*[0] 
   - für Knoten mit Index *i*, 0 ≤ *i* ≤ *L*.*length* gilt:
     - Parent von *i* in *L*[⌊(*i*−1)⌋] für *i* > 0 2
     - linkesKindvon*i*in*L*[2*i*+1] für 2*i*+1<*L*.*length*
     - rechtesKindvon*i*in*L*[2*i*+2] für 2*i*+2<*L*.*length* 
   - Achtung: leere Felder, falls Kind nicht vorhanden!
   - Vorteile sequentieller Speicherung 
     1. für **(fast) vollständige und ausgeglichene Binärbäume** sehr <u>elegant</u> und <u>speichereffizient</u>

     2. Wechsel zwischen Ebenen/Elementen <u>ohne explizite Verweise oder Links (Zeiger)</u>
   - Nachteile sequentieller Speicherung
     1. sehr ineffizient wenn Baum zu einer linearen Liste <u>degeneriert</u> (nur linke oder rechte Unterbäume vorhanden)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120145043440.png" alt="image-20230120145043440" style="zoom:30%;" />

## Traversierung (Baumdurchlauf)

Vorordnung (preorder): WLR (first time meet)

Zwischenordnung (inorder): LWR (second time meet)

Nachordnung (postorder): LRW (third time meet)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230107170306978.png" alt="image-20230107170306978" style="zoom:35%;" />

Klausur: Baum in-order und post-order traversieren

### rekursive Traversierung Algorithmus 

1. rekursive WLR Traversierung

```pseudocode
def void DurchlaufPreOrder(B):
	if(EMPTY(B) == True) then 
		return;
	else 
		print(ROOT(B));
		DurchlaufPreOrder(LEFT(B));
		DurchlaufPreOrder(RIGHT(B));
```

2. rekursive LWR Traversierung

```pseudocode
input: Binärbaum B
output: Ausagebe der LWR Traversierung von B

def void DurchlaufInOrder(B):
	if(EMPTY(B) == True) then
		return;
	else 
		DurchlaufInOrder(LEFT(B));
		print(ROOT(B));
		DurchlaufInOrder(RIGHT(B));
```

3. rekursive LRW Traversierung

```pseudocode 
def void DurchlaufPostOrder(B):
	if(EMPTY(B) == True) then 
		return;
	else 
		DurchlaufPostOrder(LEFT(B));
		DurchlaufPostOrder(RIGHT(B));
		print(ROOT(B));
```

### iterative Realisierung

```pseudocode
// iterative LWR Traversierung V106F33

input: Binärbaum B
output: Ausgabe der LWR Traversierung von B

v <- ROOT(B);
S <- CREATE(); // erzeuge leeren Stack S
while(EMPTY(S) == False or v != null) do	// wenn Blätter vorkommen, was passiert?
	if(v != null) then
		PUSH(S, v);	// füge Element
		v <- v.leftChild;
	else
		v <- TOP(S);	// 
		POP(S);	// lösche Element
		print(v);
		v <- v.rightChild;
```

Beispiel: V106F34

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130153713833.png" alt="image-20230130153713833" style="zoom:40%;" />

碰到叶子直接输出，其实不是碰到叶子就输出，上面说了这里简化了。比如，碰到叶子1，入栈，然后继续看下一个结点，发现是null，然后就TOP(S)，这里的top就是叶子结点1

Beispiel: freiwillige Übungsserie 6, Aufgabe 18

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130170318042.png" alt="image-20230130170318042" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130170401340.png" alt="image-20230130170401340" style="zoom:40%;" />

## Gefädelte Binärbaum

V106F36

- weitere Verbesserung iterativer Durchlaufalgorithmen
- gestaltet iterative Durchlaufalgorithmen **ohne Verwendung von Stacks** 

​		--> Hinzufügen zusätzlicher Zeiger ("Fäden"), welche die Baumknoten in Folge der Durchlaufanforderung verknüpfen.

- Zwei Typen von Fäden
  1. rFaden: verbindet jeden Knoten mit seinem Nachfolgeknoten in Durchlaufordnung
  2. lFaden: verbindet jeden Knoten mit seinem Vorgängerknoten in Durchlaufordnung
- für jede Durchlaufordnung ist Fädelung möglich

Beispiel: 

- explizite Speicherung aller Fäden (rot) und Baumzeiger (schwarz)
- Nachteil: zusätzlicher Speicheraufwand erzeugt Redundanz

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202205158114.png" alt="image-20230202205158114" style="zoom:40%;" />

# Binäre Suchbäume

## natürliche binäre Suchbäume

**links kleiner als Wurzel:** alle Werte im linken Unterbaum sind kleiner als der Wert in der Wurzel

**rechts größer als Wurzel:** alle Werte im rechten Unterbaum sind größer als der Wert in der Wurzel

### Algorithmus (direkte Suche nach Wert x) 

```pseudocode
input: Zeiger p zum Wurzelknoten eines Suchbaumes B und gesuchter Wert x
output: Zeiger zu Knoten mit Wert x oder null, wenn x nicht in Suchbaum

def search(p, x):
	if (p == null) then
		return;
	else if (x < p->value) then
		return search(p->LEFT, x);
	else if (x > p->value) then
		return search(p->RIGHT, x);
	else // find it 
		return p;
```

==**Bemerkung: **Maximale Rekursionstiefe = Tiefe des Baumes==

### Einfügen, Löschen 

Dritter Fall bei Löschen: Knoten x hat zwei nicht-leere Unterbäume, dann gibe es zwei Lösungen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221222153921411.png" alt="image-20221222153921411" style="zoom:35%;" />

### Alternative zum Löschen (nur markiert)

zu löschende Knoten werden <u>markiert</u>

- Markierte Knoten werden bei Such- und Einfügevorgängen gesondert behandelt:

- Bei der Suche den markierten Knoten nur zur Entscheidung benutzen, ob links oder rechts weitergesucht wird.

- Bei erneutem Einfügen wird die Löschmarkierung entfernt. 

  **Achtung:** Bei dieser Art des Löschens wird <u>kein Speicher frei!</u>

### Zugriffskosten

V07F11 (仅复制，没理解)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230108145041730.png" alt="image-20230108145041730" style="zoom:40%;" />

- minimale Mittlere Zugriffskosten

  Minimale Zugriffskosten können in einer **vollständigen Baumstruktur** erwartet werden. 

  mittlere Zugriffskosten: $\Theta(logn)$ 

- maximale mittlere Zugriffskosten: $O(n)$ 

- mittlere Zugriffskosten: $O(ln(n))$ 

## k-balancierte Binärbäume

In welchem Maße sollen Strukturabweichungen bei Einfügungen und Löschungen toleriert werden um die <u>Reorganisationskosten</u> auf ein Minimum zu beschränken? 

$|h(B_l(x))-h(B_r(x))| ≤ k$ 

$B_l(x)$: der linke Unterbaum,  $B_r(x)$: der rechte Unterbaum, h(...): die Höhe eines Baumes

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230108150301542.png" alt="image-20230108150301542" style="zoom:30%;" />

good question:

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230108150433357.png" alt="image-20230108150433357" style="zoom:35%;" />

​	Ist jeder 1-balancierte Baum ausgeglichen? Ist der leere Baum auch k-balanciert?

## AVL-Baum (1-balancierte Binärbaum)

AVL-Kriterium:  $|h(B_l(x))-h(B_r(x))| ≤ 1$ für alle Knoten x von B

Balancefaktor BF(x) := $h(B_l(x))-h(B_r(x))$ 

### Einfügen

Rotation zur Rebalancierung

- Einfachrotation

  dasselbe Vorzeichen

- Doppelrotation (muss aufpassen!)

  unterschiedliches Vorzeichen
  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130181012220.png" alt="image-20230130181012220" style="zoom:40%;" />
  
- **Komplexität:** Rotationen sind lokale Operationen, die nur Vertauschen einiger Zeiger erfordern und damit in Zeit $O(1)$ erfolgen.

### Löschen

wie bei Binärbaum, aber muss rebalancieren

### die Höhe von AVL-Baum

didn't go through yet

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221222160641047.png" alt="image-20221222160641047" style="zoom:35%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221222160655821.png" alt="image-20221222160655821" style="zoom:35%;" />

## Fibonacci-Bäume

"Maximal unbalancierte" AVL-Bäume

为什么叫作最大不平衡？

Baum mit Höhe von $k+1$ 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130183654947.png" alt="image-20230130183654947" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221222160953801.png" alt="image-20221222160953801" style="zoom:30%;" />

## Gewichtsbalancierte Suchbäume

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130184436114.png" alt="image-20230130184436114" style="zoom:40%;" />

$n$ Knoten des ganzen Baumes
$n_l$ Konten von linken Baum

1. **Wahl des Parameters** $α$: (越小对树的结构越没有限制)
   - $α = 1/2$: Balancierungskriterium akzeptiert <u>nur vollständige Binärbäume</u>.
   
   - $α < 1/2$: Ausgeglichenheitskriterium wird <u>zunehmend gelockert</u>.
   
   - $α = 0$: <u>Keine Beschränkung</u> der Baumstruktur liegt vor.
   
2. **Rebalancierung nach Grundoperation (bspw. Einfügen):** 
   - Einsatz derselben Rotationstypen wie beim AVL-Baum.
   - Rebalancierung ist gewährleistet durch eine Wahl von $α≤1−\sqrt\frac{1}{2}$

3. **Kosten für Suche und Aktualisierung**: $O(log n)$ 

## Positionssuche mit balancierten Bäumen 

ist die Lösung des Auswahlproblems

- Balancierte Suchbäume sind linearen Listen in fast allen Grundoperationen überlegen.
- **Aber:** Lösung des **Auswahlproblems** bzw. **Positionssuche** (Suche nach *k*-tem Element der Sortierreihenfolge) **kann jedoch noch verbessert werden.**

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130185615910.png" alt="image-20230130185615910" style="zoom:40%;" />

Rang: 左子树节点数加1 = $n_l + 1$ 

- Rangzahlen erlauben Bestimmung eines <u>direkten Suchpfads</u> im Baum für Positionssuche nach dem *k*-ten Element.

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230130185908687.png" alt="image-20230130185908687" style="zoom:40%;" />

ganz ähnlich wie Auswahlproblem

- Die Wartungsoperationen erfordern etwas mehr Aufwand: Nach Einfügen / Löschen eines Knotens müssen die Rangwerte auf dem kompletten Suchpfad angepasst werden.

# Mehrwegbäume

- Ausgangspunkt: Binäre Suchbäume (balanciert)
  - entwickelt für Hauptspeicher
  - ungeeignet für große Datenmengen

- Externspeicherzugriffe erfolgen auf Seiten
  - Abbildung von Schlüsselwerten/Sätzen auf Seiten
  - Index-Datenstruktur für schnelle Suche

- Alternativen
  - m-Wege-Suchbäume
  - B-Bäume
  - B^∗^-Bäume (heute eher als B+-Bäume bezeichnet)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230131134354590.png" alt="image-20230131134354590" style="zoom:30%;" />

## B-Baum

*Klasse t* (t > 1), dann heißt der B-Baum ein 2t-Wege-Suchbaum

**B-Bäume sind <u>(fast) ausgelichene</u> m-Wege-Suchbäume.**

### Eigenschaft

1. Blätter sind auf derselbe Stufe
2. Außer der Wurzel hat <u>jeder Knoten</u> **[t - 1, 2t - 1]** Werte (Elemente)
3. Außer der Wurzel und Blätter hat <u>jeder Knoten</u> **[t, 2t]** Kinder
4. Falls *B* nicht leer ist, hat <u>die Wurzel</u> **[1, 2t-1]** Werte.
5. Falls *B* nicht leer und <u>die Wurzel</u> kein Blatt ist, hat sie **[2, 2t]** Kinder (Unterbäume).

*Voller Knoten:* der Knoten, der $2t - 1$ Anzahl an Werten enthält

### Teilen eines Knotens

### Einfügen

**pre-empties split**: 在插入过程中，只要遇到满员的结点，就先向上分，而不是插入之后再分

==so easy to make mistakes!!!==

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202001213435.png" alt="image-20230202001213435" style="zoom:40%;" />



### Löschen

V108F16

Löschen eines Schlüssel $k$ in einem B-Baum mit Klasse $t$ 

1. Suche: beginnt mit einer Suche nach $k$ 

2. Trifft der Durchlauf auf einen Knoten $y$ mit $t-1$ Werten (Minimalzahl) $\color{red}{(Außer Wurzel?)}$

   so wird durch **Verschieben** oder **Verschmelzen** die Anzahl der Werte in $y$ auf mindestens $t$ gebracht

3. $k$ ist ein Blatt, wird der Wert $k$ direkt entfernt 

4. $k$ ist eine innere Knoten, suche den größten Wert $k´$ im linken (oder kleinsten, im rechten) zum Wert gehörigen Unterbaum. 

   Dann ersetze $k$ durch $k´$ und lösche $k´$  ((muss noch ein Knoten min. t-1 Werte besitzen gelten))

   ==Bemerkung:== nach Löschen das Loch muss erfüllt werden, wenn $k$ eine innere Knoten ist. Also egal nach Löschen wie viele Werte gibt's bei der Knoten noch

- **Verschieben**

  Der rechte/linke Geschwisterknoten $y′$ von $y$ hat $b ≥ t$ Werte
  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120162907712.png" alt="image-20230120162907712" style="zoom:30%;" /><img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120162928454.png" alt="image-20230120162928454" style="zoom:25%;" />

- **Verschmelzen** 

  Der rechte/linke Geschwisterknoten $y′$ von $y$ hat $t − 1$ Werte

  mit Wurzel und Geschwistern
  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120163027400.png" alt="image-20230120163027400" style="zoom:25%;" /><img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230120163057452.png" alt="image-20230120163057452" style="zoom:25%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230108172127252.png" alt="image-20230108172127252" style="zoom:35%;" />

in diesem Beispiel habe "lösche 19" nicht verstanden: 1. nach 19 suchen, aber trifft nicht 1 Wert Knoten, warum verschmelzen?

### die Höhe eines B-Baumes

die Höhe wächst logarithmisch mit der Zahl seiner Werte: $h ≤ 1 + log_t({n+1\over 2})$ 

## B*-Baum

Überlegen welche Information ist in der inneren Knoten und in den Blattknoten?

- Innere Knoten führen nur $(K_i,P_i)$ als Einträge.
- <u>Information</u> $(K_i,D_i)$ wird in den **Blattknoten** abgelegt. Dabei werden alle Werte mit ihren zugehörigen Daten in Sortierreihenfolge in den Blättern abgelegt.
- **Die inneren Knoten** <u>bilden also einen Index</u>, der einen schnellen direkten Zugriff zu den Schlüsseln gestattet.
- Der <u>Verzweigungsgrad</u> erhöht sich beträchtlich, was wiederum die Höhe des Baumes reduziert.
- Durch Verkettung aller Blattknoten lässt sich eine effiziente sequentielle Verarbeitung erreichen, die beim B-Baum einen umständlichen Durchlauf in symmetrischer Ordnung erforderte.

## Digitale Suchbäume

Prinzip <u>digitaler Suchbäume</u> (kurz: **Digitalbäume**):

- <u>Zerlegung</u> des **Schlüssels** - bestehend aus Zeichen eines Alphabets $\sum$ - in Teile
- Aufbau des Baumes **nach Schlüsselteilen**
- Suche im Baum **durch Vergleich von Schlüsselteilen**
- Jede unterschiedliche Folge von Teilschlüsseln ergibt eigenen Suchweg im Baum.
- Alle Schlüssel mit dem gleichen Präfix haben in der Länge des Präfixes den gleichen Suchweg.

**Was sind Schlüsselteile ?**

- Schlüsselteile können gebildet werden durch Elemente (Bits, Ziffern, Zeichen) eines Alphabets oder durch Zusammenfassungen dieser Grundelemente (bspw. Silben der Länge $k$).
- Höhe des Baumes = $\frac{l}{k}$ + 1, wenn $l$ die maximale Schlüssellänge und $k$ die Schlüsselteillänge ist.

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230131144025128.png" alt="image-20230131144025128" style="zoom:30%;" />

## Trie

Spezielle Implementierung des Digitalbaumes: Trie

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230131151132004.png" alt="image-20230131151132004" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230131151059536.png" alt="image-20230131151059536" style="zoom:35%;" />

## PATRICIA-Tree



# Hashing

- Gestreute Speicherungsstrukturen / Hashing:
  (Schlüsseltransformation, Adressberechnungsverfahren, scatter-storage technique usw.)

1. Berechnung der Satzadresse *SA*(*i*) aus Satzschlüssel *K**i*: Schlüsseltransformation

2. Speicherung des Satzes bei *SA*(*i*)

3. Ziele: schnelle direkte Suche + Gleichverteilung der Sätze (möglichst wenig Synonyme)



## Kollision, Synonym, Kollisinsklasse

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221221143321912.png" alt="image-20221221143321912" style="zoom:30%;" />

## Wahrscheinlichkeit für Kollision

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20221221143542445.png" alt="image-20221221143542445" style="zoom:40%;" />

## Hash-Verfahren: Einflussfaktoren

Hash-Funktion, Datentyp, Verteilung, Belegungsfaktor, Bucket-Kapazität, Technik zur Kollisionsauflösung, Reihenfolge der Speicherung der Sätze

## Offene Hash-Verfahren

### Lineares Sondieren

$h_0(K_p) = h(K_p)$ 

$h_i(K_p) = (h_0(K_p) + i)$ mod $m, i = 1,2,...$ 

#### Verbesserungen

$h_i(K_p) = (h_0(K_p) + f(i))$ mod $m, i = 1,2,...$ 

$h_i(K_p) = (h_0(K_p) + f(i,h(K_p)))$ mod $m, i = 1,2,...$ 

z.B. $f(i)$ kann $ci$ sein; $f(i) := ci(-1)^i$ 

### Quadratisches Sondieren

$h_0(K_p) = h(K_p)$ 

$h_i(K_p) = (h_0(K_p) + ai + bi^2)$ mod $m,i = 1,2,...$ 

### Weitere

- Sondieren mit Zufallszahlen
- Double Hashing: $h_i(K_p) = (h_0(K_p) + i \cdot h´(K_p))$ 
- Kettung von Synonymen

## Hashtabelle H

Beispiel

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230105154257184.png" alt="image-20230105154257184" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230105154234748.png" alt="image-20230105154234748" style="zoom:40%;" />



## Analyse

### Kostenmaße

## Signaturfunktion

V110F25

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230125105414965.png" alt="image-20230125105414965" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230126102545789.png" alt="image-20230126102545789" style="zoom:40%;" />

$q[ ]= ADCACA$
Das Muster muss  mal zeichenweise verglichen werden. <-- $h(q) = h(t_2[i...i+5])$ 
in diesem Beispiel: $h(q)=3$ und $h(t_2[0]),h(t_2[4]),h(t_2[7])=3$ , deswegen 3 mal

## HAMT

HAMT: Hashed Array Mapped Tries

## Anwendung Hashing: Signaturen

### Karp-Rabin

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202214336515.png" alt="image-20230202214336515" style="zoom:40%;" />

# Textsuche

## KMP 

KMP: Knuth-Morris-Pratt

Schritt 1: Präfix-Analyse (um next[ ] zu finden)
Schritt 2: Suche

### Präfix-Analyse 

In dieser Vorlesung benutzen wir die Version: $j$ beginnt von 0 und next[0] = -1 （wir verwenden 0-basiert Version）

Präfix/Suffix Analyse 最长前后缀分析: Bestimme für alle j > 0 **längstes Präfix** von pattern, das auch **echtes Suffix** von patter ist.

**next[j]**$:=$ Anzahl der direkt vorangegangenen Zeichen, die ein Präfix des Musters bilden, ohne am Anfang des Musters zu beginnen (在这个版本中，在next数组中存储的就是最长公共前后缀的长度，不需要再加1)
Wichtig!: next[j] liefert die nächste zu prüfende Position des Musters nach Mismatch bei pattern[j]

```pseudocode
input: Muster pattern [0...m-1]
output: Tabelle next[0...m]

```

### Suche

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230105172808071.png" alt="image-20230105172808071" style="zoom:30%;" />

1. die Position $j$ des Mismatch 
2. find $next[j]$  
3. "Verschiebung des Musters" um $j-next[j]$ Position ? nicht ganz wahr.... Weil ....
4. Nach dem Verschieben fängt der nächste Suche nicht immer von ganz Anfang an, nächste Beginn hängt von $next[j]$ ab, das ist sehr wichtig bei Diagramm und die Vergleichzahl zu best  immen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230117113727086.png" alt="image-20230117113727086" style="zoom:30%;" />

5. !!! 粉色地方的问题：每次Mismatch之后的确是要计算j-next[j], 但是其实每次就是在Mis的那一列继续比较，哪一行就要看next[j]的值，这就是为什么在D（粉色后面）最上面的Mis后，直接到第二行开始比较。因为最上面Mis的是B，B的next是1，所以就在同一列的第二行比较

- läuft bis zum Ende des pattern, also wenn in der Mitte schon gefunden wird, suche trotzdem weiter



## BM

BM: Boyer-Moore

### Vorkommens-Heuristik

**Beispiel**

1. pattern(Muster): ACAD

   | c                   | A    | C    | D    | Rest |
   | ------------------- | ---- | ---- | ---- | ---- |
   | last[c] (0-basiert) | 2    | 1    | 3    | -1   |

   A在ACAD中最后一次出现的位置是2

   C在ACAD中最后一次出现的位置是1

   D在ACAD中最后一次出现的位置是3

   Rest是指其余，什么是其余呢？其余是指text/string/被比较的字符串中除了pattern之外的字符

2. pattern(Muster): hooligan

   | c                   | h    | o    | l    | i    | g    | a    | n    | Rest |
   | ------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
   | last[c] (0-basiert) | 0    | 2    | 3    | 4    | 5    | 6    | 7    | -1   |



**Algorithmus (Erstelle last)**

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230104205231374.png" alt="image-20230104205231374" style="zoom:40%;" />

### Suche

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230104205325343.png" alt="image-20230104205325343" style="zoom:35%;" />

1. Wenn Mismatch $c$ in String in Muster nicht vorkommt, verschiebe Muster nach rechts hinter $c$  

   <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230117115851172.png" alt="image-20230117115851172" style="zoom:30%;" />

2. Wenn Mismatch $c$ von String in Muster vorkommt, verschiebe Muster nach rechts um die Position, wo genau $c$ in String letztes mal vorkommt (also $last[c]$) 

   <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230117115938429.png" alt="image-20230117115938429" style="zoom:30%;" />

$i$ : die Position der pattern in string
$j$ : die Position des Mismatches von pattern in pattern
$i = i+j-last[c]$ , $c$ ist Mismatch in string; wenn $i <= (old)i$ , dann $i = i+1$ 

| KMP                | BM                                              |                |
| ------------------ | ----------------------------------------------- | -------------- |
| 匹配成功就停止     | 匹配成功继续匹配 (题目有时会要求找到一次就暂停) | 具体看题目要求 |
| next 是指pattern   | last是指string                                  |                |
| 每次匹配是从前向后 | 每次匹配是从后向前                              |                |
|                    |                                                 |                |

## k-Mismatch-Suchproblem

Gesucht werden alle Vorkommen eines Musters in einem Text, sodass höchstens an k der m Stellen des Musters ein Mismatch vorliegt, d.h. die Hammeng-Distanz $≤ k$ ist. 

```pseudocode
input: string[0...n-1], pattern[0...m-1]
output: Index des Auftretens von k-Mismatch und Anzahl Mismatches

for (i = 0; i < n-m; i++) do 	// 
	z <- 0;
	for (j = 0; j < m-1; j++) do
		if (string[i+j] != pattern[j]) then
			z <- z+1;
	if (z <= k) then
		Gib Treffer in i mit z Mismatches aus;
		
其实就是拿着patter放在string上从前向后对比
```

- Exakte (Text-) Suche ergibt sich als Spezialfall mit k=0.
- Naiver Suchalgorithmus kann für k-Mismatch-Problem leicht angepasst werden (siehe rechts)
- Auch effizientere Suchalgorighmen(KMP, BM, ...) können angepasst werden 


$𝑡2[]=$BCABADCACADCABDA,
und das Muster$q[]=$ADCACA

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230126103141320.png" alt="image-20230126103141320" style="zoom:40%;" />

# Suffixbaum

## Das Schriftzeichen $

wenn kein $, kann ein Suffix s von S ein Präfix eines anderen Suffixex t von S sein



**Optimierungen / Speicherverbrauch**

– Kantenlabel nicht als String (“ab”), sondern als Paar (i,j) *S*[*i* . . . *j*] speichern 
– 12 bytes pro Character
– **Suffixbäume haben großen Overhead!**



wotd (write-only-top-down)

## Anwendung - Textsuche



<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230117150125864.png" alt="image-20230117150125864" style="zoom:30%;" />



## Anwendung - längster k-facher Substring

Problem: Sei $S$ eine Zeichenkette und $k ∈ N$. Finde einen <u>längsten Substring von $S$</u>, welcher <u>$k$ Vorkommen</u> in $S$ hat.

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202160150498.png" alt="image-20230202160150498" style="zoom:35%;" />

Frage: warum pre-order und post-order? beanwortet folgendes

找到出现两次最长的子串

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230202160637103.png" alt="image-20230202160637103" style="zoom:40%;" />

Rot: Länge des Gesamtlabels
Länge des Gesamtlabels, weil wir nach längsten Substring suchen, je länger diese Zahl ist, desto ist es besser
um die zu bestimmen, Durchlauf in pre-order

Blau: Anzahl der Blätter im Unterbaum
<u>die Anzahl der Blätter im Unterbaum</u> bedeutet wie viele mal kommt die string, also diese Zahl gleich $k$ sein
Um die Anzahl der Unterbäume zu bestimmen, brauchen wir Durchlauf in post-order. Warum? 

In diesem Fall 'ab' kommt auch zweimal vor, aber die Länge 2 ist kleiner als 'bab'

## Suffix Links

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230129230727330.png" alt="image-20230129230727330" style="zoom:40%;" />

**v->w, v只比w多了一个字符而已**

## Generalisierter Suffixbaum

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230129232512549.png" alt="image-20230129232512549" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230129232533060.png" alt="image-20230129232533060" style="zoom:40%;" />

- Anwendung - Longest Common Substring



# Suffixarray

normal



<u>Enhanced Suffixarray</u>

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230117161906115.png" alt="image-20230117161906115" style="zoom:40%;" />

normal <u>Suffixarray</u> ist die Array ohne LCP und $SL[i]$ 

Suffix ist <u>alphabetisch</u> geordnetet, nicht nach Länge....!!!

LCP: Longest Common Prefix (compare with previous)

$SL$: Suffix Links
在$SL$里储存的数字是当前Suffix的Suffix的起初位置$i$的数字 

## Enhanced Suffixarrays: Anwendung

Problem:  $(l,k)$ - Substrings
Finde alle Substrings der Länge $l ∈ N$, die wenigstens $k ∈ N$ Vorkommen in einer gegebenen Zeichenkette $S$ haben.



## Anwendung - Stringsuche

# Datenkompression

verlustfrei: Codierung eindeutig umkehrbar

verlustbehaftet: Originaldaten können im Allgemeinen nicht eindeutig aus der komprimierten Codierung zurückgewonnen worden

## Lauflängencodierung

Aufeinanderfolgende identische Zeichen werden zusammengefasst

**Läufe (Runs)** = lange Folgen sich wiederholender Zeichen
Ersetze jeden Run durch seine Länge und das wiederholte Zeichen
Lohnt sich nur für Läufe mit Länge > 2

**Escape-Zeichen**

Jedes Auftreten dieses Zeichens besagt, dass die folgenden beiden Buchstaben ein Paar (Zähler, Zeichen) bilden.
Ein solches Tripel wird als **Escape-Sequenz** bezeichnet

## Burrows-Wheeler-Transformation

verwendet in bzip 

produziere lange Runs von Zeichen

## Move-To-Front

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230129190810319.png" alt="image-20230129190810319" style="zoom:30%;" />

string = 'broood' -> zu codierende Zeichenfolge
$\sum= \lbrace a,b,d,o,r\rbrace$ -> (endliches) Alphabet mit Ordnung

## Huffman-Codierung

Häufiger auftretende Zeichen werden mit weniger Bit codiert

## Kompression mit BWT

Kompression in 3 Schritten:

1. Burrows-Wheeler-Transformation (BWT): 

   produziere lange Runs von Zeichen

2. Move-To-Front (MTF):

   produziere daraus lange Läufe von Nullen

3. Komprimieren (Huffman-Codierung) 
   normaleweise brauchen wir <u>4 Bits</u>, um ein Zeichen zu speichern

- bzip-Funktionen: 

  BWT-Kompression(x) = Huffmann(MTF(BWT(x)))

  BWT-Dekompression(y) = BTW^-1^ (MTF^-1^Huffmann^-1^(y)) (= BWT-Kompression^-1^(y)) 

- Wozu das Ganze?

  BWT erzeugt durch Sortierung lange Läufe gleicher Zeichen

  MTF erzeugt daraus kleine (Index-) Zahlen für häufig wiederholte Zeichen (genauer: Lange Folgen von '0')

  Transformation erlaubt gute Kompression:

  - Lauflängen-Codierer (evtl. speziell für '0') oder
  - Huffman-Codierer (möglichst kurze Bitfolge für häufige Zeichen)

## Entropie

ungenaue Definition: die Entropie ist ein Maß für den mittleren Informationsgehalt eines Textes.

Gut komprimierbare Texte haben geringe Entropie.

- der Informationsgehalt (eines Zeichens x) sei $I(x)=-log_2p(x)$ 

- die Entropie (eines Zeichens x) im Text ist dann:

  $H_1 = \sum_{x\in \mathcal{A}} p(x)I(x) = -\sum_{x\in \mathcal{A}}p(x)log_2p(x)$ 

   

# Word Embedding

Mögliche Aufgaben:

- Begriff soll **exakt so wie gesucht** vorkommen → KMP, BM, invertierte Listen, Signaturen
- Begriff darf **mit wenigen Abweichungen** vorkommen→ <u>Hamming-Distanz</u>, Editierdistanz, <u>k-Mismatch-Suchproblem</u> und angepasste Algorithmen
- es sollen auch **Synonyme** und **andere semantisch ähnliche Begriffe** gefunden werden → mit Hilfe von geschickt gewählten <u>Wortvektoren</u> und einem <u>Ähnlichkeitsmaß</u> 
  *mögliche Frage dazu: welche Methode gibt es, wenn man Synonyme und andere semantisch ähnliche Begriffe suchen will? mit Hilfe von Wortvektoren und Ähnlichkeitsmaß* 

**Wortvektoren**

1. Wortvektoren sind Vektoren aus dem Raum $R^m$ wobei $m$ beliebig, aber fest ist.
2. Jedem Wort in einem Vokabular ist ein Wortvektor zugewiesen
3. Wünschenswerte Eigenschaft: semantisch ähnliche Wörter werden durch ähnliche Wortvektoren repräsentiert

# Bloom Filter

Motivation

- Hashtabellen sind effizient, nur wenn sie möglichst <u>wenige Kollision</u> aufweisen

  Hashtabellen können sehr groß werden und dadurch ineffizient sein

- eine <u>probabilistische</u> Datenstruktur

- der klassische Bloom Filter kann mit <u>geringem Speicherbedarf</u> beantworten:

  Ob ein Element in der Datenmenge nicht vorkommt

  Oder ob es wahrscheinlich darin enthalten ist

- Diese Datenstrukturen nutzte er zum Erstellen eines Wörterbuchs zur Silbentrennung

Fingerabdrucks

- Hierzu wird eine einzeilige Hashtabelle mit fester Breite erstellt. 
- Jeder bekannte Datensatz wird gehasht
- Die Position des Hashs wird in der Tabelle auf 1 gesetzt

Bloom Filter sind eine <u>probabilistische</u> Datenstruktur, die

- <u>schnell einfügen</u>: schnell Daten in die Struktur einfügen kann
- schnell feststellten kann, ob ein Datensatz nicht bekannt ist
- einen <u>geringen Speicherverbrauch</u> hat
- berechenbar in Buzug minimal notwendige Größe ist
- <u>aufwendig entfernen</u>: das Entfernen von Objekten aber recht aufwendig ist

# Game Engines

**Sweep and Prune: Sortieren!**: Insertionsort

# Priority Queues

# Eingebettete Systeme

Ein eingebettetes System ist ein <u>elektronischer Rechner</u>, der in einen <u>technischen Kontext</u> eingebunden ist.

**Eingebettete Systeme** **Warum ist das interessant?**

- kleine, leistungsreduzierte CPU mit kleinem Befehlssatz (ARM, AVR, ...) 
- wenig oder kein Speicherplatz (Read-only Memory: ROM)
- oft nur CPU Register, kein Hauptspeicher

**Was bedeutet das für Sortieralgorithmen?**

- Sort In Place (langsame Allokation, wenig Speicher, Heap-Fragmentation, ...)

- kein Rekursion (langsam, Stack Overflows, ...)

- kleine Code-Basis

- sauberer Code (wenige Code-Sprünge/Branching)

- gutes Verhalten ( O für avg und worst case ) 

  ⇒ **Shellsort**

**Introsort**: ist ein hybrid aus Quicksort, Heapsort und Insertion sort.
