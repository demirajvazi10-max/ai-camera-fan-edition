# AI Camera — Fan Edition 🏆📷

## What I built

**AI Camera** is a phone-camera app that describes what it sees, out loud, in real time — powered by Google's Gemini vision model. It started as an assistive tool for blind and low-vision users (general scene description, reading text aloud, describing an item for a marketplace listing, describing a person's appearance). For this challenge, I added a fifth mode built specifically around **passion**:

🏆 **Fan Mode** — point your phone at a jersey, scarf, flag, or any fan gear, and the app turns into a hyped-up stadium commentator, calling out colors, team details, and team spirit with real enthusiasm. With the World Cup happening right now, it felt like the right moment to build it.

> 📱 **Important: this is a mobile-first app.** It's built around your phone's rear camera and needs to be held up and pointed at real things — please try it on a phone, not a desktop, for the intended experience.

## Try it

🔗 **Live app (open on your phone):** https://demirajvazi10-max.github.io/ai-camera-fan-edition/
🔗 **Source code:** https://github.com/demirajvazi10-max/ai-camera-fan-edition

You'll need a free Gemini API key from [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) — paste it in when the app asks. It's stored only in your browser and never leaves your device except to call Google's API directly.

*(I wasn't able to put together a screen recording for this submission — camera-based apps are a bit awkward to record on a phone! Since the whole thing runs client-side with no backend, the live link above lets you try Fan Mode yourself on your own phone in about 30 seconds.)*

## Inspiration

Passion shows up in different ways. Sometimes it's the quiet kind — building something so a person who can't see can still "see" the world around them. Sometimes it's the loud kind — losing your mind over your team's jersey during a World Cup year. I already had the first one built. Adding Fan Mode let the same engine carry both.

## How I built it

- Vanilla HTML/CSS/JS — no framework, no build step, no backend
- Camera access via `getUserMedia`, photo captured to a canvas and sent as base64 to the **Gemini API** (`gemini-1.5-flash`) with a mode-specific prompt
- Each mode is just a different prompt string — Fan Mode's prompt asks Gemini to respond "like a hyped-up sports commentator hyping up the crowd"
- Responses are read aloud via the browser's Web Speech API (free, works offline once the page is loaded)
- The whole thing is one static `index.html`, so it deploys straight to GitHub Pages with HTTPS — which matters, because phones require a secure context for camera access

## Prize category

Uses **Google AI** (Gemini vision model) as the core of the app — every mode depends on it.

## Notes for judges

- Please test on a phone if possible — that's the intended experience (rear camera + held up to real objects)
- Any Gemini API key works; a free one takes under a minute to generate
- Fan Mode is the new addition for this challenge; the other four modes existed before as an accessibility tool
