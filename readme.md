# Hough idea 

## Introduction

This is a few scripts to bring together an idea on how to fit functions to
short sections of data without predefining the sections. It was inspired by
[this](http://stackoverflow.com/questions/24134894/identify-graph-uptrend-or-downtrend?)
SO post and some reading on the [Hough
transform](http://en.wikipedia.org/wiki/Hough_transform)

## Overview of method

Given some data `x` and `y` select a function which you think will fit well,
for now we will stick to linear functions of the form `y = mx + c`. Then define
a grid in the parameter space e.g `m` and `c`. Now the idea is for each point
decide how well it fits the data, if it fits within some threshold then add a 1
to this point. Doing this for all points in the grid will build up a heatmap.
The maxima of the heatmap are the values of `m` and `c` which best fit sections
of the data. 

There is then some technicality in picking out these maxima and deciding which
parts of the plot they actually fitted to but I think the principle works for now
even if it isn't perfect.  
 
