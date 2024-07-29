import customtkinter as ctk
from omdbapi.movie_search import GetMovie, GetMovieException
from tkinter.messagebox import showerror
from PIL import Image
import requests



class PageSlider(ctk.CTkSlider):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self._from_ = 1
        self._to = 5
        self._number_of_steps = self._to-1
        self.set(1)


class MoviesContainer(ctk.CTkScrollableFrame):
    def __init__(self, master, apikey, **kwargs):
        super().__init__(master=master, **kwargs)
        self.master = master
        self.apikey = apikey
    
    def show_movie(self):
        for child in self.winfo_children():
            child.destroy()

        poster_image = Image.open('temp/poster.jpg')
        widget_width = self.winfo_width()

        normal_img_width = poster_image.width
        normal_img_height = poster_image.height
        ratio = normal_img_width/normal_img_height

        new_img_width = (90*widget_width)/100
        new_img_height = new_img_width/ratio

        self.columnconfigure(0, weight=1)

        poster_ctk_image = ctk.CTkImage(light_image=poster_image, dark_image=poster_image, size=(new_img_width,new_img_height))
        poster_label = ctk.CTkLabel(self, image=poster_ctk_image, text="")
        poster_label.grid(row=0,column=0, pady=10)

        ctk.CTkLabel(self, text=self.movie.title, font=self.master.fonts['h1'], wraplength=450).grid(row=1,column=0,pady=10)
        ctk.CTkLabel(self, text=f"{(self.movie.type).upper()} - {(self.movie.genre).upper()}", font=self.master.fonts['h2'], wraplength=450).grid(row=2,column=0,pady=10)
        ctk.CTkLabel(self, text=self.movie.plot, font=self.master.fonts['p'],wraplength=450).grid(row=3,column=0,pady=10)

        try:
            current_row = 4
            suits_texts = [
                ["Relesead",self.movie.released],["Director",self.movie.director],
                ["Writer",self.movie.writer], ["Actors",self.movie.actors],
                ["Language",self.movie.language], ["Country",self.movie.country],
                ["BoxOffice",self.movie.boxoffice]
            ]

            for [title,value] in suits_texts:
                ctk.CTkLabel(self, text=title, font=self.master.fonts['h1'], wraplength=450).grid(row=current_row,column=0,pady=10)
                ctk.CTkLabel(self, text=value, font=self.master.fonts['p'],wraplength=450).grid(row=current_row+1,column=0,pady=10)
                current_row += 2
        except:
            pass


    def load_movies(self, target_movie):
        try:
            self.movie = GetMovie(api_key=self.apikey)
            self.movie.get_movie(target_movie, plot='full')
            poster = requests.get(self.movie.poster)
            poster_file = open('temp/poster.jpg','wb')
            poster_file.write(poster.content)
            poster_file.close()
            self.show_movie()

        except Exception as err:
            showerror(title="Oups!",message=f"Movie `{target_movie}` not found!")


class SearchBar(ctk.CTkFrame):
    def __init__(self, master, command, **kwargs):
        super().__init__(master=master, **kwargs)
        self.command = command
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0, weight=1)
        
        def cta_pressed():
            if self.command is not None:
                self.command(
                    self.searchbar_main_field.get()
                )
                self.searchbar_main_field.delete(0, 'end')


        self.searchbar_main_field = ctk.CTkEntry(self, placeholder_text='write any word', font=master.fonts['h2'])
        self.searchbar_cta_button = ctk.CTkButton(self, text="Lauchn Search", font=master.fonts['h2'], command=cta_pressed)
        
        self.searchbar_main_field.grid(row=0, column=0, sticky='we', pady=(10,5), padx=10, ipadx=5, ipady=5)
        self.searchbar_cta_button.grid(row=1, column=0, sticky='we', pady=(5,10), padx=10, ipadx=5, ipady=5)