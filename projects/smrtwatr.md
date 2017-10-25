---
layout: page
title: 'SMRT WATR'
subtitle: 'An Interactive Water Fountain Quiz Game'
---

![](/img/projects/smrtwatr/smrtwatr.jpg)

## Purpose

For our second third year design project, we were challenged to use internet of things (IOT) technology to address a problem of our choosing. We decided to use IOT technology to create a piece of electronic art, that would encourage social interaction among its viewers. We created a multiplayer quiz game and a robotic fountain that reacts to users' answers, where the winner was given control over the fountain's motion.


## Role

I worked on this project with [Emma Cooper](https://www.linkedin.com/in/emmamcooper/), [Matt Jones](https://www.linkedin.com/in/matt--jones/), [Isaac Hunter](https://isaachunter.ca/), [Adam Thompson](http://adamthompson.ca/), and Shubh Jagani. My role was to design the fountain's pumping system, motion system, lighting system and controls.

## Design of the Fountain

Designing the fountain was a fun problem, because we had a tightly constrained budget and we wanted it to be as visually interesting as possible. For the water jets, we procured some cheap aquarium pumps and built laminar flow nozzles out of small drinking straws and surgical tubing. I created PWM mosfet drivers for each of the aquarium pumps that allowed us to vary the height of the water jets. I also connected four of the five water jets to small servo motors so that they could be swept across a wide arc.

For the lighting we used dotstar LED strips from Adafruit industries. Every LED on these strips is serial addressable, which meant that we could use a single microcontroller to control all 200 lights at an update rate of 100Hz, which meant that transitions were imperceptible to human eye and we could use persistence of vision effects.

For control, two separate microcontrollers were used. One controlled the lighting, and the other controlled the fountain's pumps and servo motors. Both controllers had a collection of pre-programmed motion scripts loaded into their flash memory. A low-cost raspberry pi PC with wifi continuously polled for gameplay updates from the quiz game server, and sent the relevant motion commands to the two microcontrollers via USB.

## Gameplay

The interface of the quiz game is shown below.

![](/img/projects/smrtwatr/smrtwatr-lobby-ingame.jpg)
![](/img/projects/smrtwatr/smrtwatr-endgame.jpg)

While users played our quiz game, they were assigned a corner of the fountain to stand beside. This corner's jet and lighting would react to their performance throughout the game. For example, at any given time, the player with the highest water jet was the player with the highest score. The fountain reacted immediately with a change of motion to events such as scoring a point or getting an answer wrong. 

At the end of the game, the player who scored the most point got to control the fountain by running several pre-programmed routines. They could switch between the routines as often as they liked.

Here's a demo of the game in action:


<div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/x0ej92Pg6EA" frameborder="0" gesture="media" allowfullscreen></iframe>
</div>