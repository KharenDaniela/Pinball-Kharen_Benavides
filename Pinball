from tkinter import*
import time
import random

global puntaje
global punt
punt=0
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
    global ventana
    ventana=Toplevel()#Nueva Ventana
    ventana.title("PINBALL")
    pantalla2 = Canvas(ventana, width=400,height=400)#Dimensiones Canvas Nueva Ventana
    pantalla2.pack()#Inserta El Canvas 
    ventana.update()#Actualiza 1 Milipixel x Segundo La Nueva Ventana
    #Labels Info Del Jugador
    player=Label(ventana,text="Jugador: ",font=("Arial",10)).place(x=0,y=0)#Label Player
    nombretomado=Label(ventana,text=nombre.get(),font=("Arial",10)).place(x=50,y=0)#Label Nombre Jugador
    npuntaje=Label(ventana,text="Puntaje: ",font=("Arial",10)).place(x=100,y=0)#Label Player
    #labelpuntaje=Label(ventana,text="Puntaje: ",font=("Arial",10)).place(x=100,y=0)#Label Puntaje
    main(pantalla2,ventana)#Llamada Al Loop(ciclo) Principal

   
class Bola: #Esta clase contiene la descripcion de nuestra bola,
                #la posicion, la funcion mover, coordenas de ventana,
                #dimensiones de la bola y de la ventana, condiciones
                #de rebote.


    def __init__(self,canvas,palanca1,puntaje):
        self.canvas=canvas
        self.palanca1=palanca1
        self.puntaje=puntaje
        #Descripcion Objetos
        self.linea01=canvas.create_line(1,70,1,310)#Esta Linea Y Sus Colisiones Son Para El Inicio De LA Bola
        self.linea0=canvas.create_line(40,70,40,320)#Esta Linea Y Sus Colisiones Son Para El Inicio De La Bola
        self.lineasoporte=canvas.create_line(43,70,43,320)#Esta Linea Y Sus Colisiones Son Para El Inicio De La Bola
        self.lineasoporte2=canvas.create_line(1,1,40,1)
        self.canvas.move(self.lineasoporte2,0,70)
        self.linea1=canvas.create_line(0,300,100,350)#Linea De Contencion 1
        self.linea3=canvas.create_rectangle(0,4,100,4,fill="black")
        self.canvas.move(self.linea3,150,200)
        self.linea4=canvas.create_rectangle(0,50,200,100,fill="black")
        self.canvas.move(self.linea4,100,-4)
        #Descripcion Objetos De Puntaje
        self.rectangulo1=canvas.create_rectangle(0,4,10,14,fill="black")
        self.canvas.move(self.rectangulo1,190,0)
        self.rectangulo2=canvas.create_rectangle(0,4,10,20,fill="black")
        self.canvas.move(self.rectangulo2,41,200)
        self.rectangulo3=canvas.create_rectangle(0,4,10,20,fill="black")
        self.canvas.move(self.rectangulo3,195,180)
        self.rectangulo4=canvas.create_rectangle(0,4,10,20,fill="black")
        self.canvas.move(self.rectangulo4,390,300)
        
        
        #Descripcion Bola
        self.id=canvas.create_oval(10, 10, 20, 20, fill="red")
        self.canvas.move(self.id,0,200)
        self.canvas_altura=self.canvas.winfo_height()
        self.canvas_ancho=self.canvas.winfo_width()
        d=[-3,-2,-1,1,2,3]
        random.shuffle(d)#Permite Sacar Valores Aleatorios De La Lista Para Las Direcciones De La Bola
        self.x=d[0]#Permite Que La Posicion X De La Bola Sea Un Valor Aleatorio De La Lista D
        self.y=1
        self.perder=False

    #Funciones De Colision Con Objetos
    def colision_palanca1(self,p):#Funcion De Colision Con Palanca1
        palanca1_p=self.canvas.coords(self.palanca1.id)#Devuelve Una Lista Con Coordenadas
        #Del Objeto Asi: [x1, y1, x2, y2]
        if p[2]>=palanca1_p[0] and p[0]<=palanca1_p[2]:
            if p[3]>=palanca1_p[1] and p[3]<=palanca1_p[3]:
                return True
        return False
    def colision_linea01(self,p):
        linea01_p=self.canvas.coords(self.linea01)
        if p[2]>=linea01_p[0] and p[0]<=linea01_p[2]:
            if p[3]>=linea01_p[1] and p[3]<=linea01_p[3]:
                return True
        return False
    def colision_linea0(self,p):
        linea0_p=self.canvas.coords(self.linea0)
        if p[2]>=linea0_p[0] and p[0]<=linea0_p[2]:
            if p[3]>=linea0_p[1] and p[3]<=linea0_p[3]:
                return True
        return False
    def colision_lineasoporte(self,p):
        lineasoporte_p=self.canvas.coords(self.lineasoporte)
        if p[2]>=lineasoporte_p[0] and p[0]<=lineasoporte_p[2]:
            if p[3]>=lineasoporte_p[1] and p[3]<=lineasoporte_p[3]:
                return True
        return False
    def colision_lineasoporte2(self,p):
       lineasoporte2_p=self.canvas.coords(self.lineasoporte2)
       if p[2]>=lineasoporte2_p[0] and p[0]<=lineasoporte2_p[2]:
           if p[3]>=lineasoporte2_p[1] and p[3]<=lineasoporte2_p[3]:
               return True
       return False
    def colision_linea1(self,p):
        linea1_p=self.canvas.coords(self.linea1)
        if p[2]>=linea1_p[0] and p[0]<=linea1_p[2]:
            if p[3]>=linea1_p[1] and p[3]<=linea1_p[3]:
                return True
        return False
   
    def colision_linea3(self,p):
        linea3_p=self.canvas.coords(self.linea3)
        if p[2]>=linea3_p[0] and p[0]<=linea3_p[2]:
            if p[3]>=linea3_p[1] and p[3]<=linea3_p[3]:
                return True
        return False
    def colision_linea4(self,p):
        linea4_p=self.canvas.coords(self.linea4)
        if p[2]>=linea4_p[0] and p[0]<=linea4_p[2]:
            if p[3]>=linea4_p[1] and p[3]<=linea4_p[3]:
                return True
        return False
    #Funciones Colision De Puntaje
    def rectangulo11(self,p):
        rectangulo1_p=self.canvas.coords(self.rectangulo1)
        if p[2]>=rectangulo1_p[0] and p[0]<=rectangulo1_p[2]:
            if p[3]>=rectangulo1_p[1] and p[3]<=rectangulo1_p[3]:
                return True
        return False
    def rectangulo22(self,p):
        rectangulo2_p=self.canvas.coords(self.rectangulo2)
        if p[2]>=rectangulo2_p[0] and p[0]<=rectangulo2_p[2]:
            if p[3]>=rectangulo2_p[1] and p[3]<=rectangulo2_p[3]:
                return True
        return False
    def rectangulo33(self,p):
        rectangulo3_p=self.canvas.coords(self.rectangulo3)
        if p[2]>=rectangulo3_p[0] and p[0]<=rectangulo3_p[2]:
            if p[3]>=rectangulo3_p[1] and p[3]<=rectangulo3_p[3]:
                return True
        return False
    def rectangulo44(self,p):
        rectangulo4_p=self.canvas.coords(self.rectangulo4)
        if p[2]>=rectangulo4_p[0] and p[0]<=rectangulo4_p[2]:
            if p[3]>=rectangulo4_p[1] and p[3]<=rectangulo4_p[3]:
                return True
        return False
    



    #Funcion Mover Bola
    def mover(self):
      punt=0
      d=[-3,-2,-1,1,2,3]
      random.shuffle(d)#Permite Sacar Valores Aleatorios De La Lista Para Las Direcciones De La Bola
        
      self.canvas.move(self.id, self.x, self.y)#Mover Objeto              
      p=self.canvas.coords(self.id)#Obtener Posiciones De Objeto
      if p[1]<=0:
          self.y=1
      if p[3]>=self.canvas_altura:
          self.perder=True#Golpea El Fondo
          ventanaperdida=Toplevel()
          ventanaperdida.title("Suerte La Proxima")
          pantalla3=Canvas(ventanaperdida, width=400,height=400)
          pantalla3.pack()
          perdiste=Label( ventanaperdida, text="PERDISTE", font = ("Algerian",30)).place(x=120,y=200)
          salir=Button(ventanaperdida,text=("Salir"),font=("Arial",15),width=30,command=tk.destroy).place(x=50,y=300)
      #Condiciones De Colision de Objetos
      if self.colision_palanca1(p)==True:#Al Colisionar Con Palanca1 Devuelve True
          self.y*=-1
      if self.colision_linea01(p)==True:#Al Colisionar Con Linea4 Devuelve True
          self.y=-1
          self.x=1     
      if self.colision_linea0(p)==True:#Al Colisionar Con Linea0 Devuelve True
          self.y=-1
          self.x=-1
      if self.colision_lineasoporte(p)==True:#Al Colisionar Con Lineasoporte Devuelve True
          self.y*=-1
          self.x=1
      if self.colision_lineasoporte2(p)==True:#Al Colisionar Con Lineasoporte2 Devuelve True
          self.y1=-1
      if self.colision_linea1(p)==True:#Al Colisionar Con Linea1 Devuelve True
          self.y*=-1
      if self.colision_linea3(p)==True:#Al Colisionar Con Linea3 Devuelve True
          self.y*=-1
      if self.colision_linea4(p)==True:#Al Colisionar Con Linea4 Devuelve True
          self.y*=-1
      #Condiciones De Colision de Objetos De Puntaje
      if self.rectangulo11(p)==True:
          self.puntaje.arb()
      if self.rectangulo22(p)==True:
          self.puntaje.arb()
      if self.rectangulo33(p)==True:
          self.puntaje.arb()
      if self.rectangulo44(p)==True:
          self.puntaje.arb()
          
     
      
       
           
      #Condiciones De Colision Lados Del Tablero   
      if p[0]<=0:
          self.x=d[0]
          self.y=1
      if p[2]>=self.canvas_ancho:
          self.x=d[0]
          self.y=1
      
           

    
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

class Puntaje():#Clase Puntaje  

    def __init__(self,canvas):
        self.puntuacion=0
        self.canvas= canvas
        self.id = canvas.create_text(300,10,font=("Arial",12),text=self.puntuacion)#Crea Un Texto Sobre El Canvas
    def arb(self):
        self.puntuacion +=50#Funcion Suma Puntaje
        self.canvas.itemconfig(self.id, text=self.puntuacion)#Muestra EL Texto En Pantalla
    
    
        




tk=Tk()


tk.title("Super Pinball KBA")

pantalla = Canvas(tk,width=400,height=400)
pantalla.pack()
tk.update()

inicio()


def main(pantalla2,ventana):#Loop Principal
    palanca1=Palanca1(pantalla2)
    puntaje=Puntaje(pantalla2)
    bola=Bola(pantalla2,palanca1,puntaje)#Llamado De La Clase Como Variable Para Facilitar Trabajo
    
    while 1:
        if bola.perder==False:
            #la variable usa las funciones de la clase con un punto(.)
            bola.mover()
            palanca1.mover()
        
        
        #tk.update_idletasks()#Actualiza Nuevamente Por Segundo
        tk.update()
        #ventana.update_idletasks()#Actualiza Nuevamente Por Segundo
        ventana.update()
        
        time.sleep(0.01)#Funcion De Tiempo
