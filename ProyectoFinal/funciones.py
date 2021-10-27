import pandas as pd
from dfply import *
import re

def getting(df, grupos):
    current = {}
    
    for i in grupos.index:
        print(i)
        articulo = pd.read_html(grupos.iloc[i][1])
        articulo = articulo[13]
        articulo = articulo.iloc[1: ,1]
        grupo = grupos.iloc[i][0]
        current.update(producto = articulo, grupo = grupo)
        df = df.append(pd.DataFrame(current))
    
    return df
    
def cleaning(df):
    #x = df.iterrows()
    #tipo_de_producto
    #tipo_de_producto = x
    tipo_de_producto = df["producto"].str.split('.- ', n=1, expand=True)
    tipo_de_producto.columns = ['productos', 'tipo_de_producto']
    tipo_de_producto = tipo_de_producto["tipo_de_producto"].str.split(':',n=1,expand=True)
    tipo_de_producto.columns = ['tipo_de_producto', 'productos']
    tipo_de_producto = tipo_de_producto.drop(['productos'], axis=1)
    df = pd.concat([df, tipo_de_producto], axis=1)
    
    #titulo
    #titulo = x
    titulo = df["producto"].str.split(': ', n=1, expand=True)
    titulo.columns = ['productos', 'titulo']
    titulo = titulo["titulo"].str.split(',.*',n=1,expand=True)
    titulo.columns = ['titulo', 'a']
    titulo = titulo.drop(['a'], axis=1)
    titulo = titulo["titulo"].str.split('  ',n=1,expand=True)
    titulo.columns = ['titulo', 'pais_revista']
    df = pd.concat([df, titulo], axis=1)
    
    #revista
    #revista = df.iterrows()
    revista = df["producto"].str.split(', ', n=1, expand=True)
    revista.columns = ['a', 'revista']
    revista = revista.drop(['a'], axis=1)
    revista = revista["revista"].str.split(' ISSN.*',n=1,expand=True)
    revista.columns = ['a', 'revista']
    revista.columns = ['revista', 'a']
    revista = revista.drop(['a'], axis=1)
    df = pd.concat([df, revista], axis=1)
    
    #ISSN
    #issn = x
    issn = df["producto"].str.split('ISSN: ', expand=True)
    issn.columns = ['a', 'issn']
    issn = issn["issn"].str.split(',',n=1,expand=True)
    issn.columns = ['issn', 'a']
    issn = issn.drop(['a'], axis=1)
    df = pd.concat([df, issn], axis=1)
    
    #año
    #ano = x
    ano = df["producto"].str.split('ISSN: ', expand=True)
    ano.columns = ['a', 'ano']
    ano = ano["ano"].str.split(', ',n=1,expand=True)
    ano.columns = ['a', 'ano']
    ano = ano["ano"].str.split(' ',n=1,expand=True)
    ano.columns = ['ano', 'a']
    ano = ano.drop(['a'], axis=1)
    df = pd.concat([df, ano], axis=1)
    
    #volumen
    #vol = x
    vol = df["producto"].str.split('vol:', expand=True)
    vol.columns = ['a', 'vol']
    vol = vol["vol"].str.split(' .*',n=1,expand=True)
    vol.columns = ['vol', 'a']
    vol = vol.drop(['a'], axis=1)
    df = pd.concat([df, vol], axis=1)
    
    #fasc
    #fasc = x
    fasc = df["producto"].str.split('fasc: ', expand=True)
    fasc.columns = ['a', 'fasc']
    fasc = fasc["fasc"].str.split(' .*',n=1,expand=True)
    fasc.columns = ['fasc', 'a']
    fasc = fasc.drop(['a'], axis=1)
    df = pd.concat([df, fasc], axis=1)
    
    #pags
    #pags = x
    pags = df["producto"].str.split('págs: ', expand=True)
    pags.columns = ['a', 'pags']
    pags = pags["pags"].str.split(', .*',n=1,expand=True)
    pags.columns = ['pags', 'a']
    pags = pags.drop(['a'], axis=1)
    df = pd.concat([df, pags], axis=1)
    
    #doi
    #doi = x
    doi = df["producto"].str.split('DOI:', expand=True)
    doi.columns = ['a', 'doi','b']
    doi = doi["doi"].str.split(' Aut.*',n=1,expand=True)
    doi.columns = ['doi', 'a',]
    doi = doi.drop(['a'], axis=1)
    df = pd.concat([df, doi], axis=1)
    
    #autores 
    #autor = x
    autor = df["producto"].str.split('Autores: ', expand=True)
    autor.columns = ['a', 'autor']
    autor = autor.drop(['a'], axis=1)
    df = pd.concat([df, autor], axis=1)  

    return df   

def exportar(x1,x2):
    
    x1.to_csv('ucla.csv', header=True, index=False)
    x2.to_csv('comparar.csv', header=True, index=False)