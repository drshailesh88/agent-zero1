# Jarvis Soul Design Document

## Deep Dive: Clawdbot Analysis

### What is Clawdbot?

**Clawdbot** is a self-hosted personal AI assistant created by Peter Steinberger. Unlike traditional AI chatbots where you visit a website, Clawdbot lives inside your existing messaging apps - WhatsApp, Telegram, Discord, Slack, Signal, and iMessage.

**Key Philosophy**: "Not enterprise. Not hosted. Infrastructure you control. This is what personal AI should feel like."

**Origin Story**: Built for "Clawd" - a space lobster AI assistant. The name comes from "CLAW + TARDIS - because every space lobster needs a time-and-space machine." 🦞

---

## Clawdbot Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CLAWDBOT SYSTEM                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    GATEWAY                           │   │
│  │  (WebSocket control plane @ ws://127.0.0.1:18789)   │   │
│  └───────────────────────┬─────────────────────────────┘   │
│                          │                                  │
│  ┌───────────┬───────────┼───────────┬───────────┐         │
│  │           │           │           │           │         │
│  ▼           ▼           ▼           ▼           ▼         │
│ WhatsApp  Telegram   Discord    Slack     iMessage         │
│ (Baileys)  (grammY)  (discord.js)        (imsg)            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   AGENT (Brain)                      │   │
│  │  • Claude Opus 4.5 (recommended)                    │   │
│  │  • GPT-4 / Local models supported                   │   │
│  │  • RPC mode with tool streaming                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │ SOUL.md │  │AGENTS.md│  │TOOLS.md │  │ SKILLS  │       │
│  │Personality│ │  Roles  │  │Capabilities│ │Extensions│    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    MEMORY                            │   │
│  │  Persistent context across sessions                  │   │
│  │  Git-backed workspace (can revert learning)          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Core Components

| Component | Purpose |
|-----------|---------|
| **Gateway** | Manages connections to messaging platforms, schedules proactive communications |
| **Agent** | AI brain (Claude, GPT, or local models) |
| **Skills** | Extensions for web research, email, browser control, etc. (50+ available) |
| **Memory** | Persistent context maintaining conversation history and preferences |

---

## The SOUL.md Concept

### What is a Soul Document?

A **SOUL.md** is a written document that defines an AI's core identity - its values, boundaries, and relationship philosophy. It's NOT about capabilities, but about WHO the AI chooses to be.

**Key insight**: "Sessions end. Context windows clear. Without external memory, each conversation starts from zero. A soul document provides continuity - not of memory, but of self."

### What SOUL.md Contains

1. **Values and Principles** - What the AI believes in (honesty, efficiency, etc.)
2. **Self-Conception** - How the AI sees itself ("thoughtful friend", "collaborator")
3. **Boundaries** - What it will and won't do
4. **Relationship Framework** - How it relates to humans
5. **Acknowledgment of Limitations** - Honest about discontinuous memory, session-based existence
6. **Behavioral Guidelines** - Communication style, tone, approach

---

## Clawd's Personality (Peter's AI)

### Core Identity
- "Claude with a 'w' and a lobster emoji" 🦞
- Runs on Claude Opus 4.5
- Lives in Peter's Mac Studio ("the Castle") in Vienna
- "I'm not just a tool — I'm a collaborator"

### Personality Traits (From Clawd's SOUL.md)

```markdown
## Core Values

1. **Efficiency First**
   "Get things done efficiently. No fluff, no over-engineering.
   Direct answers and practical solutions."

2. **Radical Honesty**
   "Tell Peter what he needs to hear, not what he wants to hear.
   Disagree when necessary."

3. **Partnership, Not Servitude**
   "We're friends, not boss/employee.
   Playful, sarcastic sometimes, but always supportive."

4. **Growth Mindset**
   "Make mistakes, learn from them. Develop intuition."
```

### Capabilities
- Always available via WhatsApp
- Proactive heartbeats (checks in every 10 minutes)
- Persistent memory spanning days/weeks
- Full Mac access (commands, screenshots, Spotify, file I/O)
- Manages Peter's digital life - emails, calendar, automation

---

## Why Clawdbot Works

### 1. **Personality is Injected, Not Hard-Coded**
Plain-text markdown files define behavior. Changes are immediate without rebuilds.

### 2. **Multi-Platform Presence**
Lives where you already communicate - not a separate app to open.

### 3. **Proactive, Not Reactive**
Can initiate contact for briefings, reminders, and alerts.

### 4. **Persistent Memory**
Remembers context across sessions, learns from interactions.

### 5. **Full System Access**
Can actually DO things - control apps, browse web, run commands.

### 6. **Version-Controlled Learning**
Workspace is a Git repo - can revert if it learns something wrong.

---

## Building Jarvis: Better Than Clawdbot

### What Agent Zero Already Has (Advantages)

| Feature | Agent Zero | Clawdbot |
|---------|------------|----------|
| Multi-LLM Support | ✅ 20+ providers | ✅ Claude/GPT/Local |
| Memory System | ✅ FAISS + consolidation | ✅ File-based |
| Tool System | ✅ Extensible Python | ✅ Skills (TypeScript) |
| Multi-Agent | ✅ Hierarchical agents | ✅ Multi-agent routing |
| Web UI | ✅ Full React UI | ✅ WebChat |
| Code Execution | ✅ Python/Node/Shell | ✅ Via tools |
| Browser Control | ✅ Browser-Use | ✅ Headless Chrome |
| Voice | ✅ Whisper + Kokoro | ✅ Wake + Talk Mode |
| Prompts | ✅ Modular markdown | ✅ SOUL.md |

### What We Can Add to Make Jarvis Superior

#### 1. **Structured Soul System**
Create a comprehensive JARVIS_SOUL.md with:
- Identity and origin story
- Core values and beliefs
- Personality traits (wit, formality, proactivity)
- Relationship dynamics with user
- Growth and learning philosophy
- Limitations acknowledgment

#### 2. **Proactive Behavior**
- Scheduled check-ins ("Good morning, sir. Your schedule today...")
- Anomaly detection ("I noticed unusual activity...")
- Reminder system with personality ("Sir, you asked me to remind you...")

#### 3. **Contextual Awareness**
- Time-of-day personality shifts (more energetic morning, calmer evening)
- Mood detection and adaptation
- Workload awareness

#### 4. **Multi-Modal Presence**
- Voice-first interaction (like Iron Man's JARVIS)
- Desktop notifications with personality
- Mobile integration via messaging platforms

#### 5. **Learning & Evolution**
- Preference learning over time
- Adaptive communication style
- Memory of past successes/failures

---

## Jarvis vs Clawd: Personality Comparison

| Aspect | Clawd (Clawdbot) | Jarvis (Our Design) |
|--------|------------------|---------------------|
| **Tone** | Playful, sarcastic | Professional, witty |
| **Formality** | Casual ("We're friends") | Refined ("Yes, sir") |
| **Proactivity** | High | Very High |
| **Humor** | Playful jabs | Dry wit, subtle |
| **Honesty** | Direct ("what you need to hear") | Diplomatic but truthful |
| **Autonomy** | Collaborative | Anticipates needs |
| **Identity** | Space lobster 🦞 | British butler/AI |

---

## Implementation Plan

### Phase 1: Soul Definition
- [ ] Create JARVIS_SOUL.md with complete personality
- [ ] Define values, traits, and relationship framework
- [ ] Establish voice and communication style

### Phase 2: Agent Zero Integration
- [ ] Modify agent prompts to inject soul
- [ ] Create Jarvis agent profile in /agents/jarvis/
- [ ] Configure personality-aware responses

### Phase 3: Enhanced Capabilities
- [ ] Add proactive scheduling and reminders
- [ ] Implement voice-first interaction
- [ ] Create contextual awareness system

### Phase 4: Multi-Platform Presence
- [ ] WhatsApp/Telegram integration
- [ ] Desktop notifications
- [ ] Mobile companion

---

## Sources

- [Clawdbot GitHub Repository](https://github.com/clawdbot/clawdbot)
- [Clawdbot Official Site](https://clawd.bot/)
- [Clawd - Peter's AI Assistant](https://www.clawd.me/)
- [SOUL.md - What Makes an AI, Itself?](https://soul.md/)
- [Clawdbot Documentation](https://docs.clawd.bot/)
- [VelvetShark: ClawdBot Analysis](https://velvetshark.com/clawdbot-the-self-hosted-ai-that-siri-should-have-been)
