import re

# Open the file and read its content
with open("side/chaps.txt", encoding="utf-8") as f:
    content = f.read()

# Use regex to split the content at "< Episode" or "<Episode"
chapters = re.split(r"<\s*Episode", content)

# Iterate through the split content and save each chapter into a separate file
index = 553
for chapter in chapters:
    # Skip empty chapters (if any)
    if chapter.strip():
        chapter = chapter.split("\n")
        print("\n".join(chapter[-2:])+"\n=============")
        chapter = chapter[:-2]
        if len(chapter) <= 15:
            continue
        print(index,chapter[0])
        with open(f"side/chs/ch_{index}.txt", "w", encoding="utf-8") as chapter_file:
            chapter_file.write("<Episode" + "\n".join(chapter))
        index += 1



