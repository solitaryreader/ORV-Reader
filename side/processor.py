import os
import re


for i,file in enumerate(os.listdir("./side/chs")):

    file_index = int(file.replace(".txt", "").replace("ch_",""))
    print(file_index)

    if not file.endswith(".txt"):
        continue
    with open(f"./side/chs/{file}", "r", encoding="utf-8") as f:
        text = f.read().split("\n")

    chap = ""
    title = f"Ch {file_index} {text[0].replace("<","").replace(">", "")}"
    chap += f"<title>{title.replace("Chapter","Ch")}\n"

    text.pop(0)

    for index,line in enumerate(text):

        if line == "":
            chap += "\n"
        elif line.startswith("["):
                cleaned_text = re.sub(r"[\[\]]", "", line)
                chap += f"<!>[{cleaned_text}]\n"
        elif line.startswith("【"):
                cleaned_text = re.sub(r"[【】]", "", line)
                chap += f"<#>【{cleaned_text}】\n"
        elif line.startswith("「"):
                cleaned_text = re.sub(r"[「」]", "", line)
                chap += f"<&>「{cleaned_text}」\n"
        elif line.startswith("(TL"):
                cleaned_text = re.sub(r"[()]", "", line)
                chap += f"<?>{cleaned_text.replace("TL: ", "")}"
        elif line == "*":
            chap += f"***\n"
        else:
            chap += line+"\n"

        
    with open(f"./side/chs/{file}", "w", encoding="utf-8") as f:
        f.write(chap)
