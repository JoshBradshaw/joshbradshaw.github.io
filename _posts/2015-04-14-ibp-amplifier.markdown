---
layout: post
title:  IBP Transducer Amplifier Build
date:   2015-04-14 22:48:45
description: Quick post describing the design process for an MRI compatible IBP transducer amplifier, which I built hastily in preparation for an experiment.
categories:
- Instrumentation
- MRI
---

NOTE: THIS BLOG POST IS STILL UNDER CONSTRUCTION, PENDING APPROVAL TO PUBLISH THE FIGURES

This is the last week of my co-op term at SickKids, so I decided to tackle a fun little project. The goal was to interface the Transpac IV invasive blood pressure transducer with my invasive blood pressure triggering unit. The Transpac IV is marketed as being 'MRI compatible' which is a slightly misleading term, because MRI compatibility means only that the sensor is safe to operate in the MRI scanner, not that it will function or operate within its specifications.

The Transpac IV is dead simple. Its just a Wheatstone bridge pressure transducer, with four variable resistive elements. The datasheet for the transducer that Transpac uses is available here.



I measured each of the bridge elements on one of my Transpac IV samples and the resistance values in the sensor's zeroed-state were all 384 ohms.

Given that I only needed to build a single unit, and cost wasn't really an object, I opted to amplify the transducer using an instrumentation amplifier. The first circuit I tested is shown below.

[insert figure of the first circuit schematic and explanation]

I tested this circuit by connecting the Transpac IV to an expired IV bag, and using the largest graduated cylinder I could find filled with distilled water as a pressure reference. The results of my test are shown below.

Next, I tested the MRI compatibility of my system by accompanying Chris Roy down to the Siemens 3T MRI scanner. Chris had some long phase contrast scans to run, so I built up the same testing setup as described above, except that the Transpac and the amplifier were within 4' of the MRI scanner. I couldn't bring my oscilloscope into the MRI, so I placed it against the window in the control room and used a high quality piece of coax to connect to the amplifier. 

I performed the exact same test as before, and the amplifier's performance was indistinguishable from the bench test, until the MRI scanner's gradient coil was activated. When the MRI scanner began sending gradient pulses, the amplifier showed DC offset errors at the moment at which the pulse was fired. The most noticeable effect occurred when the localizers were fired (for those unfamiliar with MRI, the pulses are clearly distinguishable by listening to the noises that the scanner makes).

To reduce the effect of the MRI scanner's RF interference I revised the circuit to have an RF filter on the input, and used an instrumentation amplifier that's better for RF applications.

[insert figure for second circuit]

I built this circuit and tested it in the MRI.