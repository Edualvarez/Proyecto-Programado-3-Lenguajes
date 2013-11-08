## funcion que lee y archivo y mete en la lista las expresiones

def leer_archivo(archivo):
    archivo=open(archivo,"r")
    cont=-1
    lista_var=[]
    linea=(archivo.readline().strip("\n")).strip("\t")
    aux=""
    while linea!="":
        if linea[0:3]!="val" and linea[0:3]!="let":
            lista_var[cont]=lista_var[cont]+" "+linea
            linea=(archivo.readline().strip("\n")).strip("\t")
        else:
            cont+=1
            lista_var=lista_var+[linea]
            linea=(archivo.readline().strip("\n")).strip("\t")
            
    archivo.close
    return (lista_var)
    for i in lista_var:
        print (i)
l1=leer_archivo("Codigo.txt")
for i in l1:
    i=i.split(" ")
  #  print (i)

## Funcion que elimina espacios en blanco de una expresion

def eliminaEspacios(expresion):
    largo=len(expresion)
    i=0
    result=""
    while i!=largo:
        if expresion[i]!=" ":
            result+=expresion[i]
            i+=1
        else:
            i+=1
    return result

## Valida si lo que entra es un flotante, entero o string
  
def prueba (palabra):
    resultado = ""
    try:
        int (palabra)
        resultado = "entero"
        return resultado
    except:
        try:
            float (palabra)
            resultado = "flotante"
            return resultado
        except:
                resultado = "string"
                return resultado

## funcion que separa las expresiones cuando vienen un let

def separarLet():
    lista= leer_archivo("Codigo.txt")
    result=[]
    largo =len(lista)
    i=0
    while largo!=i:
        if lista[i].find("let")!=-1 and lista[i][(lista[i].find("let"))-1]!="=":
            result+=[lista[i][:lista[i].find("let")]]
            result+=[lista[i][lista[i].find("let"):]]
            i+=1
        else:
            result+=[lista[i]]
            i+=1
    return result
            
        
        
# Recibe una lista y realiza la evaluación de expresiones sencillas

def evaluarSencillo ():
    lista = separarLet()
    resultado = []
    largo = len (lista)
    #print (largo)
    i=0
    while largo!=i:
        if lista[i]!="":
            if lista[i][:3]!="let":
                expresion = lista[i].strip("val")
                expresion = expresion.strip(" ")
                ##expresion=eliminaEspacios(expresion)
                if expresion.find("let")==-1:
                    
                    if expresion[2]=="i" and expresion[3]=="f":
                        resultado+=[[expresion[:1],expresion[2:]]]
                        i+=1
                    else:
                        expresion=eliminaEspacios(expresion)
                        expresion=expresion.split("=")
                        if prueba(expresion[1])=="entero":
                            resultado +=[[expresion[0],"int"]]
                            i+=1
                        elif prueba(expresion[1])=="flotante":
                            resultado +=[[expresion[0],"double"]]
                            i+=1
                        else:
                            if expresion[1][0]=='"':
                                resultado += [[expresion[0],"string"]]
                                i+=1
                            else:
                                if expresion[1]=="true" or expresion[1] == "false":
                                    resultado += [[expresion[0],"bool"]]
                                    i+=1
                                else:
                                    resultado += [[expresion[0], expresion[1]]]
                                    i+=1
                else:
                    posicion = expresion.find("=")
                    resultado+=[[expresion[:posicion],expresion[posicion+1:]]]
                    i+=1
                     
            else:
                resultado+=[[lista[i][:3],lista[i][3:]]]
                i+=1
        else:
            i+=1
            
    return resultado

## funcion que separa los elementos de una expresion compleja
## que estan en la lista de evaluar sencillo.

def separarExpresion(expre):
    i=0
    lista=[]
    largo = len(expre)
    while i != largo:
        lista1=[]
        if expre[i]=="(":
            while expre[i]!= ")":
                lista1+= expre[i]
                i+=1
            lista1+=expre[i]
            lista += lista1
            i+=1
        else:
            lista+=expre[i]
            i+=1
    return lista

## funcion que evalua expresiones compuestas por variables y constantes

def evaluarCompleja():
    lista=evaluarSencillo()
    i=0;
    largo = len (lista)
    lista1=[]
    while i!=largo:
        if lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool":
            lista1+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 :
                lista1+= [lista[i]]
                i+=1
            else:
                if lista[i][1].find(",")!=-1 or lista[i][1].find("[")!=-1 :
                    lista1+= [lista[i]]
                    i+=1
                else:
                    listaExpresion= separarExpresion(lista[i][1])
                    cont = len(listaExpresion)
                    j=0
                    while j!=cont:
                        if listaExpresion[j]=="(" or listaExpresion[j]==")":
                            if j==cont-1:
                                lista[i][1]
                                lista1 +=[[lista[i][0],lista[i][1]]]
                                j=cont
                            else:
                                j+=1
                        else:
                            if prueba(listaExpresion[j])=="entero":
                                lista1 +=[[lista[i][0],"int"]]
                                j=cont
                            elif prueba(listaExpresion[j])=="flotante":
                                lista1 +=[[lista[i][0],"double"]]
                                j=cont
                            elif listaExpresion[j]=='"':
                                lista1 +=[[lista[i][0],"string"]]
                                j=cont
                            else:
                                if j==cont-1:
                                    lista[i][1]
                                    lista1 +=[[lista[i][0],lista[i][1]]]
                                    j=cont
                                else:
                                    j+=1
                    i+=1
    return lista1

## funcion que busca los elementos de una lista

def buscar(expresion,posicion,lista):
    i=0
    resultado=[]
    while i!=posicion:
        if len(lista[i])!=3:
            if lista[i][0]==expresion:
                resultado+=[lista[i][1]]
                i+=1
            else:
                i+=1
        else:
            i+=1
    return resultado

## funcion que determina el tipo de las expresiones compuestas solo por variables

def evaluarVariable():
    lista= evaluarCompleja()
    i=0
    lista1=[]
    largo = len(lista)
    while i!=largo:
        if lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool":
            lista1+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 :
                lista1+= [lista[i]]
                i+=1
            else:
                if lista[i][1].find(",")!=-1 or lista[i][1].find("[")!=-1 :
                    lista1+= [lista[i]]
                    i+=1
                else:
                    j=0
                    while lista [i][1][j]=="(":
                        j+=1
                    expresionBuscar = buscar(lista[i][1][j],i,lista1)
                    lista1+=[[lista[i][0], expresionBuscar[-1]]]
                    i+=1
    return lista1



# Funcion que determina la cantidad de elementos que componen una tupla

def elementosTupla(expresion):
    i=0
    largo=len(expresion)
    contador=0
    while i!=largo:
        if expresion[i]==",":
            contador+=1
            i+=1
        else:
            i+=1
    return contador

## Funcion que evalua expresiones y retorna el tipo de la expresion

def evaluarComplejaTupla(lista):
    j=0
    expresion=""
    while j!=len(lista):
        expresion+=lista[j]
        j+=1
    expresion
    i=0;
    largo = len (lista)
    resultado=""
    while i!=largo:
            if prueba(lista[i])=="entero" and expresion.find(".")==-1:
                resultado="int"
                i=largo
            
            elif expresion.find(".")!=-1:
                resultado="double"
                i=largo
            elif lista[i]=='"':
                resultado="string"
                i=largo
            elif (lista[i]=="t" and lista[i+1]=="r") or (lista[i]=="f" and lista[i+1]=="a"):
                resultado="bool"
                i=largo
            else:
               i+=1
    return resultado

# Funcion que evalua expresiones compuestas unicamente con variables y retorna el tipo de la expresion
def evaluarVariableTupla(lista,j):
    listaEvaluada=evaluarVariable()
    i=0
    resultado=""
    largo = len(lista)
    while i!=largo:
        if lista[i]!="+" and lista[i]!="-" and lista[i]!="*" and lista[i]!="^" and lista[i]!="(" and lista[i]!=")":
            expresionBuscar = buscar(lista[i],j,listaEvaluada)
            if expresionBuscar!=[]:
                resultado= expresionBuscar[-1]
                i=largo
            else:
                resultado
                i=largo
        else:
            i+=1
    return resultado


## Funcion que evalua y determina los tipos de las tuplas

def evaluarTuplasSencillo():
    lista=evaluarVariable()
    i=0
    largo=len(lista)
    resultado=[]
    tipo=""
    while i!=largo:
        if lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool":
            resultado+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 or lista[i][1].find("[")!=-1 :
                resultado+= [lista[i]]
                i+=1
            else:
                if lista[i][1].find(",")!=-1:
                    expresion=separarExpresion(lista[i][1])
                    if elementosTupla(expresion)==1:
                        posicion=lista[i][1].find(",")
                        listaparte1=expresion[:posicion]
                        listaparte2=expresion[posicion+1:]
                        if (evaluarComplejaTupla(listaparte1)=="int" or evaluarComplejaTupla(listaparte1)=="double" or evaluarComplejaTupla(listaparte1)=="string")and(evaluarComplejaTupla(listaparte2)=="int" or evaluarComplejaTupla(listaparte2)=="double" or evaluarComplejaTupla(listaparte2)=="string"):
                            tipo=evaluarComplejaTupla(listaparte1)
                            tipo+="*"
                            tipo+=evaluarComplejaTupla(listaparte2)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        elif  (evaluarVariableTupla(listaparte1,i)!="")and (evaluarVariableTupla(listaparte1,i)=="int" or evaluarVariableTupla(listaparte1,i)=="double" or evaluarVariableTupla(listaparte1,i)=="string") and (evaluarVariableTupla(listaparte2,i)!="")and(evaluarVariableTupla(listaparte2,i)=="int" or evaluarVariableTupla(listaparte2,i)=="double" or evaluarVariableTupla(listaparte2,i)=="string"):
                            tipo=evaluarVariableTupla(listaparte1,i)
                            tipo+="*"
                            tipo+=evaluarVariableTupla(listaparte2,i)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        elif (evaluarComplejaTupla(listaparte1)=="int" or evaluarComplejaTupla(listaparte1)=="double" or evaluarComplejaTupla(listaparte1)=="string") and (evaluarVariableTupla(listaparte2,i)!="") and(evaluarVariableTupla(listaparte2,i)=="int" or evaluarVariableTupla(listaparte2,i)=="double" or evaluarVariableTupla(listaparte2,i)=="string"):
                            tipo=evaluarComplejaTupla(listaparte1)
                            tipo+="*"
                            tipo+=evaluarVariableTupla(listaparte2,i)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        elif (evaluarVariableTupla(listaparte1,i)!="") and(evaluarVariableTupla(listaparte1,i)=="int" or evaluarVariableTupla(listaparte1,i)=="double" or evaluarVariableTupla(listaparte1,i)=="string") and (evaluarComplejaTupla(listaparte2)=="int" or evaluarComplejaTupla(listaparte2)=="double" or evaluarComplejaTupla(listaparte2)=="string"):
                            tipo=evaluarVariableTupla(listaparte1,i)
                            tipo+="*"
                            tipo+=evaluarComplejaTupla(listaparte2)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        else:
                            resultado+=[lista[i]]
                            i+=1
                    else:
                        resultado+=[lista[i]]
                        i+=1
                else:
                    i+=1
    return resultado
                                    

## funcion que separa los elementos cuando vienen una tupla dentro de otra tupla

def separarTuplaTupla(lista):
    largo= len(lista)
    i=0
    cont=0
    while i!=largo:
        if lista[i]=="," and (lista[i-1]==")" or lista[i+1]=="("):
            cont=i
            i=largo
        else:
            i+=1
    return cont

## funcion que retorne la posicion hasta donde se encuentra una coma

def encontrarComa(lista):
    largo= len(lista)
    i=0
    cont=0
    while i!=largo:
        if lista[i]==",":
            cont=i
            i=largo
        else:
            i+=1
    return cont


## funcion que recibe una tupla y retorna su tipo

def evaluarTipoTupla(expresion,j):
    i=0
    largo = len(expresion)
    tipo=""
    while i!=largo:
        if encontrarComa(expresion)!=0:
            posicion=encontrarComa(expresion)
            listaparte1=expresion[:posicion]
            listaparte2=expresion[posicion+1:]
            if (evaluarComplejaTupla(listaparte1)=="int" or evaluarComplejaTupla(listaparte1)=="double" or evaluarComplejaTupla(listaparte1)=="string")and(evaluarComplejaTupla(listaparte2)=="int" or evaluarComplejaTupla(listaparte2)=="double" or evaluarComplejaTupla(listaparte2)=="string"):
                tipo+="("
                tipo+=evaluarComplejaTupla(listaparte1)
                tipo+="*"
                tipo+=evaluarComplejaTupla(listaparte2)
                tipo+=")"
                i=largo
            elif  (evaluarVariableTupla(listaparte1,j)!="")and (evaluarVariableTupla(listaparte1,j)=="int" or evaluarVariableTupla(listaparte1,j)=="double" or evaluarVariableTupla(listaparte1,j)=="string") and (evaluarVariableTupla(listaparte2,j)!="")and(evaluarVariableTupla(listaparte2,j)=="int" or evaluarVariableTupla(listaparte2,j)=="double" or evaluarVariableTupla(listaparte2,j)=="string"):
                tipo+="("
                tipo+=evaluarVariableTupla(listaparte1,j)
                tipo+="*"
                tipo+=evaluarVariableTupla(listaparte2,j)
                tipo+=")"
                i=largo
            elif (evaluarComplejaTupla(listaparte1)=="int" or evaluarComplejaTupla(listaparte1)=="double" or evaluarComplejaTupla(listaparte1)=="string") and (evaluarVariableTupla(listaparte2,j)!="") and(evaluarVariableTupla(listaparte2,j)=="int" or evaluarVariableTupla(listaparte2,j)=="double" or evaluarVariableTupla(listaparte2,j)=="string"):
                tipo+="("
                tipo+=evaluarComplejaTupla(listaparte1)
                tipo+="*"
                tipo+=evaluarVariableTupla(listaparte2,j)
                tipo+=")"
                i=largo
            elif (evaluarVariableTupla(listaparte1,j)!="") and(evaluarVariableTupla(listaparte1,j)=="int" or evaluarVariableTupla(listaparte1,j)=="double" or evaluarVariableTupla(listaparte1,j)=="string") and (evaluarComplejaTupla(listaparte2)=="int" or evaluarComplejaTupla(listaparte2)=="double" or evaluarComplejaTupla(listaparte2)=="string"):
                tipo+="("
                tipo+=evaluarVariableTupla(listaparte1,j)
                tipo+="*"
                tipo+=evaluarComplejaTupla(listaparte2)
                tipo+=")"
                i=largo
            else:
                i=largo
        else:
            if (evaluarComplejaTupla(expresion)=="int" or evaluarComplejaTupla(expresion)=="double" or evaluarComplejaTupla(expresion)=="string"):
                tipo=evaluarComplejaTupla(expresion)
                i=largo
            else:
                if (expresion[i]=="t" and expresion[i+1]=="r") or (expresion[i]=="f" and expresion[i+1]=="a"):
                    tipo="bool"
                    i=largo
                else:
                    tipo=evaluarVariableTupla(expresion,j)
                    i=largo
    return tipo            
                    
                
## funcion que evalua tuplas de tuplas

def evaluarTuplaTuplas():
    lista=evaluarTuplasSencillo()
    i=0
    largo=len(lista)
    resultado=[]
    tipo=""
    while i!=largo:
        if lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool":
            resultado+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 or lista[i][1].find("[")!=-1 :
                resultado+= [lista[i]]
                i+=1
            else:
                expresion=separarExpresion(lista[i][1])
                posicion= separarTuplaTupla(expresion)
                listaparte1=expresion[:posicion]
                listaparte2=expresion[posicion+1:]
                tipo=evaluarTipoTupla(listaparte1,i)
                tipo+="*"
                tipo+=evaluarTipoTupla(listaparte2,i)
                resultado+=[[lista[i][0],tipo]]
                i+=1
    return resultado

## funcion que evalua los elementos que son listas

def evaluarListaSencilla():
    lista=evaluarTuplaTuplas()
    i=0
    largo=len(lista)
    resultado=[]
    while i!=largo:
        if lista[i][1][1]=="[" or lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool" or (lista[i][1]=="int" and lista[i][1].find("*")!=-1) or (lista[i][1]=="double" and lista[i][1].find("*")!=-1) or (lista[i][1]=="string" and lista[i][1].find("*")!=-1) :
            resultado+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 or  lista[i][1][0]=="(":
                resultado+= [lista[i]]
                i+=1
            else:
                expresion = lista[i][1]
                if expresion[1]!="[":
                    if prueba(expresion[1])=="entero":
                        resultado+=[[lista[i][0],"int list"]]
                        i+=1
                    elif prueba(expresion[1])=="flotante":
                        resultado+=[[lista[i][0],"double list"]]
                        i+=1
                    elif expresion[1]=='"':
                        resultado+=[[lista[i][0],"string list"]]
                        i+=1
                    elif (expresion[1]=="t" and expresion[2]=="r") or (expresion[1]=="f" and expresion[2]=="a") :
                        resultado+=[[lista[i][0],"bool list"]]
                        i+=1
                    else:
                        j=1
                        while j!=len(expresion):
                            if expresion[j]!="(":
                                if expresion[j]!=")" or expresion[j]!="+" or expresion[j]!="-" or expresion[j]!="*" or expresion[j]!="^" or (expresion[j]!="m" and expresion[j+1]!="o") or (expresion[j]!="d" and expresion[j+1]!="i"):
                                    if prueba(expresion[j])=="entero":
                                        if prueba(expresion[j])=="entero" and expresion.find(".")==-1:
                                            resultado+=[[lista[i][0],"int"+" list"]]
                                            j=len(expresion)
                                        else:
                                            resultado+=[[lista[i][0],"double"+" list"]]
                                            j=len(expresion)
                                    elif (expresion[j]=="t" and expresion[j+1]=="r") or (expresion[j]=="f" and expresion[j+1]=="a") :
                                        resultado+=[[lista[i][0],"bool list"]]
                                        j=len(expresion)
                                    else:
                                        if j == (len(expresion)-1):
                                            resultado+=[lista[i]]
                                            j=len(expresion)
                                        else:
                                            j+=1
                                else:
                                    j+=1
                            else:
                                if expresion[j]=="(":
                                    pos=expresion.find(")")
                                    aux=expresion[j:]
                                    aux=aux[:pos]
                                    if aux.find(",")!=-1:
                                        resultado+=[lista[i]]
                                        j=len(expresion)
                                    else:
                                        j+=1
                                else:
                                    j+=1
                        i+=1
    return resultado        
                                    
## Función que evalua los elementos que son listas yson complejas, es decir formados por variables

def evaluarListaCompleja():
    lista=evaluarListaSencilla()
    i=0
    largo=len(lista)
    resultado=[]
    while i!=largo:
        if (lista[i][1][1]=="[" or lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool") or (lista[i][1]=="int" and lista[i][1].find("*")!=-1) or (lista[i][1]=="double" and lista[i][1].find("*")!=-1) or (lista[i][1]=="string" and lista[i][1].find("*")!=-1) :
            resultado+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 or  lista[i][1][0]=="(":
                resultado+= [lista[i]]
                i+=1
            else:
                if lista[i][1]=="int list" or lista[i][1]=="string list" or lista[i][1]=="bool list" or lista[i][1]=="double list":
                    resultado+= [lista[i]]
                    i+=1
                else:
                    expresion=lista[i][1]
                    
                    j=1
                    while j!=len(expresion):
                        if expresion[j]!="(":
                            if expresion[j]!=")" or expresion[j]!="+" or expresion[j]!="-" or expresion[j]!="*" or expresion[j]!="^" or (expresion[j]!="m" and expresion[j+1]!="o") or (expresion[j]!="d" and expresion[j+1]!="i"):
                                expresionBuscar=buscar(expresion[j],i,lista)
                                if expresionBuscar!=[]:
                                    resultado+=[[lista[i][0],expresionBuscar[-1]+" list"]]
                                    j=len(expresion)
                                else:
                                    j+=1
                            else:
                                j+=1
                        else:
                            if expresion[j]=="(":
                                pos=expresion.find(")")
                                aux=expresion[j:]
                                aux=aux[:pos]
                                if aux.find(",")!=-1:
                                    resultado+=[lista[i]]
                                    j=len(expresion)
                                else:
                                    j+=1
                            else:
                                j+=1
                    i+=1
    return resultado            
                                
                    
def evaluarTuplasLista():
    lista=evaluarListaCompleja()
    i=0
    largo=len(lista)
    resultado=[]
    while i!=largo:
        if (lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool") or (lista[i][1]=="int" and lista[i][1].find("*")!=-1) or (lista[i][1]=="double" and lista[i][1].find("*")!=-1) or (lista[i][1]=="string" and lista[i][1].find("*")!=-1) :
            resultado+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 or  lista[i][1][0]=="(":
                resultado+= [lista[i]]
                i+=1
            else:
                if lista[i][1]=="int list" or lista[i][1]=="string list" or lista[i][1]=="bool list" or lista[i][1]=="double list":
                    resultado+= [lista[i]]
                    i+=1
                else:
                    expresion= lista[i][1]
                    j=1
                    while j!=len(expresion):
                        if expresion[j]!="[":
                            pos=expresion.find(")")
                            if pos+2!=len(expresion):
                                if expresion[pos+2]=="(":
                                    exp=separarExpresion(lista[i][1])
                                    posicion= separarTuplaTupla(exp)
                                    listaparte1=exp[1:posicion]
                                    listaparte2=exp[posicion+1:]
                                    resultado+=[[lista[i][0],evaluarTipoTupla(listaparte1,i)+"*"+evaluarTipoTupla(listaparte2,i)+"list"]]
                                    j=len(expresion)
                                else:
                                    resultado+= [lista[i]]
                                    j=len(expresion)
                            else:
                                aux=expresion[j:]
                                aux=aux[:pos]
                                expre=separarExpresion(aux)
                                resultado+=[[lista[i][0],evaluarTipoTupla(expre,i)+"list"]]
                                j=len(expresion)                                
                        else:
                            resultado+=[lista[i]]
                            j=len(expresion)
                    i+=1
                            
    return resultado                        
    
 ## funcion que determina el tipo de las listas

def evaluarTipoLista(lista,i):
    j=1
    largo=len(lista)
    resultado=""
    lista1=evaluarTuplasLista()
    if prueba(lista[1])=="entero" and lista.find(".")==-1:
        resultado="int list"
    elif lista.find(".")!=-1:
        resultado="double list"
    elif lista[1]=='"':
        resultado="string list"                          
    elif (lista[1]=="t" and lista[2]=="r") or (lista[1]=="f" and lista[2]=="a") :
        resultado="bool list"
    else:
        while j!=len(lista):
            if lista!= "]" or lista[j]!=")" or lista[j]!="+" or lista[j]!="-" or lista[j]!="*" or lista[j]!="^" or (lista[j]!="m" and lista[j+1]!="o") or (lista[j]!="d" and lista[j+1]!="i"):
                if prueba(lista[j])=="entero":
                    if prueba(lista[j])=="entero" and lista.find(".")==-1:
                        resultado="int list"
                        j=len(lista)
                    else:
                        resultado="double"+" list"
                        j=len(lista)
                elif (lista[j]=="t" and lista[j+1]=="r") or (lista[j]=="f" and lista[j+1]=="a") :
                    resultado="bool list"
                    j=len(lista)
                else:
                    j+=1
            else:
                j+=1
        if resultado=="":
            j=1
            while j!=len(lista):
                if lista!= "]" or lista[j]!=")" or lista[j]!="+" or lista[j]!="-" or lista[j]!="*" or lista[j]!="^" or (lista[j]!="m" and lista[j+1]!="o") or (lista[j]!="d" and lista[j+1]!="i"):
                    expresionBuscar=buscar(lista[j],i,lista1)
                    if expresionBuscar!=[]:
                        resultado=expresionBuscar[-1]+" list"
                        j=len(lista)
                    else:
                        j+=1
                else:
                    j+=1
    return resultado

## funcion que evalua el tipo de lista de listas

def evaluarListaListas():
    lista= evaluarTuplasLista()
    i=0
    largo=len(lista)
    resultado=[]
    while i!=largo:
        if (lista[i][1]=="int" or lista[i][1]=="double" or lista[i][1]=="string" or lista[i][1]== "bool") or (lista[i][1]=="int" and lista[i][1].find("*")!=-1) or (lista[i][1]=="double" and lista[i][1].find("*")!=-1) or (lista[i][1]=="string" and lista[i][1].find("*")!=-1) :
            resultado+= [lista[i]]
            i+=1
        else:
            if lista[i][1].find("if")!=-1 or lista[i][1].find("let")!=-1 or lista[i][1].find("val")!=-1 or lista[i][1].find("in")!=-1 or  lista[i][1][0]=="(":
                resultado+= [lista[i]]
                i+=1
            else:
                if lista[i][1]=="int list" or lista[i][1]=="string list" or lista[i][1]=="bool list" or lista[i][1]=="double list":
                    resultado+= [lista[i]]
                    i+=1
                else:
                    expresion=lista[i][1]
                    lar=len(expresion)
                    expresion=expresion[1:lar-1]
                    resultado+=[[lista[i][0],"("+evaluarTipoLista(expresion,i)+")"+" list"]]
                    i+=1
    return resultado


 ## funcion que determina el tipo de las listas

def evaluarExpresiones(lista,i,lista1):
    j=1
    largo=len(lista)
    resultado=""
    if lista.find(".")!=-1:
        resultado="double list"
    elif prueba(lista[1])=="entero":
        resultado="int list"
    elif lista[1]=='"':
        resultado="string list"                          
    elif (lista[1]=="t" and lista[2]=="r") or (lista[1]=="f" and lista[2]=="a") :
        resultado="bool list"
    else:
        while j!=len(lista):
            if lista[j]!= "]" or lista[j]!=")" or lista[j]!="+" or lista[j]!="-" or lista[j]!="*" or lista[j]!="^" or (lista[j]!="m" and lista[j+1]!="o") or (lista[j]!="d" and lista[j+1]!="i"):
                if prueba(lista[j])=="entero":
                    if prueba(lista[j])=="entero" and lista.find(".")==-1:
                        resultado="int list"
                        j=len(lista)
                    else:
                        resultado="double"+" list"
                        j=len(lista)
                elif (lista[j]=="t" and lista[j+1]=="r") or (lista[j]=="f" and lista[j+1]=="a") :
                    resultado="bool list"
                    j=len(lista)
                else:
                    j+=1
            else:
                j+=1
        if resultado=="":
            j=1
            while j!=len(lista):
                if lista[j]!= "]" or lista[j]!=")" or lista[j]!="+" or lista[j]!="-" or lista[j]!="*" or lista[j]!="^" or (lista[j]!="m" and lista[j+1]!="o") or (lista[j]!="d" and lista[j+1]!="i"):
                    expresionBuscar=buscar(lista[j],i,lista1)
                    if expresionBuscar!=[]:
                        resultado=expresionBuscar[-1]+" list"
                        j=len(lista)
                    else:
                        j+=1
                else:
                    j+=1
    return resultado

## funcion que evalua los vals

def evaluarVals(expresion,i,result):
    pos=expresion.find("val")
    tipo=""
    if pos!=-1:
        expr_temp=expresion[:pos-1]
        expresion=expresion[pos+4:]
        po= expr_temp.find("=")
        exp3=expr_temp[:po]
        exp4="["+expr_temp[po+1:]+"]"
        if exp4[1]=="[" and exp4[2]!="[":
            exp4=exp1[po+1:]
            tipo=evaluarTipoLista(exp4,i)
            result+=[[exp3,tipo]]
            if expresion!="":
                evaluarVals(expresion,i,result)
            else:
                result
        elif exp4[1]=="[" and exp4[2]=="[":
            exp4=exp4[1:len(exp4)-1]
            tipo=evaluarTipoLista(exp4,i)+" list"
            result+=[[exp3,tipo]]
            if expresion!="":
                evaluarVals(expresion,i,result)
            else:
                result
        else:
            tipo=evaluarTipoLista(exp4,i)
            tipo=tipo.rstrip("list")
            if tipo[0]=="[" and tipo[1]=="[":
                lar=len(tipo)
                tipo=tipo[1:lar-1]
                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                result+=[[exp3,tipo]]
                if expresion!="":
                    evaluarVals(expresion,i,result)
                else:
                    result
            else:
                tipo
                result+=[[exp3,tipo]]
                if expresion!="":
                    evaluarVals(expresion,i,result)
                else:
                    result
    else:
        po= expresion.find("=")
        exp3=expresion[:po]
        exp4="["+expresion[po+1:]+"]"
        if exp4[1]=="[" and exp4[2]!="[":
            exp4=expresion[po+1:]
            tipo=evaluarTipoLista(exp4,i)
            result+=[[exp3,tipo]]
        elif exp4[1]=="[" and exp4[2]=="[":
            exp4=exp4[1:len(exp4)-1]
            tipo=evaluarTipoLista(exp4,i)+" list"
            result+=[[exp3,tipo]]
        else:
            tipo=evaluarTipoLista(exp4,i)
            tipo=tipo.rstrip("list")
            if tipo[0]=="[" and tipo[1]=="[":
                lar=len(tipo)
                tipo=tipo[1:lar-1]
                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                result+=[[exp3,tipo]]
            else:
                tipo
                result+=[[exp3,tipo]]
    return result


    

## funcion que evalua los let sencillos

def evaluarLetSencillo():
    lista = evaluarListaListas()
    largo=len (lista)
    i=0
    lista_temp=[]
    resultado=[]
    while i!=largo:
        if lista[i][0]!="let":
            resultado+=[lista[i]]
            i+=1
        else:
            expresion= lista[i][1]
            if expresion.find("let")!=-1 or expresion.find("if")!=-1:
                resultado+=[lista[i]]
                i+=1
            else:
                pos=expresion.find("in")
                exp1=expresion[:pos]
                exp1=exp1.strip("val ")
                exp2=expresion[pos+2:]
                exp2=exp2.rstrip(" end")
                if exp1.find("val")!=-1:
                    lista_temp=evaluarVals(exp1,i,[])
                    if exp2.find("=")==-1:
                        exp5="["+exp2+"]"
                        if exp5[0]=="[" and exp5[1]!="[":
                            tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                            tipo=tipo.rstrip("list")
                            resultado+=[[exp2,tipo,1]]
                            i+=1
                        elif exp5[1]=="[" and exp5[2]=="[":
                            tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                            tipo+=" list"
                            resultado+=[[exp2,tipo,1]]
                            i+=1
                        else:
                            tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                            resultado+=[[exp2,tipo,1]]
                            i+=1
                    else:
                        exp5="["+exp2[exp2.find("=")+1:]+"]"
                        
                        if exp5[0]=="[" and exp5[1]!="[":
                            tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                i+=1
                            else:
                                resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                i+=1
                        elif exp5[1]=="[" and exp5[2]=="[":
                            tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                i+=1
                            else:
                                resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                i+=1
                        else:
                            tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                i+=1
                            else:
                                resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                i+=1
                else:
                    po= exp1.find("=")
                    exp3=exp1[:po]
                    exp4="["+exp1[po+1:]+"]"
                    if exp4[1]=="[" and exp4[2]!="[":
                        exp4=exp1[po+1:]
                        tipo=evaluarTipoLista(exp4,i)
                        lista_temp+=[[exp3,tipo]]
                        if exp2.find("=")==-1:
                            resultado+=[[exp3,tipo,1]]
                            i+=1
                        else:
                            exp5="["+exp2[exp2.find("=")+1:]+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo+=" list"
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            else:
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                    elif exp4[1]=="[" and exp4[2]=="[":
                        exp4=exp4[1:len(exp4)-1]
                        tipo=evaluarTipoLista(exp4,i)+" list"
                        lista_temp+=[[exp3,tipo]]
                        if exp2.find("=")==-1:
                            resultado+=[[exp3,tipo,1]]
                            i+=1
                        else:
                            exp5="["+exp2[exp2.find("=")+1:]+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo+=" list"
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            else:
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                    else:
                        tipo=evaluarTipoLista(exp4,i)
                        tipo=tipo.rstrip("list")
                        if tipo[0]=="[" and tipo[1]=="[":
                            lar=len(tipo)
                            tipo=tipo[1:lar-1]
                            tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("=")==-1:
                                resultado+=[[exp3,tipo,1]]
                                i+=1
                            else:
                                exp5="["+exp2[exp2.find("=")+1:]+"]"
                                if exp5[0]=="[" and exp5[1]!="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo=tipo.rstrip("list")
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                        i+=1
                                    else:
                                        resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                        i+=1
                                elif exp5[1]=="[" and exp5[2]=="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo+=" list"
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                        i+=1
                                    else:
                                        resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                        i+=1
                                else:
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                        i+=1
                                    else:
                                        resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                        i+=1

                        else:
                            tipo
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("=")==-1:
                                resultado+=[[exp3,tipo,1]]
                                i+=1
                            else:
                                exp5="["+exp2[exp2.find("=")+1:]+"]"
                                if exp5[0]=="[" and exp5[1]!="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo=tipo.rstrip("list")
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                        i+=1
                                    else:
                                        resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                        i+=1
                                elif exp5[1]=="[" and exp5[2]=="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo+=" list"
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                        i+=1
                                    else:
                                        resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                        i+=1
                                else:
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                        i+=1
                                    else:
                                        resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                        i+=1
    return resultado

## funcion que evalua el tipo del if

def tipo_if(expresion,lista,i):
    resultado=""
    exp2=expresion.find("else")
    exp3=expresion[exp2+5:]
    exp3=exp3.rstrip(" ")
    exp3="["+exp3+"]"
##    tipo=evaluarTipoLista(exp3,i)
    if exp3[0]=="[" and exp3[1]!="[":
        tipo=evaluarExpresiones(exp3,i,lista)
        tipo=tipo.rstrip("list")
        resultado+=tipo
    elif exp3[1]=="[" and exp3[2]=="[":
        tipo=evaluarExpresiones(exp3,i,lista)
        tipo+=" list"
        resultado+=tipo
    else:
        tipo=evaluarExpresiones(exp3,i,lista)
        resultado+=tipo
    return resultado

## Funcion que
def evaluarExpresionValsLet(expresion,result,lista_temporal):
    pos=expresion.find("val")
    tipo=""
    if pos!=-1:
        expr_temp=expresion[:pos-1]
        expresion=expresion[pos+4:]
        if expr_temp.find("if")==-1:
            po= expr_temp.find("=")
            exp3=expr_temp[:po]
            exp4="["+expr_temp[po+1:]+"]"
            if exp4[1]=="[" and exp4[2]!="[":
                exp4=exp1[po+1:]
                tipo=evaluarExpresiones(exp4,len(lista_temporal),lista_temporal)
                result+=[[exp3,tipo]]
                if expresion!="":
                    evaluarExpresionValsLet(expresion,result,lista_temporal)
                else:
                    result
            elif exp4[1]=="[" and exp4[2]=="[":
                exp4=exp4[1:len(exp4)-1]
                tipo=evaluarExpresiones(exp4,len(lista_temporal),lista_temporal)+" list"
                result+=[[exp3,tipo]]
                if expresion!="":
                    evaluarExpresionValsLet(expresion,result,lista_temporal)
                else:
                    result
            else:
                tipo=evaluarExpresiones(exp4,len(lista_temporal),lista_temporal)
                tipo=tipo.rstrip("list")
                if tipo[0]=="[" and tipo[1]=="[":
                    lar=len(tipo)
                    tipo=tipo[1:lar-1]
                    tipo="("+evaluarExpresiones((tipo,len(lista_temporal),lista_temporal))+")"+" list"
                    result+=[[exp3,tipo]]
                    if expresion!="":
                        evaluarExpresionValsLet(expresion,result,lista_temporal)
                    else:
                        result
                else:
                    tipo
                    result+=[[exp3,tipo]]
                    if expresion!="":
                        evaluarExpresionValsLet(expresion,result,lista_temporal)
                    else:
                        result
        else:
            exp3=expr_temp[:expr_temp.find("=")]
            exp4=expr_temp[expr_temp.find("=")+1:]
            tipo=tipo_if(exp4,lista_temporal,len(lista_temporal))
            result+=[[exp3,tipo]]
            if expresion!="":
                evaluarExpresionValsLet(expresion,result,lista_temporal)
            else:
                result
                
            
    else:
        po= expresion.find("=")
        exp3=expresion[:po]
        exp4=expresion[po+1:]
        if exp4.find("if")==-1:
            exp4="["+expresion[po+1:]+"]"
            if exp4[1]=="[" and exp4[2]!="[":
                exp4=expresion[po+1:]
                tipo=evaluarExpresiones(exp4,len(lista_temporal),lista_temporal)
                result+=[[exp3,tipo]]
            elif exp4[1]=="[" and exp4[2]=="[":
                exp4=exp4[1:len(exp4)-1]
                tipo=evaluarExpresiones(exp4,len(lista_temporal),lista_temporal)+" list"
                result+=[[exp3,tipo]]
            else:
                tipo=evaluarExpresiones(exp4,len(lista_temporal),lista_temporal)######
                tipo=tipo.rstrip("list")
                if tipo[0]=="[" and tipo[1]=="[":
                    lar=len(tipo)
                    tipo=tipo[1:lar-1]
                    tipo="("+evaluarExpresiones(tipo,len(lista_temporal),lista_temporal)+")"+" list"
                    result+=[[exp3,tipo]]
                else:
                    tipo
                    result+=[[exp3,tipo]]
        else:
            tipo=tipo_if(exp4,lista_temporal,len(lista_temporal))
            result+=[[exp3,tipo]]
    return result


#### Funcion que recibe un let y retorna el tipo del resultado

def evaluarTipoLetLet(expresion,lista_TEMP):
    lista_temp=[]
    resultado=""
    pos=expresion.find("in")
    exp1=expresion[:pos]
    exp1.strip(" ")
    exp1=exp1.strip("val ")
    exp2=expresion[pos+2:]
    exp2=exp2.strip(" ")
    exp2=exp2.rstrip(" ")
    exp2=exp2.rstrip(" end")
    if exp1.find("val")!=-1:
        lista_temp=evaluarExpresionValsLet(exp1,[],lista_TEMP)
        if exp2.find("=")==-1:
            exp5="["+exp2+"]"
            if exp5[0]=="[" and exp5[1]!="[":
                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                tipo=tipo.rstrip("list")
                if tipo=="":
                    tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)                
                    resultado+=tipo
                else:
                    resultado+=tipo
            elif exp5[1]=="[" and exp5[2]=="[":
                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                tipo+=" list"
                if tipo=="":
                    tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                    resultado+=tipo
                else:
                    resultado+=tipo
            else:
                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                if tipo=="":
                    tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                    resultado+=tipo
                else:
                    resultado+=tipo
        else:
            exp5="["+exp2[exp2.find("=")+1:]+"]"
            
            if exp5[0]=="[" and exp5[1]!="[":
                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                if tipo=="":
                    tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                    tipo=tipo.rstrip("list")
                    if exp2[:exp2.find("=")].find("val")==-1:
                        resultado+=tipo
                    else:
                        resultado+=tipo
                else:
                    tipo=tipo.rstrip("list")
                    if exp2[:exp2.find("=")].find("val")==-1:
                        resultado+=tipo
                    else:
                        resultado+=tipo
            elif exp5[1]=="[" and exp5[2]=="[":
                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                if tipo=="":
                    tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                    tipo+=" list"
                    if exp2[:exp2.find("=")].find("val")==-1:
                        resultado+=tipo
                    else:
                        resultado+=tipo
                else:
                    tipo+=" list"
                    if exp2[:exp2.find("=")].find("val")==-1:
                        resultado+=tipo
                    else:
                        resultado+=tipo         
            else:
                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                if tipo=="":
                    tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                    if exp2[:exp2.find("=")].find("val")==-1:
                        resultado+=tipo
                    else:
                        resultado+=tipo
                else:
                    if exp2[:exp2.find("=")].find("val")==-1:
                        resultado+=tipo
                    else:
                        resultado+=tipo
    else:   #############
        po= exp1.find("=")
        exp3=exp1[:po]
        exp4="["+exp1[po+1:]+"]"
        if exp4[1]=="[" and exp4[2]!="[":
            exp4=exp1[po+1:]
            tipo=evaluarTipoLista(exp4,i)
            lista_temp+=[[exp3,tipo]]
            if exp2.find("=")==-1:
                resultado+=tipo
            else:
                exp5="["+exp2[exp2.find("=")+1:]+"]"
                if exp5[0]=="[" and exp5[1]!="[":
                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                    if tipo=="":
                        tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                        tipo=tipo.rstrip("list")
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                    else:
                        tipo=tipo.rstrip("list")
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                elif exp5[1]=="[" and exp5[2]=="[":
                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                    if tipo=="":
                        tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                        tipo+=" list"
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                    else:
                        tipo+=" list"
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo  
                else:
                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                    if tipo=="":
                        tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                    else:
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
        elif exp4[1]=="[" and exp4[2]=="[":
            exp4=exp4[1:len(exp4)-1]
            tipo=evaluarTipoLista(exp4,i)+" list"
            lista_temp+=[[exp3,tipo]]
            if exp2.find("=")==-1:
                resultado+=tipo
            else:
                exp5="["+exp2[exp2.find("=")+1:]+"]"
                if exp5[0]=="[" and exp5[1]!="[":
                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                    if tipo=="":
                        tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                        tipo=tipo.rstrip("list")
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                    else:
                        tipo=tipo.rstrip("list")
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                elif exp5[1]=="[" and exp5[2]=="[":
                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                    if tipo=="":
                        tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                        tipo+=" list"
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                    else:
                        tipo+=" list"
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo 
                else:
                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                    if tipo=="":
                        tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
                    else:
                        if exp2[:exp2.find("=")].find("val")==-1:
                            resultado+=tipo
                        else:
                            resultado+=tipo
        else:
            tipo=evaluarExpresiones(exp4,len(lista_TEMP),lista_TEMP)
            tipo=tipo.rstrip("list")
            if tipo[0]=="[" and tipo[1]=="[":
                lar=len(tipo)
                tipo=tipo[1:lar-1]
                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                lista_temp+=[[exp3,tipo]]
                if exp2.find("=")==-1:
                    resultado+=tipo
                else:
                    exp5="["+exp2[exp2.find("=")+1:]+"]"
                    if exp5[0]=="[" and exp5[1]!="[":
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                    elif exp5[1]=="[" and exp5[2]=="[":
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo 
                    else:
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo

            else:
                tipo
                lista_temp+=[[exp3,tipo]] 
                if exp2.find("=")==-1:
                    exp5="["+exp2+"]"
                    if exp5[0]=="[" and exp5[1]!="[":
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                    elif exp5[1]=="[" and exp5[2]=="[":
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo 
                    else:
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                else:
                    exp5="["+exp2[exp2.find("=")+1:]+"]"
                    if exp5[0]=="[" and exp5[1]!="[":
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                    elif exp5[1]=="[" and exp5[2]=="[":
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo 
                    else:
                        tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                        if tipo=="":
                            tipo=evaluarExpresiones(exp5,len(lista_TEMP),lista_TEMP)
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
                        else:
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=tipo
                            else:
                                resultado+=tipo
    return resultado
            
            
    
                
 ## Funcion que evalua el tipo de un let dentro de otro let               
                
def evaluarLetComplejo():
    lista = evaluarLetSencillo()
    largo=len (lista)
    i=0
    lista_temp=[]
    resultado=[]
    while i!=largo:
        if lista[i][0]!="let":
            resultado+=[lista[i]]
            i+=1
        else:
            expresion= lista[i][1]
            if expresion.find("if")!=-1:
                resultado+=[lista[i]]
                i+=1
            else:
                pos=expresion.find("in")
                exp1=expresion[:pos]
                exp1=exp1.strip("val ")
                exp2=expresion[pos+2:]
                if exp2[1]=="(":
                    exp2=exp2.strip(" (")
                    exp2=exp2.strip("let ")
                    exp2=exp2.rstrip(" end)")
                    exp2=exp2.rstrip(" end")
                    if exp1.find("val")!=-1:
                        lista_temp=evaluarVals(exp1,i,[])
                        if exp2.find("let")==-1:
                            tipo=evaluarTipoLetLet(exp2,lista_temp)
                            val=exp2[exp2.find("in")+2:]
                            if val.find("val ")==-1:
                                resultado+=[["Resultado",tipo,1]]
                                i+=1
                            else:
                                val=val.strip("val ")
                                resultado+=[[val[:val.find("=")],tipo,1]]
                                i+=1
                        else:
                            aux1=exp2[:exp2.find("let")]
                            aux1=aux1.strip("(val ")
                            aux1=aux1[:aux1.find(" end")]
                            aux2=exp2[exp2.find("let")+4:]
                            aux2=aux2.strip("val ")
                            tipo1=evaluarTipoLetLet(aux1,lista_temp)
                            tipo2=evaluarTipoLetLet(aux2,lista_temp)
                            resultado+=[["Resultado",tipo1,1]]
                            i+=1
                    else:
                        po= exp1.find("=")
                        exp3=exp1[:po]
                        exp4="["+exp1[po+1:]+"]"
                        if exp4[1]=="[" and exp4[2]!="[":
                            exp4=exp1[po+1:]
                            tipo=evaluarTipoLista(exp4,i)
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:  
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[["Resultado",tipo,1]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[val[:val.find("=")],tipo,1]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[["Resultado",tipo1,1]]
                                i+=1
                        elif exp4[1]=="[" and exp4[2]=="[":
                            exp4=exp4[1:len(exp4)-1]
                            tipo=evaluarTipoLista(exp4,i)+" list"
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[["Resultado",tipo,1]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[val[:val.find("=")],tipo,1]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[["Resultado",tipo1,1]]
                                i+=1
                        else:
                            tipo=evaluarTipoLista(exp4,i)
                            tipo=tipo.rstrip("list")
                            if tipo[0]=="[" and tipo[1]=="[":
                                lar=len(tipo)
                                tipo=tipo[1:lar-1]
                                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[["Resultado",tipo,1]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[val[:val.find("=")],tipo,1]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[["Resultado",tipo1,1]]
                                    i+=1
                            else:
                                tipo
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[["Resultado",tipo,1]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[val[:val.find("=")],tipo,1]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[["Resultado",tipo1,1]]
                                    i+=1
                else:
                    exp2=exp2.strip("let ")
                    exp2=exp2.rstrip(" end")
                    if exp1.find("val")!=-1:
                        lista_temp=evaluarVals(exp1,i,[])
                        if exp2.find("let")==-1:
                            tipo=evaluarTipoLetLet(exp2,lista_temp)
                            val=exp2[exp2.find("in")+2:]
                            if val.find("val ")==-1:
                                resultado+=[["Resultado",tipo,1]]
                                i+=1
                            else:
                                val=val.strip("val ")
                                resultado+=[[val[:val.find("=")],tipo,1]]
                                i+=1
                        else:
                            aux1=exp2[:exp2.find("let")]
                            aux1=aux1.strip("(val ")
                            aux1=aux1[:aux1.find(" end")]
                            aux2=exp2[exp2.find("let")+4:]
                            aux2=aux2.strip("val ")
                            tipo1=evaluarTipoLetLet(aux1,lista_temp)
                            tipo2=evaluarTipoLetLet(aux2,lista_temp)
                            resultado+=[["Resultado",tipo1,1]]
                            i+=1
                        
                        
                    else:
                        po= exp1.find("=")
                        exp3=exp1[:po]
                        exp4="["+exp1[po+1:]+"]"
                        if exp4[1]=="[" and exp4[2]!="[":
                            exp4=exp1[po+1:]
                            tipo=evaluarTipoLista(exp4,i)
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[["Resultado",tipo,1]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[val[:val.find("=")],tipo,1]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[["Resultado",tipo1,1]]
                                i+=1
                        elif exp4[1]=="[" and exp4[2]=="[":
                            exp4=exp4[1:len(exp4)-1]
                            tipo=evaluarTipoLista(exp4,i)+" list"
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[["Resultado",tipo,1]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[val[:val.find("=")],tipo,1]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[["Resultado",tipo1,1]]
                                i+=1
                        else:
                            tipo=evaluarTipoLista(exp4,i) 
                            tipo=tipo.rstrip("list")
                            if tipo[0]=="[" and tipo[1]=="[":
                                lar=len(tipo)
                                tipo=tipo[1:lar-1]
                                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[["Resultado",tipo,1]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[val[:val.find("=")],tipo,1]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[["Resultado",tipo1,1]]
                                    i+=1
                            else:
                                tipo
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[["Resultado",tipo,1]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[val[:val.find("=")],tipo,1]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[["Resultado",tipo1,1]]
                                    i+=1
               
    return resultado        


## Funcion que evaluael tipo de una variable determina por un let sencillo

def evaluarLetSencillo2():
    lista = evaluarLetComplejo()
    largo=len (lista)
    i=0
    lista_temp=[]
    resultado=[]
    while i!=largo:
        if lista[i][1].find("let")==-1:
            resultado+=[lista[i]]
            i+=1
        else:
            expresion= lista[i][1]
            expresion=expresion[expresion.find("let")+4:]
            if expresion.find("let")!=-1 or expresion.find("if")!=-1:
                resultado+=[lista[i]]
                i+=1
            else:
                pos=expresion.find("in")
                exp1=expresion[:pos]
                exp1=exp1.strip("val ")
                exp2=expresion[pos+2:]
                exp2=exp2.rstrip(" end")
                if exp1.find("val")!=-1:
                    lista_temp=evaluarVals(exp1,i,[])
                    if exp2.find("=")==-1:
                        exp5="["+exp2+"]"
                        if exp5[0]=="[" and exp5[1]!="[":
                            tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                            tipo=tipo.rstrip("list")
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        elif exp5[1]=="[" and exp5[2]=="[":
                            tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                            tipo+=" list"
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        else:
                            tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                    else:
                        exp5="["+exp2[exp2.find("=")+1:]+"]"
                        
                        if exp5[0]=="[" and exp5[1]!="[":
                            tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                            tipo=tipo.rstrip("list")
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        elif exp5[1]=="[" and exp5[2]=="[":
                            tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                            tipo+=" list"
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        else:
                            tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                            if exp2[:exp2.find("=")].find("val")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                else:
                    po= exp1.find("=")
                    exp3=exp1[:po]
                    exp4="["+exp1[po+1:]+"]"
                    if exp4[1]=="[" and exp4[2]!="[":
                        exp4=exp1[po+1:]
                        tipo=evaluarTipoLista(exp4,i)
                        lista_temp+=[[exp3,tipo]]
                        if exp2.find("=")==-1:
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        else:
                            exp5="["+exp2[exp2.find("=")+1:]+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo+=" list"
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                    elif exp4[1]=="[" and exp4[2]=="[":
                        exp4=exp4[1:len(exp4)-1]
                        tipo=evaluarTipoLista(exp4,i)+" list"
                        lista_temp+=[[exp3,tipo]]
                        if exp2.find("=")==-1:
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        else:
                            exp5="["+exp2[exp2.find("=")+1:]+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo+=" list"
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                    else:
                        tipo=evaluarTipoLista(exp4,i)
                        tipo=tipo.rstrip("list")
                        if tipo[0]=="[" and tipo[1]=="[":
                            lar=len(tipo)
                            tipo=tipo[1:lar-1]
                            tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("=")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                exp5="["+exp2[exp2.find("=")+1:]+"]"
                                if exp5[0]=="[" and exp5[1]!="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo=tipo.rstrip("list")
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                elif exp5[1]=="[" and exp5[2]=="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo+=" list"
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                else:
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1

                        else:
                            tipo
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("=")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                exp5="["+exp2[exp2.find("=")+1:]+"]"
                                if exp5[0]=="[" and exp5[1]!="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo=tipo.rstrip("list")
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                elif exp5[1]=="[" and exp5[2]=="[":
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    tipo+=" list"
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                else:
                                    tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                    if exp2[:exp2.find("=")].find("val")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
    return resultado

## Funcion que determina el tipo de una variable que esta determinada por uno o varios lets

def evaluarLetComplejo2():
    lista = evaluarLetSencillo2()
    largo=len (lista)
    i=0
    lista_temp=[]
    resultado=[]
    while i!=largo:
        if lista[i][1].find("let ")==-1:
            resultado+=[lista[i]]
            i+=1
        else:
            expresion= lista[i][1]
            expresion= expresion[expresion.find(" val"):]
            if expresion.find("if")!=-1:
                resultado+=[lista[i]]
                i+=1
            else:
                pos=expresion.find("in")
                exp1=expresion[:pos]
                exp1=exp1.strip("val ")
                exp2=expresion[pos+2:]
                if exp2[1]=="(":
                    exp2=exp2.strip(" (")
                    exp2=exp2.strip("let ")
                    exp2=exp2.rstrip(" end)")
                    exp2=exp2.rstrip(" end")
                    if exp1.find("val")!=-1:
                        lista_temp=evaluarVals(exp1,i,[])
                        if exp2.find("let")==-1:
                            tipo=evaluarTipoLetLet(exp2,lista_temp)
                            val=exp2[exp2.find("in")+2:]
                            if val.find("val ")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                val=val.strip("val ")
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        else:
                            aux1=exp2[:exp2.find("let")]
                            aux1=aux1.strip("(val ")
                            aux1=aux1[:aux1.find(" end")]
                            aux2=exp2[exp2.find("let")+4:]
                            aux2=aux2.strip("val ")
                            tipo1=evaluarTipoLetLet(aux1,lista_temp)
                            tipo2=evaluarTipoLetLet(aux2,lista_temp)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                    else:
                        po= exp1.find("=")
                        exp3=exp1[:po]
                        exp4="["+exp1[po+1:]+"]"
                        if exp4[1]=="[" and exp4[2]!="[":
                            exp4=exp1[po+1:]
                            tipo=evaluarTipoLista(exp4,i)
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:  
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        elif exp4[1]=="[" and exp4[2]=="[":
                            exp4=exp4[1:len(exp4)-1]
                            tipo=evaluarTipoLista(exp4,i)+" list"
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        else:
                            tipo=evaluarTipoLista(exp4,i)
                            tipo=tipo.rstrip("list")
                            if tipo[0]=="[" and tipo[1]=="[":
                                lar=len(tipo)
                                tipo=tipo[1:lar-1]
                                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                tipo
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                else:
                    exp2=exp2.strip("let ")
                    exp2=exp2.rstrip(" end")
                    if exp1.find("val")!=-1:
                        lista_temp=evaluarVals(exp1,i,[])
                        if exp2.find("let")==-1:
                            tipo=evaluarTipoLetLet(exp2,lista_temp)
                            val=exp2[exp2.find("in")+2:]
                            if val.find("val ")==-1:
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                            else:
                                val=val.strip("val ")
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        else:
                            aux1=exp2[:exp2.find("let")]
                            aux1=aux1.strip("(val ")
                            aux1=aux1[:aux1.find(" end")]
                            aux2=exp2[exp2.find("let")+4:]
                            aux2=aux2.strip("val ")
                            tipo1=evaluarTipoLetLet(aux1,lista_temp)
                            tipo2=evaluarTipoLetLet(aux2,lista_temp)
                            resultado+=[[lista[i][0],tipo]]
                            i+=1
                        
                        
                    else:
                        po= exp1.find("=")
                        exp3=exp1[:po]
                        exp4="["+exp1[po+1:]+"]"
                        if exp4[1]=="[" and exp4[2]!="[":
                            exp4=exp1[po+1:]
                            tipo=evaluarTipoLista(exp4,i)
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1:  
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        elif exp4[1]=="[" and exp4[2]=="[":
                            exp4=exp4[1:len(exp4)-1]
                            tipo=evaluarTipoLista(exp4,i)+" list"
                            lista_temp+=[[exp3,tipo]]
                            if exp2.find("let")==-1: 
                                tipo=evaluarTipoLetLet(exp2,lista_temp)
                                val=exp2[exp2.find("in")+2:]
                                if val.find("val ")==-1:
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                                else:
                                    val=val.strip("val ")
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                aux1=exp2[:exp2.find("let")]
                                aux1=aux1.strip("(val ")
                                aux1=aux1.strip("val ")
                                aux1=aux1[:aux1.find(" end")]
                                aux2=exp2[exp2.find("let")+4:]
                                aux2=aux2.strip("val ")
                                aux2=aux2[:aux2.find(" end")]
                                tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                resultado+=[[lista[i][0],tipo]]
                                i+=1
                        else:
                            tipo=evaluarTipoLista(exp4,i) 
                            tipo=tipo.rstrip("list")
                            if tipo[0]=="[" and tipo[1]=="[":
                                lar=len(tipo)
                                tipo=tipo[1:lar-1]
                                tipo="("+evaluarTipoLista(tipo,i)+")"+" list"
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:  
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
                            else:
                                tipo
                                lista_temp+=[[exp3,tipo]]
                                if exp2.find("let")==-1:
                                    tipo=evaluarTipoLetLet(exp2,lista_temp)
                                    val=exp2[exp2.find("in")+2:]
                                    if val.find("val ")==-1:
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                    else:
                                        val=val.strip("val ")
                                        resultado+=[[lista[i][0],tipo]]
                                        i+=1
                                else:
                                    aux1=exp2[:exp2.find("let")]
                                    aux1=aux1.strip("(val ")
                                    aux1=aux1.strip("val ")
                                    aux1=aux1[:aux1.find(" end")]
                                    aux2=exp2[exp2.find("let")+4:]
                                    aux2=aux2.strip("val ")
                                    aux2=aux2[:aux2.find(" end")]
                                    tipo1=evaluarTipoLetLet(aux1,lista_temp)
                                    tipo2=evaluarTipoLetLet(aux2,lista_temp)
                                    resultado+=[[lista[i][0],tipo]]
                                    i+=1
               
    return resultado


## Funcion que evalua un if dentro de un val simple       
def evaluarValIf():
    lista=evaluarLetComplejo2()
    largo=len(lista)
    i=0
    resultado=[]
    tipo=""
    while i!=largo:
        if lista[i][1].find("if")!=0:
            resultado+=[lista[i]]
            i+=1
        else:
            expresion=lista[i][1]
            tipo+=tipo_if(expresion,lista,i)
            resultado+=[[lista[i][0],tipo]]
            i+=1
    return resultado
        

## funcion que evalua los let con if

def evaluarLetIfSimple():
    lista = evaluarValIf()
    largo=len (lista)
    i=0
    lista_temp=[]
    resultado=[]
    while i!=largo:
        if lista[i][0]!="let":
            resultado+=[lista[i]]
            i+=1
        else:
            expresion= lista[i][1]
            if expresion.find("let")!=-1:
                resultado+=[lista[i]]
                i+=1
            else:
                pos=expresion.find("in")
                exp1=expresion[:pos]
                exp1=exp1.strip("val ")
                exp2=expresion[pos+2:]
                exp2=exp2.rstrip(" end")
                if exp2.find("if")!=-1:
                    if exp1.find("val")!=-1:
                        lista_temp=evaluarExpresionValsLet(exp1,[],lista)
                        if exp2.find("=")!=-1:
                            exp2=exp2.strip(" val ")
                            print(exp2,"hhhhhhhhhhh")
                            exp6=exp2[:exp2.find("=")]
                            exp5=exp2[exp2.find("=")+1:]
                            tipo=tipo_if(exp5,lista_temp,len(lista_temp))   
                            resultado+=[[exp6,tipo,1]]
                            i+=1
                        else:
                            tipo=tipo_if(exp2,lista_temp,len(lista_temp))
                            resultado+=[["Resultado",tipo,1]]
                            i+=1
                    else:
                        po= exp1.find("=")
                        exp3=exp1[:po]
                        exp4=exp1[po+1:]
                        tipo=tipo_if(exp4,lista,i)
                        lista_temp+=[[exp3,tipo]]
                        if exp2.find("=")!=-1:
                            exp6=exp2[:exp2.find("=")]
                            exp5=exp2[exp2.find("=")+1:]
                            tipo=tipo_if(exp5,lista_temp,len(lista_temp))   
                            resultado+=[[exp6,tipo,1]]
                            i+=1
                        else:
                            tipo=tipo_if(exp2,lista_temp,len(lista_temp))
                            resultado+=[["Resultado",tipo,1]]
                            i+=1
                        
                else:
                    if exp1.find("val")!=-1:
                        lista_temp=evaluarExpresionValsLet(exp1,[],lista)
                        if exp2.find("=")==-1:
                            exp5="["+exp2+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                resultado+=[[exp2,tipo,1]]
                                i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                                tipo+=" list"
                                resultado+=[[exp2,tipo,1]]
                                i+=1
                            else:
                                tipo=evaluarExpresiones(exp2,len(lista_temp),lista_temp)
                                resultado+=[[exp2,tipo,1]]
                                i+=1
                        else:
                            exp5="["+exp2[exp2.find("=")+1:]+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo+=" list"
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            else:
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                    else:
                        po= exp1.find("=")
                        exp3=exp1[:po]
                        exp4=exp1[po+1:]
                        tipo=tipo_if(exp4,lista,i)
                        
                        lista_temp+=[[exp3,tipo]]
                        if exp2.find("=")==-1:
                            resultado+=[[exp3,tipo,1]]
                            i+=1
                        else:
                            exp5="["+exp2[exp2.find("=")+1:]+"]"
                            if exp5[0]=="[" and exp5[1]!="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo=tipo.rstrip("list")
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            elif exp5[1]=="[" and exp5[2]=="[":
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                tipo+=" list"
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                            else:
                                tipo=evaluarExpresiones(exp5,len(lista_temp),lista_temp)
                                if exp2[:exp2.find("=")].find("val")==-1:
                                    resultado+=[[exp2[:exp2.find("=")],tipo,1]]
                                    i+=1
                                else:
                                    resultado+=[[exp2[5:exp2.find("=")],tipo,1]]
                                    i+=1
                       

    return resultado

## Funcion que evalua el ambiente estatico e imprime la tabla

def Estatico():
    lista= evaluarLetIfSimple()
    largo= len(lista)
    i=0
    print("*************************AMBIENTE ESTÁTICO*******************************")
    print("")
    print("")
    print ("\t","\t","VARIABLE","\t","\t", "TIPO")
    print("")
    while i!=largo:
        if lista[i][0]=="Resultado":
            print ("\t","\t",lista[i][0],"\t","\t",lista[i][1])
            i+=1
        else: 
            print ("\t","\t",lista[i][0],"\t","\t","\t",lista[i][1])
            i+=1
        
    

##Funcion en cargada de administrar las diferentes expreciones que se puedan encontrar en el codigo :3
def Procesar_Exp(L):
    tabla=[]
    for i in L:
      if "+" in i or"-" in i or"*" in i or"div" in i:
        tabla += [i[4]+"  "+"-->"+(operacion(i))]
      elif i[8:11] == "True" or i[8:11] == "False":
        tabla+=[i[4]+"  "+"-->"+i[8:11]]
      elif i[8:11]!="if "and i[8:11]!= "let":
        tabla+=[i[4]+"  "+"-->"+i[8:]]
      elif i[8:11]=="if":
        return procesar_if(i)
      else:
        return precesar_let(i)
    return imprimirTab(tabla)

##def procesar_if(e):
##    return""
##def procesar_let():
##    return ""
##    for i in tabla:
##        if e[12]==i[0] and e==i[]:
            
    
##
##
def operacion(L,i=0,temp1="",temp2="",oper=""):
        L=L[8:]
        z=len(L)
        while i<z:
            
            if  oper=="" and (esnumint(L[0])==True) :
                temp1+=L[0]
                i+=1
                L=L[1:]

            elif L[0]=="+" or L[0]=="-" or L[0]=="*":
                oper+=L[0]
                i+=1
                L=L[1:]
            elif L[0:3]=="div":
                oper=oper+"div"
                i+=3
                L=L[3:]
            elif oper!="" and(esnumint(L[0]))==True:
                temp2+=L[0]
                i+=1
                L=L[1:]
            else:
                    L=L[1:]
        return(operar2num(temp1,oper,temp2))

            
            


def operar2num(a,b,c):
        if b=="+":
            return str((tonum(a)+tonum(c)))
        elif b=="-":
            return (tonum(a)-tonum(c))
        elif b=="*":
            return (tonum(a)*tonum(c))
        elif b=="div":    
            return (tonum(a)//tonum(c))
            
##            elif oper!="" and  (esnumint(L[i])==False)and L[i]==",":
##                end=False
                
                
            
           
def esnumint(s):
    try:
        int (s)
        return True
    except ValueError:
        return False

def tonum(s):
    try:
        
        return int(s)
    except ValueError:
        return False


##def convertStr(s):
## 	try:
## 		ret = int(s)
## 	except ValueError:
## 		
## 		ret = float(s)
## 	return ret
##
##
def imprimirTab(t):
    print(" Tabla Dinamica")
    print("--------------------")
    for i in t:
        print(i)
    print("--------------------")
    return ""
    


def Menu():
    print("******************BIENVENIDO******************")
    print(" ")
    print ("Digite 1 si desea ver el ambiente estático")
    print ("Digite 2 si desea ver el ambiente dinámico")
    opcion=int(input("Cual ambiente desea ver?: "))
    if opcion==1:
        print(" ")
        Estatico()
        opcion=input("Desea volver al menu? Y/N  ")
        if opcion=="Y":
            print(" ")
            print(" ")
            Menu()
        else:
            print(" ")
            print ("Gracias :D")
    else:
        print(" ")
        Procesar_Exp(leer_archivo("Codigo.txt"))
        opcion=input("Desea volver al menu? Y/N")
        if opcion=="Y":
            print(" ")
            print(" ")
            Menu()
        else:
            print(" ")
            print ("Gracias :D")

Menu()








                                
                            
