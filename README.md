# 📷 AI Camera — Fan Edition

An AI-powered camera app that looks at the world for you — and describes it out loud.

Built for the **DEV Weekend Challenge: Passion Edition**. Point your phone's camera at something and get an instant spoken description, powered by Google's Gemini vision model. Originally built as an assistive tool for blind and low-vision users, this edition adds a **Fan Mode** 🏆 that turns your camera into a hyped-up sports commentator for jerseys, scarves, flags, and match-day gear — perfect for World Cup season.

> 📱 **This app is designed mobile-first.** It uses your phone's rear camera and text-to-speech, and it's meant to be held up and pointed at things in the real world — not used on a desktop. For the best experience, open it on your phone.

## 🔴 Try it live

**[Open on your phone → demirajvazi10-max.github.io/ai-camera-fan-edition](https://demirajvazi10-max.github.io/ai-camera-fan-edition/)**

You'll need a free Gemini API key (see below) — it's entered directly in the app and never leaves your device.

## ✨ Modes

| Mode | What it does |
|---|---|
| 🔍 General | Describes everything in view — objects, colors, people, text, room |
| 🏷️ For Sale | Describes an item like a marketplace listing (condition, details, flaws) |
| 🧍 Person | Describes people in frame — clothing, hair, general appearance |
| 📄 Read Text | Reads any visible text aloud, word for word |
| 🏆 **Fan Mode** | Hypes up jerseys, scarves, flags, and fan gear like a stadium commentator |

## 🛠 How it works

- Pure HTML/CSS/JS, no build step, no backend server required
- Camera access via `getUserMedia` (rear camera preferred)
- Each photo is sent straight from the browser to the **Gemini API** (`gemini-1.5-flash`) with a mode-specific prompt
- The response is read aloud using the browser's built-in **Web Speech API** — free, no extra API needed
- Your Gemini API key is stored only in your browser's `localStorage` — it's never sent anywhere except Google's API

## 🔑 Get a free Gemini API key

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in and create a free key
3. Paste it into the app when prompted

## 🚀 Run it yourself

### Option 1 — Deploy to GitHub Pages (recommended, works on any phone)
1. Fork or clone this repo
2. In repo Settings → Pages, set the source to the `main` branch (root)
3. Open the generated `https://<username>.github.io/<repo>/` link on your phone
4. Camera access requires HTTPS — GitHub Pages gives you that for free

### Option 2 — Run locally and test over WiFi
```bash
python3 run-server.py
```
This starts a local server and prints a `http://<your-ip>:8080` address. Open that address on a phone connected to the **same WiFi network**.

> ⚠️ Note: some mobile browsers block camera access on plain `http://` unless it's `localhost`. If your phone refuses camera permission over WiFi, use Option 1 (GitHub Pages) instead — it's the more reliable path for real device testing.

## 🎯 Why this fits "Passion"

Passion isn't just fandom — it's also the obsession that makes you build something useful at 2am. This app started as a way to help people who can't see describe the world around them. Fan Mode takes that same engine and turns it toward pure, loud, unfiltered team spirit — because sometimes passion is quiet devotion, and sometimes it's screaming about a jersey.

## 🏗 Built with

- [Google Gemini API](https://ai.google.dev/) — image understanding
- Vanilla JS, HTML, CSS — no frameworks, no dependencies
- Web Speech API — text-to-speech

## 📄 License

MIT — feel free to fork, remix, and build your own mode.
