# Do Myers-Briggs Personality Dimensions Align with Neural Engagement Patterns During Formal Presentations?

## Overview

This project investigates whether MBTI personality dimensions and Emotional Intelligence (EI) 
categories align with measurable neural engagement patterns during formal student presentations.

EEG bandpower data was collected from 42 anonymised participants via the Muse 2 wearable headband. 
Neural engagement (beta/alpha ratio) and cognitive workload (theta/alpha ratio) were derived from 
raw signals, and unsupervised K-means clustering was applied to identify naturally occurring 
engagement profiles. Clusters were then interpreted against MBTI dimensions and EI categories 
using Tableau visualisations.

The study found that personality dimensions align with neural engagement in terms of timing and 
variability rather than overall magnitude, with Extraverts, Judging, and Thinking types showing 
sharper engagement spikes at key presentation moments, while Introverts and Feeling types sustain 
steadier patterns throughout.

---

## Key Findings

- MBTI dimensions do not predict average neural engagement level, but do align with engagement 
  timing and variability
- Extraverts, Judgers, and Thinking types show sharper neural spikes at key presentation moments
- Introverts and Feeling types engage more consistently, with lower peak volatility
- 86% of participants fall into a single dominant neural engagement cluster
- Higher EI is associated with more stable and regulated neural engagement throughout

---

## Dataset

Anonymised OSC exports from Muse 2 wearable EEG devices, containing timestamped bandpower 
values (delta, theta, alpha, beta, gamma) per participant. MBTI and EI data were provided 
separately and merged at participant level.

All data is anonymised and used solely for academic research purposes.

---

## Tools and Technologies

- Python (pandas, numpy) — data preprocessing and feature engineering
- Weka — K-means clustering
- Tableau — visual analytics (10 visualisations across 2 dashboards)
- Muse 2 wearable EEG device

---

## Academic Context

BSc Information Technology and Business Information Systems
CST3395 – IT Solution Deployment Planning
Middlesex University | 2025/2026
Supervisor: George Dafoulas

---

## Author

[Chioma Audrey Uche-Nwosu](https://www.chiomaaudrey.com)
