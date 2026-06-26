#!/bin/bash
# Extract GitHub token from git-credentials
TOKEN=$(python3 -c "import re; open('/home/paperclip/.git-credentials').read()" 2>/dev/null && \
  python3 -c "
with open('/home/paperclip/.git-credentials') as f:
    line = f.read().strip()
    # extract password from https://user:pass@github.com
    token = line.split('://')[1].split('@')[0].split(':')[1]
    print(token)
")
curl -s -u "astra-intelligence:${TOKEN}" \
  "https://api.github.com/user/repos" \
  -d '{"name":"astrawatch-landing","description":"AstraWatch landing page with waitlist signup","private":false,"auto_init":false}'
