class Formulas:
    def __init__(self,w) -> None:
        self.list_w = w

# la formula usada para la sumatoria total neta es: [x0*w0+x1*w11+x2*w12]
    def sum_net(self,list_index_logical):
        z_toria = 0
        index = 0
        while index < len(list_index_logical)-1:
           # print(self.list_w)
            #print(list_index_logical)
            z_toria += list_index_logical[index+1] * self.list_w[index]
            index += 1
        return z_toria
        
        
