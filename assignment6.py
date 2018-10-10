#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:02:07 2018

@author: lcampbe3

exercise 6 #1 - head function
"""
#number 1 - replicates functionality of head
def head(file, lines):
    InFile = open(file)
    linenumber=0
    for l in InFile:
        linenumber=linenumber+1
        if linenumber > lines:
            break
        print l
        
head("wages.csv", 3) #could use any number for lines

#number 2
import pandas
iris_data = pandas.read_csv("iris.csv", sep = ",")
iris_data.shape
print(iris_data.loc[148:149, "Petal.Width":"Species"])

species_count = iris_data["Species"].value_counts()
print(species_count)


rows = iris_data.loc[iris_data["Sepal.Width"] > 3.5]
print(rows)

#setosa.csv
setosa = iris_data.loc[iris_data["Species"] == "setosa"]
setosa.to_csv("setosa.csv", sep=",")

virginica = iris_data.loc[iris_data["Species"] == "virginica"]
virginica["Petal.Length"].mean()
virginica["Petal.Length"].min()
virginica["Petal.Length"].max()