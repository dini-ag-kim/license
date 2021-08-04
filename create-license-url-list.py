# First step is to create one N-Triples file from the single 
# license descriptions in https://github.com/spdx/license-list-data:
# git clone git@github.com:spdx/license-list-data.git ../license-list-data
# $ cat ../license-list-data/rdfnt/*.nt >> spx-licenses.nt
# Maybe someone can update the script in the future to include this step...

import rdflib

g = rdflib.Graph()

g.parse("spx-licenses.nt", format="nt")

qres = g.query(
    """
    PREFIX spdx:  <http://spdx.org/rdf/terms#> 
    PREFIX doap:  <http://usefulinc.com/ns/doap#> 
    PREFIX ptr:   <http://www.w3.org/2009/pointers#> 

    SELECT DISTINCT ?url
       WHERE {
           ?license spdx:crossRef [
               spdx:url ?url
           ]
       }""")



with open("spx-license-urls.txt", "a") as output:
    for row in qres:
        output.write("%s" % row)
        output.write("\n")

# Some post processing is necessary to:
# - remove the "legalcode" string from CC licenses
# - remove duplicate URLs
# Maybe someone can update the script in the future to include
#  this step...