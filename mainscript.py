#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import os

x = 1
while x < 350:
	table= 'wp_' + str(x) + '_posts'
	query= "SELECT post_content FROM "+ str(table) + " WHERE post_status = 'publish' AND post_type = 'post'"



# save as file
	f = open('wp_' + str(x) + '_posts.txt', 'a')
	try:
		con = mdb.connect(host="", port=, user="", passwd="", db="");


		cur = con.cursor()
		cur.execute(str(query))

		rows = cur.fetchall()

	   # for row in rows:
		  # print row

		for row in rows:
			line = str(row)
			f.write(line +'\n')
	except:
		os.remove('wp_' + str(x) + '_posts.txt')
		f.close
	x += 1