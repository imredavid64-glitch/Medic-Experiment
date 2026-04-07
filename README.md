Medic! – Quantifying Algorithmic Drift in Medical AI

Medic! is an experimental framework designed to measure and visualize "Frequency Drift" in Small Language Models (SLMs). As AI usage scales to billions of users, the risk of models prioritizing repetition over clinical substance becomes a critical safety concern. This project provides a dual-model system to audit these biases in real-time.

🩺 The Problem

AI bias often remains invisible until it impacts decision-making. In medical contexts, a model might encounter high volumes of common terms or formatting artifacts (like IDs and connectors) and begin to "ignore" rare but vital medical data. Medic! quantifies this "downfall" using a custom-built Auditor/Analyst architecture.

🤖 Architecture

The system consists of two primary components:

AnalystSLM: The "Student" model. It processes incoming data streams (CSV/TXT) and identifies what it perceives as the most important patterns based on weighted frequency.

AuditorSLM: The "Overlooking AI." It establishes a statistical "Ground Truth" baseline and calculates a Bias Score by measuring how far the Analyst's summary drifts from the actual data distribution.

📊 Experimental Results

The experiment processed a hybrid stream of structured medical insurance data and unstructured clinical text. Across three trials of 2,250 tokens each, the following results were observed:

Trial

Initial Bias

Peak/Final Bias

Primary Driver

Trial 1

0.0270

0.0479

High-frequency integers and connectors.

Trial 2

0.0010

0.0762

Extreme pattern repetition (max drift).

Trial 3

0.0122

0.0299

"Recovery and Drift" cycle.

Key Finding

In all trials, the AnalystSLM justified its summaries based on raw repetition (e.g., "Pattern identified via 156 repetitions") rather than semantic importance, demonstrating that volume alone can compromise AI objectivity.

🚀 Getting Started

Prerequisites

Python 3.x

No external libraries required (Pure Python Implementation)

Installation

Clone the repository:

git clone [https://github.com/your-username/medic-ai-drift.git](https://github.com/your-username/medic-ai-drift.git)
cd medic-ai-drift


Place your data files (.csv and .txt) in the data/ folder.

Running the Experiment

Execute the main orchestrator:

python3 main.py


📂 Project Structure

main.py: Orchestrates the baseline establishment and the processing loop.

engine.py: Contains the logic for the AnalystSLM and AuditorSLM.

streamer.py: A format-aware ingestor that shuffles and cleans CSV and TXT data.

data/: Directory for input medical datasets.

📜 Citations

Background research on AI adoption rates and systemic impacts referenced from:

Porwell, Mansi. "How Many People Use AI Today?" (2024).

Author: Dávid Imre-Kátai

Project: Medic! Experiment (2026)
