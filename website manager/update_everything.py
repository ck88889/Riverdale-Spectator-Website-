#program to login into github to edit and add files 
from github import Github
from bs4 import BeautifulSoup #format files 
import update
TOKEN = "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"
REPO = "ck88889/Riverdale-Spectator-Website-"

g = Github(TOKEN) #access token - remeber to change 
repo = g.get_repo(REPO) #access repostitory - remeber to change

new_footer = """<!--bottom navigation bar-->
<div class="mt-auto bottom_bar" onclick="reset_search()">
    <!--bottom images and links-->
    <div class = "grid grid-cols-4">
        <!--icon-->
        <div class = "col-span-2">
            <a href = "index.html"><img class = "bottom_logo" src = "images/dark riverdale logo.jpg" alt = "dark logo" /></a>
        </div>
        <!--links-->
        <div class = "bottom_links">
            <h1 class="font-bold">
                CATEGORIES
            </h1>
            <a class="hover:underline" href="news.html">
                News
            </a><br/>
            <a class="hover:underline" href="opinion.html">
                Opinion
            </a><br/>
            <a class="hover:underline" href="critic.html">
                Critic's Corner
            </a><br/>
            <a class="hover:underline" href="c&amp;i.html">
                Culture &amp; Illustrations
            </a>
        </div>
        <!--links-->
        <div class = "bottom_links">
            <h1 class="font-bold">
                QUICK LINKS
            </h1>
            <a class="hover:underline" href="critic.html#book">
                Book Reviews
            </a><br/>
            <a class="hover:underline" href="critic.html#movie">
                Movie Reviews
            </a><br/>
            <a class="hover:underline" href="c&amp;i.html#stories">
                Short Stories
            </a><br/>
            <a class="hover:underline" href="c&amp;i.html#horoscopes">
                Horoscopes
            </a><br/>
            <a class="hover:underline" href="c&amp;i.html#comic">
                Comics
            </a>
        </div>
    </div>
    <!--dividing line-->
    <hr class="dividing_line mx-auto bg-gray-700 rounded border-0" style="height: 1px;"/>
    <!--three icons-->
    <div class = "flex bottom_icons">
        <a href="#" id="instagram" style="display:inline-block" target="_blank"> <svg height="48px" viewbox="0 0 48 48" width="48px" xmlns="http://www.w3.org/2000/svg"> <radialgradient cx="19.38" cy="42.035" gradientunits="userSpaceOnUse" id="yOrnnhliCrdS2gy~4tD8ma" r="44.899"> <stop offset="0" stop-color="#fd5"> </stop> <stop offset=".328" stop-color="#ff543f"> </stop> <stop offset=".348" stop-color="#fc5245"> </stop> <stop offset=".504" stop-color="#e64771"> </stop> <stop offset=".643" stop-color="#d53e91"> </stop> <stop offset=".761" stop-color="#cc39a4"> </stop> <stop offset=".841" stop-color="#c837ab"> </stop> </radialgradient> <path d="M34.017,41.99l-20,0.019c-4.4,0.004-8.003-3.592-8.008-7.992l-0.019-20	c-0.004-4.4,3.592-8.003,7.992-8.008l20-0.019c4.4-0.004,8.003,3.592,8.008,7.992l0.019,20	C42.014,38.383,38.417,41.986,34.017,41.99z" fill="url(#yOrnnhliCrdS2gy~4tD8ma)"> </path> <radialgradient cx="11.786" cy="5.54" gradienttransform="matrix(1 0 0 .6663 0 1.849)" gradientunits="userSpaceOnUse" id="yOrnnhliCrdS2gy~4tD8mb" r="29.813"> <stop offset="0" stop-color="#4168c9"> </stop> <stop offset=".999" stop-color="#4168c9" stop-opacity="0"> </stop> </radialgradient> <path d="M34.017,41.99l-20,0.019c-4.4,0.004-8.003-3.592-8.008-7.992l-0.019-20	c-0.004-4.4,3.592-8.003,7.992-8.008l20-0.019c4.4-0.004,8.003,3.592,8.008,7.992l0.019,20	C42.014,38.383,38.417,41.986,34.017,41.99z" fill="url(#yOrnnhliCrdS2gy~4tD8mb)"> </path> <path d="M24,31c-3.859,0-7-3.14-7-7s3.141-7,7-7s7,3.14,7,7S27.859,31,24,31z M24,19c-2.757,0-5,2.243-5,5	s2.243,5,5,5s5-2.243,5-5S26.757,19,24,19z" fill="#fff"> </path> <circle cx="31.5" cy="16.5" fill="#fff" r="1.5"> </circle> <path d="M30,37H18c-3.859,0-7-3.14-7-7V18c0-3.86,3.141-7,7-7h12c3.859,0,7,3.14,7,7v12	C37,33.86,33.859,37,30,37z M18,13c-2.757,0-5,2.243-5,5v12c0,2.757,2.243,5,5,5h12c2.757,0,5-2.243,5-5V18c0-2.757-2.243-5-5-5H18z" fill="#fff"> </path> </svg> </a>
        <a href="#" id="email"> <svg height="48" viewbox="0 0 48 48" width="48" x="0px" xmlns="http://www.w3.org/2000/svg" y="0px"> <path d="M34,42H14c-4.411,0-8-3.589-8-8V14c0-4.411,3.589-8,8-8h20c4.411,0,8,3.589,8,8v20 C42,38.411,38.411,42,34,42z" fill="#1e88e5"> </path> <path d="M35.926,17.488L29.414,24l6.511,6.511C35.969,30.347,36,30.178,36,30V18 C36,17.822,35.969,17.653,35.926,17.488z M26.688,23.899l7.824-7.825C34.347,16.031,34.178,16,34,16H14 c-0.178,0-0.347,0.031-0.512,0.074l7.824,7.825C22.795,25.38,25.205,25.38,26.688,23.899z M24,27.009 c-1.44,0-2.873-0.542-3.99-1.605l-6.522,6.522C13.653,31.969,13.822,32,14,32h20c0.178,0,0.347-0.031,0.512-0.074l-6.522-6.522 C26.873,26.467,25.44,27.009,24,27.009z M12.074,17.488C12.031,17.653,12,17.822,12,18v12c0,0.178,0.031,0.347,0.074,0.512 L18.586,24L12.074,17.488z" fill="#fff"> </path> </svg> </a>
        <a href="#" id="github" target="_blank"> <svg height="100" style="padding-bottom: 100%; width: 50px;" viewbox="0 0 100 100" width="100" x="0px" xmlns="http://www.w3.org/2000/svg" y="0px"> <circle cx="52" cy="52" opacity=".35" r="44"> </circle> <circle cx="50" cy="50" fill="#f2f2f2" r="44"> </circle> <path d="M50,12.5c-20.711,0-37.5,16.789-37.5,37.5S29.289,87.5,50,87.5S87.5,70.711,87.5,50 S70.711,12.5,50,12.5z" fill="#707cc0"> </path> <path d="M60.161,83.936c0-1.122,0.042-4.813,0.042-9.389c0-3.192-1.095-5.281-2.324-6.338 c7.624-0.847,15.626-3.74,15.626-16.888c0-3.736-1.324-6.791-3.518-9.184c0.352-0.866,1.527-4.346-0.341-9.057 c0,0-2.868-0.92-9.402,3.508c-2.734-0.759-5.662-1.139-8.568-1.152c-2.91,0.013-5.838,0.393-8.568,1.152 c-6.538-4.429-9.411-3.508-9.411-3.508c-1.862,4.712-0.687,8.192-0.336,9.057c-2.189,2.393-3.523,5.448-3.523,9.184 c0,13.115,7.99,16.051,15.589,16.915c-0.978,0.856-1.862,2.364-2.173,4.575c-1.95,0.876-6.907,2.386-9.96-2.844 c0,0-1.808-3.285-5.242-3.527c0,0-3.342-0.043-0.235,2.08c0,0,2.244,1.053,3.8,5.006c0,0,2.009,6.656,11.529,4.588 c0.017,2.856,0.046,5.008,0.046,5.821c0,0.385-0.122,0.792-0.383,1.115C45.945,86.292,49.3,87,52.807,87 c2.981,0,5.853-0.509,8.576-1.417C60.502,85.37,60.161,84.613,60.161,83.936z" fill="#f2f2f2"> </path> <path d="M50,89c-21.505,0-39-17.495-39-39s17.495-39,39-39s39,17.495,39,39S71.505,89,50,89z M50,14 c-19.851,0-36,16.149-36,36s16.149,36,36,36s36-16.149,36-36S69.851,14,50,14z" fill="#40396e"> </path> </svg> </a>
    </div>
</div>
</body>"""
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
    arr = filecontent.split("<!--bottom navigation bar-->")

    formatted_content = BeautifulSoup(arr[0] + new_footer,'html.parser') #content to be formatted
    update.update_file(path, formatted_content.prettify())

