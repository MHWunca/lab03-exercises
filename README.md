# Lab 03 Exercises!

## Find All Duplicates
#### Write a function (or static method in the case of Java) that accepts a list of integers and returns a list of only those integers that appear more than once.
Done.

## Describe Different Approaches to Solving This Problem
#### Describe the two different ways to figure out all of the duplicate values of a list of integers in english. The first solution is the nested loop solution. The second solution is to use a dictionary or a map (similar to the containsPair method we wrote in class. Describe both in as much detail as you can (with no code) and describe the trade-offs between the two solutions.
One can use a loop iterating through a list with a another loop inside checking the elements of the list after the element we are on, and seeing if they are equal. One can also use a dictionary or map, and if we see that we've already set the value for a key (the integer) in the dictionary or we have a collision in the map, then we know which integers we are seeing for the second time.
