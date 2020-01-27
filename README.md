# Decision-Tree-model
A C4.5 implementation of Decision Tree for Iris and House votes dataset

Subject: Machine learning
Name: Samarth Manjunath
UTA ID: 1001522809
Assignment-1
-------------------------------------------------------------------
Language used: Python 3.7
-------------------------------------------------------------------
Algorithm implemented: C4.5
------------------------------------------------------------------
About C4.5
1. It is an algorithm used to generate a decision tree. 
2. It is based on ID3 algorithm.
3. Information gain and entropy is calculated and based on that tree is developed.
--------------------------------------------------------------------
How to execute:
py main.py [data-file-name] [names-file-name]
For house of votes 84 dataset,
py main.py house-votes84.data house-votes84.names
For iris dataset,
py main.py iris.data iris.names
----------------------------------------------------------------------
Sample output:

1. For House of Votes 84 dataset

C:\Users\Samarth Manjunath\Desktop>py main.py house-votes84.data house-votes84.names
physician-fee-freeze = y :
        export-administration-act-south-africa = y :
                synfuels-corporation-cutback = y :
                        mx-missile = y :
                                handicapped-infants = y :
                                        adoption-of-the-budget-resolution = y : republican
                                        adoption-of-the-budget-resolution = n : democrat
                                handicapped-infants = n : democrat
                        mx-missile = n :
                                adoption-of-the-budget-resolution = y :
                                        water-project-cost-sharing = y : democrat
                                        water-project-cost-sharing = n : republican
                                adoption-of-the-budget-resolution = n : republican
                synfuels-corporation-cutback = n :
                        superfund-right-to-sue = y : republican
                        superfund-right-to-sue = n : republican
        export-administration-act-south-africa = n :
                adoption-of-the-budget-resolution = y : democrat
                adoption-of-the-budget-resolution = n : republican
physician-fee-freeze = n :
        education-spending = y : democrat
        education-spending = n :
                adoption-of-the-budget-resolution = y : democrat
                adoption-of-the-budget-resolution = n :
                        synfuels-corporation-cutback = y : democrat
                        synfuels-corporation-cutback = n :
                                religious-groups-in-schools = y : democrat
                                religious-groups-in-schools = n :
                                        crime = y : republican
                                        crime = n : democrat

2. For Iris dataset

C:\Users\Samarth Manjunath\Desktop>py main.py iris.data iris.names
petal width <= 0.75 : Iris-setosa
petal width > 0.75 :
        petal length <= 4.85 :
                sepal length <= 4.95 :
                        sepal width <= 2.45 : Iris-versicolor
                        sepal width > 2.45 : Iris-virginica
                sepal length > 4.95 :
                        sepal width <= 2.8499999999999996 : Iris-versicolor
                        sepal width > 2.8499999999999996 : Iris-versicolor
        petal length > 4.85 :
                sepal width <= 3.1500000000000004 :
                        sepal length <= 7.0 : Iris-virginica
                        sepal length > 7.0 : Iris-virginica
                sepal width > 3.1500000000000004 : Iris-virginica




