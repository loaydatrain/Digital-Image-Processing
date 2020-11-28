# Project Proposal 

## Project Id and title

20 - Manga Colorization

## Github link
https://github.com/Digital-Image-Processing-IIITH/project-framed

## Team Members

 - Haripraveen Subramanian
 - Jayant Duneja
 - Loay Rashid
 - Rishabh Daga

## The main goal(s) of the project
Primary goal of the project is to implement an algorithm that performs flood fill-like colorization on black and white manga. A combination of intensity and pattern-continuity is used to perform colorization. The problem is compounded due to the heavy use of hatching, halftoning and screening in manga.

## Problem definition (What is the problem? How things will be done ?)
In order to create detail and a dramatic atmosphere manga artists intensively use strokes, hatching, halftoning, and screening, This imposes many difficulties in digital colorization. We plan to segment the image using the continuity of pattern and intensity and then use flood fill to colorize the image.

the level set method is used to model multiple boundaries present within the image. this takes a planar 2-d image and converts to a 3-d curved surface. The flexibility of this method allows us to segment multiple disjointed regions and leak-proof during colorization.


## Results of the project (What will be done? What is the expected final result ?)
The result of the project will be an algorithm which will demonstrate how colourization will work on various manga comic images.


## What are the project milestones and expected timeline?
*31st October:*

1. level set propagation and get to work on section 3.3 of the paper-31st

2. final deliverables

*18th November:* 

Final deliverable

## Is there a dataset you need? How do you plan to get it?
We need a dataset to test the effectiveness of our algorithm.


We can also get images by searching off of google images.
