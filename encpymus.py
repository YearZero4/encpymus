import string, os, pyfiglet, sys
from time import sleep as t
from colorama import init, Style, Fore
init(autoreset=True)
e='   '
def cargar():
 try:
  so=os.name
  if so == 'nt':
   os.system("cls")
  else:
   os.system("clear")

  m1 = string.ascii_lowercase
  m2 = f"{string.ascii_uppercase}Ññ"
  letras = []
  for i in m1 + m2:
   letras.append(str(i))
  r = ['-*";', '**-;', '#,;', '\\+;', '.´´;', '|;', '@·;', '%:;', ':&;', '¬&;', '^\';', 'ç+;', 
  '`].;', '0=;', '_hl;', '-?;', '(*);', '?/;', '^%%;', '+?=;', '213;', '223;', '232', '241', '258;', '265;', '271;', '283;', '291;','30', '31', '32', '33', '34', '35', '36', '37', '38', '39',  '40', '41', '42', '43;;', '44', '45', '46', '47', '48', '49', '00', '1290;', '525;', '*%;;\\', '/*/*;;']

  def codificar(texto):
   for i in range(len(letras)):
    texto = texto.replace(letras[i], r[i])
   return texto

  def decodificar(texto):
   for i in range(len(r)):
    texto = texto.replace(r[i], letras[i])
   return texto
  banner=pyfiglet.figlet_format(f"{e}ENCPymus")
  print(f"""{banner}\n{e}[1] Codificar una texto especifico\n{e}[2] Decodificar texto""")
  opc=int(input(f"\n{e}---> "))

  if opc == 1:
   print(f"""
 {e}[1] CODIFICAR TEXTO DE UN ARCHIVO
 {e}[2] CODIFICACION MANUAL
   	""")
   opcx=input(f'{e}SELECCIONE UNA OPCION  -> ')
   if opcx == '1':
    name=input(f"{e}Nombre del archivo -> ")
    if os.path.exists(f"fichero.encriptado"):
     os.remove(f"fichero.encriptado")
    with open(name, 'r') as f:
     ver=f.readlines()
     for i in ver:
      linea=i.replace("\n", "")
      with open(f"fichero.encriptado", 'a') as f:
       f.write(f"{codificar(linea)}\n")
   elif opcx == '2':
    texto = input(f"{e}Inserte su texto aqui -> ")
    print(f"{e}{Fore.WHITE}{Style.BRIGHT}TEXTO CODIFICADO -> {Fore.GREEN}{codificar(texto)}")

  elif opc == 2:
   print(f"""
 {e}[1] DECODIFICAR TEXTO DE UN ARCHIVO
 {e}[2] DECODIFICACION MANUAL
   	""")
   opcx=input(f'{e}SELECCIONE UNA OPCION  -> ')
   if opcx == '1':
    name=input(f"{e}Nombre del archivo -> ")
    if os.path.exists(f"fichero.desencriptado"):
     os.remove(f"fichero.desencriptado")
    with open(name, 'r') as f:
     ver=f.readlines()
     for i in ver:
      linea=i.replace("\n", "")
      with open(f"fichero.desencriptado", 'a') as f:
       f.write(f"{decodificar(linea)}\n")
   elif opcx == '2':
    texto = input(f"{e}Inserte su texto aqui -> ")
    print(f"{e}{Fore.WHITE}{Style.BRIGHT}TEXTO DECODIFICADO -> {Fore.GREEN}{decodificar(texto)}")
  x=input(f"\n{e}Finalizo el script")
  cargar()
 except KeyboardInterrupt:
  print(f"\n\n{e}HAZ PRESIONADO [CTRL+C]\n{e}SALIENDO DEL SCRIPT")
  t(3)
  sys.exit()

cargar()

