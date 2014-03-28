#!/usr/bin/python
import sys

PI = 3.1415926535897931159979634685441852
def funcion(n):
   suma=0.0
   for i in range(1,n+1):
     x_i=float(i-1.0/2)/n     
     fx_i= 4.0/(1+x_i**2)
     suma=suma+fx_i
   pi = (1.0/float(n))*suma
   return PI
def error(nro_intervalos, n_test, umbral):
   intervalo = nro_intervalos
   lista = []
for i in range (nro_test):
   valor_pi = funcion (intervalo)
   intervalo += nro_intervalos
   lista.append (valor_PI)
   pi35 = []
for i in range (nro_test):
   pi35.append (PI35DT)
   dif35 = []
for i in range (nro_test):
   dif35.append (abs(pi35[i] - lista[i]))
   correcto = 0
if (dif35[i] <= umbral):
   correcto = correcto + 1
   porcentaje = 100.0 * (1.0 - (float(correcto) / float(nro_test)))
   return (porcentaje)
if __name__ == "__main__":
   argumentos = sys.argv[1:]  
if (len(argumentos) == 3):
   n = int (argumentos[0])
   aproximaciones = int (argumentos[1])
   umbral = float (argumentos[2])
else:
    print "Introduzca el numero de intervalos (n > 0):"
    n = int (raw_input ());
    print "Introduzca el numero de aproximaciones:"
    aproximaciones = int (raw_input ());
    print "Introduzca el umbral de error:"
    umbral = float (raw_input ());
if (n > 0):
   porcentaje = error (n, aproximaciones, umbral)
   print "El porcentaje de fallos es del ", porcentaje
else:
   print "El valor de los intervalos debe ser mayor que 0"    
for repeticion in range(1,veces+1):
     zpi = funcion(n)
     z = z+[zpi]
     resta = funcion(n) - PI
     print'%d %1.35f | %1.35f | %1.35f' % (repeticion, PI, funcion(n), resta)
     n = n*2
     print z

   