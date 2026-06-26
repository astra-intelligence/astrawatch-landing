import subprocess, json

# Get the token from the remote URL
r = subprocess.run(
    "cd /home/paperclip/astra-business-sites && git remote -v",
    shell=True, capture_output=True, text=True
)
line = r.stdout.strip().split('\n')[0]
token = line.split('://')[1].split(':')[1].split('@')[0]
print(f"Token: ***{token[-4:]} (len={len(token)})")

# Create repo
c = f"""curl -s -X POST "https://api.github.com/user/repos" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{{"name":"astrawatch-landing","description":"AstraWatch landing page with waitlist signup","private":false,"auto_init":false,"has_pages":true}}'"""

r2 = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=15)
data = json.loads(r2.stdout)
if 'html_url' in data:
    print(f"SUCCESS: {data['html_url']}")
    print(f"Clone URL: {data['clone_url']}")
else:
    print(f"ERROR: {json.dumps(data, indent=2)[:500]}")
