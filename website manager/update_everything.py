#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
import re
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

replacement = """
        <div>
            <!--logo image-->
            <div class = "logo">
                <img class = "logo" src = "images/riverdale spectator logo crop.jpg">
            </div>

            <!--website main pages links-->
            <div class = "nav_links grid grid-cols-5">
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
            </div>

            <!--search bar-->
            <div class = "search_bar">
                <div  class = "shadow-md">
                    <!--icon-->
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" style="padding: 2px; background-color: black; color: white; display:inline-block;" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                        </path>
                    </svg>
                    <!--input-->
                    <input id="searchbar" onkeyup="searchbar()" placeholder="Search..." style="color: black;" type="text"/>
                </div>
                <div id="searchdrop" style="box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;">
                    <div id="searchlist">
                    </div>
                </div>
            </div>
        </div>"""

ignore_arr = ["ContentFile(path=\"c&i.html\")", "ContentFile(path=\"critic.html\")", 
            "ContentFile(path=\"opinion.html\")" ,"ContentFile(path=\"news.html\")", 
            "ContentFile(path=\"index.html\")"]
articles_arr = repo.get_contents("")

for i in range(len(articles_arr) - 1, -1, -1):
            for x in range(len(ignore_arr) - 1, -1, -1): 
                if ignore_arr[x] == str(articles_arr[i]):
                    articles_arr.pop(i)
                    break

path = str(ignore_arr[len(ignore_arr) -1]).replace("ContentFile(path=\"", "").replace("\")", "")
    
#acess file 
filecontent = str(repo.get_contents(path).decoded_content.decode())
arr_1 = filecontent.split("<!--top navigation bar-->")
arr_2 = arr_1[1].split("<!--main articles-->")

updated_file = arr_1[0] + "<!--top navigation bar-->\n" + replacement +  "<!--main articles-->" + arr_2[1]
f = repo.get_contents(path)
formatted_content = BeautifulSoup(updated_file,'html.parser') #content to be formatted
repo.update_file(path, "updating file", updated_file, f.sha)
