import requests

# 获取网页源代码
source_code = requests.get("https://www.abebooks.com/collections/?cm_sp=TopNav-_-Home-_-Collections").text
with open("source_code.html", "w", encoding="utf-8") as f:
    f.write(source_code)
