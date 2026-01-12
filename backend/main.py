from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RefineRequest, RefinedPrompt
from refiner import refine_prompt

app = FastAPI(title="Multi-Modal Prompt Refinement System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/refine", response_model=RefinedPrompt)
def refine(data: RefineRequest):
    return refine_prompt(
        text=data.text,
        images=data.images,
        documents=data.documents
    )
