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

The Arterial Blood Pressure Triggering System was my primary project during my four month co-op term in Dr. Chris Macgowan's MRI lab at SickKids. Chris hired me because he needed instrumentation to synchronize MRI scans with the motion of fetal pig hearts, but the only solutions available cost >$20,000 and were not guaranteed to work.

#### Learning about the setting

To gain a better understanding of the unique challenges associated with MRI research, I watched a variety of MRI scans including unusual cases such as fetal scans and neonatal scans. I also volunteered for various protocol trials, and spent several hours in the scanner. Through the process of these scans I got familiar with cardiac imaging protocols and the various existing MRI compatible instruments.

#### The problem

MRI scanners take a significant amount of time to acquire enough signal for a diagnostic quality image. This means that to image a heart, which is constantly in motion, the MRI scanner must be synchronized with the cardiac and respiratory motion. In adults, we either use ECG or pulse oximeter to obtain the synchronization signal. In the case of the fetal imaging experiment, neither of these techniques were viable options, so in coordination with the cardiology department, we opted to use invasive blood pressure transducers for the cardiac monitoring. 

My job was to design an interface between the blood pressure transducer and the MRI scanner, providing a continuous real-time synchronization signal. I was also tasked with making an interface so that the experimenters and surgeons could monitor the pig's heart rate and blood pressure, so that they can identify and deal with any abnormalities or lapses in synchronization as they happen.

#### The design

I designed and built and extensively tested the device over the course of one four month co-op term. It is currently being used in a series of experiments at SickKids, and the design has been open-sourced so that other researchers can adapt it for their own experiments.

Resources:

1. <a href="{{ '/assets/jabradsh-SYDEWRPT300.pdf' | prepend: site.baseurl | prepend: site.url }}">Whitepaper describing the device</a>
2. [Device documentation and usage instructions](http://joshbradshaw.ca/Arterial-BP-MRI-Triggering-Unit/)
3. [The github repo with the source code, schematics and PCB layouts for the design](https://github.com/JoshBradshaw/Arterial-BP-MRI-Triggering-Unit)