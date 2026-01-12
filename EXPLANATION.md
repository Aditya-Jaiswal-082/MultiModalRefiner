Multi-Modal Prompt Refinement System – Design & Thought Process
1. Problem Understanding

The goal of this assignment is not simply to build an API, but to demonstrate how I approach an open-ended, ambiguous systems design problem.

The core challenge is:

Inputs can be incomplete, noisy, ambiguous

Inputs can come from different modalities

Downstream AI systems require structured, consistent prompts

Therefore, the real problem is standardization under uncertainty, not just parsing text.

2. My Thought Process & Approach
2.1 Key Observations

From the problem statement, I identified four critical challenges:

Input ambiguity
Users rarely provide complete or perfectly structured requirements.

Modal diversity
Text, images, and documents need different extraction strategies.

Consistency requirement
Output must follow a predictable schema regardless of input type.

Explainability
The system must explain what it knows, what it assumes, and what is missing.

2.2 Design Philosophy

Instead of directly jumping to an LLM-heavy solution, I chose a layered approach:

Deterministic structure first

Confidence and uncertainty tracking

Human-readable refinement output

AI-assisted enrichment (future-ready)

This ensures:

Predictable outputs

Debuggability

Easier validation

Better trust in AI pipelines

3. Prompt Template / Data Structure Design
3.1 Why This Structure?

The refined prompt output contains the following top-level sections:

{
  "meta": {},
  "intent": {},
  "functional_requirements": [],
  "technical_constraints": [],
  "non_functional_requirements": [],
  "expected_outputs": [],
  "assumptions": [],
  "open_questions": []
}

3.2 Rationale Behind Each Section
meta

Purpose:

Track confidence

Track detected input types

Record missing fields

Why important:

Downstream AI systems can decide whether to proceed or request clarification.

intent

Purpose:

Capture the core idea

Identify domain and target users

Why important:

Everything else depends on intent clarity.

functional_requirements

Purpose:

What the system must do

Why important:

Primary driver of system behavior.

technical_constraints

Purpose:

Technologies, platforms, limitations

Why important:

Prevents incompatible AI-generated solutions.

non_functional_requirements

Purpose:

Performance, security, usability

Why important:

Often overlooked but critical in real systems.

expected_outputs

Purpose:

What success looks like

Why important:

Helps align stakeholders and AI agents.

assumptions

Purpose:

Explicitly document inferred decisions

Why important:

Makes hidden assumptions visible and auditable.

open_questions

Purpose:

Highlight missing or unclear information

Why important:

Enables iterative refinement instead of silent failure.

4. Handling Missing or Ambiguous Information

Instead of rejecting incomplete inputs, the system:

Lowers confidence score

Adds open questions

Adds assumptions when reasonable

This mirrors real-world requirement engineering, where clarification is iterative.

5. Information Extraction Strategy
Current (Implemented)

Rule-based keyword detection

Lightweight heuristics

Deterministic logic

Future (Planned)

OCR for images

PDF parsing

LLM-based semantic extraction

Cross-modal confidence aggregation

I intentionally started with simple logic to demonstrate architectural clarity before complexity.

6. Validation & Error Handling

Validation is achieved through:

Pydantic schemas

Required vs optional fields

Confidence scoring

Explicit open questions

Irrelevant or empty input:

Reduces confidence

Generates clarification prompts

7. Alternative Approaches Considered
Option 1: Fully LLM-based extraction

❌ Rejected initially due to:

Non-deterministic outputs

Difficult debugging

Harder evaluation

Option 2: Fixed rigid schema with mandatory fields

❌ Rejected because:

Real-world inputs are incomplete

Leads to frequent failures

Chosen Approach: Hybrid & extensible

✅ Deterministic base + AI augmentation

8. My Unique Contribution vs AI Assistance
AI-Assisted:

Boilerplate suggestions

FastAPI setup patterns

React form scaffolding

My Original Contributions:

Prompt template design

Confidence + assumptions concept

Open questions mechanism

Architectural decisions

Evaluation-driven prioritization

I critically evaluated AI suggestions and adapted them to fit the problem constraints instead of blindly using them.

9. Conclusion

This system demonstrates:

Structured thinking

Practical requirement engineering

AI-aware system design

Clear separation of uncertainty vs certainty

The current prototype is intentionally simple but architecturally scalable to full multi-modal intelligence.