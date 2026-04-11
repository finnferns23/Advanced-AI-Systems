# 🚀 AI Trading System

An autonomous, multi-agent trading platform where AI agents independently research, analyze, and execute trades using tool-based APIs, persistent memory, and market data integration.

This project simulates a hedge-fund-style trading environment powered by modern agentic AI architecture.

---

## 🧠 Overview

This system implements a **multi-agent AI ecosystem** where:

- Each trader is an independent AI agent
- Agents use tools to execute actions (buy/sell, fetch data, etc.)
- A scheduler continuously runs agents
- Trades are executed on simulated accounts
- All activity is logged and visualized in a dashboard

The system uses **Model Context Protocol (MCP)** to expose tools and enable structured agent interaction.

---

## 🏗️ Architecture

### Core Components

#### 1. Trading Engine
- Portfolio management
- Buy/sell execution
- Balance tracking
- Transaction history
- Profit & loss calculation

#### 2. Market Data Layer
- Polygon API integration
- Fallback to simulated data
- Market caching

#### 3. Database (SQLite)
Stores:
- Accounts
- Transactions
- Logs
- Market data

#### 4. MCP Tool Servers
Expose functionality as tools:
- Account operations
- Market price lookup
- Notifications

#### 5. AI Agents
Each trader:
- Has a unique strategy
- Performs research and analysis
- Executes trades autonomously

#### 6. Scheduler
- Runs agents periodically
- Alternates between trading and rebalancing

#### 7. Dashboard (Gradio)
- Portfolio visualization
- Trade logs
- Live updates

#### 8. Observability
- Logs agent activity
- Tracks tool execution

---

## 🤖 Traders & Strategies

| Trader  | Strategy |
|--------|---------|
| Warren | Value investing |
| George | Macro trading |
| Ray    | Diversified systematic |
| Cathie | Innovation / crypto |

---

## 📂 Project Structure

```
.
├── accounts.py
├── accounts_client.py
├── accounts_server.py
├── app.py
├── database.py
├── market.py
├── market_server.py
├── mcp_params.py
├── push_server.py
├── requirements.txt
├── reset.py
├── templates.py
├── tracers.py
├── traders.py
├── trading_floor.py
├── util.py
```

---

## ⚙️ Setup

### 1. Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-trading-system.git
cd ai-trading-system
```

### 2. Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\\Scripts\\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file:

```env
RUN_EVERY_N_MINUTES=60
RUN_EVEN_WHEN_MARKET_IS_CLOSED=true
USE_MANY_MODELS=false

POLYGON_API_KEY=
POLYGON_PLAN=free

BRAVE_API_KEY=

PUSHOVER_USER=
PUSHOVER_TOKEN=

DEEPSEEK_API_KEY=
GOOGLE_API_KEY=
GROK_API_KEY=
OPENROUTER_API_KEY=
```

### 5. Initialize Accounts

```bash
python reset.py
```

---

## ▶️ Running

### Dashboard

```bash
python app.py
```

### Autonomous Trading

```bash
python trading_floor.py
```

---

## 🔌 MCP Integration

The system uses MCP servers for:
- Trading operations
- Market data access
- Notifications

Agents interact with tools instead of direct function calls, enabling modular architecture.

---

## 📊 Features

- Multi-agent trading system
- Autonomous decision-making
- Tool-based architecture
- Strategy-driven agents
- Persistent storage
- Live dashboard
- Logging & tracing

---

## ⚠️ Limitations

- No risk management layer
- No backtesting engine
- Simulated execution model
- Limited real-world integration

---

## 🚀 Future Improvements

- Risk management engine
- Backtesting framework
- Real-time data streaming
- Cloud deployment
- Advanced analytics dashboard

---

## 🧠 Tech Stack

- Python
- MCP (Model Context Protocol)
- LLM Agents
- Gradio
- SQLite
- Polygon API

---

## 📜 License

For educational and experimental use.

---

## ⭐ Summary

This project demonstrates how multi-agent AI systems can autonomously research, analyze, and execute trades using modern tool-based architectures.

It serves as a foundation for building advanced AI-driven trading platforms.

