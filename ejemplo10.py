
archivo = open("data/atp_tennis.csv","r")

lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]

num = 0 
for x in lineas[1:]:
    cadena = """<b>Torneo:</b> %s <br> <b>Ganador:</b> %s""" % (x[0],x[9])
    num = num+1
    print(cadena)
    archivo_generado = open("data/Ganador-%d-%s.html" % (num,x[9]),"w")
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close