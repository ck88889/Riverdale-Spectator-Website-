import update
import generate
import datetime
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog 
from tkinter.simpledialog import askstring
from tkinter.messagebox import askyesno
from tkinter import messagebox

main = Tk()
main.title("WEBSITE MANAGER")
main.geometry("400x400")

#uploading img to github 
def upload_image(img_file, img_name):
    IMG_PREFIX = "images"
    git_file = IMG_PREFIX + "/" + img_name
    update.repo.create_file(git_file, "committing image file", img_file, branch="main")

class File():
    def file_delete(self):
        self.file_heading.grid_remove()

        #delete drop menu of article topics
        self.type_l.grid_remove()
        self.drop_type.grid_remove()

        #delete menu for date
        self.issue_l.grid_remove()
        self.drop_month.grid_remove()
        self.drop_year.grid_remove()

        #delete author input
        self.author_l.grid_remove()
        self.author_entry.grid_remove()

        #delete title input
        self.title_l.grid_remove()
        self.title_entry.grid_remove()

        #delete subtitle input
        self.sub_l.grid_remove()
        self.sub_entry.grid_remove()

        #delete body paragraphs of the article 
        self.buffer2.grid_remove()
        self.body_heading.grid_remove()
        self.body_entry.grid_remove()

        #get image file
        self.buffer1.grid_remove()
        self.getimage_btn.grid_remove()

        #get featured articles
        self.FeaturedButton.grid_remove()

    def get_info(self): #return all info about article 
        #format date 
        date = str(self.month.get()) + " " + self.year.get()

        #get all relevant info 
        info = [self.type.get(), date, self.title_entry.get("1.0",END).replace('\n', ''), self.sub_entry.get("1.0",END).replace('\n', ''),
               self.author_entry.get("1.0",END).replace('\n', ''), self.body_entry.get("1.0",END), self.img_filename, self.photographer, self.isfeatured.get()]
        
        return info

    def back_btn(self):
        self.file_delete()
        new_view = View(self.next, self.back)

    def next_btn(self):
        info = self.get_info() 
        create = generate.Text_Based(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])
        self.selected_file.update_article(create.get_file())

        messagebox.showinfo("Information","Changes have been saved")
        self.back_btn()

    def get_img(self):
        try:
            filename = filedialog.askopenfilename( #select file 
                filetypes=[
                ('image files', ('.png', '.jpg')),
            ]
            )

            with open(filename, "rb") as image:
                f = image.read()  
            
            #get photographer name and generate filename 
            self.photographer = askstring("Photography Credits", "Enter name of the photographer")
            self.img_filename =  str(datetime.datetime.now().strftime("%f")) + ".jpg"
            
            #add img to github            
            git_file = "images/" + self.img_filename #byte array -> what to upload
            update.repo.create_file(git_file, "committing image file", bytes(bytearray(f)), branch="main")

        except:
            pass

    def __init__(self, next, back, selected_idx):
        #heading of page 
        self.file_heading = Label(text = "\n\t     EDIT FILE", font=("Helvetica", 12, "bold"))
        self.file_heading.grid(column=0, row=0, columnspan = 4)
        
        self.selected_file = update.Repo_Mang()
        contents = self.selected_file.filecontents(selected_idx)

        #img filename and photographer name 
        self.img_filename = self.selected_file.get_img(contents)[0: len(self.selected_file.get_img(contents)) - 1]
        tmp = self.selected_file.get_photographer(contents).split("\n")
        self.photographer = tmp[0]

        #type of article 
        self.type_opt = ["News", "Opinion", "Book Reviews", "Movie Reviews" "Horoscopes", "Short Stories", "Other"]
        self.type = StringVar()
        self.type.set(self.selected_file.get_genre(contents))

        #drop menu of article topics 
        self.type_l = Label(main, text = "   Type", font=("Helvetica", 10, "bold"))
        self.drop_type = OptionMenu(main, self.type , *self.type_opt)
        self.drop_type.config(bg="WHITE", width = 10)

        self.type_l .grid(column=0, row=1)
        self.drop_type.grid(column = 1, row =1)

        #drop menu of dates
        date = self.selected_file.get_date(contents).split(" ")

        self.month_opt = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September","October","November","December"]
        self.month = StringVar()
        self.month.set(date[0])

        self.year_opt = []
        tmp_year = 2010
        for x in range(30):
            tmp_year += 1
            self.year_opt.append(tmp_year)
        self.year = StringVar()
        self.year.set(int(date[1]))
        
        self.issue_l = Label(main, text = "   Issue", font=("Helvetica", 10, "bold"))
        self.drop_month = OptionMenu(main, self.month , *self.month_opt)
        self.drop_month.config(bg="WHITE", width = 10)
        self.drop_year = OptionMenu(main, self.year , *self.year_opt)
        self.drop_year.config(bg="WHITE")

        self.issue_l .grid(column=2, row=1)
        self.drop_month.grid(column=3, row = 1)
        self.drop_year.grid(column=4, row = 1)

        #author of the article
        self.author_l = Label(main, text = "  Author", font=("Helvetica", 10, "bold"))
        self.author_entry = Text(main, height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.author_entry.insert(END, self.selected_file.get_author(contents))
        self.author_l.grid(column=0, row=2)
        self.author_entry.grid(column=1, row=2, columnspan = 4)

        #title of the article 
        self.title_l = Label(main, text = "Title", font=("Helvetica", 10, "bold"))
        self.title_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.title_entry.insert(END, self.selected_file.get_title(contents))
        self.title_l.grid(column=0, row=3)
        self.title_entry.grid(column=1, row=3, columnspan = 4)

        #subtitle of the article 
        self.sub_l = Label(main, text = "Subtitle", font=("Helvetica", 10, "bold"))
        self.sub_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.sub_entry.insert(END, self.selected_file.get_subtitle(contents))
        self.sub_l.grid(column=0, row=4)
        self.sub_entry.grid(column=1, row=4, columnspan = 4)

        #get image file
        self.buffer1= Label(text = "", font=("Helvetica", 4, "normal"))
        self.buffer1.grid(column=0, row=5, columnspan = 4)

        self.getimage_btn = Button(main, text ="Replace Image", bg = "white", font=("Helvetica", 9, "normal"))
        self.getimage_btn.grid(column = 3, row = 6, columnspan = 2)

        #get featured articles
        if self.selected_file.get_featured(contents) == "yes":
            self.isfeatured = IntVar(value = 1)
        else:
            self.isfeatured = IntVar(value = 0)

        self.FeaturedButton = Checkbutton(main, text = "Featured",variable = self.isfeatured, 
                onvalue = 1, offvalue = 0, font=("Helvetica", 10, "normal"))
        self.FeaturedButton.grid(column = 1, row = 6)

        #get body text 
        self.buffer2 = Label(text = "", font=("Helvetica", 4, "normal"))
        self.buffer2.grid(column=0, row=7, columnspan = 4)

        self.body_heading = Label(text = "Body", font=("Helvetica", 10, "bold"))
        self.body_heading.grid(column=0, row=6)

        self.body_entry = scrolledtext.ScrolledText(main,height = 8,width = 45, font = ("Helvetica", 10, "normal"))
        self.body_entry.insert(END, self.selected_file.get_body(contents))
        self.body_entry.grid(column=1, row=8, columnspan = 4)

        #pass next and back buttons 
        self.next = next
        self.back = back
        next.configure(command = self.next_btn, text = "Save")
        back.configure(command = self.back_btn, text = "Back")
        self.getimage_btn.configure(command = self.get_img)
        
class View():
    def view_delete(self):
        self.view_heading.forget()
        self.article_listbox.forget()
        self.scrollbar.forget()
        self.frame.forget()
        self.delete_btn.forget()

    def get_file(self, path):
        return path[18:len(path) - 2]
        
    def back_btn(self):
        self.view_delete()
        new_main = Main()

    def next_btn(self):
        self.view_delete() 
        selected_idx = int(str(self.article_listbox.curselection())[1 : len(str(self.article_listbox.curselection())) - 2])
        file = File(self.next, self.back, selected_idx)

    def delete_btn(self):
        selected_idx = int(str(self.article_listbox.curselection())[1 : len(str(self.article_listbox.curselection())) - 2])
        confirmation = askyesno(title='Delete File', message='Are you sure that you want to delete the file?')
        
        if confirmation:
            deletefile = update.DeleteFile(selected_idx)
            deletefile.deletefile() #delete file 

            messagebox.showinfo("Information","The file has been deleted")

            self.view_delete()
            view = View(self.next, self.back)

    def __init__(self, next, back):
        self.view_heading = Label(text = "\n\nAll Files", 
                font=("Helvetica", 15, "normal")) 

        #get all article files 
        self.view = update.Repo_Mang()
        self.all_articles = self.view.get_articles()

        self.frame = Frame(main)

        #view all article files 
        self.article_listbox = Listbox(self.frame, selectmode = "single", width = 55, height = 13)
        index = 0
        for x in self.all_articles:
            self.article_listbox.insert(index, x)
            index += 1
        self.article_listbox.selection_set(0) 

        self.scrollbar = Scrollbar(self.frame, command = self.article_listbox.yview)

        self.delete_btn = Button(main, text ="Delete File", command = self.delete_btn, bg = "white", font=("Helvetica", 9, "normal"), width = 50)
        self.delete_btn.configure(bg="gray62", activebackground="gray62")

        #pass next and back buttons 
        self.next = next
        self.back = back

        next.configure(command = self.next_btn, text="Next")
        back.configure(command = self.back_btn, text="Back")
        self.view_heading.pack()
        self.frame.pack()
        self.article_listbox.pack(side = "left", fill = "y")
        self.scrollbar.pack(side = "right", fill = "y")
        self.delete_btn.pack()
        
class NewTextBased(): #new text based article 
    def newfile_delete(self):
        self.new_file_heading.grid_remove()

        #type of article
        self.type_l.grid_remove()
        self.drop_type.grid_remove()
        
        #date of issue
        self.issue_l.grid_remove()
        self.drop_month.grid_remove()
        self.drop_year.grid_remove()

        #author of the article
        self.author_l.grid_remove()
        self.author_entry.grid_remove()

        #title of the article 
        self.title_l.grid_remove()
        self.title_entry.grid_remove()

        #subtitle of the article 
        self.sub_l.grid_remove()
        self.sub_entry.grid_remove()

        #get image file
        self.FeaturedButton.grid_remove()
        self.buffer1.grid_remove()
        self.buffer2.grid_remove()
        self.getimage_btn.grid_remove()

        #body paragraphs of the article 
        self.body_heading.grid_remove()
        self.body_entry.grid_remove()

    def back_btn(self):
        self.newfile_delete()
        main_menu = Main()

    def get_info(self): #return all info about article 
        #format date 
        date = str(self.month.get()) + " " + self.year.get()

        #get all relevant info 
        info = [self.type.get(), date, self.title_entry.get("1.0",END).replace('\n', ''), self.sub_entry.get("1.0",END).replace('\n', ''),
               self.author_entry.get("1.0",END).replace('\n', ''), self.body_entry.get("1.0",END), self.img_filename, self.photographer, self.isfeatured.get()]
        
        return info

    def next_btn(self): #create new file, upload it to github, update genre page and front page
        info = self.get_info() 

        create = generate.Text_Based(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])

        filename = create.get_filname()
        generate.upload(filename,create.get_file())

        updatejs = generate.UpdateJs()
        updatejs.newfile(self.title_entry.get("1.0",END).replace('\n', ''), (filename).replace('\n', ''))

        update_main = update.UpdateType()
        if "News" in self.type.get():
            update_main.news_op("news.html")
        elif "Opinion" in self.type.get():
            update_main.news_op("opinion.html")
        elif "Reviews" in self.type.get():
            update_main.critic()
        else:
            update_main.culture()

        if self.isfeatured.get() == 1:
            update_main.home()

        messagebox.showinfo("Information","New article file created")
        self.back_btn()

    def get_img(self):
        try:
            filename = filedialog.askopenfilename( #select file 
                filetypes=[
                ('image files', ('.png', '.jpg')),
            ]
            )

            with open(filename, "rb") as image:
                f = image.read()  
            
            #get photographer name and generate filename 
            self.photographer = askstring("Photography Credits", "Enter name of the photographer")
            self.img_filename =  str(datetime.datetime.now().strftime("%f")) + ".jpg"
            
            #add img to github            
            git_file = "images/" + self.img_filename #byte array -> what to upload
            update.repo.create_file(git_file, "committing image file", bytes(bytearray(f)), branch="main")
        except:
            pass

    def __init__(self, next, back):
        #init image data 
        self.img_filename = ""
        self.photographer = ""

        self.new_file_heading = Label(text = "\n            NEW ARTICLE", font=("Helvetica", 12, "bold"))
        self.new_file_heading.grid(column=0, row=0, columnspan = 5)

        #type of article 
        self.type_opt = ["News", "Opinion", "Book Reviews", "Movie Reviews", "Horoscopes", "Short Stories", "Other"]
        self.type = StringVar()
        self.type.set("News")

        self.type_l = Label(main, text = "   Type", font=("Helvetica", 10, "bold"))
        self.drop_type = OptionMenu(main, self.type , *self.type_opt)
        self.drop_type.config(bg="WHITE", width = 10)

        self.type_l .grid(column=0, row=1)
        self.drop_type.grid(column = 1, row =1)

        #issue date of the article 
        self.month_opt = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September","October","November","December"]
        self.month = StringVar()
        self.month.set("January")

        self.year_opt = []
        tmp_year = 2010
        for x in range(30):
            tmp_year += 1
            self.year_opt.append(tmp_year)
        self.year = StringVar()
        self.year.set(2000)
        
        self.issue_l = Label(main, text = "   Issue", font=("Helvetica", 10, "bold"))
        self.drop_month = OptionMenu(main, self.month , *self.month_opt)
        self.drop_month.config(bg="WHITE", width = 10)
        self.drop_year = OptionMenu(main, self.year , *self.year_opt)
        self.drop_year.config(bg="WHITE")

        self.issue_l .grid(column=2, row=1)
        self.drop_month.grid(column=3, row = 1)
        self.drop_year.grid(column=4, row = 1)

        #author of the article
        self.author_l = Label(main, text = "  Author", font=("Helvetica", 10, "bold"))
        self.author_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.author_l.grid(column=0, row=2)
        self.author_entry.grid(column=1, row=2, columnspan = 4)

        #title of the article 
        self.title_l = Label(main, text = "Title", font=("Helvetica", 10, "bold"))
        self.title_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.title_l.grid(column=0, row=3)
        self.title_entry.grid(column=1, row=3, columnspan = 4)

        #subtitle of the article 
        self.sub_l = Label(main, text = "Subtitle", font=("Helvetica", 10, "bold"))
        self.sub_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.sub_l.grid(column=0, row=4)
        self.sub_entry.grid(column=1, row=4, columnspan = 4)

        #get image file
        self.buffer1= Label(text = "", font=("Helvetica", 4, "normal"))
        self.buffer1.grid(column=0, row=5, columnspan = 4)

        self.getimage_btn = Button(main, text ="Image File", bg = "white", font=("Helvetica", 9, "normal"))
        self.getimage_btn.grid(column = 4, row = 6)

        #get featured articles
        self.isfeatured = IntVar() 
        self.FeaturedButton = Checkbutton(main, text = "Featured",variable = self.isfeatured, 
                onvalue = 1, offvalue = 0, font=("Helvetica", 10, "normal"))
        self.FeaturedButton.grid(column = 1, row = 6)

        #get body text 
        self.buffer2 = Label(text = "", font=("Helvetica", 4, "normal"))
        self.buffer2.grid(column=0, row=7, columnspan = 4)

        self.body_heading = Label(text = "Body", font=("Helvetica", 10, "bold"))
        self.body_heading.grid(column=0, row=6)

        self.body_entry = scrolledtext.ScrolledText(main,height = 8,width = 45, font = ("Helvetica", 10, "normal"))
        self.body_entry.grid(column=1, row=8, columnspan = 4)

        #pass next and back buttons 
        self.next = next
        self.back = back
        next.configure(command = self.next_btn, text = "Save")
        back.configure(command = self.back_btn, text = "Back")
        self.getimage_btn.configure(command = self.get_img)

class Comic():
    def comicfile_delete(self):
        self.new_file_heading.grid_remove()

        #type of article
        self.type_l.grid_remove()
        self.drop_type.grid_remove()
        
        #date of issue
        self.issue_l.grid_remove()
        self.drop_month.grid_remove()
        self.drop_year.grid_remove()

        #author of the article
        self.author_l.grid_remove()
        self.author_entry.grid_remove()

        #title of the article 
        self.title_l.grid_remove()
        self.title_entry.grid_remove()

        #subtitle of the article 
        self.sub_l.grid_remove()
        self.sub_entry.grid_remove()

        #get image file
        self.FeaturedButton.grid_remove()
        self.buffer1.grid_remove()
        self.getimage_btn.grid_remove()

    def back_btn(self):
        self.comicfile_delete()
        main_menu = Main()

    def get_info(self): #return all info about article 
        #format date 
        date = str(self.month.get()) + " " + self.year.get()
        #get all relevant info 
        info = [self.type.get(), date, self.title_entry.get("1.0",END).replace('\n', ''), self.sub_entry.get("1.0",END).replace('\n', ''),
               self.author_entry.get("1.0",END).replace('\n', ''), self.img_filename, self.isfeatured.get()]
        return info

    def next_btn(self): #create new file, upload it to github, update genre page and front page
        info = self.get_info() 

        if self.img_filename == "":
            messagebox.showinfo("Information","Error: no image uploaded")
        else:
                                    #genre,   date,   title, subtitle, author, img_filename, isfeatured
            create = generate.Comic(info[0], info[1], info[2], info[3], info[4], info[5], info[6])

            filename = create.get_filname()
            generate.upload(filename,create.get_file())

            updatejs = generate.UpdateJs()
            updatejs.newfile(self.title_entry.get("1.0",END).replace('\n', ''), (filename).replace('\n', ''))

            #update main pages 
            update_main = update.UpdateType()
            update_main.culture()

            if self.isfeatured.get() == 1:
                update_main.home()

            messagebox.showinfo("Information","New comic file created")
            self.back_btn()

    def get_img(self):
        try:
            filename = filedialog.askopenfilename( #select file 
                filetypes=[
                ('image files', ('.png', '.jpg')),
            ]
            )

            with open(filename, "rb") as image:
                f = image.read()  
            
            #get photographer name and generate filename 
            messagebox.showinfo("Information","Image file sucessfully uploaded")
            self.img_filename =  str(datetime.datetime.now().strftime("%f")) + ".jpg"
            
            #add img to github            
            git_file = "images/" + self.img_filename #byte array -> what to upload
            update.repo.create_file(git_file, "committing image file", bytes(bytearray(f)), branch="main")
        except:
            pass

    def __init__(self, next, back):
        #init image data 
        self.img_filename = ""

        self.new_file_heading = Label(text = "\n            NEW COMIC", font=("Helvetica", 12, "bold"))
        self.new_file_heading.grid(column=0, row=0, columnspan = 5)

        #type of article 
        self.type_opt = ["Comics & Cartoons"]
        self.type = StringVar()
        self.type.set("Comics & Cartoons")

        self.type_l = Label(main, text = "Type", font=("Helvetica", 10, "bold"))
        self.drop_type = OptionMenu(main, self.type , *self.type_opt)
        self.drop_type.config(bg="WHITE", width = 10)

        self.type_l .grid(column=0, row=1)
        self.drop_type.grid(column = 1, row =1)

        #issue date of the article 
        self.month_opt = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September","October","November","December"]
        self.month = StringVar()
        self.month.set("January")

        self.year_opt = []
        tmp_year = 2010
        for x in range(30):
            tmp_year += 1
            self.year_opt.append(tmp_year)
        self.year = StringVar()
        self.year.set(2000)
        
        self.issue_l = Label(main, text = "   Issue", font=("Helvetica", 10, "bold"))
        self.drop_month = OptionMenu(main, self.month , *self.month_opt)
        self.drop_month.config(bg="WHITE", width = 10)
        self.drop_year = OptionMenu(main, self.year , *self.year_opt)
        self.drop_year.config(bg="WHITE")

        self.issue_l .grid(column=2, row=1)
        self.drop_month.grid(column=3, row = 1)
        self.drop_year.grid(column=4, row = 1)

        #author of the article
        self.author_l = Label(main, text = "  Author", font=("Helvetica", 10, "bold"))
        self.author_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.author_l.grid(column=0, row=2)
        self.author_entry.grid(column=1, row=2, columnspan = 4)

        #title of the article 
        self.title_l = Label(main, text = "Title", font=("Helvetica", 10, "bold"))
        self.title_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.title_l.grid(column=0, row=3)
        self.title_entry.grid(column=1, row=3, columnspan = 4)

        #subtitle of the article 
        self.sub_l = Label(main, text = "Subtitle", font=("Helvetica", 10, "bold"))
        self.sub_entry = Text(main,height = 1,width = 45, font = ("Helvetica", 10, "normal"))
        self.sub_l.grid(column=0, row=4)
        self.sub_entry.grid(column=1, row=4, columnspan = 4)

        #get image file
        self.buffer1= Label(text = "", font=("Helvetica", 4, "normal"))
        self.buffer1.grid(column=0, row=5, columnspan = 4)

        self.getimage_btn = Button(main, text ="Image File", bg = "white", font=("Helvetica", 9, "normal"))
        self.getimage_btn.grid(column = 4, row = 6)

        #get featured articles
        self.isfeatured = IntVar() 
        self.FeaturedButton = Checkbutton(main, text = "Featured",variable = self.isfeatured, 
                onvalue = 1, offvalue = 0, font=("Helvetica", 10, "normal"))
        self.FeaturedButton.grid(column = 1, row = 6)

        #pass next and back buttons 
        self.next = next
        self.back = back
        next.configure(command = self.next_btn, text = "Create")
        back.configure(command = self.back_btn, text = "Back")
        self.getimage_btn.configure(command = self.get_img)

class Main():
    def main_delete(self):
            self.main_heading.forget()
            self.ViewButton.forget()
            self.CreateButton.forget()
            self.ComicButton.forget()

            if self.opt_main.get() == 1:
                view = View(self.next, self.back)
            elif self.opt_main.get() == 0:
                create = NewTextBased(self.next, self.back)
            elif self.opt_main.get() == 2:
                comic = Comic(self.next, self.back)

    def __init__(self):
        self.main_heading = Label(text = "\n\nWebsite Manager", 
                    font=("Helvetica", 15, "normal"))

        self.opt_main = IntVar() 
        self.CreateButton = Radiobutton(main, text = "Create new article", 
                    variable = self.opt_main,
                    value = 0,
                    height = 3,
                    width = 20, 
                    font=("Helvetica", 12, "normal"))
        self.ComicButton = Radiobutton(main, text = "Create new comic",
                    variable = self.opt_main,
                    value = 2, 
                    width = 20,
                    font=("Helvetica", 12, "normal"))
        self.ViewButton = Radiobutton(main, text = "View all files",
                    variable = self.opt_main,
                    value = 1, 
                    height = 3,
                    width = 20,
                    font=("Helvetica", 12, "normal"))
        self.opt_main.set(0)

        #next and back buttons
        self.next = Button(main, text ="Next", 
                command = self.main_delete, bg = "white", 
                padx = 20, font=("Helvetica", 10, "normal"))

        self.back = Button(main, text ="Back", bg = "white", 
                padx = 20, font=("Helvetica", 10, "normal"))

        #create widgets 
        self.main_heading.pack()
        self.CreateButton.pack()  
        self.ComicButton.pack()
        self.ViewButton.pack()
        self.next.pack()
        self.next.place(x = 300, y = 350)
        self.back.pack()
        self.back.place(x = 20, y = 350)

main_menu = Main()
mainloop()