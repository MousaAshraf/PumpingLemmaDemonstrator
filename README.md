# Pumping Lemma Demonstrator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue)
![License](https://img.shields.io/github/license/MousaAshraf/PumpingLemmaDemonstrator)

## 📖 Overview
**Pumping Lemma Demonstrator** is an interactive educational tool developed in Python to visualize and experiment with the Pumping Lemma for regular and context-free languages. This application features an easy-to-use graphical interface built with Tkinter, allowing users to:
- Define a language (e.g., `aⁿbⁿ`, `aⁿbⁿcⁿ`, palindromes).
- Input a string `s` and split it into substrings `x`, `y`, and `z`.
- Experiment with pumping factor `i` to observe whether the pumped string belongs to the specified language.

This tool is perfect for students, educators, and enthusiasts of formal languages and automata theory.

---

## ✨ Features
- **Language Definition**: Supports common languages such as `aⁿbⁿ`, `aⁿbⁿcⁿ`, and palindromes.
- **Interactive String Pumping**: Split strings into substrings `x`, `y`, and `z` and experiment with different pumping factors `i`.
- **Validation**: Ensures inputs adhere to the Pumping Lemma constraints (e.g., `|y| > 0` and `|xy| ≤ p`).
- **Dynamic Pumping Length**: Allows users to adjust the pumping length dynamically.
- **Result Feedback**: Displays detailed results, including whether the pumped string belongs to the defined language.

---

## 🚀 Getting Started

### Prerequisites
To run the Pumping Lemma Demonstrator, ensure you have the following installed:
- Python 3.x
- Tkinter (comes pre-installed with Python on most platforms)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/MousaAshraf/PumpingLemmaDemonstrator.git
