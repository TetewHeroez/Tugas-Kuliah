# Learnable Petri Net Neural Network Using Max-Plus Algebra

Implementasi paper: **Hameed, M.S.A., Lassoued, S., Schwung, A. (2025)**  
_Machine Learning and Knowledge Extraction_, 7, 100

## 📋 Overview

Proyek ini mengimplementasikan representasi Petri net yang dapat dipelajari menggunakan neural network dalam domain max-plus algebra. Sistem ini mendemonstrasikan bagaimana Timed Event Graphs (TEG) dapat dimodelkan sebagai tropical neural network dan dipelajari menggunakan supervised learning.

## 🎯 Tujuan

1. Menghubungkan **Petri nets** dengan **neural networks** melalui **max-plus algebra**
2. Membuat model yang **interpretable** dan **learnable**
3. Aplikasi pada **production scheduling** di robot manufacturing cell

## 📁 File Structure

```
Neural Network Petri Net/
├── PetriNet.ipynb          # Implementasi lengkap
├── README.md               # Dokumentasi ini
└── (output images)         # Hasil visualisasi
```

## 🚀 Cara Menjalankan

### Prerequisites

```bash
pip install numpy matplotlib seaborn scipy
```

### Running the Notebook

1. Buka `PetriNet.ipynb` di Jupyter/VS Code
2. Run all cells (Ctrl+Shift+Enter atau Run All)
3. Hasil visualisasi akan tersimpan sebagai PNG

## 📊 Komponen Implementasi

### 1. Max-Plus Algebra (`MaxPlusAlgebra` class)

- Operasi ⊕ (max) dan ⊗ (plus)
- Perkalian matriks dan vektor
- Elemen identitas ε dan e

### 2. Tropical Neural Network (`TropicalNeuralNetwork` class)

- Forward pass dengan hard-max units
- Backward pass untuk gradient update
- Activation path tracking

### 3. Training Algorithm

- Dataset generation dengan reference matrices
- Supervised learning dengan L1 loss
- Forward-backward propagation

### 4. Robot Manufacturing Cell Model

- 2 workpiece types (WP₁, WP₂)
- 3 processing stations (S₁, S₂, S₃)
- Processing dan transport times

## 📈 Hasil

### Training Performance

- **Loss convergence**: ~1000 samples
- **Learning rate optimal**: 0.01
- **MAE pada test set**: ~0.18

### Matrix Reconstruction

- **Minkowski distance (A)**: 2.05
- **Minkowski distance (B)**: 0.82

### Visualisasi

1. `training_results.png` - Training loss curve dan matrix error
2. `matrix_elements.png` - Evolusi elemen-elemen matrix
3. `test_predictions.png` - Prediksi vs ground truth

## 🔑 Key Concepts

### Max-Plus Algebra

```
a ⊕ b = max(a, b)
a ⊗ b = a + b
ε = -∞ (identitas ⊕)
e = 0 (identitas ⊗)
```

### TEG Dater Equation

```
x^d(k+1) = A ⊗ x^d(k) ⊕ B ⊗ u^d(k)
```

### Tropical Neural Network

- State equation = two-layer maxout network
- Hard-max activation function
- Learnable matrices A dan B

## 💡 Aplikasi

1. **Production Scheduling**: Optimasi waktu proses produksi
2. **Manufacturing Systems**: Model sistem manufaktur dengan timing uncertainty
3. **Smart Factory**: Online learning untuk adaptive scheduling

## 📚 Referensi

**Paper Utama:**
Hameed, M.S.A., Lassoued, S., Schwung, A. (2025). Learnable Petri Net Neural Network Using Max-Plus Algebra. _Machine Learning and Knowledge Extraction_, 7, 100.

**Konsep Terkait:**

- Petri nets dan Timed Event Graphs
- Max-plus (tropical) algebra
- Neural networks dengan piecewise linear activations
- Production scheduling dan discrete event systems

## 🎓 Untuk Presentasi

Presentasi LaTeX beamer tersedia di:

```
../Aplikasi Petri Net/Aplikasi Petri Net.tex
```

Compile dengan:

```bash
pdflatex "Aplikasi Petri Net.tex"
biber "Aplikasi Petri Net"
pdflatex "Aplikasi Petri Net.tex"
```

## 📝 Catatan Implementasi

### Perbedaan dengan Paper

1. **Simplified model**: Menggunakan 3 state (vs sistem penuh dengan M memory)
2. **Synthetic data**: Random generation (vs real robot data)
3. **Fixed architecture**: TEG structure predefined (vs learned structure)

### Challenges

1. **Initial state**: Harus finite values (bukan -∞) untuk gradient flow
2. **Learning rate**: Perlu tuning untuk convergence
3. **Hard-max**: Non-differentiable, perlu path tracking

## 🔮 Future Improvements

1. ✅ Implementasi dasar dengan supervised learning
2. 🔲 Integrasi reinforcement learning untuk scheduling
3. 🔲 Extend ke multi-job systems
4. 🔲 Real-world data dari manufacturing systems
5. 🔲 Online learning dengan dynamic adaptation

## 👨‍💻 Author

**Teosofi Hidayah Agung** (5002221132)  
Departemen Matematika, Institut Teknologi Sepuluh Nopember

---

_Implementasi untuk mata kuliah Aljabar Max-Plus, Semester 7_
