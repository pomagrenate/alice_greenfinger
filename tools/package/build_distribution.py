#!/usr/bin/env python3
"""
Standalone Game Distribution Packaging Pipeline.
Bundles the reconstructed executable, asset folders, and generates distribution_manifest.json.
"""

import os
import shutil
import hashlib
import json

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
DIST_DIR = os.path.join(PROJECT_ROOT, 'distribution')
BUILD_EXE = os.path.join(PROJECT_ROOT, 'build', 'alice_greenfingers_reconstructed.exe')
ASSETS_DIR = os.path.join(PROJECT_ROOT, 'assets')
RESOURCES_DIR = os.path.join(PROJECT_ROOT, 'resources')
MANIFEST_PATH = os.path.join(PROJECT_ROOT, 'analysis', 'distribution_manifest.json')

def build_distribution():
    print("Building standalone distribution package...")
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR, exist_ok=True)

    manifest_entries = []

    # Copy executable
    dest_exe = os.path.join(DIST_DIR, 'AliceGreenfingers_Reconstructed.exe')
    shutil.copy2(BUILD_EXE, dest_exe)
    exe_data = open(dest_exe, 'rb').read()
    manifest_entries.append({
        "file": "AliceGreenfingers_Reconstructed.exe",
        "relative_path": "AliceGreenfingers_Reconstructed.exe",
        "size_bytes": len(exe_data),
        "sha256": hashlib.sha256(exe_data).hexdigest(),
        "type": "EXECUTABLE",
        "provenance": "Phase 7 Reconstructed C++ Standalone Target"
    })

    # Copy assets
    dest_assets = os.path.join(DIST_DIR, 'assets')
    shutil.copytree(ASSETS_DIR, dest_assets)
    for root, dirs, files in os.walk(dest_assets):
        for f in files:
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, DIST_DIR)
            data = open(fp, 'rb').read()
            manifest_entries.append({
                "file": f,
                "relative_path": rel.replace('\\', '/'),
                "size_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "type": "ASSET_FILE",
                "provenance": "Extracted Game Asset"
            })

    # Copy resources
    dest_res = os.path.join(DIST_DIR, 'resources')
    shutil.copytree(RESOURCES_DIR, dest_res)
    for root, dirs, files in os.walk(dest_res):
        for f in files:
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, DIST_DIR)
            data = open(fp, 'rb').read()
            manifest_entries.append({
                "file": f,
                "relative_path": rel.replace('\\', '/'),
                "size_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "type": "METADATA_FILE",
                "provenance": "Recovered PopCap LBTC Metadata"
            })

    # Write README.txt
    readme_path = os.path.join(DIST_DIR, 'README.txt')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("ALICE GREENFINGERS - STANDALONE FORENSIC RECONSTRUCTION\n")
        f.write("Evidence-Backed C++ Recreation\n")
        f.write("Built with MinGW GCC 15.1.0 + CMake / Ninja\n")
        f.write("Execute AliceGreenfingers_Reconstructed.exe to run.\n")

    manifest_data = {
        "package_name": "AliceGreenfingers_Reconstructed_Standalone",
        "total_files": len(manifest_entries),
        "files": manifest_entries
    }
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2)

    with open(os.path.join(DIST_DIR, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2)

    print(f"Distribution package created at {DIST_DIR} ({len(manifest_entries)} files cataloged in manifest).")

if __name__ == '__main__':
    build_distribution()
