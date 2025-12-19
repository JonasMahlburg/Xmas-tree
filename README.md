# 🎄 Xmas-tree — Festlicher Terminal-Weihnachtsbaum

Eine kleine, fröhliche Python-Animation, die in deinem Terminal einen bunt dekorierten Weihnachtsbaum aus Sternen ausgibt. Perfekt als nettes Terminal-Gimmick oder kleines Lernprojekt. ✨

---

## ✨ Übersicht

Dieses Projekt enthält ein einfaches Skript (`tree.py`), das mit zufälligen Farben und Sternen einen hübschen Weihnachtsbaum in der Konsole darstellt.

## 🔧 Voraussetzungen

- Python 3.8 oder neuer
- Paket: `termcolor` (für farbige Ausgabe)

Installation von `termcolor`:

```bash
pip install termcolor
```

## ▶️ Nutzung

Im Projektordner genügt ein Aufruf:

```bash
python3 tree.py
```

Das Skript erzeugt einen ASCII-Weihnachtsbaum mit zufälligen Farben für die Sterne. Du kannst die Größe anpassen, indem du den Funktionsaufruf `xmas_tree(20)` in `tree.py` änderst.

## 🎨 Anpassung

- Farben ändern: Passe die Liste `colours = ["red", "green", "blue", "white"]` in `tree.py` an.
- Baumgröße: Ändere den Parameter in `xmas_tree(20)` (z. B. `xmas_tree(10)` für einen kleineren Baum).
- Weiterentwicklung: Du kannst das Skript leicht in ein CLI-Tool umwandeln (z. B. mit `argparse`) oder weitere Deko-Symbole hinzufügen.

## 📸 Beispielausgabe

So könnte die Ausgabe im Terminal aussehen (Farben werden im echten Terminal angezeigt):

```
                 * * * 
                * * * * 
               * * * * * 
              * * * * * * 
                 ###
                 ###
                 ###
```

---

## 🤝 Mitmachen

Beiträge sind willkommen — erstelle einfach einen Issue oder einen Pull Request. Kleines Feature, Bugfix oder ein festliches GIF zur README? Immer her damit!

## 📝 Lizenz

Dieses Projekt steht unter der **MIT License**. Siehe `LICENSE` für Details.

---

Frohe Weihnachten und viel Spaß beim Basteln! 🎅✨
