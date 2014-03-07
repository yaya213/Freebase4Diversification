# -*- coding:utf-8 -*-
"""

SPARQL Query using :meth:`rdflib.graph.Graph.query`

The method returns a :class:`~rdflib.query.Result`, iterating over
this yields :class:`~rdflib.query.ResultRow` objects 

The variable bindings can be access as attributes of the row objects
For variable names that are not valid python identifiers, dict access
(i.e. with ``row[var] / __getitem__``) is also possible.

:attr:`~rdflib.query.ResultRow.vars` contains the variables

"""

import rdflib

if __name__=='__main__':
    g = rdflib.Graph()
    g.load("ontology.owl")

    # the QueryProcessor knows the FOAF prefix from the graph
    # which in turn knows it from reading the RDF/XML file

#results = g.query('select ?s ?label ?URL where {?s rdfs:label ?label. ?s ont:URL ?URL. }')
results = g.query('select ?s ?p ?o where {?s ?p ?o.}')

print results

for row in results:
	print row
for row in results:
	print row.s, row.p, row.o
#	print '%s\t%s\t%s' %(row.s, row.label, row.URL)   
#for row in g.query(
#            'select ?s ?label ?URL where {?s rdfs:label ?label. ?s ont:URL ?URL. }'):
	    # 'select ?s ?label where {?s rdfs:label ?label. ?s rdfs:label "那英".}'):
	    # 'select ?s ?label where {?s rdfs:label ?label.}'):
            # 'select ?s where { [] foaf:knows ?s .}'):
#       print row
#	print row.label
#	print row.URL
        # or row["s"]
        # or row[rdflib.Variable("s")]




