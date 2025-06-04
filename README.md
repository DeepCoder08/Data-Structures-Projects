# GCMS: Generalized Container Management System

This project implements a Generalized Container Management System (GCMS) for managing bins and objects using AVL trees for optimized storage and retrieval. It includes a full suite of AVL tree implementations and an efficient mechanism for object allocation based on attributes like size and color.

---

## 🚀 Features

- **Efficient AVL-based data structures** for storing bins and objects.
- **Multiple AVL trees** for different storage and access strategies:
  - Sorted by capacity and ID in ascending/descending order
  - Direct access by bin ID or object ID
- **Color-aware object insertion policy**:
  - `BLUE`: Least capacity, least ID
  - `YELLOW`: Least capacity, greatest ID
  - `RED`: Greatest capacity, least ID
  - `GREEN`: Greatest capacity, greatest ID
- **Exception Handling** for when no suitable bin is found.
- **Test suite** (`main.py`) compares the AVL-based system against a naive implementation to validate correctness.

---

## 📁 Folder Structure

