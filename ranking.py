from wsgiref.handlers import CGIHandler

import os
import sqlite3

def include(filename):
	if os.path.exists(filename): 
		execfile(filename)
		
def main():
	print 'Content-type: text/html'
	print '<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">'
    print '<p>TOP 5</p>'
	print '<table width="380" border="0">'
	print '<tr>'
    print '<td width="89">Posição</td>'
    print '<td width="142">Nome</td>'
    print '</tr>'
    resultado = ranking2()
    escrever_ranking(resultado)
    print '</table>'

def escrever_ranking(resultado):
	for i in range(len(resultado)):
		posicao = i + 1
		print '<td>' + posicao + '</td>'
		print '<td>' + resultado[i] + '</td>'


def ranking2():
	posicao = 1
	resultado = []
	conn = sqlite3.connect('storage.db')
	elementos = """SELECT nome FROM classifica JOIN estabelecimentos ON classifica.id_est=estabelecimentos.id_est WHERE id_ranking = 2 ORDER BY posicao Limit 10"""
	if elementos == "":
		conn.close()
		print("Conexão perdida")
	else:
		for i in range(len(row)):
			resultado[i] = row[i]
	return resultado


if __name__ == '__main__':
    main()
