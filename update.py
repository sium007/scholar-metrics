from scholarly import scholarly
import json
from datetime import datetime

author = scholarly.search_author_id("SVlK4e8AAAAJ")
author = scholarly.fill(author)

data = {
    "citations": author["citedby"],
    "h_index": author["hindex"],
    "i10_index": author["i10index"],
    "updated": datetime.utcnow().strftime("%Y-%m-%d")
}

with open("metrics.json", "w") as f:
    json.dump(data, f, indent=2)
