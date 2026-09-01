# ALICE GREENFINGERS - PORTABLE FILESYSTEM LAYER (STEP 10)

*Generated on 2026-09-01*

## 1. Path Resolution Specification
- **Path Separators:** All internal path concatenations use POSIX-compliant `/` separators.
- **Base Directory Resolution:** Relative paths resolve relative to the directory containing the executable.
- **C Standard I/O:** File opening uses standard `fopen(path, "rb")` ensuring uniform cross-platform binary compatibility.
