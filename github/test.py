from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from transformacao import *

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt


class github:


    def __init__(self):
        self.pontos = {}
        self.w = 800
        self.h = 800
        self.sides = 50
        self.keybindings = {chr(27): exit}
        glutInit()
        glutInitWindowSize(self.w, self.h)
        self.git = glutCreateWindow('Github')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glClearColor(0, 0, 0, 0)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMouseFunc(self.mouse)
        glOrtho(0.0, self.w, 0.0, self.h, 0.0, 1.0)
        self.ctrlPoints = [[100,100,0],[130,200,0],[170,200,0],[200,100,0]]
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.ctrlPoints)
        glEnable(GL_MAP1_VERTEX_3)
        self.indice=0
        self.linha=0
        self.rotacao = False
        self.teste ,self.print= False,False
        self.operacao = 'orelha_direita'
        self.alpha = 0
        self.transf = Transformacao(self.w,self.h)



    def reshape(self,rsp1,rsp2):
        pass

    def substitui(self,tp2,x,y):

        if tp2==0:
            self.indice = 0
            menor = 102500000000000000
            for ponto in self.pontos['g']:
                i = 0
                # for ponto in pontos:
                px = ponto[0]
                py = ponto[1]
                euclidiana = sqrt((x-px)**2+(y-py)**2)
                if euclidiana < menor:
                    self.indice = i
                    menor = euclidiana
                i+=1
        else:
            print(self.pontos['g'][self.indice])
            print([x,y,0])
            print(self.indice)
            self.pontos['g'][self.indice] = [x,y,0]
            print(self.pontos['g'][self.indice])
            

    def mouse(self,tp1,tp2,x,y):
        y = 1024 - y
        if tp2==0:
            print('pressionou [',x,',',y,',',0,'],',sep='')
        elif tp2==1:
            print('soltou [',x,',',y,',',0,'],',sep='')
        self.substitui(tp2,x,y)
        
    def circle(self,circulo):
        x = circulo[0][0]*2
        y = circulo[0][1]*2
        x1 = circulo[1][0]*2
        y1 = circulo[1][1]*2
        raio = sqrt(((x-x1)**2)+((y-y1)**2) )
        glColor3f(255, 255, 255)
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = raio * cos(i*2*pi/self.sides) + x
            sine = raio * sin(i*2*pi/self.sides) + y
            glVertex2f(cosine, sine)
        glEnd()
        glPointSize(1)
        glBegin(GL_POINTS)
        glColor3f(255, 0,0)
        glColor(255,255,0)
        glVertex3fv(circulo[0])
        glVertex3fv(circulo[1])
        glEnd()

    def bezier(self,pontos,tipo=''):
        glClearColor(0.0,0.0,0.0,0.0)
        glColor3f(255, 255, 255)
        glMap2d(GL_MAP2_VERTEX_3,0, 1, 10, 0,pontos)
        glEnable(GL_MAP2_VERTEX_3)
        glEnable(GL_AUTO_NORMAL)
        glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
        glShadeModel(GL_FLAT)
        glPushMatrix()
        # glRotatef(85.0,1.0,1.0,1.0)
        glEvalMesh2(GL_FILL,0,20,0,20)
        glPopMatrix()
        if self.print:
            glPointSize(5)
            glBegin(GL_POINTS)
            glColor3f(255, 0,0)
            i = 0
            for lista in pontos:
                if i==1:
                    glColor(0,255,0)
                elif i ==2:
                    glColor(0,0,255)
                elif i ==3:
                    glColor(255,255,0)
                for ponto in lista:
                    glVertex3fv(ponto)
                i+=1
                
            glEnd()
    def t (self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(self.pontos['t'][0][0]*2,self.pontos['t'][0][1]*2)  # Coordinates for the bottom left point
        glVertex2f(self.pontos['t'][1][0]*2,self.pontos['t'][1][1]*2)  # Coordinates for the bottom right point
        glVertex2f(self.pontos['t'][2][0]*2,self.pontos['t'][2][1]*2)  # Coordinates for the top right point
        glVertex2f(self.pontos['t'][3][0]*2,self.pontos['t'][3][1]*2)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing


    def i (self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(self.pontos['i'][0][0]*2,self.pontos['i'][0][1]*2)  # Coordinates for the bottom left point
        glVertex2f(self.pontos['i'][1][0]*2,self.pontos['i'][1][1]*2)  # Coordinates for the bottom right point
        glVertex2f(self.pontos['i'][2][0]*2,self.pontos['i'][2][1]*2)  # Coordinates for the top right point
        glVertex2f(self.pontos['i'][3][0]*2,self.pontos['i'][3][1]*2)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing

    def g(self,vet):
        
        glColor3f(255, 255,255)
        i = 0
        glBegin(GL_POLYGON)
        p1,p2,p3 =vet[0],vet[1],vet[2]
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)
        # 123,234,345
        glEnd()
        for i in range(3,len(vet)):
            p4 = vet[i]
            glBegin(GL_POLYGON)
            glVertex3fv(p2)
            glVertex3fv(p3)
            glVertex3fv(p4)
            p0 =vet[i]
            glEnd()
            pn = p2
            pn1 = p3
            pn2 = p4
            p2 = p3
            p3 = p4
        
    def fundo_branco(self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(-self.w, self.h)  # Coordinates for the bottom left point
        glVertex2f(self.w, self.h)  # Coordinates for the bottom right point
        glVertex2f(self.w, -self.h)  # Coordinates for the top right point
        glVertex2f(-self.w,-self.h)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
    


    def display(self):
        self.indice+=1
        x = float(input('x: '))
        y = float(input('y: '))
        self.pontos['b'].append([x*2,y*2,0])
        self.g(self.pontos['b'])
        print(self.pontos['b'])
        glFlush()
        # input()


    def inicializa(self):
        self.pontos['fundo_preto'] = [[0,0,0],[0.590,0,0]] # adiciona o fundo preto
        self.pontos['cabeca']= [[[-0.302734375, 0.2421875, 0], [-0.1640625, 0.3671875, 0], [0.091796875, 0.36328125, 0], [0.232421875, 0.294921875, 0], [0.296875, 0.224609375, 0]], [[-0.390625, 0.158203125, 0], [0.041015625, 0.166015625, 0], [-0.14453125, 0.1171875, 0], [0.197265625, 0.146484375, 0], [0.37109375, 0.125, 0]], [[-0.404296875, 0.005859375, 0], [-0.12109375, 0.033203125, 0], [0.044921875, -0.03125, 0], [0.21484375, -0.060546875, 0], [0.373046875, -0.0078125, 0]], [[-0.341796875, -0.130859375, 0], [-0.23828125, -0.263671875, 0], [0.056640625, -0.28515625, 0], [0.232421875, -0.23046875, 0], [0.3203125, -0.107421875, 0]]]
        self.pontos['orelha_esquerda']= [[[-0.34765625, 0.263671875, 0], [-0.337890625, 0.326171875, 0], [-0.359375, 0.435546875, 0], [-0.2578125, 0.349609375, 0], [-0.1875, 0.298828125, 0], [-0.13671875, 0.279296875, 0]], [[-0.34765625, 0.173828125, 0], [-0.283203125, 0.2578125, 0], [-0.279296875, 0.2578125, 0], [-0.236328125, 0.29296875, 0], [-0.19140625, 0.29296875, 0], [-0.13671875, 0.306640625, 0]], [[-0.3125, 0.193359375, 0], [-0.267578125, 0.201171875, 0], [-0.22265625, 0.216796875, 0], [-0.18359375, 0.24609375, 0], [-0.158203125, 0.2578125, 0], [-0.119140625, 0.2578125, 0]]]
        self.pontos['orelha_direita']= [[[0.150390625, 0.3046875, 0], [0.15625, 0.369140625, 0], [0.384765625, 0.322265625, 0], [0.23046875, 0.484375, 0], [0.349609375, 0.263671875, 0], [0.294921875, 0.20703125, 0]], [[0.1015625, 0.296875, 0], [0.26953125, 0.20703125, 0], [0.20703125, 0.23046875, 0], [0.158203125, 0.263671875, 0], [0.119140625, 0.279296875, 0], [0.294921875, 0.212890625, 0]]]
        self.pontos['braco']= [[[-0.16015625, -0.31640625, 0], [-0.2578125, -0.376953125, 0], [-0.32421875, -0.306640625, 0], [-0.361328125, -0.240234375, 0], [-0.40234375, -0.203125, 0], [-0.462890625, -0.212890625, 0]], [[-0.169921875, -0.40234375, 0], [-0.22265625, -0.396484375, 0], [-0.31640625, -0.439453125, 0], [-0.33203125, -0.3671875, 0], [-0.40234375, -0.302734375, 0], [-0.3671875, -0.314453125, 0]]]
        self.pontos['pescoco']= [[[-0.271484375, -0.546875, 0], [-0.185546875, -0.564453125, 0], [-0.16796875, -0.5234375, 0], [-0.1484375, -0.54296875, 0], [-0.2109375, -0.30078125, 0], [-0.1171875, -0.216796875, 0]], [[-0.07421875, -0.564453125, 0], [-0.064453125, -0.486328125, 0], [-0.060546875, -0.40234375, 0], [-0.056640625, -0.333984375, 0], [-0.052734375, -0.28515625, 0], [-0.05078125, -0.234375, 0]], [[0.068359375, -0.705078125, 0], [0.0625, -0.45703125, 0], [0.060546875, -0.404296875, 0], [0.060546875, -0.345703125, 0], [0.064453125, -0.275390625, 0], [0.056640625, -0.234375, 0]], [[0.193359375, -0.560546875, 0], [0.125, -0.544921875, 0], [0.12109375, -0.55078125, 0], [0.1328125, -0.560546875, 0], [0.1640625, -0.279296875, 0], [0.064453125, -0.228515625, 0]]]
        self.pontos['pingo_i'] = [[181.83,266.52,0],[188.87,267.03,0]]
        self.pontos['g'] =[[330.02, 541.16, 0], [324.9, 521.16, 0], [319.96, 543.0, 0], [313.0, 521.9, 0], [313.0, 544.34, 0], [301.02, 522.32, 0], [306.62, 545.64, 0], [301.02, 522.32, 0], [301.7, 546.22, 0], [301.02, 522.32, 0], [297.02, 546.36, 0], [293.66, 522.36, 0], [291.52, 546.14, 0], [288.14, 521.74, 0], [285.24, 545.1, 0], [283.64, 520.22, 0], [279.7, 544.0, 0], [282.76, 519.9, 0], [273.02, 542.06, 0], [278.58, 517.92, 0], [265.88, 538.58, 0], [273.42, 513.88, 0], [259.36, 532.56, 0], [270.98, 510.72, 0], [252.3, 527.92, 0], [268.94, 507.56, 0], [248.16, 523.48, 0], [267.04, 504.24, 0], [244.44, 518.78, 0], [265.92, 501.22, 0], [241.28, 513.06, 0], [265.0, 499.44, 0], [239.34, 508.74, 0], [263.84, 496.08, 0], [237.7, 503.28, 0], [263.06, 493.32, 0], [236.64, 498.02, 0], [262.24, 487.34, 0], [235.86, 486.18, 0], [261.44, 478.82, 0], [235.92, 469.84, 0], [261.94, 468.56, 0], [235.96, 459.9, 0], [263.58, 460.46, 0], [237.6, 451.88, 0], [265.72, 453.12, 0], [239.22, 446.22, 0], [266.16, 448.66, 0], [241.44, 441.34, 0], [267.56, 448.8, 0], [244.48, 435.2, 0], [267.96, 448.04, 0], [247.88, 430.26, 0], [269.24, 446.08, 0], [250.84, 426.12, 0], [270.66, 444.46, 0], [254.44, 423.16, 0], [273.24, 441.48, 0], [259.24, 418.76, 0], [276.36, 438.3, 0], [265.12, 415.44, 0], [276.48, 438.04, 0], [270.94, 412.86, 0], [279.94, 436.2, 0], [276.9, 410.78, 0], [284.8, 434.32, 0], [283.52, 409.56, 0], [291.04, 432.96, 0], [289.88, 409.02, 0], [296.04, 432.14, 0], [298.48, 409.36, 0], [301.32, 432.28, 0], [304.56, 409.82, 0], [307.74, 432.96, 0], [310.72, 411.1, 0], [311.66, 434.66, 0], [316.8, 412.8, 0], [313.36, 437.02, 0], [322.08, 414.08, 0], [313.36, 437.02, 0], [327.08, 416.18, 0], [313.36, 437.02, 0], [331.82, 418.88, 0], [313.36, 437.02, 0], [334.26, 421.74, 0], [313.36, 437.02, 0], [334.86, 426.94, 0], [314.16, 440.6, 0], [335.74, 439.6, 0], [314.58, 448.38, 0], [335.88, 458.66, 0], [313.7, 458.8, 0], [335.74, 479.64, 0], [314.1, 459.28, 0], [313.82, 480.18, 0], [306.38, 462.18, 0], [294.42, 480.04, 0], [292.46, 464.14, 0], [284.88, 480.38, 0], [285.82, 464.82, 0]]
        self.pontos['i'] = [[175.81,253.25,0],[187.75,253.15,0],[187.54,205.81,0],[175.81,205.81,0]]
        self.pontos['t'] = [[201.94,262.08,0],[212.83,264.78,0],[214.5,204.83,0],[201.96,204.83,0]]
        self.pontos['t2'] = [194.21,253.24,0],[223.49,253.34,0],[223.97,242.53,0],[194.21,242.53]
        self.pontos['t3'] = [[213.83,215.45,0],[224.68,215.05,0],[224.86,204.35,0],[214.78,204.44,0]]
        self.pontos['h']=[[[230.69,271.97,0],[230.52,205.33,0],[243.69,205.33,0],[243.69,271.97,0]],[[243.69,245.45,0],[243.69,233.35,0],[269.23,233.35,0],[269.23,245.45,0]],[[269.23,271.97,0],[269.23,205.33,0],[280.99,205.33,0],[280.99,271.97,0]]]
        self.pontos['u']= [[605.54, 506.82, 0], [580.72, 506.9, 0], [605.38, 470.66, 0], [581.5, 470.22, 0], [606.16, 447.42, 0], [582.66, 436.1, 0], [606.6, 437.26, 0], [583.98, 427.36, 0], [607.58, 434.96, 0], [586.28, 420.9, 0], [608.38, 433.36, 0], [588.4, 417.28, 0], [610.76, 431.78, 0], [591.22, 413.92, 0], [611.12, 431.06, 0], [595.3, 411.88, 0], [609.08, 432.66, 0], [599.98, 409.86, 0], [611.3, 431.34, 0], [606.08, 408.7, 0], [615.3, 430.0, 0], [613.24, 408.62, 0], [620.22, 429.4, 0], [620.76, 410.04, 0], [625.44, 430.72, 0], [627.56, 413.22, 0], [629.76, 432.74, 0], [634.0, 416.66, 0], [633.84, 436.64, 0], [639.4, 421.96, 0], [635.34, 440.08, 0], [637.64, 454.84, 0], [643.56, 423.38, 0], [637.46, 506.9, 0], [661.06, 506.38, 0], [662.02, 428.94, 0], [643.64, 423.3, 0], [646.04, 420.72, 0], [662.3, 428.94, 0], [648.5, 412.96, 0], [663.8, 418.88, 0], [665.04, 410.38, 0], [650.98, 411.54, 0], [660.52, 506.64, 0], [637.1, 507.44, 0], [648.16, 413.48, 0], [663.18, 428.42, 0], [634.8, 421.44, 0], [637.46, 454.32, 0]]
        self.pontos['b'] = [[681.76, 543.76, 0], [681.76, 416.76, 0], [707.76, 433.26, 0], [681.76, 543.76, 0], [707.76, 543.76, 0], [681.76, 416.76, 0], [709.32, 432.22, 0], [688.9, 412.86, 0], [711.52, 430.46, 0], [697.3, 411.18, 0], [715.86, 430.0, 0], [714.0, 409.6, 0], [723.82, 429.74, 0], [724.34, 409.5, 0], [730.52, 431.06, 0], [731.68, 410.22, 0], [735.92, 434.6, 0], [742.02, 412.6, 0], [738.04, 437.44, 0], [746.18, 414.54, 0], [739.28, 440.62, 0], [750.68, 419.98, 0], [733.88, 433.82, 0], [761.56, 430.8, 0], [738.92, 440.36, 0], [765.44, 440.52, 0], [742.1, 447.96, 0], [765.98, 446.98, 0], [742.72, 453.78, 0], [766.42, 459.8, 0], [743.52, 461.3, 0], [765.88, 469.7, 0], [742.82, 469.08, 0], [764.82, 484.46, 0], [739.82, 478.26, 0], [760.84, 493.64, 0], [735.74, 484.28, 0], [755.54, 500.98, 0], [729.64, 487.82, 0], [745.08, 506.34, 0], [723.56, 487.28, 0], [736.56, 508.8, 0], [724.44, 487.72, 0], [726.6, 508.8, 0], [717.08, 485.98, 0], [713.6, 503.3, 0], [709.86, 478.2, 0], [706.54, 499.7, 0], [683.58, 475.44, 0]]



if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()



