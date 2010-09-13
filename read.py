#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import Connection
from pymongo.binary import Binary
import String

connection = Connection()
db = connection.cet

def proj(openfile):
	f = open('file/%s' % openfile,'r')
	for line in f:
		inline = line.split(",")
		insertproj ={"nproject":inline[0],
					"startnumeric":inline[1],
					"endnumeric":inline[2],
					"startindcard":inline[3],
					"endindcard":inline[4],
					"nameproject":Binary(inline[5]),
					"other1":inline[6],
					"other2":inline[7]}
		proj = db.proj
		proj.insert(insertproj)
	f.close()
		
def p(openfile):
	f = open('file/%s' % openfile,'r')
	for line in f:
		print line[0:5]
		
def label(openfile):
	f = open('file/%s' % openfile,'r')
	for line in f:
		print line[0:5]
#proj("PROJ.txt")
#p("p4548.dat")