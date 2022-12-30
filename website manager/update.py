#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
import re
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
        filecontent = str(repo.get_contents(path_list[idx]).decoded_content.decode())
        self.path = path_list[idx]

        return filecontent

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

        if FIND in megastring:
            tmp = megastring[megastring.index(FIND):len(megastring)]
            subtitle = tmp[len(FIND):tmp.index("</h1>")]
            return subtitle
        else:
            return ""

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

    def get_body(self, filecontent):
        tmp_1 = filecontent.split("<!--article body-->")
        tmp_2 = tmp_1[1].split("<!--bottom navigation bar-->")

        #strip html tags 
        CLEANR = re.compile('<.*?>') 
        cleantext = (re.sub(CLEANR, '', tmp_2[0])).split("\n")

        #get rid of blank spaces 
        for x in range(len(cleantext) - 1, -1, -1 ):
            if cleantext[x].replace(" ", "") == "":
                cleantext.pop(x)

        #join text 
        full_txt = ""
        for x in cleantext:
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
        self.book = []
        self.movie = []
        self.other = []
        self.stories = []
        self.horoscopes = []
        self.comics = []

        ignore_arr = ["ContentFile(path=\"js\")", "ContentFile(path=\"c&i.html\")", 
            "ContentFile(path=\"critic.html\")", "ContentFile(path=\"images\")", "ContentFile(path=\"js\")", "ContentFile(path=\"opinion.html\")" , 
            "ContentFile(path=\"riverdale spectator.css\")", "ContentFile(path=\"website manager\")", "ContentFile(path=\"news.html\")", "ContentFile(path=\"puzzles.html\")"]
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
            if "<img alt=\"article image\" class=\"comic\"" in filecontent: #img of comic file
                tmp = filecontent[filecontent.index("<img alt=\"article image\" class=\"comic\""):len(filecontent)]
                img = tmp[len("<img alt=\"article image\"") + 27:tmp.index("/>")].replace('images\u005c','')
                img = ("images/" + img.replace("\"", ""))
            elif "<img alt=\"article image\"" in filecontent: #img of regular file 
                tmp = filecontent[filecontent.index("<img alt=\"article image\""):len(filecontent)]
                img = tmp[len("<img alt=\"article image\"") + 22:tmp.index("/>")].replace('images\u005c','')
                img = "images/" + img.replace("\"", "")
            else:
                img = "images/placeholder.jpg"

            #sort into the right array of types 
            if "News" in filecontent_arr[5]:
                #link, title, author, img, date
                self.news.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            elif "Opinion" in filecontent_arr[5]:
                #link, title, author, img, date
                self.opinion.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            #crictic's corner
            elif "Book Reviews" in filecontent_arr[5]:
                #link, title, author, img, date
                self.book.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            elif "Movie Reviews" in filecontent_arr[5]:
                #link, title, author, img, date
                self.movie.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            #culture and illustrations
            elif "Short Stories" in filecontent_arr[5]:
                #link, title, author, img, date
                self.stories.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            elif "Horoscopes" in filecontent_arr[5]:
                img = "images/fortune placeholder.jpg"
                #link, title, author, img, date
                self.horoscopes.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            elif "Other" in filecontent_arr[5]:
                #link, title, author, img, date
                self.other.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
            elif "Comics" in filecontent_arr[5]:
                #link, title, author, img, date
                self.comics.append([filename, filecontent_arr[13], filecontent_arr[9], img, filecontent_arr[1]])
        
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
    
    def critic(self):
        filecontent = str(repo.get_contents("critic.html").decoded_content.decode())

        #get top part of the program
        tmp_1 = filecontent.split("<!--movie reviews-->")
        top_half = tmp_1[0] + "\n<!--movie reviews-->"
        
        #generate movie part of the program
        movie_half = "<div id = \"movie\">\n<!---heading-->\n<h2 class = \"culture uppercase\">Movie Reviews</h2>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>\n<b><h2 class=\"type uppercase\">\nthe Latest\n</h2></b>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>"
        #class -> movie for identifying 
        for x in range(len(self.movie)):
            movie_half += "<!--article card-->\n<div class = \"flex type_card\">\n<div>\n"
            movie_half += "<a href = \"" + self.movie[x][0] + "\">\n<img class = \"typeinner\" alt=\"article image\" src=\"" + self.movie[x][3] + "\"/>\n</div>"
            movie_half += "<div class = \"typeinner\">\n <a href = \"" + self.movie[x][0] + "\">\n"
            movie_half += "<h1 class = \"hover:underline break-words typeinner\">\n" + self.movie[x][1] + "</h1>\n"
            movie_half += "<h2 class = \"typeinner\">" + self.movie[x][2] + "</h2>\n</div>\n</div>\n"
        movie_half += "<!--view more movie reviews-->\n<button class=\"more rounded-lg\" id=\"view more\" style = \"margin-left: 300px\" onclick=\"viewmore(all_movie)\">\nView more\n</button>\n</div>"
        
        #generate book part of the program
        book_half = "<!--book reviews heading-->\n<div id = \"book\">\n<h2 class = \"culture uppercase\">Book Reviews</h2>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>\n<b><h2 class=\"type uppercase\">\nthe Latest\n</h2></b>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>"
        #class -> book for identifying 
        for x in range(len(self.book)):
            book_half += "<!--article card-->\n<div class = \"flex type_card\">\n<div>\n"
            book_half += "<a href = \"" + self.book[x][0] + "\">\n<img class = \"typeinner\" alt=\"article image\" src=\"" + self.book[x][3] + "\"/>\n</div>"
            book_half += "<div class = \"typeinner\">\n <a href = \"" + self.book[x][0] + "\">\n"
            book_half += "<h1 class = \"hover:underline break-words typeinner\">\n" + self.book[x][1] + "</h1>\n"
            book_half += "<h2 class = \"typeinner\">" + self.book[x][2] + "</h2>\n</div>\n</div>\n"
        
        book_half += "\n<!--view more book reviews-->\n<button class=\"more rounded-lg\" id=\"view more\" style = \"margin-left: 300px\" onclick=\"viewmore(all_book)\">\nView more\n</button>\n</div>\n</div>"
        
        tmp_2 = tmp_1[1].split("<!--bottom navigation bar-->")
        bottom_half = "\n<!--bottom navigation bar-->\n" + tmp_2[1]

        formatted_content = BeautifulSoup(top_half + movie_half + book_half + bottom_half,'html.parser') #content to be formatted
        update_file("critic.html", formatted_content.prettify())
    
    def culture(self):
        filecontent = str(repo.get_contents("c&i.html").decoded_content.decode())

        #get top part of the program
        tmp_1 = filecontent.split("<!--entertainment heading-->")
        top_half = tmp_1[0]

        #get entertainment section of page 
        entertainment = "<!--entertainment heading-->\n<div id=\"entertainment\">\n<h2 class=\"culture uppercase\">\nEntertainment\n</h2>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>\n<b><h2 class=\"type uppercase\">\nthe Latest\n</h2></b>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>"
        for x in range(len(self.other)):
            entertainment += "<!--article card-->\n<div class = \"flex type_card\">\n<div>\n"
            entertainment += "<a href = \"" + self.other[x][0] + "\">\n<img class = \"typeinner\" alt=\"article image\" src=\"" + self.other[x][3] + "\"/>\n</div>"
            entertainment += "<div class = \"typeinner\">\n <a href = \"" + self.other[x][0] + "\">\n"
            entertainment += "<h1 class = \"hover:underline break-words typeinner\">\n" + self.other[x][1] + "</h1>\n"
            entertainment += "<h2 class = \"typeinner\">" + self.other[x][2] + "</h2>\n</div>\n</div>\n"
        entertainment += "<!--view more book reviews-->\n<button class=\"more rounded-lg\" id=\"view more\" onclick=\"viewmore(all_enter)\" style=\"margin-left: 300px\">\nView more\n</button>\n</div>"

        #get short stories
        stories = "<!--short story heading-->\n<div id=\"stories\">\n<h2 class=\"culture uppercase\">\nShort Stories\n</h2>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>\n<b><h2 class=\"type uppercase\">\nthe Latest\n</h2></b>\n<hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/>"
        for x in range(len(self.stories)):
            stories += "<!--article card-->\n<div class = \"flex type_card\">\n<div>\n"
            stories += "<a href = \"" + self.stories[x][0] + "\">\n<img class = \"typeinner\" alt=\"article image\" src=\"" + self.stories[x][3] + "\"/>\n</div>"
            stories += "<div class = \"typeinner\">\n <a href = \"" + self.stories[x][0] + "\">\n"
            stories += "<h1 class = \"hover:underline break-words typeinner\">\n" + self.stories[x][1] + "</h1>\n"
            stories += "<h2 class = \"typeinner\">" + self.stories[x][2] + "</h2>\n</div>\n</div>\n"
        stories += "<!--view more book reviews-->\n<button class=\"more rounded-lg\" id=\"view more\" onclick=\"viewmore(all_stories)\" style=\"margin-left: 300px\">\nView more\n</button>\n</div>"
        
        #get comics and cartoons
        #top part 
        horoscopes = "<!--horoscopes display--> <div id=\"horoscopes\" style = \"margin-bottom: 50px\"> <!--horoscopes heading--> <h2 class=\"culture uppercase\">Horoscopes</h2> <hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/> <b><h2 class=\"type uppercase\"> the Latest </h2></b> <hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/> <!--horoscopes carousel--> <div class=\"carousel grid grid-cols-12\" style=\"display:flex;align-items:center;\"> <!--back button--> <div><button class=\"carousel\" onclick=\"carouselback(all_horoscopes)\"> <svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.5\" viewbox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M15.75 19.5L8.25 12l7.5-7.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path></svg> </button> </div> <!--display--> <div class=\"col-span-10\" style=\"margin-right: auto; margin-left: auto;\">"
        #middle 
        for x in range(0, len(self.horoscopes), 3):
            horoscopes += "<!--carousel item--><div class=\"carousel_item grid grid-cols-3 gap-3\">\n"
            for y in range(3):
                horoscopes += "<div class=\"carousel_card\"><a href=\"" + self.horoscopes[x + y][0] + "\">"
                horoscopes += "\n\t<img class=\"carousel\" src=\"" + self.horoscopes[x +y][3] + "\" alt = \"carousel image\"/>" 
                horoscopes += "\n\t<h1 class=\"hover:underline break-words carousel_card\">" + self.horoscopes[x + y][1] + "</h1>"
                horoscopes += "\n\t<h2 class=\"break-words carousel_card\">" + self.horoscopes[x + y][2] + "</h2>\n"
                horoscopes += "</a></div>\n"
            horoscopes += "</div>\n"
        #bottom part 
        horoscopes += "</div><!--next button--> <div style=\"margin-right: 0; margin-left: auto;\"><button class=\"carousel\" onclick=\"carouselnext(all_horoscopes)\"> <svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.5\" viewbox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M8.25 4.5l7.5 7.5-7.5 7.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path></svg> </button></div> </div> </div>"

        #get comics and cartoons
        #top part 
        comics = "<!--comics display--> <div id=\"comic\" style = \"margin-bottom: 50px\"> <!--comics heading--> <h2 class=\"culture uppercase\"> Comics and Cartoons </h2> <hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/> <b><h2 class=\"type uppercase\"> the Latest </h2></b> <hr class=\"type mx-auto bg-black rounded border-1 genre\" style=\"height: 1px;\"/> <!--horoscopes carousel--> <div class=\"carousel grid grid-cols-12\" style=\"display:flex;align-items:center;\"> <!--back button--> <div><button class=\"carousel\" onclick=\"carouselback(all_comics)\"> <svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.5\" viewbox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M15.75 19.5L8.25 12l7.5-7.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path></svg> </button> </div> <!--display--> <div class=\"col-span-10\" style=\"margin-right: auto; margin-left: auto;\">"
        #middle 
        for x in range(0, len(self.comics), 3):
            comics += "<!--carousel item--><div class=\"carousel_item grid grid-cols-3 gap-3\">\n"
            for y in range(3):
                comics += "<div class=\"carousel_card\"><a href=\"" + self.comics[x + y][0] + "\">"
                comics += "\n\t<img class=\"carousel\" src=\"" + self.comics[x +y][3] + "\" alt = \"carousel image\"/>" 
                comics += "\n\t<h1 class=\"hover:underline break-words carousel_card\">" + self.comics[x + y][1] + "</h1>"
                comics += "\n\t<h2 class=\"break-words carousel_card\">" + self.comics[x + y][2] + "</h2>\n"
                comics += "</a></div>\n"
            comics += "</div>\n"
        #bottom part 
        comics += "</div><!--next button--> <div style=\"margin-right: 0; margin-left: auto;\"><button class=\"carousel\" onclick=\"carouselnext(all_comics)\"> <svg class=\"w-6 h-6\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.5\" viewbox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M8.25 4.5l7.5 7.5-7.5 7.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"></path></svg> </button></div> </div> </div>"

        tmp_2 = tmp_1[1].split("<!--bottom navigation bar-->")
        bottom_half = "\n</div><!--bottom navigation bar-->\n" + tmp_2[1]
        
        formatted_content = BeautifulSoup(top_half + entertainment + stories + horoscopes + comics + bottom_half,'html.parser') #content to be formatted
        update_file("c&i.html", formatted_content.prettify())

#swap rows 
# thing = [[1,2], 
#               [4,5], 
#               [9,8]]
#     thing[1] = thing[2]