# NN-Perceptron

Dieses Repository enthält eine einfache Implementierung eines Neuronalen Netzes mit einem Perzeptron, das eine Entscheidungsgrenze generiert und zufällige Daten klassifiziert.

## Funktionen

### `generate(m=10, x1=(-1, 1), x2=(-1, 1))`
Diese Funktion erzeugt `m` zufällige Datenpunkte innerhalb des angegebenen Bereichs `x1` und `x2`.

**Parameter:**
- `m` (int): Anzahl der zu generierenden Punkte.
- `x1` (tuple): Bereich für die erste Koordinate.
- `x2` (tuple): Bereich für die zweite Koordinate.

**Rückgabewert:**
- Liste mit `m` zufälligen Punkten.

### `boundary(x1=(-1, 1), x2=(-1, 1))`
Erstellt eine zufällige Entscheidungsgrenze basierend auf zwei zufällig gewählten Punkten.

**Rückgabewert:**
- Ein Tupel `(b, -m, 1)`, das die Gleichung einer Linie repräsentiert: `b + x1 * (-m) + x2 * 1 = 0`.

### `predict(weight, data)`
Klassifiziert die gegebenen Datenpunkte basierend auf den Gewichtungen der Entscheidungsgrenze.

**Parameter:**
- `weight` (tuple): Die von `boundary` erzeugten Gewichte.
- `data` (list): Die zu klassifizierenden Punkte.

**Rückgabewert:**
- Die übergebene Datenliste mit einer zusätzlichen Spalte für die Klassifikation (`1` oder `-1`).

## Beispiel
```python
if __name__ == '__main__':
    x_ext = generate()
    w = boundary()
    x = predict(w, x_ext)
    print(x)
```

## Voraussetzungen
- Python 3.x

## Installation
Kein spezielles Setup erforderlich. Einfach das Skript ausführen:
```sh
python script.py
```

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
