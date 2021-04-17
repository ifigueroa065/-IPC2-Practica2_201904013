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

