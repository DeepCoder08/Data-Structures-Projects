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


├── avl.py # AVL tree implementations (three variants)
├── bin.py # Bin class using AVL trees to store objects
├── exceptions.py # Custom exception: NoBinFoundException
├── gcms.py # Main GCMS logic for adding/removing bins and objects
├── main.py # Testing suite for benchmarking GCMS against a naive implementation
├── node.py # Node class for AVL trees
├── object.py # Object and Color enum definitions

This will:

Add bins and objects

Verify bin and object information

Simulate deletions and reinsertions

Ensure AVL-based GCMS matches a naive reference implementation

⚠️ Exception Handling
The system raises a NoBinFoundException if no bin has sufficient capacity to store a given object.

📌 Requirements
Python 3.6+

No external libraries required

🛠️ Author & License
Author: [Deepanshu 2023MT10689]



🧠 Notes
AVL trees are used to keep insert/search/delete operations logarithmic in time.

This setup is ideal for dynamic bin packing problems or simulations involving resource allocation.

