import customtkinter as ctk
from widgets import SearchBar, MoviesContainer, PageSlider
import json



ctk.set_default_color_theme('green')
class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.config_file = 'config.json'
        self.load_configs()
        self.screen_dimensions = [
            self.winfo_screenwidth(),
            self.winfo_screenheight()
        ]

        self.window_dimensions= self.get_geometry()
        self.title("Cinepédia v0.1")
        self.geometry(f"{self.window_dimensions[0]}x{self.window_dimensions[1]}")
        self.resizable(width=False,height=False)
        self.build()
    

    def build(self):
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.fonts = {
            "h1":ctk.CTkFont('Ubuntu',30),
            "h2":ctk.CTkFont('Ubuntu',20),
            "p":ctk.CTkFont('Ubuntu',15)
        }

        #? cinepedia label
        ctk.CTkLabel(self, text="Cinepédia Home", font=self.fonts['h1']).grid(row=0, column=0, sticky='nw', pady=(20,10), padx=20)
        
        #? searchbar
        self.searchbar = SearchBar(master=self, command=None)
        self.searchbar.grid(row=1, column=0, sticky='nwe', padx=20, pady=10)

        #? movies container
        self.moviescontainer = MoviesContainer(master=self, apikey=self.configs['api']['apikey'])
        self.moviescontainer.grid(row=2, column=0, sticky='nswe', padx=20, pady=(10,20))

        #? update searchbar
        self.searchbar.command = self.moviescontainer.load_movies


    def get_geometry(self):
        geometry_width = round((
            self.configs['sizes']['window_width_percent']
            *self.screen_dimensions[0]
            )/100)
        geometry_height = round(geometry_width/self.configs['sizes']['window_ratio'])

        return [
            geometry_width,
            geometry_height
        ]


    def load_configs(self):
        with open(self.config_file,'rb+') as config_file:
            self.configs = json.load(config_file)
            config_file.close()
        return True



app = MainWindow()
app.mainloop()