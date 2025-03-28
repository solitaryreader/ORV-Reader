sitemapStart = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

urls = []

with open("./website/meta/orv.json", "r", encoding="utf-8") as f:
    import json
    chapters = json.loads(f.read())

urls.append(sitemapStart)
urls.append(f'''<url><loc>https://orv.pages.dev/</loc><priority>1</priority></url>''')
urls.append(f'''<url><loc>https://orv.pages.dev/stories</loc><priority>1</priority></url>''')
urls.append(f'''<url><loc>https://orv.pages.dev/stories/orv</loc><priority>0.9</priority></url>''')
urls.append(f'''<url><loc>https://orv.pages.dev/stories/cont</loc><priority>0.85</priority></url>''')
urls.append(f'''<url><loc>https://orv.pages.dev/stories/side</loc><priority>0.8</priority></url>''')

for i in chapters:
    urls.append( f'''<url><loc>https://orv.pages.dev/stories/orv/read/ch_{i["index"]+1}</loc><priority>0.6</priority></url>''')

with open("./website/meta/side.json", "r", encoding="utf-8") as f:
    import json
    chapters = json.loads(f.read())

for i in chapters:
    urls.append( f'''<url><loc>https://orv.pages.dev/stories/side/read/ch_{i["index"]+1}</loc><priority>0.4</priority></url>''')


with open("./website/meta/cont.json", "r", encoding="utf-8") as f:
    import json
    chapters = json.loads(f.read())

for i in chapters:
    urls.append( f'''<url><loc>https://orv.pages.dev/stories/cont/read/ch_{i["index"]+1}</loc><priority>0.5</priority></url>''')

urls.append('''</urlset>''')

with open("website/sitemap.xml","w") as f:
    f.write("\n".join(urls))
