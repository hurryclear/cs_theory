# Übersicht

| Vorlesung | Inhalt                                                       | für Klausur                      |
| --------- | ------------------------------------------------------------ | -------------------------------- |
| yks 1     | Graphen                                                      |                                  |
|           | Algorithmus von Kruskal (minimaler Spannbaum)                |                                  |
| 2wee      | DAGS                                                         |                                  |
|           | Travisierung (DFS,BFS)                                       |                                  |
|           | Tarjan-Algorithmus für starke Zusammenhangskomponenten       | ja und schwer, viele Schritten   |
| tr3s      | Greedy-Algorithmen                                           |                                  |
|           | Mengensystem                                                 |                                  |
| fyr4      | Flüsse und Netzwerke                                         |                                  |
| *pe*5e ̈   | Push&Relabel                                                 | ja und schwer und Zeit aufwändig |
|           |                                                              |                                  |
| шест6     | Gomory Hu: min cut (nach jede cut welche Knoten belieben und mit wem) | ja und Zeit aufwändig            |
|           | Wie kann ich schnell min cut finden?                         |                                  |
|           | Editierdistanz                                               |                                  |
|           | Matrixmultiplikation                                         |                                  |
|           | TSP                                                          |                                  |
|           |                                                              |                                  |
|           |                                                              |                                  |
| t10       | Brance and Bound                                             |                                  |
|           | B&B TSP                                                      |                                  |
|           | B&B Rucksackproblem                                          |                                  |



# Tutorium

am 10.05.2023 bei Carl

1. Push und Relabel

   Den Max. FLuss finden, und anders sein als Ford-Fulkerson



# Graphen

| Graphen                    | $G= (V,E)$ und $G´= (V´, E´)$ Graphen                        | z.B. |
| -------------------------- | ------------------------------------------------------------ | ---- |
| Weg                        | $k$ heißt Weg der Länge $l$, wenn all Kanten in $k$ auch in $E$ sind |      |
| Pfad                       | ist weg, jeder Knoten ist im Pfad eindeutig (kein Knoten im Pfad mehr als einmal vorkommt) |      |
| Zyklus                     |                                                              |      |
| zusammenhängend            | für alle $x,y \in V$ ein Pfad zwischen $x$ und $y$ existiert |      |
| Wald                       | Wald oder <u>zyklenfrei</u>, wenn kein Weg in $G$ ein Zyklus ist |      |
| Baum                       | Baum, wenn $G$ ein Baum ist und zusammenhängend ist          |      |
|                            |                                                              |      |
| Teilgraph                  | wenn $V´\subseteq V$ und $E´\subseteq E$ , dann ist $G´$ ein Teilgraph von $G$ |      |
| aufspannender Teilgraph    | $G´$ enthält dieselben Knoten wie $G$                        |      |
| induzierter Teilgraph      | 1. Alle Kanten aus $G$, deren zwei Knoten in $G´$ liegen, sind auch in $G´$ enthalten<br />2. oder so zu schreiben: für alle $e = \lbrace a, b\rbrace \in E$ gilt: $\lbrace a,b \rbrace \subseteq V´ \Rightarrow e \in E´$ |      |
|                            |                                                              |      |
| Vorgänger                  |                                                              |      |
| Menge der Vorgänger von v  | pred(v)                                                      |      |
| Nachfolger                 |                                                              |      |
| Menge der Nachfolger von v | succ(v)                                                      |      |
| Eingangsgrad               | eg(v) = \|pred(v)\|                                          |      |
| Ausgangsgrad               | ag(v) = \|succ(v)\|                                          |      |



## Teilgraphen

V1F12

$G= (V,E)$ und $G´= (V´, E´)$ Graphen

**Definition**
*Teilgraph:* wenn $V´\subseteq V$ und $E´\subseteq E$ , dann ist $G´$ ein Teilgraph von $G$ 
*aufspannender Teilgraph:* $G´$ enthält dieselben Knoten wie $G$ 

*induzierter Teilgraph:* 

1. Alle Kanten aus $G$, deren zwei Knoten in $G´$ liegen, sind auch in $G´$ enthalten 
2. oder so zu schreiben: für alle $e = \lbrace a, b\rbrace \in E$ gilt: $\lbrace a,b \rbrace \subseteq V´ \Rightarrow e \in E´$ 

*Weg:* $k$ heißt Weg der Länge $l$, wenn all Kanten in $k$ auch in $E$ sind
*Pfad:* ist weg, jeder Knoten ist im Pfad eindeutig (kein Knoten im Pfad mehr als einmal vorkommt) 
*Zyklus (Kreis):* (wie kann man formal beschreiben?) 
*zusammenhängend:* für alle $x,y \in V$ ein Pfad zwischen $x$ und $y$ existiert 

Sei $G = (V,E)$ ein Graph 
*Wälder:* Wald oder <u>zyklenfrei</u>, wenn kein Weg in $G$ ein Zyklus ist
*Bäume:* Baum, wenn $G$ ein Baum ist und zusammenhängend ist

*Theorem:* Ist $G$ ein Baum, so hat $G$ genau $|V| - 1$ Kanten.
*Beweis:* (V1F16)

## Kruskal-Algorithmus (A1)

Minimaler Spannbaum

$G = (V, E, w)$

Gesucht: Spannbaum $T = (V, F)$ mit minimaler Kantensumme. **$\sum_{e\in F} w(e)$ möglichst klein**
Spannbaum: minimaler zusammenhängender Teilgraph des urspünglichen Graphen. <u>Der enthält alle Knoten aus ursprünglichen Graphen, aber kein Zyklus.</u>

Kruskal-Algorithmus

```pseudocode
// Minimaler Spannbaum
input: Graph G = (V, E, w)
output: Minimalter Spannbaum T = (V, F) von G

F <- \empty;	// initialiere F als leere Menge
L <- sort(E);	// erzeuge Liste L der nach Gewicht sortierten Kanten in E

while (EMPTY(L) == false) do 
	entferne Kante e = {u, v} mit kleinstem Gewicht aus L
	if (T = (V, F) enthält keinen Pfad zwischen u und v) then
		F = F U {e};
	else
		tue nichts
```

![image-20230424235355762](/Users/hurjiang/Library/Application Support/typora-user-images/image-20230424235355762.png)

## Speicherung

Knotenliste, Kantenliste

| Speicherung          | Def.                                                         | z.B. |
| -------------------- | ------------------------------------------------------------ | ---- |
| Kantenliste          | Knotenzahl, Kantenzahl, Liste von Kanten(je als 2 Zahlen)    |      |
| Knotenliste          | Knotenzahl, Kantenzahl, Liste von Knoteninformationen (Ausgangsgrad & Nachfolger) |      |
| Adjazenzmatrix       |                                                              |      |
| Adjazenzlisten       |                                                              |      |
|                      |                                                              |      |
| Knotenfogle          |                                                              |      |
| Kantenfolge $k$      | der Länge $l$ von $v_0$ nach $v_l$, wenn für alle $i\in \lbrace 1,...,l\rbrace$ gilt: $(v_{i-1}, v_i)\in E$ |      |
| Kantenzug            | wenn $k$ Kantenfogle ist und für alle $i,j \in \lbrace 0,...,l-1\rbrace$ mit $i≠j$ gilt: $(v_i,v_{i+1})≠(v_j,v_{j+1})$ |      |
| Pfad                 |                                                              |      |
| Zyklus               |                                                              |      |
| hamiltonscher Zyklus | Wenn $k$ Zyklus ist und $l = |V|$                            |      |



### Adjazenzmatrix



### Listen





## DAGs

Wikipedia: https://en.wikipedia.org/wiki/Directed_acyclic_graph

DAGs steht für <u>gerichtete azyklische Graphen</u> 非循环的

**Definition**

*azyklisch:* für jede Kantenfolge $k$ in $G$ gilt: $k$ ist kein Zyklus

## Topologische Sortierung

Ziel: lineare Ordnung auf Knoten zu finden, jede Knoten in der Reihenfolgen nach seiner Vorgängen kommt

知乎讲解：https://zhuanlan.zhihu.com/p/135094687
Zusatzvideo: https://www.youtube.com/watch?v=6LlKwzsrPB4

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230412160236236.png" alt="image-20230412160236236" style="zoom:35%;" />

?? wie soll man die Definition verstehen?? : was ist |V|, was heißt die bijektive Abbildung?



### Theorem 

ein Digraph $G$ besitzt eine topologische Sortierung $\iff$ $G$ azyklisch
*Beweis:* 略

### Algorithmus für topologische Sortierung

```pseudocode
input: Graph G = (V, E)
output: topologischen Sortierung s von G


```

### Anwendungsbeispiel

Task scheduling

## Hüllen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/Bildschirm­foto 2023-04-12 um 16.31.42.png" alt="Bildschirm­foto 2023-04-12 um 16.31.42" style="zoom:35%;" />

Jede Knoten sind von anderen Knoten erreichbar, inkl. sich selbst

Was heißt Reflexivität? V2F15

#### Floyd-Warshall Algorithmus

liefert für jedes Knotenpaar(u, v) den günstigsten Weg (summiert über Kantengewichte), oder $\infin$ falls nicht erreichbar

1. Naiver Ansatz

2. Warshall-Algorithmus

## Traversierung

das Durchlaufen eines Graphen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/Bildschirm­foto 2023-04-12 um 16.45.48.png" alt="Bildschirm­foto 2023-04-12 um 16.45.48" style="zoom:40%;" />

### Breitendurchlauf

BFS: Breadth First Search



### Tiefendurchlauf

DFS: Depth First Search

## Tarjan-Algorithmus (sZshk) (A3)

--> starke Zusammenhangskomponente

--> führen Tiefensuch(DFS) auf G aus

stark zusammenhängend: ein gerichteter Graph $G = (V, E)$, wenn für alle $u,v \in V$ gilt: Es gibt einen Pfad von $u$ nach $v$ 

starke Zusammenhangskomponente: eine starke Zusammenhangskomponente von $G$ ist ein <u>maximaler</u> <u>stark zusammenhängender</u> <u>Teilgraph</u> von $G$



<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230509161448512.png" alt="image-20230509161448512" style="zoom:50%;" />

```pseudocode
Tarjan-visit(G, v): // besuche Knoten v in Graph G mit Tarjan Algorithmus
	// 1. markiere Knoten v grau 
	// 2. addiere zeit um 1 (zeit ist hier "global" Variable) 
	// 3. setzte in[v] und l[v] auf zeit (zeit fängt von 0 an bei Initialisierung)
	farbe[v] = grau; zeit = zeit + 1; in[v] = zeit; l[v] = zeit;
	// push Knoten in Stack S
	PUSH(S,v);
	// besuche jede Nachfolger von Knoten v (hier beginne DFS)
	for (jeden Knoten u in succ(v)) do // succ(v) ist die Menge der Nachfolger von v
		// Fallunterscheidung
		// Fall1: der Nachfolger wurde nicht markiert, also noch weiß, nicht grau oder schwarz
		// 				dann besuche den Nachfolger rekursiv
		//				setze l[v] auf Minimum von l[v] und l[u], hier: u ist "der" Nachfolger, nicht alle Nachfolger
		if (farbe[u] == weiß) then
			Tarjan-visit(G,u);
			l[v] = min(l[v], l[u]);
		// Fall2: der Nachfolger wurde markiert (grau oder schwarz)
		// 				wenn der Nachfolger ist auch noch in Stack
		//				dann setze l[v] auf Minimum von l[v] und in[u]
		else
			if u in S then
				l[v] = min(l[v], in[u]);
	// Nach Travisierung der Nachfolger: wenn l[v] ist gleich in[v], dann bekommen wir eine starke Zusammenhangskomponte
	// gebe Knoten in Stack aus bis Knoten v, also der aktulle Knoten
	if l[v] == in[v] then
		Ausgabe ("starke Zusammenhangskomponte");
		repeat
			u = TOP(S); Ausgabe(u); POP(S);
		until u == v;
	// markiere Knoten v schwarz
	farbe[v] = schwarz;
```

`l[v] = min(l[v], l[u]);` 什么时候才会执行？

Was ist schwer? Wenn wir bis Ende der Rekursion kommen, und dann nach obene Eben geben!!! Bitte genau überlegen, was da passiert

### drei Teile

- Setup
- Aktualisierung von 𝑙[𝑣] und Aufruf des Algorithmus für die Nachfolger des jeweiligen Knotens
- potentielle Ausgabe einer starken Zusammenhangskomponente

#  Greedy

## Mengensystem (A10)

- Mengensystem $(E,\mathcal{M})$ 

  $E:$ eine endliche Menge, $\mathcal{M}:$ eine Teilmenge von $E$, also $\mathcal M \sube \mathcal P(E)$ 

  (Sei $E$ eine endliche Menge und $\mathcal M$ eine Menge von Teilmengen von $E$, also $\mathcal M \sube \mathcal P(E)$. Dann heißt $(E, \mathcal M)$ Mengensystem)

- Unabhängigkeitssystem $(E, \mathcal M)$ 

  ein <u>Mengensystem</u> $(E, \mathcal M)$ heißt Unabhängigkeitssytem, wenn $\empty \in \mathcal M$ und zu jeder Menge in $\mathcal M$ auch alle Teilmengen erhalten sind, also gilt: 
  Aus $A \in \mathcal M$  und $B \sube A$ folgt $B \in \mathcal M$ 

- Matroid $(E, \mathcal M)$ 

  ein <u>Unabhängigkeitssystem</u> $(E, \mathcal M)$ heißt Matroid, wenn für alle $A, B \in \mathcal M$ die folgende Austauscheigenschaft gilt: 
  Ist $|A| > |B|$, dann gibt es $x \in A \backslash B$, so dass $B \cup \lbrace x \rbrace \in \mathcal M$ 

- Basis $B$ 

  Sei $(E, \mathcal{M})$ ein Matroid und $B \in \mathcal{M}$ ein maximales Element, also für alle $x \in E \backslash B: B \cup \lbrace x \rbrace \notin \mathcal{M}$. 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230509214056776.png" alt="image-20230509214056776" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230509214115819.png" alt="image-20230509214115819" style="zoom:35%;" />

## Greedy-Algorithmen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617093550520.png" alt="image-20230617093550520" style="zoom:50%;" />

: Nimm immer das größte Stück

### Kanonischer Greedy-Algorithmus

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617094551182.png" alt="image-20230617094551182" style="zoom:40%;" />

## Greedy Auftragsplanung

## Greedy Activity Selection

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230509230732276.png" alt="image-20230509230732276" style="zoom:40%;" />

# Flüsse und Netzwerke (A4)

## Grundlegende Wissen

- Schnitt

  $(A, B)$ ist ein Schnitt in $G$ wenn $A \cap B = \empty, A ≠ \empty, B ≠ \empty$ und $A \cup B = \empty$ 

- Schnittkanten

  $E(A, B) = \lbrace e \in E \; | \; e = (u, v), u \in A, v \in B \rbrace$  

Beispiel: 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230616160748697.png" alt="image-20230616160748697" style="zoom:50%;" />

Kantenbeschriftung: Fluss *f(e)* / Kapazität *c(e)*

Schnitt: $(\lbrace s,a\rbrace, \lbrace b,c,d,t\rbrace)$ , dazu gibt's Schnittkanten: $\lbrace (a,c),(a,b),(s,b)\rbrace$ 

-->Kapazität: $c(A,B) = \sum_{e\in E(A,B)} c(e)$ 

- Restgraph

  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617102834696.png" alt="image-20230617102834696" style="zoom:50%;" />

Beispiel: wie kriege ich *rest(e)* aus?

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/Bildschirmfoto 2023-06-17 um 10.30.26.png" alt="Bildschirmfoto 2023-06-17 um 10.30.26" style="zoom:50%;" />

## Minimal-Cut

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230920090418014.png" alt="image-20230920090418014" style="zoom:40%;" />

## Restgraphen



## Ford Fulkerson

--> optimaler Fluss

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617111847125.png" alt="image-20230617111847125" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617111912740.png" alt="image-20230617111912740" style="zoom:50%;" />

- Erweiterungspfad

  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617112550420.png" alt="image-20230617112550420" style="zoom:50%;" />

  Beispiel:

  <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230617112620381.png" alt="image-20230617112620381" style="zoom:50%;" />



## Push & Relabel

Pre-Flüsse

### Push&Relabel Algorithmus

1. Initialisierung

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230616102042564.png" alt="image-20230616102042564" style="zoom:50%;" />

2. Hauptalgorithmus

   Nach der Initialisierung haben einige Knoten *x* Exzess *ex*(*x*) > 0. Der Algorithmus läuft nun <u>so lange bis</u> <u>alle Knoten Exzess</u> <u>ex(x) = 0</u> haben.

   <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230616102200691.png" alt="image-20230616102200691" style="zoom:50%;" />

​	Aktiver Knoten: beliebiges u mit ex(u) > 0
​	Erlaubte Kante: rest(u, v) > 0 und h(u) = h(v) + 1.

3. was macht Push und Relabel?

   1. Push - fliesse Wasser von einem Knoten nach anderem Knoten

      <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230616102820201.png" alt="image-20230616102820201" style="zoom:40%;" />

   2. Relabel - erhöhe h(u)

      <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230616102838356.png" alt="image-20230616102838356" style="zoom:40%;" />

 <img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230616150025037.png" alt="image-20230616150025037" style="zoom:40%;" />

## Gomory Hu

für gewichteter ungerichteter Graph G

Max-flow = min-cut (Max-flow min-cut Theorem)

### Gomory Hu Baum

Reihenfolge der Knoten im Gomory-Hu Baum

Thomas Gatter: Die Anordnung ist durch die Cuts klar definiert. <u>Knoten bleiben immer bei den Knoten, die nicht durch den Cut gehen</u>, auch im Gomory Hu Baum. Die neue Baum-Kante geht entsprechend durch den Cut.
Die Reihenfolge der Knoten im Baum zu vertauschen kann zufällig auch einen validen Gomory Hu Baum erzeugen. Aber halt wirklich nur zufällig.

Hur: after cutting check which node connects with which node, that's all

### Gomory Hu Algorithmus

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230614212426787.png" alt="image-20230614212426787" style="zoom:50%;" />

### Beispiel

Vorlesung

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230614222045172.png" alt="image-20230614222045172" style="zoom:30%;" />



# Dynamische Programmierung

## Editierdistanz (A5)

Freiwilligeserie7 Aufgabe1

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230621000634845.png" alt="image-20230621000634845" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230621000618510.png" alt="image-20230621000618510" style="zoom:50%;" />



## Optimale Matrixmultiplikation (A7)

- Ziel

  Diejenige Reihenfolge der Multiplikation der Matrizen zu finden, für die die Gesamtzahl der auszuführenden Skalar-Multiplikationen minimal wird.

### Allgemeines Matrix-Produkt

Sei also $C_{ij}$ der minimale Aufwand für die Berechnung des Teilproduktes $M_iM_{i+1}...M_{j-1}M_j$ 

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911084355373.png" alt="image-20230911084355373" style="zoom:50%;" />



<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230607103234185.png" alt="image-20230607103234185" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230607115303533.png" alt="image-20230607115303533" style="zoom:50%;" />

$A_{1,2} := C_{1,1}+C_{2,2}+r_1\cdot r_2 \cdot r_3$ 
$A_{2,3,4} := min\lbrace C_{2,2} + C_{3,4} + r_2 \cdot r_3 \cdot r_5, C_{2,3} + C_{4,4} + r_2 \cdot r_4 \cdot r_5\rbrace$ 
$A_{1,2,3,4} := C_{1,23} + C_{4,4} + r_1 \cdot r_4 \cdot r_5$ 

## Fitch Algorithmus (n.n.)





## DP - TSP (A11)

TSP: Traveling Salesman Problem

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911140907840.png" alt="image-20230911140907840" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230614164554075.png" alt="image-20230614164554075" style="zoom:35%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230614164615395.png" alt="image-20230614164615395" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911140634520.png" alt="image-20230911140634520" style="zoom:45%;" />

Beispiel aus Seminar 08

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911140829972.png" alt="image-20230911140829972" style="zoom:50%;" />

## Kürzeste Wege

### Warshall für Distanz (n.n.)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911214156575.png" alt="image-20230911214156575" style="zoom:40%;" />

### Dijkstra

Bestimmung der von einem Knoten ausgegenden kürzesten Wege

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230614120646430.png" alt="image-20230614120646430" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911214310388.png" alt="image-20230911214310388" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911225640545.png" alt="image-20230911225640545" style="zoom:50%;" />

### Bellmann-Ford

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230614120844019.png" alt="image-20230614120844019" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911222538091.png" alt="image-20230911222538091" style="zoom:50%;" />

## DP Rucksackproblem (VL209) (n.n.)

## Mehrfach-Rucksackproblem (VL209) (n.n.)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230913141727631.png" alt="image-20230913141727631" style="zoom:40%;" />

## Hirschberg (VL209) (n.n.)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911230320542.png" alt="image-20230911230320542" style="zoom:40%;" />





# Branch and Bound

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230913142606123.png" alt="image-20230913142606123" style="zoom:50%;" />

## B&B Rucksackproblem (A12)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230913142743468.png" alt="image-20230913142743468" style="zoom:45%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230913142803585.png" alt="image-20230913142803585" style="zoom:45%;" />

## B&B TSP

- symmetrisch

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230620155805029.png" alt="image-20230620155805029" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230620155737831.png" alt="image-20230620155737831" style="zoom:40%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230620160240527.png" alt="image-20230620160240527" style="zoom:40%;" />

- asymmetrisch

# Randomisierte Algorithmen

## Fitnesslandschaft

### Adaptive Walk

find the bigger/smaller around itself

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911231130329.png" alt="image-20230911231130329" style="zoom:50%;" />

### Gradient Descent

find the biggest/smallest around itself

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911231520958.png" alt="image-20230911231520958" style="zoom:50%;" />

### Metropolis-Walks

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230911231536679.png" alt="image-20230911231536679" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230924171018707.png" alt="image-20230924171018707" style="zoom:50%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230924171002347.png" alt="image-20230924171002347" style="zoom:50%;" />



# Genetische Algorithmen (A12,5)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912082314478.png" alt="image-20230912082314478" style="zoom:50%;" />

## Cross-Over

### 1-Punkt Crossover

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912083308500.png" alt="image-20230912083308500" style="zoom:50%;" />

### Uniformer Crossover

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912083607947.png" alt="image-20230912083607947" style="zoom:40%;" />

### Geordneter Crossover

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912084248765.png" alt="image-20230912084248765" style="zoom:50%;" />

### Crossover für Vektoren (Mittelwertbidlung, Konvexe Kombination)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912084427320.png" alt="image-20230912084427320" style="zoom:45%;" />

## Bit-Flip Mutationen

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912084451570.png" alt="image-20230912084451570" style="zoom:45%;" />

有m的地方0变1，1变0，cause bitflip(x) says so

# Kryptographie

## Euklid (ggT)



## Modulo Arithmetik (A13)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912091100802.png" alt="image-20230912091100802" style="zoom:45%;" />

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230922171109247.png" alt="image-20230922171109247" style="zoom:40%;" />

## Pollard-Rho Algorithmus (n.n.)

<img src="/Users/hurjiang/Library/Application Support/typora-user-images/image-20230912091652478.png" alt="image-20230912091652478" style="zoom:40%;" />



# Sondervorlesungen (n.n.)

## Algebraic DP

