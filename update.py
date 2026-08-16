import json
import subprocess
import re
from datetime import datetime

SCHOLAR_ID = "SVlK4e8AAAAJ"

cmd = [
    "python", "scholar.py",
    "--author-id", SCHOLAR_ID,
    "--citation", "bt"
]

result = subprocess.run(cmd, capture_output=True, text=True)

text = result.stdout

nums = re.findall(r"\|\s*All\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)", text)

if not nums:
    raise Exception("Could not parse Scholar output")

citations, hindex, i10 = nums[0]

data = {
    "citations": int(citations),
    "h_index": int(hindex),
    "i10_index": int(i10),
    "updated": datetime.utcnow().strftime("%Y-%m-%d")
}

with open("metrics.json", "w") as f:
    json.dump(data, f, indent=2)
