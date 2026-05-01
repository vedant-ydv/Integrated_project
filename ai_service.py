import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import time

app = FastAPI(title="Grand Hotel AI Services")

class VisualizationRequest(BaseModel):
    prompt: str

class VisualizationResponse(BaseModel):
    narrative: str
    image_url: str

class AgentRequest(BaseModel):
    topic: str

class AgentResponse(BaseModel):
    research_data: str
    final_output: str
    agents_involved: List[str]

class MemorySearchRequest(BaseModel):
    query: str
    topK: Optional[int] = 3

class MemorySearchResult(BaseModel):
    id: str
    text: str
    score: float

MEMORIES = [
    {"id": "doc-1", "text": "Luxury beach resorts prioritize ocean-facing suites, sunset dining decks, infinity pools, and concierge-driven guest journeys."},
    {"id": "doc-2", "text": "Family-oriented hospitality concepts should include kids activities, safety-focused zoning, flexible meal plans, and nearby attraction tie-ups."},
    {"id": "doc-3", "text": "A business traveler itinerary needs fast check-in, airport transfer, meeting pods, high-speed internet, and wellness breaks."},
    {"id": "doc-4", "text": "Cultural immersion experiences combine local cuisine, craft workshops, guided heritage walks, and storytelling-based evening programming."},
    {"id": "doc-5", "text": "Sustainable hospitality plans use solar lighting, local material interiors, low-waste dining, and water conservation across operations."}
]

@app.post("/ai/visualize", response_model=VisualizationResponse)
async def visualize_concept(request: VisualizationRequest):
    prompt = request.prompt.lower()

    if "resort" in prompt:
        narrative = "A breathtaking tropical resort featuring overwater bungalows..."
        image_url = "https://images.unsplash.com/photo-1540541338287-41700207dee6"
    elif "lobby" in prompt or "interior" in prompt:
        narrative = "An opulent hotel lobby with marble columns..."
        image_url = "https://images.unsplash.com/photo-1566073771259-6a8506099945"
    else:
        narrative = f"A customized hospitality concept for '{request.prompt}'."
        image_url = "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4"

    return VisualizationResponse(narrative=narrative, image_url=image_url)

@app.post("/ai/agents/workflow", response_model=AgentResponse)
async def agent_workflow(request: AgentRequest):
    topic = request.topic
    time.sleep(1)
    research_data = f"Found extensive data on {topic}"
    time.sleep(1)
    final_output = f"Hospitality Strategy Report: {topic.capitalize()}"

    return AgentResponse(
        research_data=research_data,
        final_output=final_output,
        agents_involved=["Researcher_Agent", "Writer_Agent"]
    )

@app.post("/ai/memory/search", response_model=List[MemorySearchResult])
async def search_memory(request: MemorySearchRequest):
    query = request.query.lower()
    top_k = request.topK or 3

    results = []
    for mem in MEMORIES:
        score = 0.0
        for word in query.split():
            if word in mem["text"].lower():
                score += 0.5

        if score > 0:
            results.append(MemorySearchResult(id=mem["id"], text=mem["text"], score=score))

    results.sort(key=lambda x: x.score, reverse=True)
    return results[:top_k]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
