import pandas as pd


df = pd.DataFrame()

df['productos'] = ['1.- Publicado en revista especializada: Machine learning based analysis of speech dimensions in functional oropharyngeal dysphagia  Países Bajos, Computer Methods and Programs in Biomedicine ISSN: 0169-2607, 2021 vol:208 fasc: N/A págs: 1 - 22, DOI:10.1016/j.cmpb.2021.106248  Autores: SEBASTIAN ROLDAN VASCO, ANDRES FELIPE OROZCO DUQUE, JUAN RAFAEL OROZCO ARROYAVE']
x = df.iterrows()

#tipo_de_producto
tipo_de_producto = x
tipo_de_producto = df["productos"].str.split('.- ', n=1, expand=True)
tipo_de_producto.columns = ['productos', 'tipo_de_producto']
tipo_de_producto = tipo_de_producto["tipo_de_producto"].str.split(':',n=1,expand=True)
tipo_de_producto.columns = ['tipo_de_producto', 'productos']
tipo_de_producto = tipo_de_producto.drop(['productos'], axis=1)
df = pd.concat([df, tipo_de_producto], axis=1)

#titulo
titulo = x
titulo = df["productos"].str.split(': ', n=1, expand=True)
titulo.columns = ['productos', 'titulo']
titulo = titulo["titulo"].str.split(',.*',n=1,expand=True)
titulo.columns = ['titulo', 'a']
titulo = titulo.drop(['a'], axis=1)
titulo = titulo["titulo"].str.split('  ',n=1,expand=True)
titulo.columns = ['titulo', 'pais_revista']
df = pd.concat([df, titulo], axis=1)

#revista
revista = df.iterrows()
revista = df["productos"].str.split(', ', n=1, expand=True)
revista.columns = ['a', 'revista']
revista = revista.drop(['a'], axis=1)
revista = revista["revista"].str.split(' ISSN.*',n=1,expand=True)
revista.columns = ['a', 'revista']
revista.columns = ['revista', 'a']
revista = revista.drop(['a'], axis=1)
df = pd.concat([df, revista], axis=1)

#ISSN
issn = x
issn = df["productos"].str.split('ISSN: ', expand=True)
issn.columns = ['a', 'issn']
issn = issn["issn"].str.split(',',n=1,expand=True)
issn.columns = ['issn', 'a']
issn = issn.drop(['a'], axis=1)
df = pd.concat([df, issn], axis=1)

#año
ano = x
ano = df["productos"].str.split('ISSN: ', expand=True)
ano.columns = ['a', 'ano']
ano = ano["ano"].str.split(', ',n=1,expand=True)
ano.columns = ['a', 'ano']
ano = ano["ano"].str.split(' ',n=1,expand=True)
ano.columns = ['ano', 'a']
ano = ano.drop(['a'], axis=1)
df = pd.concat([df, ano], axis=1)

#volumen
vol = x
vol = df["productos"].str.split('vol:', expand=True)
vol.columns = ['a', 'vol']
vol = vol["vol"].str.split(' .*',n=1,expand=True)
vol.columns = ['vol', 'a']
vol = vol.drop(['a'], axis=1)
df = pd.concat([df, vol], axis=1)

#fasc
fasc = x
fasc = df["productos"].str.split('fasc: ', expand=True)
fasc.columns = ['a', 'fasc']
fasc = fasc["fasc"].str.split(' .*',n=1,expand=True)
fasc.columns = ['fasc', 'a']
fasc = fasc.drop(['a'], axis=1)
df = pd.concat([df, fasc], axis=1)

#pags
pags = x
pags = df["productos"].str.split('págs: ', expand=True)
pags.columns = ['a', 'pags']
pags = pags["pags"].str.split(', .*',n=1,expand=True)
pags.columns = ['pags', 'a']
pags = pags.drop(['a'], axis=1)
df = pd.concat([df, pags], axis=1)

#doi
doi = x
doi = df["productos"].str.split('DOI:', expand=True)
doi.columns = ['a', 'doi']
doi = doi["doi"].str.split('  .*',n=1,expand=True)
doi.columns = ['doi', 'a']
doi = doi.drop(['a'], axis=1)
df = pd.concat([df, doi], axis=1)

#autores 
autor = x
autor = df["productos"].str.split('Autores: ', expand=True)
autor.columns = ['a', 'autor']
autor = autor.drop(['a'], axis=1)
df = pd.concat([df, autor], axis=1)

