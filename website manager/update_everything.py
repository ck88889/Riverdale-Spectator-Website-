#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
import update
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

replacement = "<div class=\"logo\"><a href = \"index.html\"><img class=\"logo\" src=\"images/riverdale spectator logo crop.jpg\"/> </a></div>"

ignore_arr = ["ContentFile(path=\"all_links.txt\")", "ContentFile(path=\"js\")", "ContentFile(path=\"c&i.html\")", 
            "ContentFile(path=\"critic.html\")", "ContentFile(path=\"images\")", "ContentFile(path=\"js\")", "ContentFile(path=\"opinion.html\")" , 
            "ContentFile(path=\"riverdale spectator.css\")", "ContentFile(path=\"website manager\")", "ContentFile(path=\"news.html\")", "ContentFile(path=\"index.html\")"]

other_arr = ["ContentFile(path=\"c&i.html\")", "ContentFile(path=\"critic.html\")", "ContentFile(path=\"opinion.html\")" , 
             "ContentFile(path=\"news.html\")", "ContentFile(path=\"index.html\")"]

articles_arr = repo.get_contents("")

for i in range(len(articles_arr) - 1, -1, -1):
            for x in range(len(ignore_arr) - 1, -1, -1): 
                if ignore_arr[x] == str(articles_arr[i]):
                    articles_arr.pop(i)
                    break

for x in range(len(other_arr)):
    path = str(other_arr[x]).replace("ContentFile(path=\"", "").replace("\")", "")
    filecontent = str(repo.get_contents(path).decoded_content.decode())
    arr_1 = filecontent.split("<!--logo image-->")
    arr_2 = arr_1[1].split("<!--website main pages links-->")

    formatted_content = BeautifulSoup(arr_1[0] + "<!--logo image-->"
        + replacement + "<!--website main pages links-->" + arr_2[1],'html.parser') #content to be formatted
    update.update_file(path, formatted_content.prettify())

