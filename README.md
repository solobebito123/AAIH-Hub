# AAIH — Apex Agentic & Intelligence Hub

AI-powered appointment setter and lead management system with SMS integration, signal intelligence, and Airbnb market data scraping.

## Multi-Brain AI Engine

Your AAIH Hub is powered by a high-availability 'Multi-Brain' router that dynamically selects the best AI for the task:
- **Aisure (Billy Gene):** Specialized for sales pitches and lead handling.
- **Claude (Anthropic):** The primary technical brain for complex logic and coding.
- **Grok (xAI):** Real-time market intelligence and sentiment analysis from X (Twitter).
- **Emergent Universal Gateway:** High-reliability failover that provides access to all major models (Claude, GPT, Gemini) through a single point.

## Core Modules

### 1. Appointment Setter (Twilio SMS)
Automated scheduling and verification system that talks directly to your leads via text. 

### 2. Signal Intelligence
Scans incoming alerts (TradeSmith, etc.) and cross-references them with real-time sentiment analysis via Grok to score high-conviction trades.

### 3. Airbnb Market Scraper
Automatically fetches competitor pricing and availability in Clermont, FL, calculating market averages to optimize your passive income.

## Setup

1. `pip install -r requirements.txt`
2. Set your API keys in `.env` (see `config.py` for variables).
3. `python webhook.py` to start the Hub.
