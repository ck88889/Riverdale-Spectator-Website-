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
    
    def history(self, changes):
        f = repo.get_contents("all_links.txt")
        repo.update_file("all_links.txt", "updating link file", changes, f.sha)

    def update(sel, name, link):
        filecontent = str(repo.get_contents("all_links.txt").decoded_content.decode())
        content_arr = filecontent.split("\n")

        full_txt = ("Name: " + name + " , Link:" + link).replace("\n", "")
        for x in content_arr:
            full_txt += "\n" + x

        f = repo.get_contents("all_links.txt")
        repo.update_file("all_links.txt", "updating link file", full_txt, f.sha)

    def code(self):
        filecontent = str(repo.get_contents("all_links.txt").decoded_content.decode())
        lines = filecontent.split("\n")

        #get rid of empty spaces
        for x in range(len(lines) - 1 , -1, -1):
            if lines[x] == "":
                lines.pop(x)

        #write code for section 
        home_page = "<!--downloadables--> <div> <!--heading--> <h1 class=\"moreheadlines\" style=\"margin-bottom: 30px;\"> <hr/> DOWNLOADABLE PRINT ISSUES <hr/> </h1> <!--links--> <div class = \"downloadable\">"
        for x in range(len(lines)):
            tmp_arr = lines[x].split(",")
            name = tmp_arr[0].replace(":", "", 1).replace("Name", "")
            link = tmp_arr[1].replace(":", "", 1).replace("Link", "")

            home_page += "<!--item--> <div class = \"flex\"> <!--item rectangle--> <div class = \"link_rect\"> </div> <!--indivual link--> <div> <a href = \""
            home_page += link.replace(" ", "") +" \" style = \"display: inline-block;\" class = \"hover:underline\" target=\"_blank\">"
            home_page += name + "</a> <svg style = \"display: inline; width: 30px\" viewBox=\"0 0 24 24\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\" stroke=\"#E10000\"><g id=\"SVGRepo_bgCarrier\" stroke-width=\"0\"></g><g id=\"SVGRepo_iconCarrier\"> <path d=\"M12.0005 3.74985V15.7494\" stroke=\"#E10000\" stroke-width=\"1.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path> <path d=\"M7.56415 11.3131L12.0004 15.7494L16.4367 11.3131\" stroke=\"#E10000\" stroke-width=\"1.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path> <path d=\"M0.750946 15.8993V17.2493C0.750946 18.0449 1.067 18.808 1.62959 19.3706C2.19218 19.9331 2.95521 20.2492 3.75082 20.2492H20.2502C21.0458 20.2492 21.8088 19.9331 22.3714 19.3706C22.934 18.808 23.25 18.0449 23.25 17.2493V15.8993\" stroke=\"#E10000\" stroke-width=\"1.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path> </g></svg> </div> </div>"

        home_page += "</div> </div>"

        return home_page
            