---
layout: post
title: Fountain Control Board
date:   2015-06-10 22:48:45
description: I spent this week designing and building a control board for my design group's interactive fountain project.
categories:
- Arduino
- Robotics
- Teensy
---

I spent this weekend designing and building the main control board for my design group's ongoing interactive fountain project for SYDE 361. This board is responsible for controlling the water jet height and direction.

#### Materials

For the micro-controller I opted to use the [Teensy-LC](https://www.pjrc.com/teensy/). Teensy is cheap ($12), Arduino compatible, and ideal for this style of rapid prototyping. Unlike development boards with headers, these can be plugged directly into a breadboard, or soldered into a circuit, which is super convenient.

We ordered our pumps from China on [Aliexpress](http://www.aliexpress.com/store/product/12V-Mini-DC-Pump-3M-4-2W-Plastic-Aquarium-Pump-Submersible-240L-H-Super-long-life/912512_580455097.html). They are very powerful for the price. In tests we managed to produce streams >1m high.

For directional control of the jets we used [micro servos from Adafruit](http://www.adafruit.com/product/169). This is the [wiring diagram and code](http://www.arduino.cc/en/Tutorial/Sweep) that we used to test the board. I was initially concerned that these servos wouldn't work with 3v3 data signal with a 5V supply, but I tested it and it worked fine.

For a power supply we used an ATX model that we pulled out of an ancient desktop computer. [This guide](http://www.electronics-tutorials.ws/blog/convert-atx-psu-to-bench-supply.html) was extremely helpful to us.

All of the remaining parts came from scrap bins, our personal supplies, and [free samples from TI](http://www.ti.com/general/docs/gencontent.tsp?contentId=69854).

#### Circuit Design

My initial design involved driving a power mosfet with a PWM signal to switch the 12V supply on and off quickly and efficiently. Unfortunately, after extensive testing I was forced to abandon this approach, because the pumps would just cut out below a 75% duty cycle. Being knockoffs, there is no data sheet for these pumps, so I chose to abandon this approach. 

The circuit I settled on is based on this [reference design](http://www.edn.com/design/analog/4363990/Control-an-LM317T-with-a-PWM-signal). I opted to replace the LM317 with an [LM1085-ADJ](http://www.ti.com/lit/ds/symlink/lm1085.pdf), because the LM1085 has a a much lower dropout voltage. For the op-amp I used [LMC6484](http://www.ti.com/lit/ds/symlink/lmc6484.pdf), because its output and common mode swing are large enough for it to work properly while being powered by the same 12V supply rail as the pump. Also, the LMC6484 has an extremely convenient pinout for breadboard prototyping

The schematic is shown below:

![](/assets/img/amplifier-circuit.jpg)

I built up the prototype on [an Adafruit perma-proto breadboard](http://www.adafruit.com/products/590). The prototype has screw terminals for all five pumps, and for all of the servo motors. An overhead view of the board is shown below.

![](/assets/img/amplifier-prototype.jpg)

Here's a closeup view of wiring:

![](/assets/img/amplifier-closup.JPG)

I used [screw terminals](http://www.digikey.com/product-search/en?pv89=1&FV=fff40016%2Cfff803bf&mnonly=0&newproducts=0&ColumnSort=0&page=1&quantity=0&ptm=0&fid=0&pageSize=25) as connectors so that we could attach and replace components as required. The screw terminals on the left side of the board are the power and signal connections for the servos, while the connections on the right side of the board are the power outputs for the pumps.

One disadvantage to using linear voltage regulators as opposed to a switching solution is that the voltage regulators dissipate substantial amounts of heat when their voltage output is adjusted to be lower than their voltage input. The minimum output output voltage at which the pumps will continue to operate reliably is 5V. At this output voltage range. The power dissipated by the regulators can be calculated using:

P = (V<sup>in</sup> - V<sup>out</sup>) * I

P = (12V - 5V) * 0.3A = 2.1W

Each TO-220 silicon die of the TO-220 package is rated to dissipate only 0.25W, so heat sinking was required. We used clip on heat sinks which were rated to dissipate 4W each, and added a small fan inside the casing to help keep things cool. A more clever solution to this problem would be to use the water in the fountain to cool the board, but time was limited.

Another problem that I had to address was that according according to this [trace width table](http://www.hardwarebook.info/PCB_trace) the 16mil traces on our PCB were insufficient to meet the worst-case current requirements of our pumps and servos (approximately 1.6A), so we soldered 22 AWG wire to the bottom of all of the power traces.

Here's a video of the basic test that I used to test each pump driver. The pumps are capable of spraying very high in the air, but I opted to run it deep underwater to avoid damaging my computer and camera.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2lOExlo4CRo" frameborder="0" allowfullscreen></iframe>

Stay tuned for further write-ups about how we integrate this board with our lighting controller and raspberry-pi to make control the fountain over wifi.