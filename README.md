# ECOMOL-analysis
Chemical species preprocessing and analysis scripts

# FT-MS Time Series Data Clustering and Deep-Sea DOM Comparison

This repository contains analysis code (currently in `First_work.ipynb`) for **time-series FT-MS data from planktotron experiments**.

The workflow:

- Clusters molecular formulas based on their temporal behaviour.
- Filters noisy / rarely occurring formulas.
- Compares experimental clusters to a deep-sea DOM reference.
- Characterizes chemical composition (Van Krevelen, O-parameters).
- Identifies potentially labile species and tracks diversity over time.

---

## Features

- **Preprocessing & filtering**
  - NaN imputation, per-timepoint normalization.
  - Intensity-based noise floor and prevalence filtering.

- **Clustering**
  - Spearman rank-based distance matrices per planktotron.
  - Agglomerative clustering with K-optimisation (silhouette, CH, DB scores).
  - Bootstrap + silhouette-based selection of well-clustered formulas.

- **Chemistry & similarity**
  - Van Krevelen mapping (H/C vs O/C).
  - Similarity to deep-sea DOM via Jaccard, Bray–Curtis, and Jensen–Shannon metrics.
  - Functional O-parameters and diversity indices.

- **Labile species**
  - Instantaneous growth rate analysis to flag labile formulas.

For full methodological details, see **[`docs/methods.md`](docs/methods.md)**.

---

## Getting Started

1. Place the required data in your working directory:
   - `data_big09082023.csv`
   - `Timepoints_Zeiten.xlsx`
2. Ensure `My_Functions.py` is importable (for Van Krevelen & O-parameters).
3. Open and run `First_work.ipynb` in Jupyter / JupyterLab.
4. Adjust key parameters (e.g. cluster number, noise floor, silhouette cutoff) directly in the notebook.

---

## Dependencies

- `numpy`, `pandas`, `matplotlib`, `scipy`
- `scikit-learn` (clustering, metrics, imputation)
- `joblib` (parallelisation)
