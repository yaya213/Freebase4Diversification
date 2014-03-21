# -*- coding:utf-8 -*-

# Load queries and keywords
queries = {}
Dir = '''/Users/Yanan/Documents/KB/'''
f_keywords = open('''/Users/Yanan/Documents/subtopic mining/Experiments/NTCIR Data/ntcir9_100_query_keywords.txt''')

for line in f_keywords.readlines():
	keywords = []
	line = line.strip()
	tokens = line.split('\t')
	keywords.append(tokens[1].strip())
	if len(tokens) > 2:
		subtokens = tokens[2].strip().split(';')
		for sub in subtokens:
			keywords.append(sub.strip())

	for key in keywords:
		if key == '':
			keywords.remove(key)
	queries[tokens[0]] = keywords

print "%d queries loaded!" %len(queries)

for queryID, keywords in queries.items():
	print "filter queries for query %s" % keywords[0]

	fr = open(Dir + 'all_instances.owl', 'r')
	fw = open(Dir + 'filter_instance_' + queryID + '.owl', 'w')

	Description = ''
	tag = False
	tag_rel = False
	i = 0
	j = 0

	while True:
		line = fr.readline()
		if len(line) == 0:
			break

		if (line.find('''rdf:RDF''') > 0) or (line.find('xmlns') > 0):
			fw.write(line)

		if line.find('''<rdf:Description''') > 0:
			tag = True
		if tag == True:
			Description += line
		if line.find('''rdfs:label''') > 0:
			for key in keywords:
				if line.find(key) > 0:
					tag_rel = True
					break

		if line.find('''</rdf:Description>''') > 0:
			tag = False
			i += 1		

			if tag_rel ==  True:
				j += 1
				fw.write(Description)
				fw.flush()

			Description = ''
			tag_rel = False

	print i
	print j

	fw.close()
fr.close()
	
	
