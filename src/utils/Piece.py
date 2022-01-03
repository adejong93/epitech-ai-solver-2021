class Piece:
    def __init__(self,
                 id         : int,
                 position   : tuple[int, int]) -> None:
        self.id         : int               = id
        self.position   : tuple[int, int]   = position