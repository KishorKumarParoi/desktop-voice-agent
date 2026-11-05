# 🎙️ Desktop Voice Assistant

[![Vercel Deployment](https://img.shields.io/badge/Vercel-Production-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://desktop.kishor.tech)
[![LiveKit WebRTC](https://img.shields.io/badge/LiveKit-WebRTC-002B49?style=for-the-badge)](https://livekit.io)

An autonomous, ultra-low latency voice agent built from scratch using the **Nimbus Voice Agent** architecture.

- **Production URL**: [https://desktop.kishor.tech](https://desktop.kishor.tech)
- **Role**: Personal voice assistant that controls your desktop, launches apps, and automates tasks.
- **Capabilities**: Application Control, OS Telemetry & Safe Scripts
- **Sub-400ms Voice Pipeline**: ASR -> OpenAI GPT-4o-mini reasoning -> ElevenLabs Turbo v2.5 TTS.

## 🧪 Testing
```bash
pytest tests/ -v
```
