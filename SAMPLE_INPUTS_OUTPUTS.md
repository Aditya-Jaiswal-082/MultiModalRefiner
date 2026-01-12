Sample Inputs & Refined Outputs


Example 1 – Vague Text Input

Input
I want to build a website


Output (Summary)

Domain: software

Target users: assumed general users

Open question: What type of website?

Confidence: medium


Example 2 – Technical Requirement Input

Input
Build a React app for students to upload assignments and generate reports using Python backend


Output (Summary)

Domain: software

Target users: students

Functional requirements:

Upload files

Generate reports

Technical constraints:

React frontend

Python backend

Confidence: high


Example 3 – Incomplete Product Idea

Input
An app for healthcare


Output (Summary)

Domain: healthcare software

Missing fields:

Functional scope

Target users

Open questions generated

Confidence: low


Example 4 – Ambiguous Input

Input
Create a system to generate prompts automatically


Output (Summary)

Domain: AI tooling

Functional requirement:

Generate structured prompts

Assumption:

Used by developers

Open question:

Input formats?


Example 5 – Irrelevant Input (Rejection Case)

Input
The weather is nice today


Output (Summary)

Domain: not identified

Confidence: very low

Open question:

Is this a product idea?

Refinement halted safely