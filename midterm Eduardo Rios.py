#!/usr/bin/env python
# coding: utf-8

# ## Verdadero o falso con argumentos

# ### 1.  Una función recursiva resuelve un problema resolviendo una parte mas pequeña del mismo problema 

# Verdadero, ya que la recursividad es una función que se llama a si misma, de tal manera que reduce el problema grande en sub problemas mas pequeños para que así, se vayan resolviendo.
# Una vez resueltos estos sub problemas, si unimos las soluciones de cada problema, tendremos la solución al problema mayor.

# ### 2.  Los modelos computacionales nos ayudan a analizar la complejidad de los algoritmos, ya que nos proveen de las especificaciones de la computadora en la cual estos se ejecutarían idealmente

# Verdadero, sin embargo hay que tener en cuenta que los modelos computacionales no proveen las especificaciones de la computadora, sino que proveen el tiempo que tarda cada algoritmo en realizarse. De tal manera que podemos ver cuando nos cuesta cada operación, en referencia a la memoria de la computadora y tiempo de ejecución.

# ### 3.  La búsqueda en un árbol binario de búsqueda es siempre mas rápida que la búsqueda lineal en un arreglo

# Falso, en la busqueda binaria descartamos la mitad del rango de busqueda ya que la busqueda binaria tiene como funcion, logaritmo en base dos de (n+1)

# ### 4. Un algoritmo de complejidad O(nlog(n)) es mas rápido que un algoritmo de complejidad O(n) 

# Falso, ya que Omega analiza el mejor caso, por ende, omega (n) será más rápido que omega(nlog(n)) ya que es una complejidad lineal.

# ### 5.  Un algoritmo de complejidad Ω(nlog(n)) es mas rápido que un algoritmo de complejidad Ω(n)

# Falso, ya que O(nlog(n)) es una función que se asemeja a una función lineal pero no lo es, por lo que sabemos que la complejidad de O(n) es mucho mas sencilla y mas rápida.

# ## Problemas de programación
# #### Todo el código debe ser en Python. Si se requiere escribir funciones que hagan búsqueda o ordenamiento (search, sort), programe las funciones usando los conceptos aprendidos en clase. No use las funciones que Python provee para hacer esto. 

# ### 6. Dada una lista enlazada que represente un número. Por ejemplo, 123 es representado por la lista 1->2->3 si la lista es simple o con doble enlace si es doble. Escriba un programa que haga lo siguiente:
# 
# 1. Reciba dos números A y B como input
# 
# 2. Transforme estos números a listas enlazadas como la definida arriba
# 
# 3. Implemente la resta de los números descritos por esas listas enlazadas. El resultado (A-B) debe ser almacenado en una lista enlazada.
# 
# 4. Imprima el resultado concatenando el valor de los nodos de la lista enlazada resultante
# 
# Nota: asuma que el número A es mayor que B

# In[ ]:


import ctypes
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
        self.prev_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

    def getData(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node() 
        new_node.data = data
        new_node.next = self.cur_node 
        self.cur_node = new_node 

    def list_print(self):
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next    
    

def numToList(num):
    cabeza, cola = None, None
    for x in str(num):
        node = Node(x)
        if cabeza is not None:
            cola.next = node
        else:
            cabeza = node
            cola = node
    return cabeza

def reverse(self):
    prev = None
    current = self.head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev


def restTwoNumbers(l1, l2):

    carry = 0
    total = 0
    prev = None

    while (l1 is None) and (l2 is None):

        if not l1:
            total = l2.val
            l2 = l2.next
        elif not l2:
            total = l1.val
            l1 = l1.next
        else:
            total = l1.val - l2.val
            l1, l2 = l1.next, l2.next

        total -= carry
        if total >= 10:
            carry = 1
            total -= 10
        else:
            carry = 0
        curr = ListNode(total)
        if prev:
            prev.next = curr
        else:
            head = curr
        prev = curr
    
        if carry > 0:
            curr = ListNode(carry)
            prev.next = curr
    return head

A = int(input("Ingresar un numero A: "))
B = int(input("Ingresar un numero B: "))
AList = numToList(A)
BList = numToList(B)

#AList = LinkedList()
#BList = LinkedList()

AList = reverse(AList)
BList = reverse(BList)

CList = Node(None)
CList = A - B 
CList = numToList(CList)
answer = LinkedList(CList)


# ### 7.  Cuando introducimos el concepto de pilas (stacks), usamos como ejemplos una pila de platos. Siguiendo con el ejemplo, una pila de platos con muchos platos se puede caer. Para evitar esto, se puede empezar una nueva pila.
# 
# Implemente una clase de Python que defina un arreglo de stacks. La idea de tener este arreglo es que cuando un stack alcance su capacidad máxima, un nuevo stack empieza en el mismo arreglo. Las operación pop() debe retornar el mismo valor que lo haría si estuviéramos usando un stack simple. 
# 
# Nota: Debe definir los elementos de la clase: el arreglo de stacks, la capacidad del arreglo (# de stacks en el arreglo), la capacidad de cada stack (# de elementos que puede tener el stack). 
# 
# Hint: Cuando ingrese elementos (push), los elementos van al stack que este activo (el stack que recibe y retira elementos). Debe manejar las condiciones para cambiar el stack activo (cuando un push() deja al stack sin elementos, o cuando un pop() llena el stack).

# In[ ]:


class Stack:
    def __init__(self):
    self.elements = []

    def push(self, data):
        self.elements.append(data)
        return data
    
    def pop(self): 
        return self.elements.pop() 
        
    def peek(self): 
        return self.elements[-1] 
        
    def is_empty(self): 
        return len(self.elements) == 0


# ### 8. Dada una cola con prioridad (PriorityQueue) que contiene elementos (k,v) donde k define la prioridad y v define el valor. Recuerde que los valores con menor k tienen mayor prioridad, es decir si tenemos dos elementos (k1, v1) y (k2, v2), v2 tiene preferencia para salir de la cola antes que v1 si k2< k1. Definimos algunas de las operaciones como siguen:
# 
# ```
# import ctypes
# 
# class PriorityQueue(object):
# 
# """
# 
# Implementation of the queue data structure
# 
# """
# 
# def __init__(self, n):
# 
# self.item_count = 0
# 
# self.n = n
# 
# self.queue = self._create_queue(self.n)
# 
# def _create_queue(self, n):
# 
# """
# 
# Creates a new stack of capacity n
# 
# """
# 
# return (n * ctypes.py_object)()
# 
# def dequeue(self):
# 
# """
# 
# Remove an element from the queue
# 
# """
# 
# c = self.queue[0]
# 
# for i in range(1,self.item_count):
# 
# self.queue[i-1] = self.queue[i]
# 
# self.queue[self.item_count - 1] = ctypes.py_object
# 
# self.item_count -= 1
# 
# return c
# ```
# 
# ### Implemente los métodos enqueue y decreaseKey, tal que ambos métodos tengan complejidad O(log(n)), sin utilizar funciones nativas de Python. Por ejemplo, si necesita hacer una búsqueda, no use la función de Python que implementa esto, programe la función usando for o while loops.

# In[16]:


def enqueue(self,v1):
       node=Node(v1)

       if self.tail==None:
           self.head=self.tail=node

       if p<self.head.priority:
           node.next=self.head
           self.head=node

       if p>=self.tail.priority:
           self.tail.next=node
           self.tail=node

       else:
           tempFinal = self.head.next
           tempAntes = self.head
           while v1>tempFinal.priority:
               tempAntes=tempFinal
               tempFinal=tempFinal.next
           tempFinal.next=node
           node.next=tempFinal

def decreaseKey(self,v1,v2):
    ind = 0
    while (ind < len(self.queue)):
        if self.queue[ind][1] == v1:
            break
        else:
            ind += 1
    if ind == len(self.queue):
         print("Valor no encontrado!")
    self.queue[ind][0] = v2


# ### 9. Tenemos un árbol binario (binary tree), definimos a un nodo X como rojo, si todos los nodos en el recorrido de la raiz al nodo X tienen un valor que es menor o igual a X. Por ejemplo, en el ejemplo de abajo:
# 
# ![](./binary_tree.png)
# 
# El recorrido hacia el nodo 3 de la izquierda es 3 → 1 → 3, como todos los valores en este recorrido son menores o iguales a 3 (3=3 y 1<3), el nodo es rojo. Similarmente, en el sub-árbol de la derecha, los nodos 4 y 5 también son rojos. Escriba una función en Python que cuente el numero total de nodos rojos. El input de esta función es la raíz del árbol binario.
# 
#  

# In[ ]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def preorderTraversal(root):

        if root is None:
            return []
        stack = [root]
        out = []

        while stack:
            node = stack.pop()
            if node:
                out.append(node.val)
                for child in [node.right, node.left]:
                    if child:
                        stack.append(child)
        return out

    def max_depth_rec(root, depth):
        global answer
        if not root:
            return
        if (not root.left) and (not root.right):
            answer = max(answer, depth)
        max_depth_rec(root.left, depth + 1)
        max_depth_rec(root.right, depth + 1)


def numNodosRojos(self):
    contador = 0
    numeroTotal = []
    self.left = None 
    self.rigth = None
    
    if self.root == None:
        return 0
    
    nodos = []
    nodos.append(self.root)
    
    valor = nodos[0].val
    
    while (len(nodos)> 0):
        node = nodos.pop() 
        
        if node.val <= valor:
            contador = contador + 1
            
    return contador
    
    


# In[ ]:




