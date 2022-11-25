from requests import get
from os import system, name
global R,B,C,G
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m'
def clear(clean) -> None: return system(clean)
clean ={'nt':'cls','posix':'clear'}[name]
clear(clean)
try:
    print('[%s+%s] Bem Vindo(a) ao Painel O painel\n[%s+%s] Este painel nao ira receber mais updates\n[%s+%s] Talvez as APIs nao funcionem mais\n[%s-%s] Discord: Gucci#2661'%(G,C,G,C,G,C,B,C))
    input('\n%s> %sPress enter para continuar%s <%s'%(G,B,G,C))
    exec(get('https://raw.githubusercontent.com/GucciExploiter/Gucci_painel/main/Source/Painel.py').text)
except Exception:
    print('[ %s!%s ] Erro em carregar o painel tente novamente.'%(R,C))
