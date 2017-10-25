---
layout: page
title: Infinity Mirror
subtitle: Some Electronic Art
use-site-title: true
---

My friend Sarah likes to manage lighting and costumes for local theatre productions, so I thought that an infinty mirror would be an ideal Christmas gift for her. I had a relatively low budget for this project, so the goal was to build this mostly out of stuff that I already had cluttering up my tiny dorm room.

I based my design on the [Ikea infinity mirror instructable](http://www.instructables.com/id/IKEA-Infinity-Mirror/). The only major modification I made is that I used Adafruit dotstar LED strips, which I had left over from the SMRT WATR fountain build. I prefer the dotstar strips over the other types of serial addressable LEDs, because they use high speed SPI for their data interface, which means that they can be used for persistance of vision effects. For the LED driver, I used a Teensy LC microcontroller. These little microcontrollers cost about $10, and they have a great form factor for discretely integrating into the cord. 

I didn't want this to burn my friend's house down, so I used an Anker power supply with resettable fuse protection to power the LED lighting. That way if the mirror is dropped or handled roughly enough to short out the strips, it won't catch fire.

Here's a quick video demo I took before packaging it up as a Christmas gift. This thing is seriously bright. It looks great in any lighting dimmer than direct sunlight.


<div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/oavbHisQols" frameborder="0" allowfullscreen></iframe>
</div>