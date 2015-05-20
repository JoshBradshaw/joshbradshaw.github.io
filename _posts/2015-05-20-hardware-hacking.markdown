---
layout: post
title:  Advice for Building Quality Electronics Prototypes
date:   2015-05-20 22:48:45
description: Supporting materials for my SYDE student seminar presentation on rapid electronics prototyping.
categories:
- Electronics
- Rapid Prototyping
---

In this post I give practical advice about how to assemble a reliable and aesthetically pleasing electronics prototype for our design project course.

## Power Supplies

In Orion's lab, we powered our circuits using high quality linear power supplies. Those power supplies have two advantages over cheap power supplies. They are low noise, and they provide an output voltage that doesn't drift over time. Power supplies with those two advantages tend to be expensive. When working on a budget you essentially have two power supply options:

1. Switch mode power supplies, like the ones that you use to power your phone and laptop. Switch mode supplies have noisy voltage outputs. If not filtered out, this output voltage noise will disrupt your analog circuitry. If you're using switch mode supplies, use [bypass capacitors](http://www.seattlerobotics.org/encoder/jun97/basics.html) and [voltage regulators](https://www.sparkfun.com/products/107) to reduce power supply noise.
2. Batteries are nearly ideal voltage sources, with the obvious drawback that they run dead. Before choosing a battery solution, you need to carefully consider the power consumption of your circuit (the simplest way is to power it up, measure the current it draws and use P=VI). Also, look at the data-sheets of your components to see whether or not they will continue to work when the battery voltage eventually drops.

## Enclosures

Enclosures are great. They transform your sketchy prototype into a nice looking product. At SickKids I pretty much exclusively used these [aluminum guitar effect stomp boxes](https://www.creatroninc.com/product/aluminum-enclosure-120x95x35mm/?search_query=case&results=34). Being aluminum, it's very easy to drill and file holes into these. If your project requires cutting holes for square connectors, I recommend going with a plastic box. If you're ambitious, [you can have a PCB machined to make the front panel of your device very cheaply](https://www.youtube.com/watch?v=Yj0Bv4UEFSs).

## Soldering

Soldering is super easy to learn. [Follow the instructions in this video](https://www.youtube.com/watch?v=fYz5nIHH0iY). I recommend making a few practice joints before you begin. Orion can probably give you some broken boards and parts to play with. When you're done soldering, use alcohol wipes to clean the board, because otherwise the leftover flux will cause corrosion #coopscrewups.

## PCBs and Connectors

If you build your prototype using some combination of a breadboard and a development board like Arduino then you'll likely find that your prototype is a little bit flimsy, with wires going everywhere. I recommend these strategies to deal with this mess:

1. Once your prototype works, replace the breadboard with a [solderable breadboard pcb](https://www.adafruit.com/products/571).
2. Buy [crimp on connectors](https://www.creatroninc.com/product/3-pin-male-jr-header-set/?search_query=crimp+on&results=101) to make solid connections with your Arduino, Raspberry Pi or whatever. These are much more sturdy than just sticking pieces of wire into the headers. Protip: populate all three pins even if you don't need them, for mechanical strength.
3. If you're ambitious, you can have a PCB board manufactured for your project. Follow [this PCB tutorial](https://www.youtube.com/watch?v=1AXwjZoyNno). You can have your PCBs manufactured for $22/each at Advanced Circuits with one week turn around, $10/batch from iTead with a longer turnaround, or on campus at the 3D printing center.


Further reading:

1. [Sparkfun Electronics Tutorials](https://www.sparkfun.com/tutorials)
2. [Adafruit Tutorials](https://learn.adafruit.com/)
3. [The Signal Blog](https://e2e.ti.com/blogs_/archives/b/thesignal/)
4. Texas Instruments and Analog Devices reference designs and whitepapers.