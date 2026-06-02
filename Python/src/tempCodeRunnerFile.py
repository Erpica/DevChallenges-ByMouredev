    def book_circulation(self, title, action):
        if action == "Borrow":
            have_any = False
            for book in self.books:
                if (book["title"] == title and book["copys"] >= 1):
                    book["copys"] - 1
                    have_any = True
                    print(f"Se asigna el libro {book["title"]}")
                    break
                else:
                    print(f"En este momento no disponemos de ninguna copia de {book["title"]}")
            if have_any = False:
                print(f"No disponemos de ningun título llamado {title}")