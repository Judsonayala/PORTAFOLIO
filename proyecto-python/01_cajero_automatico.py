#cliente retira de su cuenta saldo y el cajero debe dar dinero en multiplos de 20
#y verificar que tenga saldo suficiente 
saldo_cuenta = 500.00
BILLETE_BASE = 20

monto_retiro_str = input("ingrese el monto a retirar:")
try:
    monto_retiro = float(monto_retiro_str)
except ValueError:
  print("ingrese un numero valido")
  exit()
if monto_retiro > 0 and monto_retiro %BILLETE_BASE==0:
 if monto_retiro <= saldo_cuenta:
   saldo_cuenta = saldo_cuenta - monto_retiro
   print("monto retiro de",monto_retiro)
   print("su saldo es de:",saldo_cuenta)
 else:
   print("ERROR: saldo insuficiente")
else:
  print("monto no valido")
  print("debe ser multiplo de:",BILLETE_BASE)