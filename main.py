from os import execl, system,name
from sys import executable, argv
from time import sleep

def clear(clean) -> None: return system(clean)
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m';Y='\033[1;33m'

clean ={'nt':'cls','posix':'clear'}[name]
clear(clean)

try:
    from requests import get
except:
    system('python -m pip install --upgrade pip')
    execl(executable, executable, *argv)
try:
    print('[%s+%s] Olá bem vindo ao Painel.\n[%s+%s] Antes de continuar o painel ainda esta incompleto ;-;\n[%s+%s] pretendo atualizar ele quando tiver tempo\n[%s+%s] Se vc tiver alguma api manda ai po\n[%s-%s]Discord: Gucci#2661'%(G,C,G,C,G,C,G,C,Y,C))
    input('\n%s> %s| %sAperte enter para continuar %s|%s <%s'%(G,C,B,C,G,C))
    exec(get('https://raw.githubusercontent.com/GucciExploiter/Gucci_painel/main/Source/open.py').text)
except Exception:
    print('\n[%s!%s] Verifique sua conexão com a internet!'%(R,C))
