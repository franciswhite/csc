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
    #give last candidate x-x=0 points, assign nobody negative points, move to next row
#the candidate with most points wins (tie breaking?)

#3. algorithm to check whether some player stands to benefit from manipulating the vote (for given profile and rule)
        #Plurality:
            # look at candidate count: if margin of victory > 1, declare profile not manipulable (no single player can change anything)
            # if margin of victory < 2, note who lost and look at all voter's profile in following way:
            # if rank of 2nd > actual winner's rank, declare profile manipulable
            #otherwise move to next voter
            #if no voter can manipulate, declare profile not manipulable 
	
	#Borda:
            #look at candidate count: if margin of victory > x-2, declare profile not manipulable (no single player can change anything about winner)
            #if margin of victory <= m-2, note who was within m-2 of the actual winner (LOSERS) and what the margin of victory (mov) was with respect to them. then look at all voter's profile:
            #start with first ranked candidate: if candidate = winner, move to next voter. otherwise, move to second ranked candidate for same voter:
            #if that candidate is ranked higher than winner & in LOSERS & mov<2, then declare profile manipulable. otherwise, move to third ranked candidate:
	#if that candidate is ranked higher than winner & in LOSERS & mov<3, then declare profile manipulable. otherwise, move to fourth ranked candidate etc.
            #if, for all voters, no candidate fullfils all three criteria (candidate ranked higher than winner, in LOSERS, mov within manipulable range), declare profile not manipulable
            #
