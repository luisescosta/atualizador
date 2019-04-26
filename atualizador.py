'''
		Atualizador.py
	Date:	16/05/2018 1.0
	Date:	25/04/2019 1.1 - Add config.ini
	By: 	LuisSilva
	Git:	github.com/luiseduardosilva
	Py: 	3.x 
'''
import os, time, configparser, shutil
from datetime import datetime

print("""\r
	   _   _               _ _              _            
	  /_\ | |_ _   _  __ _| (_)______ _  __| | ___  _ __ 
	 //_\\\\| __| | | |/ _` | | |_  / _` |/ _` |/ _ \| '__|
	/  _  \ |_| |_| | (_| | | |/ / (_| | (_| | (_) | |   
	\_/ \_/\__|\__,_|\__,_|_|_/___\__,_|\__,_|\___/|_|   
	                                                      
	        \n\t\tBy: LuisSilva 25/04/2019 - v1.1                                       
	""")

# CONFIG.INI
config = configparser.ConfigParser()

# LISTA DE CONEXÕES
diretorios = []

# RETORNAR LISTA DE CONEXÕES
def getDiretorios():
	return (diretorios)

# GERAR ARQUIVO CONFIG.INI PADRÃO
def criarIni():
	
	try:
		# CRIAR ARQUIVO
		cfgfile = open("config.ini",'w')
		
		# ADD CAMPOS
		config.add_section('Default')
		
		# DIRETORIOS
		config.set('Default','origem','\\\\192.168.1.1\\repositorio')
		config.set('Default','destino', 'C:\\Sistema')
			
		config.write(cfgfile)
		cfgfile.close()

	except Exception as e:
		print(e)
		time.sleep(10)

# MOVER ARQUIVOS
def lerArquivos(diretorioRede, diretorioPc):
	arquivos = []
	for root, dirs, files in os.walk(diretorioPc, topdown=False):
		for name in files:
			replaceDirPc = os.path.join(root, name).replace(diretorioPc, "")
			arquivos.append(replaceDirPc)
	for root, dirs, files in os.walk(diretorioRede, topdown=False):
		for name in files:
			replaceDirRede = os.path.join(root, name).replace(diretorioRede, "")
			if replaceDirRede in arquivos:
				dirRede	= os.path.join(root, name)
				#dirRede = diretorioRede+dirRede
				dirPc = diretorioPc+os.path.join("\\",name)
				if os.stat(dirRede).st_mtime > os.stat(dirPc).st_mtime:
					data = datetime.fromtimestamp(os.stat(dirRede).st_mtime)
					shutil.copy2(dirRede, dirPc)
					print("-> ARQUIVO/PROGRAMA:", name, "FOI ATUALIZADO! DATA:", data.strftime("%d/%m/%y - %H:%M:%S"))

try:
	config.read('config.ini')
	cont = 0
	
	for x in config.sections():
		b ={
			'origem' 		: config[x]['origem'],
			'destino' 		: config[x]['destino']}
		diretorios.append(b)
	
	if not (os.path.isfile('config.ini')):
		print("GERANDO CONFIG.INI PADRAO")
		criarIni()
	for x in getDiretorios():
		if ((os.path.exists(x['destino']))):
			if ((os.path.exists(x['origem']))):
				print("DIRETORIO_REDE[OK]\nDIRETORIO_PC[OK]")
				lerArquivos(x['origem'], x['destino'])
				time.sleep(3);
			else:
				print("DIRETORIO_REDE[OK]\nDIRETORIO_PC[NO]")
				time.sleep(10);
		else:
			print("[$ ERRO $]\nDIRETORIO_PC[NO]")
			time.sleep(10);

except configparser.DuplicateOptionError:
	print('CAMPO DUPLICADO EM CONFIG.INI')
	time.sleep(10)
	exit()
except Exception as e:
	raise (e)
	time.sleep(10)