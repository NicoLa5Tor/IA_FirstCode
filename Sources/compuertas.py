class Compuertas:
    def __init__(self,n) -> None:
        self.option = n

    def comp(self):
        com = []
        if self.option == 1:
            com = [[0,0,0],[0,1,1],[1,0,1],[1,1,1]]
        elif self.option == 2:
            com = [[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
        elif self.option == 3:
            com = [[0,0,1],[0,1,1],[1,0,1],[1,1,0]]
        elif self.option == 4:
            com = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
        return com



        
