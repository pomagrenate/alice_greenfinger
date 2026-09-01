#!/usr/bin/env python3
"""
Alice Greenfingers - Standalone Asset Viewer (Phase 16.5)
"""
import os, json

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
REG_FILE = os.path.join(PROJECT_ROOT, 'analysis', 'phase16_5', 'assets', 'graphics_registry.json')

def main():
    print("============================================================")
    print("ALICE GREENFINGERS - RECOVERED GRAPHICAL ASSET VIEWER")
    print("============================================================\n")
    with open(REG_FILE, 'r', encoding='utf-8') as f:
        reg = json.load(f)
    print(f"Total Cataloged Atlases: {reg['total_recovered_atlases']}\n")
    for a in reg['atlases']:
        print(f"- {a['atlas_filename']:20s} | Size: {a['width']:4d}x{a['height']:4d} | Mode: {a['mode']:5s} | Status: {a['confidence']}")

if __name__ == '__main__':
    main()
