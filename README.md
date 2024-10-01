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
