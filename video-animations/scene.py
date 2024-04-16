# From examples/basic_example.py
from manim import *
from manim_chess.chess_board import ChessBoard
import manimpango

class name(Scene):
    def construct(self):
        name = Text("Astral Café",font="Indie Flower",font_size=82)
        self.play(Write(name))
        self.wait()

class title(Scene):
    def construct(self):
        name = Text("Astral Café",font="Indie Flower",font_size=48)
        name.set_z_index(10)

        func = lambda pos: np.sin(pos[0]) * DR + np.cos(pos[1]) * LEFT * 3 + pos / 9

        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.25], y_range=[-2, 2, 0.25], padding=1,
            colors=[ManimColor("#3c1b96"),ManimColor("#cf619f")]
        )

        inside_rect = Rectangle(width=6, height=4)
        inside_rect.set_fill(BLACK, 0.4)
        inside_rect.set_z_index(5)

        outside_rect = Rectangle(width=8, height=6)

        self.add(inside_rect, outside_rect)
        self.play(Create(stream_lines))  # Add this line to animate the creation of stream_lines
        self.play(Write(name))
        self.wait()

class ChessToBitboard(Scene):
    def construct(self):
        board = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",1)
        board.move_to(ORIGIN)
        self.add(board)

        #fade_out, movement = board.move_piece(7, 6, 5, 5)
        #if fade_out is not None:
        #    self.play(fade_out)
        #    self.wait()
        #self.play(movement)
        #self.wait()

        self.wait(5)

        numberplane = NumberPlane(x_range=(1,9,1), y_range=(1,9,1),
                                  background_line_style={
                                    "stroke_color": DARK_BLUE,
                                    "stroke_width": 4,
                                    "stroke_opacity": 1
                                })
        self.play(Create(numberplane))
        self.wait(2)

        self.play(FadeOut(board))
        
        bitboards = []

        for piece in ["K","Q","R","B","N","P","k","q","r","b","n","p"]:
            piece_bitboard = board.get_chess_pieces(piece)
            for i in range(7,-1,-1):
                for j in range(8):
                    bit_to_add = Text(str(piece_bitboard[i][j])).move_to(RIGHT * j + LEFT * 3.5 + UP * (7 - i) + DOWN * 3.5)
                    if piece == "K":
                        self.add(bit_to_add)
                        self.wait(0.03)
            bitboards.append(piece_bitboard)

        self.wait(3)

        bitboard = VGroup(*self.mobjects)
        bitboard.copy()
