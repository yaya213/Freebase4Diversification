# -*- coding:utf-8 -*-
import rdflib

if __name__=='__main__':

    g = rdflib.Graph()
    g.load("all_instances.owl")

    # the QueryProcessor knows the FOAF prefix from the graph
    # which in turn knows it from reading the RDF/XML file
    for row in g.query(
            'select ?people ?property ?value  where {?people rdf:label "香山湖".}'):
        print row
        # or row["s"]
        # or row[rdflib.Variable("s")]
