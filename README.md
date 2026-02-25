# upGrad AC Navigator (Development)
**Version:** 1.3.x (Active Development)
**Branch:** `dev`

## Overview
This is the internal development branch for the AC Navigator. This branch focuses on transitioning from a simple program list to a multi-mode intelligence tool (Snapshot & Detailed views).

## Current Infrastructure
- **Script:** `navigator.py` (v1.3.2 Baseline - Dynamic UI)
- **Data Source 1:** `programs.json` (Full 12-program portfolio)
- **Data Source 2:** `curriculum.json` (Deep-dive academic data)

## Branching Strategy
- `main`: Stable releases for AC usage.
- `dev`: Integration branch for new features.
- `feature/*`: Specific feature development (e.g., `feature/input-validation`).

## How to Run
```bash
python navigator.py
