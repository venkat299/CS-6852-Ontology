# Loading the Turtle file to inspect its contents and extract the structure

from rdflib import Graph



# Load the Turtle file

g = Graph()

ttl_file_path = './financial-modelling5.ttl'

g.parse(ttl_file_path, format="turtle")



# Display a summary of the contents (e.g., classes, properties, etc.)

list(g)[:10]  # Display first 10 triples to understand the structure

