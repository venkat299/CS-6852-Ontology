# CS-6852 Ontology Assignments

This repository collects coursework for the CS-6852 ontology and knowledge representation class.  The exercises revolve around modelling the financial domain and evolve from an initial conceptual design to a formal OWL ontology.

## Repository structure

- **Assignment 1** – Introduces the project and outlines the financial modelling domain, including equity research and portfolio management questions that the ontology should answer.
- **Assignment 1-rework** – Refines the first assignment with a Turtle ontology (`financial-modelling5.ttl`) and a small Python script (`graph.py`) for loading the graph.
- **Assignment 2** – Explores XML data design.  It provides DTD specifications and example XML documents for stocks, bonds, mutual funds and index funds, along with solutions to XPath and XQuery exercises.
- **Assignment 3** – Delivers the final OWL/Turtle ontology describing financial instruments, market indices and sentiment information.

## Using the sample script

A minimal example in `Assignment 1-rework/graph.py` shows how to load the Turtle model using `rdflib`:

```bash
pip install rdflib
python Assignment\ 1-rework/graph.py
```

The script reads `financial-modelling5.ttl` and displays the first few triples, which is helpful for quick inspection.

## Intent

The assignments aim to build a structured representation of the financial modelling domain—covering instruments such as stocks and bonds, market indices and company information—to support queries about performance and risk.

## Authors

- DA24C021 – Venkatesh Duraiarasan
- CS24M033 – Pradeep Peter Murmu
