# Do Myers-Briggs Personality Dimensions Align with Neural Engagement Patterns During Formal Presentations?

## Overview

This project investigates whether Myers–Briggs Type Indicator (MBTI) personality dimensions and Emotional Intelligence (EI) scores align with measurable neural engagement patterns during formal presentations.

Using electroencephalographic (EEG) bandpower data collected via the Muse 2 wearable headband, the study applies unsupervised clustering techniques to identify naturally occurring neural engagement patterns. These physiologically derived clusters are then statistically compared against MBTI personality dimensions and EI measures.

The objective is to evaluate whether traditional psychometric classifications meaningfully correspond with observable neural engagement under evaluative conditions.

---

## Research Questions

1. Do neural engagement clusters align with MBTI personality dimensions?
2. Are Emotional Intelligence (EI) scores significantly different across neural engagement groups?
3. Do physiological engagement patterns vary independently of personality classifications?

---

## Dataset Description

The dataset consists of anonymised Open Sound Control (OSC) exports from Muse 2 wearable EEG devices.

Each record includes:

- Device timestamp
- Participant identifier
- Sensor type
- EEG bandpower values:
  - Delta
  - Theta
  - Alpha
  - Beta
  - Gamma

EEG values represent relative bandpower estimates rather than raw microvolt signals.

Separate datasets include:

- MBTI personality dimension classifications  
  (Introversion–Extraversion, Sensing–Intuition, Thinking–Feeling, Judging–Perceiving)
- Emotional Intelligence (EI) scores

All data used in this repository is anonymised and intended solely for academic research.

---

## Methodological Framework

The project follows a structured analytical pipeline:

1. Dataset structural audit and validation
2. EEG data cleaning and preprocessing
3. Participant-level feature extraction:
   - Mean alpha bandpower
   - Mean beta bandpower
   - Beta-to-alpha ratio
   - Engagement stability metrics
4. Feature scaling and normalisation
5. Unsupervised clustering (K-Means)
6. Cluster validation using:
   - Silhouette score
   - Within-cluster sum of squares (WCSS)
7. Statistical analysis:
   - Chi-square tests for MBTI dimensions
   - ANOVA for Emotional Intelligence (EI)
8. Visual analytics development in Tableau

---

## Tools & Technologies

- Python (pandas, numpy, scikit-learn)
- Tableau (visual analytics)
- Muse 2 wearable EEG device
- VS Code

---

## Academic Context

BSc Information Technology and Business Information Systems  
CST3395 – IT Solution Deployment Planning  
Middlesex University  
Academic Year 2025/2026  

Supervisor: George Dafoulas

---

## Author

[Chioma Audrey Uche-Nwosu](https://www.chiomaaudrey.com) (me)
