#!/usr/bin/env python3
"""
Standalone PopCap LBTC / GFX Asset Extraction Utility.
Inspects extracted metadata and generates verification manifests with SHA-256 integrity hashes.
"""

import os
import sys
import json
import hashlib

def extract_and_catalog_assets(res_dir, out_json):
    catalog = []
    if not os.path.exists(res_dir):
        print(f"Directory {res_dir} does not exist.")
        return
    
    for f in sorted(os.listdir(res_dir)):
        if f.endswith('_metadata.txt'):
            full_p = os.path.join(res_dir, f)
            data = open(full_p, 'rb').read()
            sha = hashlib.sha256(data).hexdigest()
            lines = open(full_p, 'r', encoding='utf-8', errors='ignore').readlines()
            sprites = [l.strip() for l in lines if l.startswith('Sprite #')]
            catalog.append({
                "container_file": f.replace('_metadata.txt', '.gfx'),
                "metadata_source": f,
                "file_size": len(data),
                "sha256": sha,
                "sprite_count": len(sprites),
                "format": "PopCap LBTC Container (v1)",
                "sample_sprites": sprites[:5]
            })
            
    with open(out_json, 'w', encoding='utf-8') as out_f:
        json.dump(catalog, out_f, indent=2)
    print(f"Cataloged {len(catalog)} asset containers to {out_json}")

if __name__ == '__main__':
    res_dir = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\resources'
    out_json = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\analysis\extracted_assets.json'
    extract_and_catalog_assets(res_dir, out_json)
