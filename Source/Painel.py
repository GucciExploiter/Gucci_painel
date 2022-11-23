from time import sleep
from json import loads
from os import system,name

try:
    import requests
except:
    from sys import executable
    system(executable+' -m pip install requests')
    import requests

# Cores no terminal
global R,B,C,G
R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m';Y='\033[1;33m'

# pegando o ip
try:
	from requests import get
except:
	try:
		from sys import executable
		system(executable+' -m pip install requests')
		from requests import get
	except:
		print('%s[ %s!%s ] Instale manualmente o(s) módulo(s) requests.'%(C,R,C));exit()
		
try:
	ipmenu=get('https://ipwhois.app/json/').text
	ipmenu=loads(ipmenu)
	ipmenu=ipmenu['ip']
except:
	print('%s[%s ! %s] Verifique sua conexão à Internet! \n%s'%(C,R,C))
	exit()

# versao do painel
versao = 'Versão. 0.5.3'

# logos 
logo2 = ''' __________________________________________________
/________________________________________________/ |
|           %s                                     %s| |
|           %s██████╗░██╗░░░██╗███████╗          %s  | |
|           %s██╔══██╗╚██╗░██╔╝██╔════╝        %s    | |
|           %s██████╦╝░╚████╔╝░█████╗░░      %s      | |
|           %s██╔══██╗░░╚██╔╝░░██╔══╝░░    %s        | |
|           %s██████╦╝░░░██║░░░███████╗  %s          | |
|           %s╚═════╝░░░░╚═╝░░░╚══════╝%s            | |
|                                                | |
|            [%sDiscord : Gucci#2661%s]              | |
|________________________________________________|/'''%(B,C,B,C,B,C,B,C,B,C,B,C,B,C,Y,C)
logo = ''' ___________________________________________________
/_________________________________________________/ |
|   %s                                          %s    | |
|   %s██████╗░░█████╗░██╗███╗░░██╗███████╗██╗░░░░░%s  | |
|   %s██╔══██╗██╔══██╗██║████╗░██║██╔════╝██║░░░░░%s  | |
|   %s██████╔╝███████║██║██╔██╗██║█████╗░░██║░░░░░%s  | |
|   %s██╔═══╝░██╔══██║██║██║╚████║██╔══╝░░██║░░░░░%s  | |
|   %s██║░░░░░██║░░██║██║██║░╚███║███████╗███████╗%s  | |
|   %s╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚══════╝%s  | |
|                                                 | |
|                  %sGucci - Dev%s                    | |
|                 %s%s%s                   | |
|_________________________________________________|/'''%(B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,C,B,versao,C)

# tests
def clear(clean) -> None: return system(clean)
def req(api_req) -> str: return loads(get(api_req).text)


# função de fechar o painel.
def sair():
    clear(clean);print('%s\n\n[%s+%s] %s mais recente'%(logo2,G,C,versao))
    sleep(4)
    print('\n[%s!%s] Fechando Painel. Ate mais :D'%(R,C))
    sleep(5)
    clear(clean);exit()
    

# funções de consultas
def cep() -> str:
    clear(clean)
    try:
    	result=req('https://viacep.com.br/ws/'+input('%s\n\n%s>%s Digite o CEP : '%(logo,G,C))+'/json');input('\n[CEP : %s%s%s]\n[Logradouro : %s%s%s]\n[Complemento : %s%s%s]\n[Bairro : %s%s%s]\n[Localidade : %s%s%s]\n[Estado(UF) : %s%s%s]\n[IBGE : %s%s%s]\n[GIA : %s%s%s]\n[DDD : %s%s%s]\n[SIAFI : %s%s%s]\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(B,result['cep'],C,B,result['logradouro'],C,B,result['complemento'],C,B,result['bairro'],C,B,result['localidade'],C,B,result['uf'],C,B,result['ibge'],C,B,result['gia'],C,B,result['ddd'],C,B,result['siafi'],C,G,C,B,C,G,C))
    except:
        input('\n[%s ! %s] CEP invalido!\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(R,C,G,C,B,C,G,C))
    return menu()


def bank():
    clear(clean)
    result = requests.get('https://brasilapi.com.br/api/banks/v1/'+ input('%s\n\n%s> %sDigite o codigo bancario : '%(logo,G,C))).text
    result = loads(result)
    try:
        input('\n[ISPB : %s%s%s]\n[Nome : %s%s%s]\n[Código : %s%s%s]\n[Nome Completo : %s%s%s]\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(B,result['ispb'],C,B,result['name'],C,B,result['code'],C,B,result['fullName'],C,G,C,B,C,G,C))
    except:
        input('\n[%s ! %s] codigo bancario invalido!\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(R,C,G,C,B,C,G,C))
    return menu()


def bin() -> str:
    clear(clean)
    try: 
        result=req('https://lookup.binlist.net/%s'%input('%s\n\n%s>%s Digite a BIN : '%(logo,G,C)));input('\n[Tipo : %s%s%s]\n[Marca : %s%s%s]\n[Pré-Pago : %s%s%s]\n[País : %s%s%s]\n[Nome do Banco : %s%s%s]\n[Telefone : %s%s%s]\n[Cidade : %s%s%s]\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(B,result['type'],C,B,result['brand'],C,B,str(result['prepaid']),C,B,result['country']['name'],C,B,result['bank']['name'],C,B,result['bank']['phone'],C,B,result['bank']['city'],C,G,C,B,C,G,C))
    except: 
        input('\n[%s ! %s] BIN invalido!\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(R,C,G,C,B,C,G,C))
    return menu()


def ip():
    clear(clean)
    res = requests.get('https://ipwhois.app/json/'+ input('%s\n\n%s> %sDigite o ip : '%(logo,G,C))).text
    res = loads(res)
    try:
        input('\n[ip: %s%s%s]\n[success: %s%s%s]\n[type: %s%s%s]\n[continent: %s%s%s]\n[continent_code: %s%s%s]\n[Pais: %s%s%s]\n[Pais_code: %s%s%s]\n[Pais_phone: %s%s%s]\n[region: %s%s%s]\n[Cidade: %s%s%s]\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(B,res['ip'],C,B,res['success'],C,B,res['type'],C,B,res['continent'],C,B,res['continent_code'],C,B,res['country'],C,B,res['country_code'],C,B,res['country_phone'],C,B,res['region'],C,B,res['city'],C,G,C,B,C,G,C))
    except:
        input('\n[%s ! %s] IP invalido!\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(R,C,G,C,B,C,G,C))
    return menu()


def cnpj() -> str:
    clear(clean)
    res2 = requests.get('https://api-publica.speedio.com.br/buscarcnpj?cnpj='+ input('%s\n\n%s> %sDigite o CNPJ : '%(logo,G,C))).text
    res2 = loads(res2)
    try:
        input('\n[NOME FANTASIA: %s%s%s]\n[RAZAO SOCIAL: %s%s%s]\n[CNPJ: %s%s%s]\n[STATUS: %s%s%s]\n[CNAE PRINCIPAL DESCRICAO: %s%s%s]\n[CNAE PRINCIPAL CODIGO: %s%s%s]\n[CEP: %s%s%s]\n[DATA ABERTURA: %s%s%s]\n[DDD: %s%s%s]\n[TELEFONE: %s%s%s]\n[EMAIL: %s%s%s]\n[COMPLEMENTO: %s%s%s]\n[BAIRRO: %s%s%s]\n[MUNICIPIO: %s%s%s]\n[UF: %s%s%s]\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(B,res2['NOME FANTASIA'],C,B,res2['RAZAO SOCIAL'],C,B,res2['CNPJ'],C,B,res2['STATUS'],C,B,res2['CNAE PRINCIPAL DESCRICAO'],C,B,res2['CNAE PRINCIPAL CODIGO'],C,B,res2['CEP'],C,B,res2['DATA ABERTURA'],C,B,res2['DDD'],C,B,res2['TELEFONE'],C,B,res2['EMAIL'],C,B,res2['COMPLEMENTO'],C,B,res2['BAIRRO'],C,B,res2['MUNICIPIO'],C,B,res2['UF'],C,G,C,B,C,G,C))
    except:
        input('\n[%s ! %s] CNPJ invalido!\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(R,C,G,C,B,C,G,C))
    return menu()

# menu das apis
def apis():
    clear(clean)
    input('%s\n\n%s================== |%s Lista de APIs %s| ===================%s\n[%s1%s] https://api-publica.speedio.com.br/buscarcnpj?cnpj=\n[%s2%s] https://ipwhois.app/json/\n[%s3%s] https://lookup.binlist.net/\n[%s4%s] https://viacep.com.br/ws/\n[%s5%s] https://brasilapi.com.br/api/banks/v1\n%s========================================================%s\n\n%s> %s| %sAperte enter para voltar ao menu %s|%s <%s'%(logo,B,G,B,C,G,C,G,C,G,C,G,C,G,C,B,C,G,C,B,C,G,C))
    return menu()



MatchCase={
'1':cnpj,
'2':ip,
'3':bin,
'4':cep,
'5':bank
}
MatchCase_Function={
'98':apis,
'99':sair
}

# menu do painel
def menu():
    clear(clean)
    option = str(input('''%s

[ %sSeu ip %s: %s%s%s ]

[%s Discord %s: %sGucci#2661%s ]
 _________________________
|      [%sConsultas%s]        |
|-------------------------|
| [ %s1%s ] Consulta CNPJ     |
| [ %s2%s ] Consulta IP       |
| [ %s3%s ] Consulta BIN      |
| [ %s4%s ] Consulta CEP      |
| [ %s5%s ] Consulta BANK     |
|-------------------------|
| [ %s98%s ] Apis             |
| [ %s99%s ] Sair             |
|_________________________|

%sSelect >>>%s '''%(logo,B,C,B,ipmenu,C,B,C,B,C,B,C,G,C,G,C,G,C,G,C,G,C,Y,C,R,C,B,C)))
    
    try:
        MatchCase[option]()
    except Exception:
        try:
            MatchCase_Function[option]()
        except Exception:
            menu()

if __name__ == '__main__':
	global clean
	clean ={'nt':'cls','posix':'clear'}[name]
	menu()