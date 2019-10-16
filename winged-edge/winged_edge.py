import sys
try:
    objeto = sys.argv[1]
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()

vertex_dict = {}
face_dict = {}
edge_dict = {}

vertex_file = open('./malhas/{}/vertex.csv'.format(objeto))
face_file = open('./malhas/{}/face.csv'.format(objeto))
edge_file = open('./malhas/{}/edge.csv'.format(objeto))


def read_vertex():
    cont = 0
    for linha in vertex_file:
        linha = linha.strip('\n')
        el = linha.split(',')
        posicao = list(map(int,el[0:3]))
        del(el[0:3])
        vertex_dict['v'+str(cont)] = [posicao, el]
        cont += 1
    # print(vertex_dict)
    vertex_file.close()

def read_edge():
    cont = 0
    for linha in edge_file:
        linha = linha.strip('\n')
        el = linha.split(',')
        vertex = el[0:2]
        faces = el[2:4]
        del(el[0:4])
        edge_dict['e'+str(cont)] = [vertex, faces, el]
        cont += 1
    # print(edge_dict)
    edge_file.close()


def read_face():
    cont=0
    for linha in face_file:
        linha = linha.strip('\n')
        face = linha.split(',')
        face_dict['f'+str(cont)] = face
        cont += 1
    # print(face_dict)
    face_file.close()


def get_index_list():
    index_list = []
    for edge_a,edge_b,edge_c in list(face_dict.values()):
        vertex_list=[]
        for vertex in [edge_dict[edge_a][0],edge_dict[edge_b][0],edge_dict[edge_c][0]]:
            for v in vertex:
                if not (int(v.strip('v')) in vertex_list):
                    vertex_list.append(int(v.strip('v')))
        index_list.append(vertex_list)
    return index_list

def main():
    read_vertex()
    read_edge()
    read_face()
    vertex_list =  [x[0] for x in list(vertex_dict.values())]
    index_list = get_index_list()
    print(index_list)
    print(vertex_list)

if __name__=="__main__":
    main()
