#create_Board ,buttons
class Board_2players():
    def __init__(self, master, game, player, computer):

        self.currently_highlighted = []
        if computer == "black":
            self.current_turn = player

        else:
            self.current_turn = computer
        self.game = game
        self.player = player
        self.computer = computer
        self.window = master

        self.all_buttons = []
        self.open_images()
        self.build_board(master)

 
        def open_images(self):
                self.black_cell = Image.open("C:\Bina-Noam\images\cellb.png")
                self.black_cell.thumbnail((75, 75))
                self.black_cell = ImageTk.PhotoImage(self.black_cell)

                self.white_cell = Image.open("C:\Bina-Noam\images\cellw.png")
                self.white_cell.thumbnail((75, 75))
                self.white_cell = ImageTk.PhotoImage(self.white_cell)

                self.black_queen = Image.open("C:\Bina-Noam\images\iq1")
                self.black_queen.thumbnail((75, 75))
                self.black_queen = ImageTk.PhotoImage(self.black_queen)

                self.white_queen = Image.open("C:\Bina-Noam\images\iq2")
                self.white_queen.thumbnail((75, 75))
                self.white_queen = ImageTk.PhotoImage(self.white_queen)

                self.black_piece = Image.open("C:\Bina-Noam\images\i1.png")
                self.black_piece.thumbnail((75, 75))
                self.black_piece = ImageTk.PhotoImage(self.black_piece)

                self.white_piece = Image.open("C:\Bina-Noam\images\i2.png")
                self.white_piece.thumbnail((75, 75))
                self.white_piece = ImageTk.PhotoImage(self.white_piece)

                self.highlighted_cell = Image.open("C:\Bina-Noam\images\cellb.png")
                self.highlighted_cell.thumbnail((75, 75))
                self.highlighted_cell = ImageTk.PhotoImage(self.highlighted_cell)

                self.highlighted_wqueen = Image.open("C:\Bina-Noam\images\iq2")
                self.highlighted_wqueen.thumbnail((75, 75))
                self.highlighted_wqueen = ImageTk.PhotoImage(self.highlighted_wqueen)

                self.highlighted_wpiece = Image.open("C:\Bina-Noam\images\iq2")
                self.highlighted_wpiece.thumbnail((75, 75))
                self.highlighted_wpiece = ImageTk.PhotoImage(self.highlighted_wpiece)

                self.highlighted_bqueen = Image.open("C:\Bina-Noam\images\iq1")
                self.highlighted_bqueen.thumbnail((75, 75))
                self.highlighted_bqueen = ImageTk.PhotoImage(self.highlighted_bqueen)

                self.highlighted_bpiece = Image.open("C:\Bina-Noam\images\i1.png")
                self.highlighted_bpiece.thumbnail((75, 75))
                self.highlighted_bpiece = ImageTk.PhotoImage(self.highlighted_bpiece)
