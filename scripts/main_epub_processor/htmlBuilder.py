import re
import os
import urllib.parse as urlparse


for file_index,file in enumerate(os.listdir("formatted")):

    # if not file_index == 1:
    #     continue

    if not file.endswith(".txt"):
        continue
    with open(f"./formatted/{file}", "r", encoding="utf-8") as f:
        textStr = f.read()
        text = textStr.split("\n")

    with open("template.html","r",encoding="utf-8") as f:
        template = f.read()
    
    html = []

    skip_line = 0
    for index, line in enumerate(text):
        if skip_line > 0:
            skip_line -= 1
            continue

        if line == "+":
            window_text = []
            window_text.append('<div class="orv_window">')
            if index + 1 > len(text):
                continue
            for window_line in text[index + 1 :]:
                skip_line += 1
                if window_line == "+":
                    break
                if window_line.startswith("["):
                    window_line = f"<h3>{window_line}</h3>"
                else:
                    window_line = f"<p>{window_line}</p>"
                window_text.append(window_line)
            window_text.append("</div>")
            html.extend(window_text)
            continue
        if line == "++":
            window_text = []
            window_text.append('<div class="orv_box">')
            if index + 1 > len(text):
                continue
            for window_line in text[index + 1 :]:
                skip_line += 1
                if window_line == "++":
                    break
                window_line = f'<p class="orv_line">{window_line}</p>'
                window_text.append(window_line)
            window_text.append("</div>")
            html.extend(window_text)
            continue

        if line.startswith("<title>"):
            line = re.sub(r"<title>", '<div class="orv_title"><h1>', line)
            template.replace(r"{{TITLE}}",line)
            html.insert(0,f"{line}</h1></div>")
        elif line.startswith("<!>"):
            line = re.sub(r"<!>", '<div class="orv_system"><p>', line)
            html.append(f"{line}</p></div>")
        elif line.startswith("<@>"):
            line = re.sub(r"<@>", '<div class="orv_constellation"><p>', line)
            html.append(f"{line}</p></div>")
        elif line.startswith("<#>"):
            line = re.sub(r"<#>", '<div class="orv_outergod"><p>', line)
            html.append(f"{line}</p></div>")
        elif line.startswith("<&>"):
            line = re.sub(r"<&>", '<div class="orv_quote"><p>', line)
            html.append(f"{line}</p></div>")
        elif line.startswith("<?>"):
            line = re.sub(r"<\?>", '<div class="orv_notice"><p>', line)
            html.append(f"{line}</p></div>")
        elif line.startswith("<img>"):
            line = re.findall(r"\[(.*?)\]", line)
            html.append(f'<div class="orv_image"><img src="../../../assets/images/{line[0]}" alt="{line[1]}" loading="lazy"></div>')
        elif line == "":
            html.append(f"<br>")
        elif line == "***":
            html.append(f"<hr>")
        elif line.startswith("<list>"):
            line = re.sub(r"<list>", "<ul>", line)
            html.append(f"{line}")
        elif line.startswith("<cover>"):
            line = re.findall(r"\[(.*?)\]", line)
            template = template.replace(r"{{COVER}}",f'<div class="orv_cover"><img src="../../../assets/images/{urlparse.quote(line[0])}" alt="{line[1]}"></div>')
        else:
            html.append(f'<p class="orv_line">{line}</p>')


    if file_index == 0:
        template = template.replace(r"{{PREV}}","..\\")
    else:
        template = template.replace(r"{{PREV}}",f"./{file_index}")

    if file_index == len(os.listdir("formatted"))-1:
        template = template.replace(r"{{NEXT}}","../")
    else:
        template = template.replace(r"{{NEXT}}",f"./{file_index+2}")

    template = template.replace(r"{{CONTENT}}",str("\n".join(html)))

    template = template.replace(r"{{TITLE}}","")
    template = template.replace(r"{{COVER}}","")
    template = template.replace(r"{{PREV}}","")
    template = template.replace(r"{{NEXT}}","")
    with open(f"webpage/stories/orv/read/{file_index+1}.html", "w", encoding="utf-8") as f:
        f.write(template)
