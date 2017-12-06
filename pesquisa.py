from wsgiref.handlers import CGIHandler

import os
import sqlite3

def include(filename):
	if os.path.exists(filename): 
		execfile(filename)

def main():
	print '<form action="{{ url_for('"pesquisa"')}}" method="POST">'
	print '<input type="text" id="pesquisa" name="pesquisa">'
	print '<input type="submit" id="conf_pesquisa" name="conf_pesquisa">'
	print '</form>'

@app.route("/pesquisa", methods=['POST'])
def pesquisa():
	if request.method == "POST":
		pequisa = request.form.get("pesquisa")
	search = """SELECT nome,foto,descricao FROM estabelecimentos JOIN fotos ON estabelecimentos.id_est=fotos.id_est WHERE nome LIKE """pesquisa""" LIMIT 5"""
	