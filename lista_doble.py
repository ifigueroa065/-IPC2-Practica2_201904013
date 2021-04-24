import os
from nodo import Nodo

class Lista_Doblemente():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0
    def vacia(self):
        return self.primero==None

    def Insertar_Nodo(self,nombre,apellido,telefono):
        if self.vacia():
            self.primero=self.ultimo=Nodo(nombre,apellido,telefono)
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=Nodo(nombre,apellido,telefono)
            self.ultimo.anterior=aux
        self.size+=1

    def tam(self):
        cont=0
        aux=self.primero
        while aux:
            cont+=1
            aux=aux.siguiente
        return cont

    def recorrer_lista(self):
        print("---LISTA DE CONTACTOS---")
        aux=self.primero
        while aux:
            print("-------------------------")
            print("-Nombre:"+ aux.nombre)
            print("-Apellido:"+ aux.apellido)
            print("-telefono:"+ str(aux.telefono))
            aux=aux.siguiente

    def verificando_contacto(self,nombre):
        #verificando numero
        aux=self.primero
        while aux:
            if nombre!=aux.nombre:
                aux=aux.siguiente
            else:
                return False

    def buscar(self,numero):
        #buscando numero
        aux=self.primero
        while aux:
            if numero!=aux.telefono:
                aux=aux.siguiente
            else:
                print("****CONTACTO****")
                print("-Nombre:"+ aux.nombre)
                print("-Apellido:"+ aux.apellido)
                print("-telefono:"+ str(aux.telefono))

                return False

    def CNodo(self,id,contacto):
        return (id+"[label=\""+contacto+"\"]\n")

    def UnirNodo(self,A,B):
        return (A+"->"+B+"\n")

    def visualizar(self):
        #generando grafo
        aux=self.primero

        with open("agenda.dot", mode="w",encoding="utf-8") as f:
            f.write("digraph grafo2{ \n");
            f.write("node[ style=filled ,color=\"#A3F8E9\"];\n");
            contador=2
            f.write(self.CNodo(str(contador),"AGENDA"));
            while aux:
                datos=aux.nombre+ "\n"+ aux.apellido+"\n"+ str(aux.telefono)
                contador=contador+2
                f.write(self.CNodo(str(contador),datos));
                f.write(self.UnirNodo(str(contador-2),str(contador)))
                f.write(self.UnirNodo(str(contador),str(contador-2)))
                
                aux=aux.siguiente
                                
            f.write("}\n");
        os.system('dot -Tpng agenda.dot -o AGENDA.png');

    def obtener_primero(self):
        aux=self.primero
        while aux:
            print("-Nombre:"+ aux.nombre)
            print("-Apellido:"+ aux.apellido)
            print("-telefono:"+ str(aux.telefono))
            break

    def obtener_ultimo(self):
        aux=self.primero
        while aux:
            if aux.siguiente==None:
                print("-Nombre:"+ aux.nombre)
                print("-Apellido:"+ aux.apellido)
                print("-telefono:"+ str(aux.telefono))
                break
            aux=aux.siguiente

    def Modificar(self,nombre,apellido,numero,nuevo):
        aux=self.primero
        while aux:
            if numero!=aux.telefono:
                aux=aux.siguiente
            else:
                aux.nombre=nombre
                aux.apellido=apellido
                aux.telefono=nuevo
                break


    def eliminar(self,numero):
        #buscando numero
        aux=self.primero
        eliminado=False

        if aux.siguiente is None:
            eliminado=False
        elif aux.telefono==numero:
            self.primero=aux.siguiente
            self.primero.anterior=None
            eliminado=True
        elif self.ultimo.telefono==numero:
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            eliminado=True
        else:
            while aux:
                if aux.telefono==numero:
                    aux.anterior.siguiente=aux.siguiente
                    aux.siguiente.anterior=aux.anterior
                    eliminado=True
                aux=aux.siguiente
        if eliminado:
            self.size-=1
                
    def buscar2(self,numero):
        #buscando numero
        aux=self.primero
        while aux:
            if numero!=aux.telefono:
                aux=aux.siguiente
            else:
                return False

    def eliminar_inicio(self):
        if self.vacia():
            print("esta vacia")
        elif  self.primero.siguiente==None:
            self.primero=self.ultimo=None
            self.size=0
        else:
            self.primero=self.primero.siguiente
            self.primero.anterior=None
            self.size-=1

    def eliminar_final(self):
        if self.vacia():
            print("esta vacia")
        elif  self.primero.siguiente==None:
            self.primero=self.ultimo=None
            self.size=0
        else:
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            self.size-=1