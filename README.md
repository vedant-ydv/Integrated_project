# Hospitality-App

Orchestrate and run a Hospitality .NET API with dashboard, multimodal
GenAI workflows, and agentic AI orchestration.

## Features Added

-   Classic hospitality APIs: rooms and system info.
-   Multimodal GenAI endpoint:
    -   `POST /api/ai/visualize` -\> narrative + image URL.
-   Multi-agent workflow endpoint:
    -   `POST /api/ai/agents/workflow` -\> Researcher Agent and Writer
        Agent collaborative output.
-   Vector memory search endpoint:
    -   `POST /api/ai/memory/search` -\> top-K semantic matches from
        hospitality knowledge memory.

------------------------------------------------------------------------

## Project Structure

-   **GrandHotel.API/**: .NET 8 Web API with Controllers, Services, and
    Models
-   **wwwroot/**: Cloud-Native Dashboard (HTML/CSS/JS)
-   **k8s/**: Kubernetes deployment files
-   **Dockerfile**: Containerization instructions
-   **serve.js**: Node.js API Gateway & Static Server (Mock
    Implementation)
-   **ai_service.py**: Python FastAPI AI Backend (Mock Implementation)
-   **requirements.txt**: Python dependencies

------------------------------------------------------------------------

## Quick Start (Mock Implementation)

### Prerequisites

-   Node.js (v18 or later)
-   Python (v3.9 or later)

### Steps

1.  Clone the repository and navigate: cd "Hospitality-App-main 2"

2.  Create virtual environment: python3 -m venv venv source
    venv/bin/activate

3.  Install dependencies: pip install -r requirements.txt

4.  Run AI backend: python3 ai_service.py

5.  Run Node server: node serve.js

6.  Open: http://localhost:8080

------------------------------------------------------------------------

## Full .NET Implementation

### Run:

cd Hospitality-App-main/GrandHotel.API dotnet run

------------------------------------------------------------------------

## Docker

docker build -t hospitality-app . docker run -p 8080:8080
hospitality-app

------------------------------------------------------------------------

## API Endpoints

-   GET /api/rooms
-   GET /api/system/info
-   GET /health
-   POST /api/ai/visualize
-   POST /api/ai/agents/workflow
-   POST /api/ai/memory/search
