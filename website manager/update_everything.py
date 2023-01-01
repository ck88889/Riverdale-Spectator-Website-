#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
import re
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

ignore_arr = ["ContentFile(path=\"js\")", "ContentFile(path=\"c&i.html\")", 
            "ContentFile(path=\"critic.html\")", "ContentFile(path=\"images\")", "ContentFile(path=\"js\")", "ContentFile(path=\"opinion.html\")" , 
            "ContentFile(path=\"riverdale spectator.css\")", "ContentFile(path=\"website manager\")", "ContentFile(path=\"news.html\")", "ContentFile(path=\"index.html\")"]
articles_arr = repo.get_contents("")

for i in range(len(articles_arr) - 1, -1, -1):
            for x in range(len(ignore_arr) - 1, -1, -1): 
                if ignore_arr[x] == str(articles_arr[i]):
                    articles_arr.pop(i)
                    break

print(articles_arr
)