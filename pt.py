import re


#robert 'dot' colautti 'en' queensu 'dot' ca
#chris.eckert [at] queensu.ca
#lonnie.aarssen en queensu.ca

cadena = "chris.eckert [at] queensu.ca"

'''Filtros Puntos'''

m1=re.sub(" 'dot' ",".",cadena)

'''Arrobas'''

m2=re.sub(" 'en' ","@",m1)
m3=re.sub(" en ","@",m2)
m4=re.sub(f" [at] ","@",m3)


print(f"Cadena Convertida =  {m4}")


