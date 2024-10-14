# Kilter_Board_Vision

Group:
Only Aiden Fockens (afockens@bu.edu)

Project Description:
My project will tell a rock climber where they should put their hands and feet to complete the climb.

Goal:
Make a neural net that can take in videos with certain features and come back with the order in which to put hands and feet.

How to get the data:
Kilter boards are a type of climbing wall. They use bluetooth and crowdsourcing to connect to an app on your phone that will light up certain holds to show a path up the wall. On their app, there are lots of videos of people completing the climbs. I want to download these

Modeling, visualizing, testing:
I want to scrape a bunch of these videos. I will extract important features, like the different holds that exist and their locations. This includes the starting holds, end hold, feet holds, and hand holds (the kilter board specifies) I will also extract the location of the climber, like where their feet and hands are. From here, I want to build nueral net that will train on these videos and then be able to predict what a climber should do when given a picture of a climb.



Visualization: 

Take a video. Cycle through the frames. For each frame, I need to:
  Keep track of where the holds are.
  Keep track of where the hands and feet are 
  If a hand or foot stays in a certain spot for enough time, then it is using that hold 
  Create a matrix for each move of a climber (0s for unusable holds, 5s for starting holds, 6 for ending holds, 7 for hands, 8 for feet, 1, 2, 3, and 4 for the hands and feet of where it is). Save this matrix and connect it to the next matrix that comes after it. These are training values. 
  Before the climb starts, create a pair of the matrix without any 1,2,3,4 and then of where the person starts 


Next, train the model based on these matrices. To test, give it a picture of a climb. it should then figure out the matrix and process the next move. From here, it should be able to process until finished (there are no 6's in the matrix) and then print those steps out.
  
