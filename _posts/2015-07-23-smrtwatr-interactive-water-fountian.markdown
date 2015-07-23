---
layout: post
title: SMRT WATR Interactive Fountain
date:   2015-06-10 22:48:45
description: Overview + demo video of my group's SYDE 351 design project, an interactive water fountain + quiz game.
categories:
- Arduino
- Robotics
- Teensy
- Python
---

For our 3A design project in Systems Design Engineering, Emma Cooper, Isaac Hunter, Matt Jones and I designed and built an interactive water fountain. Users interact with the fountain by playing an online game called QuizDrop. In QuizDrop, 1-4 players compete against one another. Each player is assigned a particular corner of the fountain, and as they score points the jet in their corner moves the height of the water spray increases. At the end of the three question game, the player with the most points wins full control of the fountain. They can choose between several different preprogrammed routines, and they can switch between them at will for 30 seconds.

My role in this project was designing and building the fountain's hardware and controls. I designed the [pump and motor driver circuitry]({% post_url 2015-06-15-arduino-water-jet %}) and the lighting driver. I also designed and programmed the [firmware that ran on microcontrollers](https://github.com/Adam93MT/SMRTWATR/tree/master/controls) to make the jets and lighting do various actions throughout the quiz. Finally, I made substantial contributions to the design of the fountain's basin and the various waterproof electronics enclosures.

We unveiled our fully functional prototype at our class's public design symposium on July 22, 2015. Our fountain was the crowd favorite, and during the three hour event we were able to play ~70 games. Here's a video of the fountain during the end-game while some of our classmates were playing a round:

<iframe width="560" height="315" src="https://www.youtube.com/embed/sUKH4mjTl4k" frameborder="0" allowfullscreen></iframe>

The firmware and QuizDrop game are open source, and the code is [available on Github](https://github.com/Adam93MT/SMRTWATR).

As of September, all of the members of this team will be moving away from the University to go on co-op. None of us wishes to take the fountain with us when we move, so we want to give it away (its worth approx $400 in materials alone) to a group of artists or group of students who want to do something interesting with it. If you want to aquire the fountain, post to our [Google+ page](https://plus.google.com/b/115760182356032680469/115760182356032680469/posts) explaining what you intend to use it for. You must be able to pick it up from Waterloo before August 15th.