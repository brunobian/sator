import pandas as pd 

def largoYreverso(x,Palabras):
    return (len(x)==5) and (x[::-1] in Palabras)

# cargo dos diccionarios y los junto
df = pd.read_csv('./TodasPals.csv')
Palabras = df.Palabra.tolist()
df = pd.read_csv('subtitles_sa_constraints_out.csv',sep="\t")
Palabras += df.word.tolist()

# dejo solo las que son de 5 letras y su reverso significa algo
pals5 = [x for x in Palabras if (largoYreverso(x,Palabras)) ] 
pals5 = list(set(pals5))

# Busco las centrales como aquellas que son palíndromas
centrales = [x for x in pals5 if (x[0]==x[-1] and x[1]==x[-2])]

# Para cada central busco sus posibles primeras
primeras={}
for c in centrales:
    primeras[c]=[]    
    for p in pals5:
        if (c[0] == p[2]):
            primeras[c].append(p)

# Para cada combinación de central y primera, busco las segundas
segundas={}
for c in primeras.keys():
    for p in primeras[c]:
        segundas[(c,p)]=[]
        for t in pals5:
            if t[0]==p[1] and t[2]==c[1] and t[4]==p[3]:
                segundas[(c,p)].append(t)

# Imprimo lo que encontré
for c in segundas.keys():
    #print(c)
    for v in segundas[c]:
        print(c[1],v,c[0],v[::-1],c[1][::-1])
    
