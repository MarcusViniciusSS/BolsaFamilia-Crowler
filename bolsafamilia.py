import wget
import os,errno


matriz = {}
matriz[2017] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz[2016] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz[2015] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz[2014] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
matriz[2013] = {"01","02","03","04","05","06","07","08","09","10","11","12"}
ano = {}

for ano in matriz:
    for mes in matriz[ano]:
      directory = "./Bolsafamilia/Pagamento/ANO/MES/"
      url = "http://arquivos.portaldatransparencia.gov.br/downloads.asp?a="+str(ano)+"&m="+mes+"&consulta=BolsaFamiliaFolhaPagamento"
      directory = directory.replace("ANO",str(ano))
      directory = directory.replace("MES",mes)
      arquivo = str(ano)+mes+"Pagamento.zip"
      try:  
        print " Novo Diretorio Criado :"+directory
        print "######Fazendo o donwload do arquivo do link("+url+")#######"
        os.makedirs(directory)
      except OSError as e:
          if e.errno != errno.EEXIST:
            raise "Ja existe este diretorio : "+directory
      filename = wget.download(url,directory+arquivo)