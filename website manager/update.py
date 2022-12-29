#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

#update file 
def update_file(path, change):
    f = repo.get_contents(path)
    repo.update_file(path, "updating file", change, f.sha)


#viewing and editing the repository 
class Repo_Mang:
    articles = []
    images = []
    def __init__(self):
        contents = repo.get_contents("") #all articles files
        global articles
        articles = contents

        contents = repo.get_contents(path =  "images") #all img files
        global images
        images = contents
    
    def update_article(self, change):
        update_file(self.path, change)
    
    def get_articles(self): #show all images and article files (done)
        global articles
        articles_arr = []
        for x in range(len(articles)):
            if not str(articles[x]) == "ContentFile(path=\"js\")" and not str(articles[x]) == "ContentFile(path=\"images\")" and not str(articles[x]) == "ContentFile(path=\"website manager\")" and not str(articles[x]) == "ContentFile(path=\"riverdale spectator.css\")":
                articles_arr.append(articles[x])
        return articles_arr
    
    def delete():
        print()

    def all_paths(self):
        path_list = []
        for x in self.get_articles():
            path_list.append(str(x)[str(x).index("\"")+1:len(str(x))-2])
        
        return path_list

    def filecontents(self, idx): #get_articles = path_list 
        #get file contents for single file 
        path_list = self.all_paths()
        filecontent = repo.get_contents(path_list[idx]).decoded_content.decode()
        self.path = path_list[idx]

        #get genre of the file & the line of its file 
        megastring = ""
        for x in filecontent:
            megastring += x

        return megastring

    def get_filepath(self):
        path_list = self.all_paths()
        return path_list[self.idx].replace('\n', '')

    def get_genre(self,megastring):
        content_list = megastring.split("content")
        quotation_list = content_list[2].split("\"")
        return quotation_list[1]

    def get_title(self, megastring): #done 
        content_list = megastring.split("content")
        quotation_list = content_list[4].split("\"")
        return quotation_list[1].replace('\n', '')

    def get_date(self, megastring): #done
        content_list = megastring.split("content")
        quotation_list = content_list[1].split("\"")
        return quotation_list[1]

    def get_author(self, megastring): #done
        content_list = megastring.split("content")
        quotation_list = content_list[3].split("\"")
        return quotation_list[1]

    def get_featured(self, megastring): #done
        content_list = megastring.split("name=\"feature\"")
        quotation_list = content_list[0].split("\"")
        return quotation_list[17]

    def get_subtitle(self, megastring):
        FIND = "<h1 class=\"article\" style=\"font-size: 17px; color: rgb(107 114 128)\">"
        tmp = megastring[megastring.index(FIND):len(megastring)]
        subtitle = tmp[len(FIND):tmp.index("</h1>")]
        return subtitle

    def get_img(self, megastring):
        FIND = "<img alt=\"article image\""

        if FIND in megastring:
            tmp = megastring[megastring.index(FIND):len(megastring)]
            img = tmp[len(FIND) + 22:tmp.index("/>")].replace('images\u005c','')
            return img
        else:
            return ""

    def get_photographer(self, megastring):
        if "Photographer:" in megastring:
            FIND = "Photographer:"
            tmp = megastring[megastring.index(FIND):len(megastring)]
            photographer = tmp[len(FIND) + 1:tmp.index("<")]
            return photographer
        else:
            return ""

    def get_body(self, megastring):
        FIND = "<!--article body-->"
        tmp_1 = megastring[megastring.index(FIND):len(megastring)]
        tmp_2 = tmp_1[len(FIND) + 1:tmp_1.index("</div>")]
        tmp_3 = tmp_2.replace('\n', '').split("</p>")
        
        paragraphs = []
        for x in range(len(tmp_3)-1):
            tmp_4 = tmp_3[x].split(">")
            paragraphs.append(tmp_4[1])

        full_txt = ""
        for x in paragraphs:
            full_txt += x + "\n"

        return full_txt

#delete file
class DeleteFile:
    def __init__(self, idx):
        tmp = Repo_Mang()
        tmp.filecontents(idx)

        contents = tmp.all_paths()
        self.filepath = contents[idx].replace("\n", "")
        self.filename = tmp.get_title(tmp.filecontents(idx)).replace("\n", "")
    
    def deletefile(self):
        filecontent = repo.get_contents(self.filepath)
        repo.delete_file(filecontent.path, "removed file", filecontent.sha, branch="main")

        #delete javascript
        fread = repo.get_contents("js/nav.js").decoded_content.decode()
        old = fread.split("\n")
        item_remove = ", [\"" + self.get_title() + "\", \"" + self.get_path() + "\"]"

        change = ""

        for x in range(len(old) - 1):
            change += str(old[x]).replace(item_remove, "") + "\n"
    
        change += str(old[len(old) - 1]).replace(item_remove, "")

        f = repo.get_contents("js/nav.js")
        repo.update_file("js/nav.js", "removing deleted items from search bar", change, f.sha)
    
    def get_title(self):
        return self.filename

    def get_path(self):
        return self.filepath

#update type pages 
class UpdateType:
    def __init__(self):
        self.news = []
        self.opinion = []

        ignore_arr = ["ContentFile(path=\"js\")", "ContentFile(path=\"c&i.html\")", 
            "ContentFile(path=\"critic.html\")", "ContentFile(path=\"images\")", "ContentFile(path=\"js\")", "ContentFile(path=\"opinion.html\")" , 
            "ContentFile(path=\"riverdale spectator.css\")", "ContentFile(path=\"website manager\")", "ContentFile(path=\"news.html\")"]
        self.contents = repo.get_contents("")

        for i in range(len(self.contents) - 1, -1, -1):
            for x in range(len(ignore_arr) - 1, -1, -1): 
                if ignore_arr[x] == str(self.contents[i]):
                    self.contents.pop(i)
                    break
    
    def sort_genre(self):
        for x in range(len(self.contents)):
            #get filename 
            filename = str(self.contents[x]).replace("ContentFile(path=", "").replace("\"", "").replace(")", "")
            
            #get file content
            filecontent = str(repo.get_contents(filename).decoded_content.decode())
            filecontent_arr = filecontent.split("\"")

            #get image
            FIND = "<img alt=\"article image\""

            if FIND in filecontent:
                tmp = filecontent[filecontent.index(FIND):len(filecontent)]
                img = tmp[len(FIND) + 22:tmp.index("/>")].replace('images\u005c','')
                img = "images/" + img.replace("\"", "")
            else:
                img = "images/placeholder.jpg"

            #sort into the right array of types 
            if "News" in filecontent_arr[5]:
                #link, title, author, img, date
                self.news.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            elif "Opinion" in filecontent_arr[5].replace(" ", ""):
                #link, title, author, img, date
                self.opinion.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
        
    def news_op(self, filename):
        filecontent = str(repo.get_contents(filename).decoded_content.decode())

        if filename == "news.html":
            arr = self.news
        elif filename == "opinion.html":
            arr = self.opinion
            
        #top of code 
        tmp_1 = filecontent.split("<!--all articles of type-->")
        top_half = tmp_1[0] + "\n<!--all articles of type-->"

        #bottom of code 
        tmp_2 = tmp_1[1].split("<!--show more button-->")
        bottom_half = "<!--show more button-->\n" + tmp_2[1] + "\n</html>"

        #middle of code 
        middle = ""
        for x in range(len(arr)):
            middle += "<!--article card-->\n<div class = \"flex type_card\">\n<div>\n"
            middle += "<a href = \"" + arr[x][0] + "\">\n<img class = \"typeinner\" alt=\"article image\" src=\"" + arr[x][3] + "\"/>\n</div>"
            middle += "<div class = \"typeinner\">\n <a href = \"" + arr[x][0] + "\">\n"
            middle += "<h1 class = \"hover:underline break-words typeinner\">\n" + arr[x][1] + "</h1>\n"
            middle += "<h2 class = \"typeinner\">" + arr[x][2] + "</h2>\n</div>\n</div>\n"
        
        formatted_content = BeautifulSoup(top_half + middle + bottom_half,'html.parser') #content to be formatted
        update_file(filename, formatted_content.prettify())

x = UpdateType()
x.sort_genre()
x.news_op("opinion.html")
#swap rows 
# thing = [[1,2], 
#               [4,5], 
#               [9,8]]
#     thing[1] = thing[2]