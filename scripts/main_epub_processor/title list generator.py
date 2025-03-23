import re
import os
import json

titles = []

for file_index, file in enumerate(os.listdir("formatted")):
    if not file.endswith(".txt"):
        continue
    with open(f"./formatted/{file}", "r", encoding="utf-8") as f:
        textStr = f.read()
        text = textStr.split("\n")

    skip_line = 0
    for index, line in enumerate(text):
        if line.startswith("<title>"):
            line = re.sub(r"<title>", "", line)
            titles.append({"index": index, "title": str(line)})

# Ensure non-ASCII characters are written properly
json.dump(titles, open("titles.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)

for index,item in enumerate(titles):
    print(f"""<div class="chapter_item"><p><a href="#chapter{index}">f{item}</a></p></div>""")