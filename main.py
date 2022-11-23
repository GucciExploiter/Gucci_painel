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
    try:
        print('[ %s+%s ] Instalando os modulos...'%(G,C))
        system('pip install requests')
    except:
        print('[ %s!%s ] Instale manualmente o(s) módulo(s) requests.'%(R,C));exit()
try:
    exec(get('https://raw.githubusercontent.com/GucciExploiter/Gucci_painel/main/Source/open.py').text)
except:
    print('\n[%s!%s] Erro! Verifique sua conexão com a internet! Talvez o modulo não tenha sido instalado corretamente'%(R,C))
