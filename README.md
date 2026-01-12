Project Overview

The Multi-Modal Prompt Refinement System is a full-stack application designed to accept diverse input formats (text, images, documents, or combinations) and transform them into a standardized, structured prompt suitable for downstream AI systems.

This project focuses not only on building a working prototype but also on demonstrating strong system design, structured thinking, and extensibility, which are essential for modern AI-assisted applications.


Objective

To design and implement a system that:

Accepts multi-modal inputs

Extracts core intent and requirements

Normalizes them into a consistent structured prompt format

Handles missing, ambiguous, or incomplete inputs gracefully

Is extensible for future AI/LLM integrations


Problem Statement

Different users describe ideas in different formats — text descriptions, screenshots, PDFs, or design references.
AI systems require structured, consistent prompts to work effectively.

This system bridges that gap by:

Parsing raw, unstructured inputs

Extracting meaningful information

Producing a standardized refined prompt


Features Implemented


1️ Multi-Modal Input Handling (Extensible Design)

Currently supported:

Plain text input

Architecturally supported (future-ready):

Images (product sketches, UI screenshots)

Documents (PDFs, Word specs)

Combination of multiple input types

The system is designed to easily plug in OCR, vision models, or document parsers without changing the core refinement logic.


2️ Prompt Refinement Process

Each input is transformed into a structured prompt containing:

Core intent & purpose

Functional requirements

Technical constraints

Non-functional requirements

Expected outputs

Assumptions

Open questions

Confidence score

This ensures consistent downstream AI consumption, regardless of input format.


3️ Standardized Output Template

The refined prompt follows a strict schema, ensuring uniformity across all inputs.

{
  "meta": {
    "source_types": ["text"],
    "confidence_score": 0.7,
    "missing_fields": []
  },
  "intent": {
    "summary": "",
    "domain": "",
    "target_users": ""
  },
  "functional_requirements": [],
  "technical_constraints": [],
  "non_functional_requirements": [],
  "expected_outputs": [],
  "assumptions": [],
  "open_questions": []
}



System Architecture

mml/
│
├── backend/                # FastAPI backend
│   ├── main.py             # API entry point
│   ├── refiner.py          # Core refinement logic
│   ├── schemas.py          # Pydantic models
│   └── requirements.txt
│
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   └── PromptForm.js
│   │   ├── services/
│   │   │   └── api.js
│   │   └── App.js
│   └── package.json
│
└── README.md



Technical Design Decisions

Information Extraction Strategy

Rule-based keyword extraction (baseline)

Domain inference using heuristics

Confidence scoring based on completeness

Missing information captured as open questions


Validation & Error Handling

Empty input → low confidence score

Missing intent → clarification questions added

Irrelevant inputs → flagged via open questions


Extensibility

Refinement logic is isolated (refiner.py)

Multi-modal handlers can be plugged in without refactoring API

Output schema ensures backward compatibility


Tech Stack
Backend

FastAPI

Pydantic

Uvicorn

Frontend

React

Axios

CSS


▶ How to Run the Project

Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload


Backend will run at:

http://localhost:8000


Swagger docs:

http://localhost:8000/docs


Frontend Setup
cd client
npm install
npm start


Frontend will run at:

http://localhost:3000



Sample Inputs & Refined Outputs

Example Input
Create a web app for students to upload documents and generate structured prompts using React and Python.

Refined Output
{
  "intent": {
    "summary": "Create a web app for students to upload documents...",
    "domain": "software",
    "target_users": "students"
  },
  "functional_requirements": [
    "Allow users to upload files",
    "Generate structured prompt"
  ],
  "technical_constraints": [
    "Frontend must use React",
    "Backend must use Python"
  ],
  "expected_outputs": [
    "Standardized structured prompt (JSON)"
  ]
}


Design Rationale

Why this template?

Separates intent, requirements, and constraints

Mirrors how real product specifications are written

Easily consumable by LLMs and rule-based systems

How missing information is handled?

Captured as:

assumptions

open_questions

Reflected in confidence_score


Alternative Approaches Considered
Approach	Reason Rejected
Free-form text output	Not AI-friendly
Fully LLM-based parsing	Not deterministic
Hard-coded schemas per input	Not scalable

Chosen approach balances:
determinism
clarity
extensibility


My Contribution vs AI Assistance


AI-Assisted

Boilerplate FastAPI setup

React form scaffolding


My Original Contributions

Output schema design

Refinement logic structure

Confidence scoring strategy

Missing data handling approach

System extensibility planning

End-to-end architecture decisions


Future Enhancements

Image OCR + vision model integration

PDF & Word document parsing

LLM-based semantic extraction

User feedback loop to improve confidence scores

Authentication & history tracking


Conclusion

This project demonstrates:

Strong system thinking

Practical full-stack skills

AI-friendly prompt engineering design

Scalable & extensible architecture

It is intentionally designed as a baseline system that can evolve into a production-ready AI prompt processing pipeline.