from tkinter import*
import time
import random


def inicio():
    bienvenida=Label(tk,text=("Kharen´s   PinBall"),font=("Algerian",20)).place(x=70,y=50)#Label Texto Bienvenida
    registro=Button(tk,text=("Registrate"), font=("Arial",15),width=30,command=nombre).place(x=40,y=150)
    salir=Button(tk,text=("Salir"),font=("Arial",15),width=30,command=tk.destroy).place(x=40,y=200)
def nombre():
    global nombre#Variable Global Llamada En Otra Funcion
    nombre=StringVar()#Campo De Entrada String
    global edad#Variable Global Llamada En Otra Funcion
    edad=StringVar()#Campo De Entrada String
    labelnombre=Label(tk,text=("Nombre: "),font=("Algerian")).place(x=50,y=280)
    usuarionombre=Entry(tk,text=nombre).place(x=200,y=280)#Entrada De Texto
    labeledad=Label(tk,text="Edad: ",font=("Algerian")).place(x=50,y=310)
    edadusuario=Entry(tk,text=edad).place(x=200,y=310)#Entrada De Edad
    comenzar=Button(tk,text=("Empezar Partida"), font=("Arial",15),command=juego,width=15).place(x=200,y=350)
   
def juego():
    global puntaje
    ventana=Toplevel()#Nueva Ventana
    ventana.title("PINBALL")
    pantalla2 = Canvas(ventana, width=400,height=400)#Dimensiones Canvas Nueva Ventana
    pantalla2.pack()#Inserta El Canvas 
    ventana.update()#Actualiza 1 Milipixel x Segundo La Nueva Ventana
    #Labels Info Del Jugador
    player=Label(ventana,text="Jugador: ",font=("Arial",10)).place(x=0,y=0)#Label Player
    nombretomado=Label(ventana,text=nombre.get(),font=("Arial",10)).place(x=50,y=0)#Label Nombre Jugador
    labelpuntaje=Label(ventana,text="Puntaje: ",font=("Arial",10)).place(x=100,y=0)#Label Puntaje
    #puntajetomado=Label(ventana,text=puntaje,font=("Arial",10)).place(x=200,y=0)#Label Puntaje Jugador


   
    main(pantalla2,ventana)#Llamada Al Loop(ciclo) Principal


    #Obstaculos

        
        
    
class Bola: #Esta clase contiene la descripcion de nuestra bola,
                #la posicion, la funcion mover, coordenas de ventana,
                #dimensiones de la bola y de la ventana, condiciones
                #de rebote.

    
    def __init__(self,canvas,palanca1):
        self.canvas=canvas
        self.palanca1=palanca1
      
        self.id=canvas.create_oval(10, 10, 30, 30, fill="red")
        self.canvas.move(self.id,245,245)
        self.canvas_altura=self.canvas.winfo_height()
        self.canvas_ancho=self.canvas.winfo_width()
        d=[-3,-2,-1,1,2,3]
        random.shuffle(d)
           
        self.x=d[0]
        self.y=1
        self.perder=False
    def colision_palanca1(self,p):#Funcion De Colision Con Palanca1
        palanca1_p=self.canvas.coords(self.palanca1.id)#Devuelve Una Lista Con Coordenadas
        #Del Objeto Asi: [x1, y1, x2, y2]
        if p[2]>=palanca1_p[0] and p[0]<=palanca1_p[2]:
            if p[3]>=palanca1_p[1] and p[3]<=palanca1_p[3]:
                return True
        return False
  
        
    def mover(self):
        d=[-3,-2,-1,1,2,3]
        random.shuffle(d)
        self.canvas.move(self.id, self.x, self.y)
        p=self.canvas.coords(self.id)
        if p[1]<=0:
            self.y=1
        if p[3]>=self.canvas_altura:
            self.perder=True#Golpea El Fondo
            ventanaperdida=Toplevel()
            pantalla3=Canvas(ventanaperdida, width=400,height=400)
            perdiste=Label( ventanaperdida, text="PERDISTE", font = ("Algerian")).place(x=50,y=280)
        if self.colision_palanca1(p)==True:#Al Colisionar Con Palanca1 Devuelve True
            self.y*=-1
        if p[0]<=0:
            self.x=d[0]
        if p[2]>=self.canvas_ancho:
            self.x=d[0]

class Palanca1():
    def __init__(self,canvas):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,50,5,fill="black")
        self.canvas.move(self.id,160,350)
        self.x=0
        self.y=0
        self.canvas_ancho=self.canvas.winfo_width()
        p=self.canvas.coords(self.id)
        if  'KeyPress-Left>':#Si Se Mantiene Presionada La Flecha Izquierda 
            self.canvas.bind_all('<KeyPress-Left>',self.izq)
        if 'KeyRelease-Left>':#Si Se Deja De Presionar La Flecha Izquierda
            self.canvas.bind_all('<KeyRelease-Left>',self.stop)
        if 'KeyPress-Right>':#Si Se Mantiene Presionada La Flecha Derecha
            self.canvas.bind_all('<KeyPress-Right>',self.der)
        if 'KeyRelease-Right':#Si Se Deja De Presionar La Flecha Derecha
            self.canvas.bind_all('<KeyRelease-Right>',self.stop)
        
    def mover(self):
        self.canvas.move(self.id, self.x, self.y)
        p=self.canvas.coords(self.id)
    
    def izq(self,evt):#Funcion De Evento Mover Izquierda
        self.x=-1
    def der(self,evt):#Funcion De Evento Mover Derecha
        self.x=1
    def stop(self,evet):#Funcion De Evento Detener
        self.x=0
    
    
        




tk=Tk()
tk.title("Super Pinball KBA")

pantalla = Canvas(tk,width=400,height=400)
pantalla.pack()
tk.update()

inicio()


def main(pantalla2,ventana):#Loop Principal
    palanca1=Palanca1(pantalla2)
  
    bola=Bola(pantalla2,palanca1)#Llamado De La Clase Como Variable Para Facilitar Trabajo

    while 1:
        if bola.perder==False:
            #la variable usa las funciones de la clase con un punto(.)
            bola.mover()
            palanca1.mover()
        
        
        tk.update_idletasks()#Actualiza Nuevamente Por Segundo
        tk.update()
        ventana.update_idletasks()#Actualiza Nuevamente Por Segundo
        ventana.update()
        
        time.sleep(0.01)#Funcion De Tiempo
