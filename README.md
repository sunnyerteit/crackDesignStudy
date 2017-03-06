# crackDesignStudy
Author: Sunny Islam

Year: 2017

Generates an Abaqus simulation batch describing a cracked half-plane, and outputs the J-integral

# Contents
jBatch.py

> Run this script in Abaqus. It will produce a batch with a number of simulations. All depicting a cracked plate, with constant crack length, subjected to a constant displacement normal to the crack-plane. The main objective of these simulations is to read the J-integral.
  
jRead.py

> Reads the .dat-files produced by jBatch.py. If you wish to change parameters in jBatch, the changes also need to be applied to jRead.py. This script might require you to install a couple of python packages.
  
example.png

> A visual output from one of the analyses produced by jBatch.py.
  
results.png

> Results produced from jRead.py.
  
data directory

> Contains a batch of .dat files if you for some reason is incapable of producing your own set.
  
30.odb

> An analysis produced from jBatch.py.
