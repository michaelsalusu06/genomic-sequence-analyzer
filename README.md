# Genomic Sequence Analyzer 🧬👽

A text-based DNA parsing engine built in Python. This terminal application scans string-based genetic sequences to identify standard human biological baselines alongside extraterrestrial, synthetic, and mutant anomalies. 

Built as an exploration of Python's core data structures specifically transitioning algorithmic complete-search logic into Pythonic dictionaries, sets, and control flows.

## Features

* **Strict Input Validation:** An algorithmic "bouncer" that scrubs user input, immediately rejecting numerical, symbolic, or lowercase data before processing.
* **Dual-Database Cross-Referencing:** Scans sequences against two distinct dictionaries simultaneously:
    * `normal`: Standard human traits (e.g., Cellular metabolism, TATA box).
    * `extra`: Sci-fi and anomalous signatures (e.g., Astrophage energy signatures, Chitauri neural links, Klyntar symbiosis, X-Gene).
* **Multi-Trait Detection:** Identifies multiple distinct genetic markers hidden within a single, continuous string.
* **Automated Deduplication:** Utilizes mathematical sets to filter out duplicate genetic markers, ensuring clean, readable output.

## Technologies Used

* **Python 3:** Core logic and execution.
* **Data Structures:** Dictionaries (Key-Value mapping), Lists (Storage), Sets (Deduplication).
* **Control Flow:** Boolean flagging, nested conditionals, and `enumerate()` for formatted UI output.

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/michaelsalusu06/genomic-sequence-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd genomic-sequence-analyzer
   ```
3. Run the Python script:
   ```bash
   python scanner.py
   ```

## Example Output

**Input:**
```text
Input genetic sequence here (uppercase letters only):
GGTATAXQATGCRRASTRZZ
```

**Execution:**
```text
Checking input...
1 Standard DNA transcription initiator (TATA box)
2 Baseline human cellular metabolism
3 Astrophage mitochondrial replacement
4 Mutant
```

## Logic & Architecture

This project maps substrings to complex string outputs. It handles O(N*M) character validation efficiently and utilizes Python's `in` keyword for high-speed substring searching. 
