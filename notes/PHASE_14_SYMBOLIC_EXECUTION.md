# ALICE GREENFINGERS - SYMBOLIC EXECUTION SPECIFICATION (PHASE 14)

*Generated on 2026-09-01*

## 1. Symbolic Constraint Architecture
- **Engine:** Pure-Python Quantifier-Free Linear Integer Arithmetic (QF_LIA) Solver.
- **Classification:** **`E6 (Automated Symbolic / Constraint Evidence)`**.
- **Model Replay:** Concrete models extracted from SAT solutions are replayed directly against `alice_greenfingers_reconstructed.exe`.
