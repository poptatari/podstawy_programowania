class Ebook:
    def __init__(self, title, author, num_of_pages,):
        self.title = title
        self.author = author
        self.no_of_pages = num_of_pages
        self.is_open = False
        self.current_page = 0

    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False

    def status(self):
        print(
            f'Tile: {self.title}\n'
            f'Author: {self.author}\n'
            f'Number of pages: {self.no_of_pages}\n'
            f'Current page: {self.current_page}/{self.no_of_pages}'
        )

    def go_forward(self):
        if self.is_open:
            if self.current_page < self.no_of_pages:
                self.current_page += 1
        else:
            print('The book is closed.')

    def go_backward(self):
        if self.is_open:
            if self.current_page > 0:
                self.current_page -= 1
        else:
            print('The book is closed.')
