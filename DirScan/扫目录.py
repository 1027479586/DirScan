import requests


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

input = input('请输入要扫描的网址:')
url = "http://%s"%(input)
with open("DIR.txt", mode="r") as f:
    for lines in f.readlines():
        line = lines.strip()
        r = requests.get(url + line, headers=headers)
        if r.status_code == 200:
            print("url:" + r.url)




