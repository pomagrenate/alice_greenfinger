# ALICE GREENFINGERS - PHASE 5 REPRODUCIBILITY MANUAL (STEP 18)

*Generated on 2026-09-01*

## 1. Environment & Prerequisites
- **Operating System:** Windows 10 / 11
- **C/C++ Toolchain:** MinGW-W64 GCC 15.1.0 (`g++`, `gcc`)
- **Build System:** CMake 4.0.1 + Ninja 1.12.1
- **Scripting:** Python 3.11+

## 2. Step-by-Step Reproduction Commands

### Configure & Build Standalone Executable
```powershell
cmake -B build -S reconstructed-source -G Ninja
cmake --build build
```

### Execute Standalone Reconstructed Runtime
```powershell
.\build\alice_greenfingers_reconstructed.exe
```

### Run Asset Extraction & Catalog Tool
```powershell
python tools\asset_extract\extract_assets.py
```

### Run Behavioral Differential Validation Suite
```powershell
python analysis\phase5_behavioral_diff.py
```

### Run Automated Consistency Audit
```powershell
python analysis\phase5_consistency_audit.py
```
