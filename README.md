Note: Um das ganze Benutzen zu können müssen sie stable diffusion automatic1111 installieren. Benutzen Sie am besten den Github Guide dazu.

---

# 🖼️ Image Generator App

Dies ist eine einfache Webanwendung, mit der Benutzer Bilder entweder durch Texteingaben (**Text-to-Image**) oder durch das Hochladen eines vorhandenen Bildes (**Image-to-Image**) generieren können. Die Anwendung erlaubt die Konfiguration von Parametern wie Bildgröße, Stil und Anzahl der Generierungsschritte.

---

## 📋 Features

- **Text-to-Image (Txt2Img)**: Generiere Bilder basierend auf einer textuellen Beschreibung.
- **Image-to-Image (Img2Img)**: Nutze ein vorhandenes Bild als Grundlage und modifiziere es basierend auf einem Text-Prompt.
- Auswahl des **Stils** (Checkpoint-Modell) für die Bildgenerierung.
- Anpassbare **Bildgrößen** (Breite und Höhe).
- Möglichkeit, **negative Prompts** einzugeben, um unerwünschte Elemente zu vermeiden.
- Einfache Benutzeroberfläche mit direkter Vorschau und **Download-Funktion** für generierte Bilder.

---

## 🚀 Technologien

- **HTML5**, **CSS3**, **JavaScript**
- **Flask (Python)** für die Server-seitige Verarbeitung
- **jQuery** für einfache Frontend-Interaktionen

---

## 📂 Projektstruktur

```
image-generator-app/
├── static/
│   ├── style.css         # CSS-Styles
├── templates/
│   ├── index.html        # Haupt-HTML-Datei
├── app.py                # Flask-Backend
├── requirements.txt      # Python-Abhängigkeiten
```

---

## 🛠️ Installation und Verwendung

1. **Klone das Repository**:
   ```bash
   git clone https://github.com/username/image-generator-app.git
   cd image-generator-app
   ```

2. **Installiere die Abhängigkeiten**:
   Stelle sicher, dass Python 3 installiert ist. Installiere die benötigten Pakete mit:
   ```bash
   pip install -r requirements.txt
   ```

3. **Starte den Flask-Server**:
   ```bash
   python app.py
   ```

4. **Öffne die Anwendung im Browser**:
   - Navigiere zu `http://127.0.0.1:5000/` in deinem Browser.

---

## 🌐 Deployment

Falls du die Anwendung live hosten möchtest, kannst du Plattformen wie **Heroku**, **Render**, oder **GitHub Pages** verwenden. Beachte, dass für serverseitige Flask-Anwendungen ein Backend-Hosting-Dienst benötigt wird.

---

## 🖼️ Beispielbilder

### Text-to-Image:
![Beispielbild Txt2Img](https://via.placeholder.com/400x300)

### Image-to-Image:
![Beispielbild Img2Img](https://via.placeholder.com/400x300)

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Weitere Details findest du in der Datei [LICENSE](LICENSE).

---

## 🤝 Beitrag leisten

Beiträge sind willkommen! Wenn du Ideen hast oder einen Bug findest, öffne einfach ein **Issue** oder sende einen **Pull Request**.

---

Falls du weitere Anpassungen benötigst, lass es mich wissen! 😊
