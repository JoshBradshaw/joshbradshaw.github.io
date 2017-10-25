---
layout: page
title: 'PressureTrigger'
subtitle: 'A cardiac MRI triggering system for use in animal imaging experiments'
---

![](/img/projects/pressuretrigger/DSC01219.jpg)

*The blood pressure amplifier and digital signal processing (DSP) module*

## Problem

At SickKids Hospital a massive amount of animal research is conducted. SickKids has several labs that focus predominantly on animal imaging. MRI imaging is used in a significant amount of animal research. MRI particularly useful for cancer research and research on blood circulation, because MRI has adaptable contrast that can be used to differentiate between soft tissues, measure blood flow, and numerous other measurements that are impossible with other imaging modalities.

Imaging animal circulation and cardiac motion in MRI is complicated by the fact that a gating signal is required to synchronize the MRI acquisition with the cardiac cycle. I explained the details of cardiac gating in my [introductory article on cardiac MRI](/articles/cardiac_mri). Over the years our labs have created several [specialized gating apparatusess](http://www.mouseimaging.ca/publications/assets/archive/2006%20MRM%2055%20Bishop.pdf) to handle the unique requirements imposed by particular animal imaging experiments.

The particular problem in this case was that animals needed cardiac MRI imaging as part of a study that included heart surgery, and the experimental setup prohibited the use of conventional ECG electrodes. Instead we needed some way to gate the MRI scanner based on arterial blood pressure. The basic surgical procedure already involved inserting a catheter into the aorta, so that was the site where we needed measure the arterial blood pressure from.

The researchers also wanted to be able to use the gating blood pressure probe to measure blood pressure to within 1 mmHg, so that they could use the blood pressure measurements for monitoring the subject. This meant that the blood pressure probing system had to be a calibrated sensor.


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
* The only permissible place to run cabling in between the MRI scanner room and the control room was through a 3" diameter waveguide.


## Probe System

For the pressure probe, I opted to use the disposable Transpac IV blood pressure transducer produced by ICU medical. These transducers were a great solution, because they're MRI compatible and inexpensive. As shown in their [excellent training video](https://www.youtube.com/watch?v=ryCPqoQK1Rw), the Transpac IV can be connected to a generic arterial catheter and measure the blood pressure that is transmitted through the fluid column in the IV line. 

Internally, the blood pressure works by placing a [strain gauge in the wheatstone bridge configuration](http://www.ni.com/white-paper/3642/en/) in line with the IV fluid column. That means that an amplifier is required to energize the bridge and measure the tiny voltage difference across the strain gauge.

![](/img/projects/pressuretrigger/DSC01234.jpg)

*The probe system and amplifier circuit that I constructed. The line marked arterial would connect to the subject's arterial line. The transpac IV pressure transducer is in the center of the image and connected to the amplifier circuit. The pressure infuser bag provided back pressure against the subject's arterial blood pressure, so that blood would not feed into the line.*

One of the challenges in this design was that the strain gauge had a parasitic capacitive coupling with the MRI scanner, and it would pick up interference caused by the radiofrequency electric fields used in the imaging process, and by the low frequency (300Hz-10KHz) gradient field switching of the scanner.

In practice it was relatively easy to block out the radiofrequency noise with shielding. The low frequency gradient switching was much more challenging. They had to be addressed by placing a differential low pass filter on the input stage of the filter, and using amplifiers that had an exceptionally high common mode rejection ratio.

Anyone interested in the technical details of this amplifier can read the [design report.](/pdfs/SYDE_362_IBP_Measurement_System_Final_Report.pdf). 

## Signal Processing Unit

A typical aortic blood pressure waveform looks like this:
![](/img/projects/pressuretrigger/aortic-pulse-pressure.png)

The signal processing unit had to capture the blood pressure peak, and send a signal to the MRI scanner each time the peak was detected in realtime. For this application *real-time*, meant that there could be a maximum delay of 10ms between the actual physiological blood pressure peak and the signal reaching the MRI scanner. It was also preferable that the delay be systematic, ie the delay between the blood pressure peak and the signal should be as consistent as possible.

To detect the onset of the blood pressure peaks, I modified the algorithm originally presented by W. Zong et al. in [An Open Source Algorithm to Detect Onset of Arterial Blood Pressure Pulses](http://ecg.mit.edu/george/publications/abp-cinc-2003.pdf). The main modifications were to the thresholding scheme. In the original paper, the algorithm was designed to use past and future input (working with recorded data) to determine the blood pressure pulse thresholds. For my purposes, I had to modify the algorithm so that it could come up with thresholds using only past input.

My implementation of this algorithm is [available on github](https://github.com/JoshBradshaw/Arterial-BP-MRI-Triggering-Unit).

## Monitoring

A piece of software was created to show the blood pressure traces and the gating trigger locations.