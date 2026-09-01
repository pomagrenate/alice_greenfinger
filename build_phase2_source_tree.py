#!/usr/bin/env python3
"""
Phase 2 Source Tree Generator for Alice Greenfingers Forensic Reconstruction.
Transforms Phase 0 and Phase 1 evidence-backed architecture blueprint into a
compilable, modular C/C++ reconstruction source tree without modifying original binaries.
"""

import os
import sys
import json
import re
import datetime

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
NOTES_DIR = os.path.join(PROJECT_ROOT, 'notes')
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, 'analysis')
SOURCE_DIR = os.path.join(PROJECT_ROOT, 'reconstructed-source')

def create_directory_structure():
    """Step 1: Create modular directory layout."""
    dirs = [
        os.path.join(SOURCE_DIR, 'include', 'core'),
        os.path.join(SOURCE_DIR, 'include', 'engine'),
        os.path.join(SOURCE_DIR, 'include', 'events'),
        os.path.join(SOURCE_DIR, 'include', 'state'),
        os.path.join(SOURCE_DIR, 'include', 'rendering'),
        os.path.join(SOURCE_DIR, 'include', 'resources'),
        os.path.join(SOURCE_DIR, 'include', 'audio'),
        os.path.join(SOURCE_DIR, 'include', 'objects'),
        os.path.join(SOURCE_DIR, 'include', 'globals'),
        os.path.join(SOURCE_DIR, 'include', 'platform'),
        os.path.join(SOURCE_DIR, 'include', 'recovered'),
        os.path.join(SOURCE_DIR, 'src', 'core'),
        os.path.join(SOURCE_DIR, 'src', 'engine'),
        os.path.join(SOURCE_DIR, 'src', 'events'),
        os.path.join(SOURCE_DIR, 'src', 'state'),
        os.path.join(SOURCE_DIR, 'src', 'rendering'),
        os.path.join(SOURCE_DIR, 'src', 'resources'),
        os.path.join(SOURCE_DIR, 'src', 'audio'),
        os.path.join(SOURCE_DIR, 'src', 'objects'),
        os.path.join(SOURCE_DIR, 'src', 'globals'),
        os.path.join(SOURCE_DIR, 'src', 'platform'),
        os.path.join(SOURCE_DIR, 'src', 'recovered'),
        os.path.join(SOURCE_DIR, 'generated'),
        os.path.join(SOURCE_DIR, 'unresolved'),
        os.path.join(SOURCE_DIR, 'docs'),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print(f"[Step 1] Created {len(dirs)} directories under reconstructed-source/")

def parse_function_matrix():
    """Parse all 1,847 functions from FUNCTION_RECOVERY_MATRIX.md."""
    matrix_path = os.path.join(NOTES_DIR, 'FUNCTION_RECOVERY_MATRIX.md')
    functions = []
    with open(matrix_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.strip()
            if line_str.startswith('| `0x') or line_str.startswith('| 0x'):
                parts = [p.strip().replace('`', '').replace('*', '') for p in line_str.split('|')[1:-1]]
                if len(parts) >= 8:
                    rva = parts[0]
                    fid = parts[1]
                    params = int(parts[2]) if parts[2].isdigit() else 0
                    lines_str = parts[3].replace(' lines', '').replace(' line', '').strip()
                    lines = int(lines_str) if lines_str.isdigit() else 0
                    subsys = parts[4]
                    strings = parts[5]
                    apis = parts[6]
                    conf = parts[7]
                    functions.append({
                        'rva': rva,
                        'id': fid,
                        'params': params,
                        'lines': lines,
                        'subsystem_desc': subsys,
                        'strings': strings,
                        'apis': apis,
                        'confidence_raw': conf
                    })
    print(f"Parsed {len(functions)} functions from FUNCTION_RECOVERY_MATRIX.md")
    return functions

def parse_globals():
    """Parse all 175 globals from RECOVERED_GLOBALS.md."""
    globs_path = os.path.join(NOTES_DIR, 'RECOVERED_GLOBALS.md')
    globals_list = []
    with open(globs_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.strip()
            if 'DAT_' in line_str and line_str.startswith('|'):
                parts = [p.strip().replace('`', '').replace('*', '') for p in line_str.split('|')[1:-1]]
                if len(parts) >= 5:
                    addr = parts[0]
                    freq = parts[1]
                    subsys = parts[2]
                    semantics = parts[3]
                    conf = parts[4]
                    globals_list.append({
                        'address': addr,
                        'freq': freq,
                        'subsystem': subsys,
                        'semantics': semantics,
                        'confidence': conf
                    })
    print(f"Parsed {len(globals_list)} globals from RECOVERED_GLOBALS.md")
    return globals_list

def parse_unresolved_calls():
    """Parse unresolved call sites from PHASE_0E_UNRESOLVED_CALLS.json."""
    unres_path = os.path.join(NOTES_DIR, 'PHASE_0E_UNRESOLVED_CALLS.json')
    with open(unres_path, 'r', encoding='utf-8') as f:
        calls = json.load(f)
    print(f"Parsed {len(calls)} unresolved calls from PHASE_0E_UNRESOLVED_CALLS.json")
    return calls

if __name__ == '__main__':
    create_directory_structure()
    funcs = parse_function_matrix()
    globs = parse_globals()
    unres = parse_unresolved_calls()
