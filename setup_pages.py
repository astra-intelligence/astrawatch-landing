#!/usr/bin/env python3
"""Setup GitHub Pages for astrawatch-landing repo."""
import subprocess, json

# Read token from git-credentials
token = open('/home/paperclip/.git-credentials').read().strip().split('://')[1].split('@')[0].split(':')[1]

auth_hdr = 'Authorization: Bearer ' + token

# Check repo
r = subprocess.run(['curl', '-s', 'https://api.github.com/repos/astra-intelligence/astrawatch-landing',
                     '-H', auth_hdr], capture_output=True, text=True, timeout=15)
data = json.loads(r.stdout)
print(f"has_pages: {data.get('has_pages')}")
print(f"html_url: {data.get('html_url')}")

# Enable pages
r2 = subprocess.run(['curl', '-s', '-X', 'POST',
                     'https://api.github.com/repos/astra-intelligence/astrawatch-landing/pages',
                     '-H', auth_hdr,
                     '-H', 'Content-Type: application/json',
                     '-d', '{"source":{"branch":"main","path":"/"}}'],
                    capture_output=True, text=True, timeout=15)
try:
    result = json.loads(r2.stdout or '{}')
    print(f"Pages response: {json.dumps(result, indent=2)[:300]}")
except:
    print(f"Raw output: {r2.stdout[:200]}")
    if r2.stderr:
        print(f"Error: {r2.stderr[:200]}")
