import urllib.parse
import bs4
import urllib
import os
import warnings
import re
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=bs4.XMLParsedAsHTMLWarning)

for file in os.listdir("OEBPS"):
    if not file.endswith(".xhtml"):
        continue
    with open(f"./OEBPS/{file}", "r", encoding="utf-8") as f:
        text = f.read()
        soup = BeautifulSoup(text, "lxml")

    chap = ""
    chap += f"<title>{soup.h3.text}\n"

    for tag in soup.body.children:
        tag: bs4.element.Tag

        if tag.name == "p":
            tag_text = str(tag.text)
            if tag.has_attr("id"):
                tag_id = tag.a["href"]
                chap += f"<!>{tag_id}\n"
            elif tag_text.startswith("[") and tag_text.endswith("]"):
                chap += f"<system>{tag.text}\n"
            elif tag_text.startswith("【") and tag_text.endswith("】"):
                chap += f"<outerGod>{tag.text}\n"
            elif tag_text.startswith("「") and tag_text.endswith("」"):
                chap += f"<quote>{tag.text}\n"
            else:
                chap += f"{tag.text}\n"

        elif tag.name == "br":
            chap += f"\n"

        elif tag.name == "hr":
            chap += f"***\n"

        elif tag.name == "fieldset":
            # chap += f"\n+\n"
            # for tag_child in tag.find_all():
                # tag_child.text = str(tag_child.text)
                # if tag_child.text.startswith("[") and tag.p.text.endswith("]"):
                #     chap += f"[{tag_child.text}]\n"
                # elif tag_child.text.find(":") != -1:
                #     tag_text = tag_child.text.split(":")
                #     tag_text = "<b>" + tag_text[0] + "</b>" + ":" + tag_text[1]
                #     chap += f"{tag_text}\n"
                # else:
                #     chap += f"{tag.text}\n"
            # chap += f"+\n\n"
            chap += f"\n+{str(tag.text).replace("<p>","").replace("</p>","")}+\n\n"
            

        elif tag.name == "img":
            tag_src = ""
            tag_alt = ""
            if tag.has_attr("src"):
                tag_src = urllib.parse.unquote(tag["src"])
            if tag.has_attr("alt"):
                tag_alt = tag["alt"]
            chap += f"<img>[{tag_src}][{tag_alt}]\n"
        elif tag.name == None or "div" or "aside":
            pass
        else:
            print(f"passed tag <{tag.name}>")
        


    for tag_aside in soup.find_all("aside"):
        tag_id = tag_aside["id"]
        chap = chap.replace(f"<!>#{tag_id}", f"<!>{tag_aside.text.strip()}")

    with open(f"./formatted/{file.replace("xhtml","txt")}", "w", encoding="utf-8") as f:
        f.write(chap)
