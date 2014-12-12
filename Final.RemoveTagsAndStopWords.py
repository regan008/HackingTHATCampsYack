import os, sys
import rmv

x = 2
while x < 300:

	try:
		f = open('wp_' + str(x) + '_posts.txt', 'r')
		content = f.read()
		words = rmv.stripTags(content).lower()
		fullwordlist = rmv.stripNonAlphaNum(words)
		wordlist = rmv.removeStopwords(fullwordlist, rmv.stopwords)
		fo = open('wp_' + str(x) + '_posts.txt', 'w')
		fo.write('\n' .join(wordlist))

	except Exception:
		sys.exc_clear()

	x += 1

