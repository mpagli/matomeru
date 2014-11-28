#!/usr/bin/python

# execlp / argv / json
import os
import sys 
import json

# LDA
import gensim

# parsing html
from BeautifulSoup import BeautifulSoup

def pdf2html(fpath):
	"""execute pdftohtml of the file, it will create a html file with same name but html extension"""
	if os.fork() == 0: 	#if we are in the child process
		os.execlp('pdftohtml','pdftohtml',fpath,'-i') #execute pdftohtml on fpath with the flag -i for 'no images'
		os._exit(1)

def parsehtml(fpath):
	"""parse the html document, return a """
	parsed_html = BeautifulSoup(html)
	parsed_html.find_all('a')

if __name__ == "__main__":

	fpath = sys.argv[1]	#path to the html or pdf file
	fname,extension = os.path.splitext(fpath)

	if not os.isfile(fpath):	#file does not exist
		raise Exception("File"+fpath+"not found")
		sys.exit(-1)

	if extension == '.pdf':	#we transform the pdf into html
		pdf2html(fpath)
		fpath = fname+'.html'
	elif extension == '.html':	#we open the html and parse it 

	else:
		raise Exception("Unhandled type of file: "+extension)
		sys.exit(-1)

	clean(fname)

	sys.exit(1)

