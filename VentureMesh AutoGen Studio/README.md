# VentureMesh AutoGen Studio

A modular AutoGen-style project that dynamically generates and runs AI agents to create startup ideas.

## Setup

pip install -r requirements.txt
cp .env.example .env

Add your OpenAI API key in `.env`.

## Run

python world.py

## Structure

- world.py – entry point
- creator.py – generates agents
- agent.py – core LLM logic
- messages.py – shared message object
- generated_agents/ – runtime-generated agents
- concepts/ – output ideas
