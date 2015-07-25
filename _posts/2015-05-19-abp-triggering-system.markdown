---
layout: post
title:  Arterial Blood Pressure Triggering System
date:   2015-04-14 22:48:45
description: A quick description of my 4 month research and development project at SickKids Hospital.
permalink: abpt.html
categories:
- Instrumentation
- MRI
---

![](/assets/img/ipb_unit.JPG)

The Arterial Blood Pressure Triggering System was my primary project during my four month co-op term in Dr. Chris Macgowan's MRI lab at SickKids. Chris hired me because he needed instrumentation to synchronize MRI scans with the motion of fetal pig hearts, but the only solutions available cost >$25,000 and were not guaranteed to work.

#### The problem

MRI scanners take a significant amount of time to acquire enough signal for a diagnostic quality image. This means that to image a heart, which is constantly in motion, the MRI scanner must be synchronized with the cardiac and respiratory motion. In the case of the fetal imaging experiment, neither of these techniques were viable, so we opted to do the cardiac monitoring using invasive blood pressure transducers. 

My job was to design a system to convert the invasive blood pressure signal into a real-time synchronization signal for the MRI scanner. I was also tasked with making a display so that the experimenters and veterinary surgeons could monitor the pig's heart rate and blood pressure, allowing them to identify any abnormalities.

#### Design and implementation

I designed, built and extensively tested the gating device over the course of one four month co-op term. It is currently being used in a series of experiments at SickKids, and the source code and drawings have been open-sourced so that other researchers can use and adapt the tool for their own experiments. For technical details, please see the resources below.

Resources:

1. <a href="{{ '/assets/jabradsh-SYDEWRPT300.pdf' | prepend: site.baseurl | prepend: site.url }}">Whitepaper describing the device</a>
2. [Device documentation and usage instructions](http://joshbradshaw.ca/Arterial-BP-MRI-Triggering-Unit/)
3. [The github repo with the source code, schematics and PCB layouts for the design](https://github.com/JoshBradshaw/Arterial-BP-MRI-Triggering-Unit)