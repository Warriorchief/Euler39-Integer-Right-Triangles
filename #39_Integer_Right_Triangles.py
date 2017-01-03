#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 23:52:25 2016

@author: christophergreen


Integer right triangles
Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?


a^2 + b^2 = c^2    and    a+b+c=p
... 2p(a+b)-2ab = p^2
"""

def count_pythag_triples(p):
    leg_pairs=[];
    a=1;
    while a<p/2:
        b=1;
        while b<p/2:
            leg_pairs.append([a,b]);
            b+=1;
        a+=1;
    count=0;
    holder=[];
    for pair in leg_pairs:
        if 2*p*(pair[0]+pair[1]) - 2*pair[0]*pair[1] == p**2:
            if pair[0] not in holder and pair[1] not in holder:
                holder.append(pair[0]);
                holder.append(pair[1]);
                print("found a pythag triple: sides of length",pair[0],pair[1],(pair[0]**2+pair[1]**2)**.5);
                count +=1;
    return count;

p=12;   
most=0;
while p<=1000:
    if count_pythag_triples(p)>most:
        most=count_pythag_triples(p);
        print("having",p,"as the perimeter gives us a new high of",most);
    p+=1;

    #--> biggest is having 840 as the perimeter gives us a new high of 8 CORRECT