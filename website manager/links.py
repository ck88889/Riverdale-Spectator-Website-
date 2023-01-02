#program to login into github to edit and add files 
from github import Github
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

class File:
    def __init__(self) -> None:
        pass

    def read(self):
        filecontent = str(repo.get_contents("all_links.txt").decoded_content.decode())
        return filecontent
    
    def update(sel, name, link):
        filecontent = str(repo.get_contents("all_links.txt").decoded_content.decode())
        content_arr = filecontent.split("\n")

        full_txt = ("Date: " + name + " , Link:" + link).replace("\n", "")
        for x in content_arr:
            full_txt += "\n" + x

        f = repo.get_contents("all_links.txt")
        repo.update_file("all_links.txt", "updating link file", full_txt, f.sha)