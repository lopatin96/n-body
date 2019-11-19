#!/bin/bash
mode=( 0 1 )
P=( 2 4 8 12 )
N=( 120 240 480 960 )
for m in "${mode[@]}"
do
	for p in "${P[@]}"
  do
    for n in "${N[@]}"
    do
      mpiexec -np p helloworld.py n p m
    done
  done
done