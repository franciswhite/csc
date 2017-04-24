#Steps:
#1. Generate the profiles for various n.
#2. Algorithm to determine winner under each rule
#3. Find some algorithm to check for manipulablity under each voting rule.
#3. Draw sample from profiles generated, look at manipulable fraction, do some statistical tests.

#1. Generate profiles
import numpy as np
#for n voters, x candidates. profile =  x * n array.
#1st item in row is most preferred etc.

#2. Determine winner under Plurality, Copeland and Borda
#Borda: assign each candidate a counter. move through array and update counter with Borda-vector values. pick candidate with maximal number (tie breaking?)
#Plurality: assign each candidate a counter. move through rows of array and give first candidate one point. pick candidate with maximal number (tie breaking?)
#Copeland: assign each candidate a counter. move through rows of array in following way:
    #give first candidate x-1 points, give all candidates from second place onwards -1 point.
    #give second candidate x-2 points, give all candidates from third place onwards -1 point.
    #...
    #give last candidate x-x=0 points, assign noone negative points, move to next row
#the candidate with most points wins (tie breaking?)

#
