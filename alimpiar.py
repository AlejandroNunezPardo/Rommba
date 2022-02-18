#----------------------------------------------  
# FUNCIONES  
#----------------------------------------------  
  
def calculoDeLaSuperficieALimpiar(listaDeZonas):  
   superficieALimpiar = 0  
   for zona in listaDeZonas:
       largo = zona.get("largo")/100  
       ancho = zona.get("ancho")/100  
       calculo = largo*ancho  
       print (str(largo)+" x "+str(ancho)+"= "+str(calculo))  
       superficieALimpiar = superficieALimpiar +calculo  
   return (superficieALimpiar)  
  
#----------------------------------------------  
# APLICACIÓN  
#---------------------------------------------- 
