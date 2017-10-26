---
layout: page
title: 'PressureTrigger'
subtitle: 'A cardiac MRI triggering system for use in animal imaging experiments'
---

The code for this project is open source and [available on Github](https://github.com/JoshBradshaw/IBP-Reciever). If you're interested in the hardware, please contact me.

![](/img/projects/pressuretrigger/DSC01219.jpg)

*The blood pressure amplifier and digital signal processing (DSP) module that I created*

## Problem

At SickKids Hospital a significant amount of animal research is conducted. MRI imaging is used for animal studies in cancer research and cardiac research, because MRI has adaptable contrast that can be used to differentiate between soft tissues and measure blood flow.

Imaging animal circulation and cardiac motion in MRI is complicated by the fact that a gating signal is required to synchronize the MRI acquisition with the cardiac cycle. I explained the details of cardiac gating in my [introductory article on cardiac MRI](/articles/cardiac_mri). Over the years the labs at SickKids have created several [specialized gating apparatusess](http://www.mouseimaging.ca/publications/assets/archive/2006%20MRM%2055%20Bishop.pdf) to handle the requirements of particular animal imaging experiments.

The particular challenge in this case was that animals needed cardiac MRI imaging as part of a study for which the experimental setup prohibited the use of conventional ECG electrodes. Instead the scientists needed some way to gate the MRI scanner using an arterial blood pressure signal. The basic surgical procedure already involved inserting a catheter into the aorta, so that was the site where we needed measure the arterial blood pressure from.

The researchers also wanted to be able to use the gating blood pressure probe to measure blood pressure to within 1 mmHg, so that they could use the blood pressure measurements for monitoring the subject. This meant that the blood pressure probing system had to be a calibrated sensor, and the monitoring software needed to have provisions for zeroing the measurement relative to atmospheric pressure.


## Description of Required Device

To trigger the the MRI scanner, the minimum components required were:

* A calibrated pressure probe that could be inserted into an artery >= 1mm in diameter and measure the blood pressure waveform in real time.
* An analog to digital converter (ADC) that could convert the blood pressure signal into a calibrated voltage.
* A real-time digital signal processing system that would:
    - Detect the peak blood pressure for each cardiac cycle and send a 5V TTL triggering signal to the MRI scanner.
    - Continuously record the blood pressure measurements into a file, for review after the experiment.

## Primary Constraints on the Design

* Any components located within the MRI scanner room were required to be fully MRI compatible, which meant that they could not contain any ferrous materials or self-heat in the high power RF fields produced by the scanner.
* Any components located directly in the MRI scanner's bore had to be MRI compatible, and tested in imaging to ensure that they didn't produce any image artifacting. Some metals such as non-ferrous stainless steel cause very severe image artifacts if they're placed directly in the bore.
* Any components located within the surgical field were subject to standard hospital cleanliness and disease control regulations. For components such as cabling, disinfection with chlorohexidine was standard practice. Components used in the surgery itself were expected to either be autoclaved or disposed of.
* The only permissible place to run cabling in between the MRI scanner room and the control room was through a 12cm diameter waveguide.

## System Components

The components of the gating system design included:

- The Transpac IV blood pressure transducer
- An amplifier that boosted the blood pressure signal level by 40dB before transmitting it back to the scanner.
- A monitoring board located within the MRI control room that digitized the blood pressure signal, detected the pressure peaks and gated the scanner.
- A computer in the monitoring room that could (optionally) be connected to the monitoring board to display the blood pressure traces overlayed with the gating signals.


## Probe System

In my first prototype of this device, I used the [Samba Preclin pressure transducer](http://harvardbioscience.ca/HAC-Samba.html). These pressure transducers worked well for our application, because the sensing element was fibre optic and composed only of plastic and glass fiber. This meant that the sensor was totally MRI compatible and did not produce any image artifacts.

I was able to get the entire gating system up and running using these pressure transuducers without much trouble. Unfortunately, the fiber optic sensing elements proved to be too delicate and when we started testing and we broke all of our sensors within the first few animal experiments. To add insult to injury, Samba sensors went bankrupt within the same year, so we couldn't order more.

For the second revision, I opted to use the disposable Transpac IV blood pressure transducer produced by ICU medical. These transducers were a great solution, because they're MRI compatible and inexpensive. As shown in their [training video](https://www.youtube.com/watch?v=ryCPqoQK1Rw), the Transpac IV can be connected to a generic arterial catheter and measure the blood pressure that is transmitted through the fluid column in the IV line. 

Internally, the blood pressure works by placing a [strain gauge in the wheatstone bridge configuration](http://www.ni.com/white-paper/3642/en/) in line with the IV fluid column. That means that an amplifier is required to energize the bridge and measure the tiny voltage difference across the strain gauge.

![](/img/projects/pressuretrigger/DSC01234.jpg)

*The probe system and amplifier circuit that I constructed. The line marked arterial would connect to the subject's arterial line. The transpac IV pressure transducer is in the center of the image and connected to the amplifier circuit. The pressure infuser bag provided back pressure against the subject's arterial blood pressure, so that blood would not back feed into the line.*

One of the challenges in this design was that the strain gauge had a parasitic capacitive coupling with the MRI scanner, and it would pick up interference caused by the radiofrequency electric fields used in the imaging process, and by the low frequency (300Hz-10KHz) gradient field switching of the scanner.

In practice it was relatively easy to block out the radiofrequency noise with shielding. The low frequency gradient switching noise was much more challenging. They had to be addressed by placing a differential low pass filter on the input stage of the filter, and using amplifiers that had an exceptionally high common mode rejection ratio.

Anyone interested in the technical details of this amplifier can read the [design report.](/pdfs/SYDE_362_IBP_Measurement_System_Final_Report.pdf). 

## Signal Processing Unit

A typical aortic blood pressure waveform looks like this:
![](/img/projects/pressuretrigger/aortic-pulse-pressure.png)

The signal processing unit had to capture the blood pressure peak, and send a signal to the MRI scanner each time the peak was detected in realtime. For this application *real-time*, meant that there could be a maximum delay of 10ms between the actual physiological blood pressure peak and the signal reaching the MRI scanner. It was also preferable that the delay be systematic, ie the delay between the blood pressure peak and the signal should be as consistent as possible.

To detect the onset of the blood pressure peaks, I modified the algorithm originally presented by W. Zong et al. in [An Open Source Algorithm to Detect Onset of Arterial Blood Pressure Pulses](http://ecg.mit.edu/george/publications/abp-cinc-2003.pdf). The main modifications were to the thresholding scheme. In the original paper, the algorithm was designed to use past and future input (working with recorded data) to determine the blood pressure pulse thresholds. For my purposes, I had to modify the algorithm so that it could come up with thresholds using only past input.

My implementation of this algorithm is [available on github](https://github.com/JoshBradshaw/Arterial-BP-MRI-Triggering-Unit).

## Cabling

Running cabling in the MRI environment is challenging. Cables running across the scan room are a serious ergonomic problem, because clinicians and technicians need to cross the scan room numerous times while transferring the subject onto the table starting the scan process. When compounded with the animal ventilator's tubing and wiring, and multiple IV lines, the scan room was already prone to being a bit of a spider web during experiments. For this reason was highly desirable to minimize the number of cables crossing the room, and make any such cables long enough that they could wind around the edge of the room instead of crossing through the high traffic areas.

Also, the cabling entirely non-ferrous and Faraday shielded. My colleague Jun Dazai at the mouse imaging center uses high end coax produced by Belden, and pure copper BNC fittings produced by Amphenol. In my case this wasn't viable, because I needed to run +15, and -15V power, as well as the two differential signal pairs. 

Instead of using conventional coax, I opted to use HDMI cable. HDMI cable is very cheap, and [some types have been tested for MRI compatibility](http://ieeexplore.ieee.org/document/6551726/?reload=true). HDMI cable is double shielded, and it provides 18 conductors in twisted pairs, which is ideal for minimizing magnetic pickup.

## Monitoring

A piece of software was created to show the blood pressure traces and the gating trigger locations.