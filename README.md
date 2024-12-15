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

### 1. **Stable Diffusion WebUI vorbereiten**

Um diese Anwendung nutzen zu können, muss die **Stable Diffusion WebUI** mit API-Unterstützung ausgeführt werden:

1. Lade die Stable Diffusion WebUI (z. B. **AUTOMATIC1111 WebUI**) herunter und installiere sie gemäß der offiziellen Dokumentation.
2. Stelle sicher, dass du die WebUI mit dem API-Modus startest. Dazu musst du die `webui-user.bat` anpassen:

   ```bash
   set COMMANDLINE_ARGS=--api
   ```

3. Starte die WebUI und vergewissere dich, dass sie unter `http://127.0.0.1:7860` läuft.

### 2. **Klone dieses Repository**

Klone dieses Repository auf deinen lokalen Rechner:

```bash
git clone https://github.com/username/image-generator-app.git
cd image-generator-app
```

### 3. **Installiere die Abhängigkeiten**

Stelle sicher, dass Python 3 installiert ist. Installiere die benötigten Pakete mit:

```bash
pip install -r requirements.txt
```

### 4. **Starte den Flask-Server**

Starte die Anwendung, indem du das Flask-Backend ausführst:

```bash
python app.py
```

### 5. **Öffne die Anwendung im Browser**

Navigiere zu `http://127.0.0.1:5000/` in deinem Browser, um die Anwendung zu verwenden.

---

## 🌐 Deployment

Falls du die Anwendung live hosten möchtest, kannst du Plattformen wie **Heroku**, **Render**, oder **GitHub Pages** verwenden. Beachte, dass für serverseitige Flask-Anwendungen ein Backend-Hosting-Dienst benötigt wird.

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Weitere Details findest du in der Datei [LICENSE](LICENSE).

---

## 🤝 Beitrag leisten

Beiträge sind willkommen! Wenn du Ideen hast oder einen Bug findest, öffne einfach ein **Issue** oder sende einen **Pull Request**.

---

Falls du noch etwas hinzufügen möchtest, lass es mich wissen! 😊
