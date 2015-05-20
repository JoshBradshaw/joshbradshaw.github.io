---
layout: post
title:  How to Build a Professional Prototype
date:   2015-04-14 22:48:45
description: Supporting materials for my SYDE student seminar presentation on rapid electronics prototyping.
categories:
- Electronics
---

In this post I give practical advice about how to assemble a reliable aesthetically pleasing electronics prototype.

## Power Supplies

In Orion's lab, we always just powered our circuits using quality variable power supplies. Those power supplies have two qualities that most cheap real world power supplies lack:

1. They are low noise, as in if you connect an oscilloscope probe to their output they don't give random high frequency voltage spikes.
2. They provide a voltage that doesn't change over time.

When working on a budget, you essentially have two power supply options. 

1. Switch mode power supplies, like the ones that you use to power your phone and laptop. Switch mode supplies provide very noisy outputs which will ruin your day if you need to make accurate readings from a sensor. If you're using switch mode supplies, use [bypass capacitors](http://www.seattlerobotics.org/encoder/jun97/basics.html) and [voltage regulators](https://www.sparkfun.com/products/107).
2. Batteries, are nearly ideal voltage sources, with the obvious drawback that they run dead. With batteries, you need to carefully consider the power consumption of your circuit (the simplest way is to power it up, measure the current it draws and use P=VI). Also, look at the data-sheets of your components and see whether or not they will work when the battery voltage drops as it begins to run dead.

## Enclosures

Enclosures are great. They transform your sketchy prototype into an awesome looking product pretty much instantly. At SickKids I pretty much exclusively used these [beautiful aluminum guitar effect stomp boxes](https://www.creatroninc.com/product/aluminum-enclosure-120x95x35mm/?search_query=case&results=34). Being aluminum, it's very easy to drill and file holes into these. If your project requires a lot of square connectors, I recommend going with a plastic box, because cutting square holes in aluminum is time consuming work. If you're ambitious, [you can have a PCB machined to make the front panel of your device very cheaply](https://www.youtube.com/watch?v=Yj0Bv4UEFSs).

## Soldering

Soldering is intimidating at first, but its super easy to learn. [Follow the instructions in this video](https://www.youtube.com/watch?v=fYz5nIHH0iY). I recommend doing some practice soldering before you begin. Orion can probably give you some broken boards and parts to play with. When you're done soldering, use alcohol wipes to clean your solder joints, because otherwise the leftover flux will corrode them away #coopfuckups.

## PCBs and Connectors

If you build your prototype using some combination of a breadboard and a development board like Arduino then you'll likely find that your prototype is a little bit flimsy, with wires going everywhere. I recommend these strategies to deal with this mess:

1. Once your protoype works, replace the breadboard with a [solderable breadboard pcb](https://www.adafruit.com/products/571).
2. Buy [crimp on connectors](https://www.creatroninc.com/product/3-pin-male-jr-header-set/?search_query=crimp+on&results=101) to make solid connections with your Arduino, Raspberry Pi or whatever. These will not fall out the way pieces of wire tend to. Protip: populate all three pins even if you don't need them, for mechanical strength.
3. If you're ambitious, you can have a PCB board manufactured for your project. Follow [this PCB tutorial](https://www.youtube.com/watch?v=1AXwjZoyNno). You can have your PCBs manufactured for $22 at Advanced Circuits with one week turn around, $10 from itead with a longer turnaround, or on campus at the 3D print center. 