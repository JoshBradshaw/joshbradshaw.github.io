---
layout: post
title:  Advice for Building Quality Electronics Prototypes
date:   2015-05-20 22:48:45
description: Supporting materials for my SYDE student seminar presentation on rapid electronics prototyping.
categories:
- Electronics
- Rapid Prototyping
---

In this post I give practical advice about how to assemble a reliable and aesthetically pleasing electronics prototype for our design project course. I'm going to keep this post basic and very general, because there are thousands of tutorials out there for the more specific topics. My intention here is to draw attention to pitfalls and kludges that I've seen time and time again in design project presentations that I want to help everyone avoid.

## Enclosures

Enclosures transform your sketchy prototype into a nice looking product. At SickKids I pretty much exclusively used these [aluminum guitar effect stomp boxes](https://www.creatroninc.com/product/aluminum-enclosure-120x95x35mm/?search_query=case&results=34). It's very easy to drill and file holes into these, and they look great. Other options include plastic project boxes, and if you're ambitious, [you can have a PCB machined to make the front panel of your device](https://www.youtube.com/watch?v=Yj0Bv4UEFSs).

## Soldering

Soldering is the method you use to transform a breadboard circuit model into a reliable prototype. [Follow the instructions in this video](https://www.youtube.com/watch?v=fYz5nIHH0iY). I recommend making a few practice joints before you begin. Orion can probably give you some broken boards and parts to play with. When you're done soldering, use alcohol wipes to clean the board, because otherwise the leftover flux will cause corrosion.

## PCBs and Connectors

If you build your prototype using some combination of a breadboard and a development board like Arduino then you'll likely find that your prototype is a little bit flimsy, with wires going everywhere. I recommend these strategies to deal with this mess:

1. Once your prototype works, replace the breadboard with a [solderable breadboard pcb](https://www.adafruit.com/products/571).
2. Buy [crimp on connectors](https://www.creatroninc.com/product/3-pin-male-jr-header-set/?search_query=crimp+on&results=101) to make solid connections with your Arduino, Raspberry Pi or whatever. These are much more sturdy than just sticking pieces of wire into the headers. Protip: populate all three pins even if you don't need them, for mechanical strength.
3. If you're ambitious, you can have a PCB board manufactured for your project. Follow [this PCB tutorial](https://www.youtube.com/watch?v=1AXwjZoyNno). You can have your PCBs manufactured for $22/each at Advanced Circuits with one week turn around, $10/batch from iTead with a longer turnaround, or on campus at the 3D printing center.

## Power Supplies

Budget power supplies do not perform as well as the high quality units that we have in the SYDE lab. Assuming that you have a relatively low budget, you will probably want to go with one of the following options:

1. Switch mode power supplies, like the ones that used to power laptops and cellphone chargers. Switch mode supplies have relatively noisy voltage outputs, which can propagate through your analog circuitry and disrupt your sensor readings. If you're using switch mode supplies, use [bypass capacitors](http://www.seattlerobotics.org/encoder/jun97/basics.html) and [voltage regulators](https://www.sparkfun.com/products/107) to reduce power supply noise.
2. Batteries are nearly ideal voltage sources, with the obvious drawback that they run dead. Before choosing a battery solution, you need to carefully consider the power consumption of your circuit (the simplest to check is to power it up, measure the current it draws and use P=VI). Also, look at the datasheets of your components to see whether or not they will continue to work when the battery voltage eventually drops.

## Pitfalls to Avoid in Circuit Design

1. [Arduinos have several obvious and not so obvious failure modes](http://www.ruggedcircuits.com/10-ways-to-destroy-an-arduino/). I destroyed a board at work by connecting the power backwards, be careful.
2. Poor ground connections. A very common mistake that electronics hobbyists make is to assume that their ground rail will have the same voltage everywhere. This assumption breaks down when you start to push a significant amount of current through your ground wiring. If your design relies on precision sensors, read this [application note on grounding](http://www.analog.com/library/analogdialogue/archives/46-06/staying_well_grounded.html).

## Further reading:

1. [Sparkfun Electronics Tutorials](https://www.sparkfun.com/tutorials)
2. [Adafruit Tutorials](https://learn.adafruit.com/)
3. [The Signal Blog](https://e2e.ti.com/blogs_/archives/b/thesignal/)
4. Texas Instruments and Analog Devices reference designs and whitepapers.