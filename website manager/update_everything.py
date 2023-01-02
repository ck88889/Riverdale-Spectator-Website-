#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
import re
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

replacement = """<div class = "nav_links grid grid-cols-8">
                <a class="hover:underline" href="index.html">
                    HOME
                </a>
                <a class="hover:underline" href="news.html">
                 NEWS
                </a>
                <a class="hover:underline" href="opinion.html">
                 OPINION
                </a>
                <a class="hover:underline col-span-2" href="critic.html">
                 CRITIC'S CORNER
                </a>
                <a class="hover:underline col-span-3" style = "text-align: left;" href="c&amp;i.html">
                 CULTURE &amp; ILLUSTRATIONS
                </a>
            </div>"""
old = """<div class = "nav_links grid grid-cols-5">
                <a class="hover:underline" href="index.html">
                    HOME
                </a>
                <a class="hover:underline" href="news.html">
                 NEWS
                </a>
                <a class="hover:underline" href="opinion.html">
                 OPINION
                </a>
                <a class="hover:underline" href="critic.html">
                 CRITIC'S CORNER
                </a>
                <a class="hover:underline" href="c&amp;i.html">
                 CULTURE &amp; ILLUSTRATIONS
                </a>
            </div>"""

ignore_arr = ["ContentFile(path=\"1.html\")", "ContentFile(path=\"images\")", "ContentFile(path=\"js\")", "ContentFile(path=\"riverdale spectator.css\")", "ContentFile(path=\"website manager\")"]
articles_arr = repo.get_contents("")

for i in range(len(articles_arr) - 1, -1, -1):
            for x in range(len(ignore_arr) - 1, -1, -1): 
                if ignore_arr[x] == str(articles_arr[i]):
                    articles_arr.pop(i)
                    break

for x in range(len(articles_arr)):
    path = str(articles_arr[x]).replace("ContentFile(path=\"", "").replace("\")", "")
    filecontent = str(repo.get_contents(path).decoded_content.decode())
    filecontent.replace(old, replacement)

    formatted_content = BeautifulSoup(filecontent,'html.parser') #content to be formatted
    f = repo.get_contents(path)
    repo.update_file(path, "updating file", formatted_content, f.sha)
