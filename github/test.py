w = 1024
h = 1024
pontos = {}      
pontos['fundo_preto'] = [[int(w/2),int(h/2),0],[int(w/2)+300,int(h/2),0]] # adiciona o fundo preto 
pontos['cabeca'] =  [[[357, 636, 0], [428, 700, 0], [559, 698, 0], [631, 663, 0], [664, 627, 0],], [[312, 593, 0], [533, 597, 0], [438, 572, 0], [613, 587, 0], [702, 576, 0],], [[305, 515, 0], [450, 529, 0], [535, 496, 0], [622, 481, 0], [703, 508, 0],], [[337, 445, 0], [390, 377, 0], [541, 366, 0], [631, 394, 0], [676, 457, 0]]]
pontos['orelha_esquerda'] =  [[[334, 647, 0], [339, 679, 0], [328, 735, 0], [380, 691, 0], [416, 665, 0], [442, 655, 0],], [[334, 601, 0], [367, 644, 0], [369, 644, 0], [391, 662, 0], [414, 662, 0], [442, 669, 0],], [[352, 611, 0], [375, 615, 0], [398, 623, 0], [418, 638, 0], [431, 644, 0], [451, 644, 0]]]
pontos['orelha_direita'] = [[[589, 668, 0], [592, 701, 0], [709, 677, 0], [630, 760, 0], [691, 647, 0], [663, 618, 0],], [[564, 664, 0], [650, 618, 0], [618, 630, 0], [593, 647, 0], [573, 655, 0], [663, 621, 0]]]
pontos['braco'] = [[[430, 350, 0], [380, 319, 0], [346, 355, 0], [327, 389, 0], [306, 408, 0], [275, 403, 0],], [[425, 306, 0], [398, 309, 0], [350, 287, 0], [342, 324, 0], [306, 357, 0], [324, 351, 0]]]
pontos['pescoco'] = [[[373, 232, 0], [417, 223, 0], [426, 244, 0], [436, 234, 0], [404, 358, 0], [452, 401, 0],], [[474, 223, 0], [479, 263, 0], [481, 306, 0], [483, 341, 0], [485, 366, 0], [486, 392, 0],], [[547, 151, 0], [544, 278, 0], [543, 305, 0], [543, 335, 0], [545, 371, 0], [541, 392, 0],], [[611, 225, 0], [576, 233, 0], [574, 230, 0], [580, 225, 0], [596, 369, 0], [545, 395, 0]]]



def escala(mat):
    for linha in mat:
        for el in linha:
            el[0]-= 512
            el[1]-= 512
            el[2] =0
            el[0] /=512
            el[1]/=512
    return mat


# print("pontos['fundo_preto']",escala(pontos['fundo_preto']))
print("\t\tself.pontos['cabeca']=",escala(pontos['cabeca']))
print("\t\tself.pontos['orelha_esquerda']=",escala(pontos['orelha_esquerda']))
print("\t\tself.pontos['orelha_direita']=",escala(pontos['orelha_direita']))
print("\t\tself.pontos['braco']=",escala(pontos['braco']))
print("\t\tself.pontos['pescoco']=",escala(pontos['pescoco']))