# ML-Driven Discovery and Property Prediction of Heusler Alloys

This repository contains an end-to-end **machine learning pipeline** for
screening **Heusler alloys** and predicting their key physical properties
using only **chemical composition**.

The project demonstrates how data-driven methods can significantly accelerate
materials discovery by reducing dependence on expensive first-principles
(DFT) calculations.

---

## 🔬 Background & Motivation

Heusler alloys (X₂YZ and XYZ compounds) are a fascinating class of materials
known for:

- Tunable **magnetic properties**
- Half-metallicity
- Applications in **spintronics**, **magnetic sensors**, and **energy devices**

Although their crystal structure is simple, the number of possible
compositions exceeds **hundreds of thousands**, making exhaustive DFT
calculations impractical.

👉 **Goal:** Use machine learning to rapidly screen and predict properties of
Heusler compounds before running costly quantum-mechanical simulations.

---

## 🎯 Project Objectives

- Build a clean dataset of **true Heusler compounds**
- Engineer **physics-informed descriptors**
- Train ML models to predict:
  - **Magnetic behavior** (Magnetic vs Non-magnetic)
  - **Formation energy** (stability trends)
- Enable **instant prediction** for unseen Heusler compositions

---

## 📂 Project Pipeline

1. **Data Collection**
   - DFT data extracted from the **Materials Project**
   - Properties include formation energy, magnetism, band gap, symmetry

2. **Heusler Filtering**
   - Identified valid:
     - Full Heuslers: `X2YZ`
     - Half Heuslers: `XYZ`
   - Removed non-Heusler compounds

3. **Descriptor Engineering**
   Physics-based compositional descriptors:
   - **VEC** – Valence Electron Count (important for Heusler magnetism)
   - **Z_mean, Z_max, Z_min** – Atomic number statistics
   - **χ_diff** – Electronegativity difference

4. **Machine Learning Models**
   - Random Forest Classifier → Magnetism
   - Random Forest Regressor → Formation Energy

5. **Prediction**
   - Predict properties of **new, unseen Heusler compounds**

---

## 🧠 Features Used

| Feature | Physical Meaning |
|------|----------------|
| VEC | Governs magnetic moment (Slater–Pauling behavior) |
| Z_mean | Average atomic size / nuclear charge |
| Z_max / Z_min | Elemental contrast |
| χ_diff | Bonding polarity and hybridization |

These descriptors embed **materials physics** directly into the ML models.

---

## 🤖 Models & Performance

### Magnetism Classification
- Model: Random Forest
- Accuracy: **~88%**
- Task: Magnetic vs Non-magnetic

### Formation Energy Regression
- Model: Random Forest
- Mean Absolute Error: **~0.13 eV/atom**

These results are sufficient for **early-stage materials screening**.

---

## 🔮 Example Usage

### Predict magnetism of a Heusler compound
```bash
python predict_magnetism.py Co2MnSi

Output:

Compound: Co2MnSi
Prediction: Magnetic
Confidence: High


This prediction is performed without running DFT.


heusler_ml_discovery/
│
├── mp_heusler_download.py        # Download DFT data
├── filter_true_heuslers.py       # Identify Heusler compounds
├── make_descriptors.py           # Feature engineering
├── train_magnetism_classifier.py# Train magnetism model
├── train_formation_energy_model.py
├── predict_magnetism.py          # Predict unseen compounds
├── heusler_ml_ready.csv          # Final ML-ready dataset
├── README.md
└── .gitignore


⚠️ Limitations

Structural relaxation effects are not explicitly included

Magnetism treated as a binary classification

Performance depends on available DFT data quality

Despite these, the pipeline is highly effective for rapid screening.

🚀 Future Work

Curie temperature prediction

Topological property classification

Uncertainty-aware ML (active learning)

High-throughput screening of large composition spaces

📜 License

This project is released under the MIT License.

🙌 Acknowledgements

Materials Project for DFT data

Open-source Python scientific ecosystem


---

## ✅ Why this README works (important)

- ✔ Clear motivation (professors love this)
- ✔ Explains *what*, *why*, and *how*
- ✔ Shows scientific maturity (limitations + future work)
- ✔ Easy for anyone to reproduce or extend

---

### 🔑 Next step (optional but powerful)

Do you want me to:
1️⃣ Add **badges + citations** (publication-style)  
2️⃣ Rewrite this for a **conference / proposal version**  
3️⃣ Help you **explain this README verbally to a professor**

Just reply **1 / 2 / 3** 🚀


