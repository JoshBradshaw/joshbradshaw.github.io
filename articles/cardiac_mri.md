---
layout: page
title: 'Cardiac MRI'
subtitle: 'An introduction to image aquisition and reconstruction'
---

## Introduction to Cardiac MRI

Imaging the heart using MRI requires a very different process than imaging a static structure such as the brain or the knee. This is because magnetic resonance imaging (MRI) is a relatively slow imaging method. With current technology, the very fastest imaging protocols that generate clinically useful images require several seconds of data acquisition. Other imaging methods such as x-ray or CT scans produce images much more quickly. For the purposes of this article we will focus specifically on cardiac motion studies, as opposed to other types of chest and abdominal imaging.

The long image acquisition times involved in MRI are problematic for imaging dynamic structures such as the heart, because when the anatomy moves during the acquisition large ghosting artifacts appear on the image. An example of image ghosting is shown below: 

![Image ghosting example. The image contains two pictures of a woman walking across the frame. In the left image her limbs are very blurry, which is a type of ghosting artifact. In the right image she is not ghosted, this is the original.](/img/projects/pressuretrigger/ghosting.jpg)

The rapid motion of the heart combined with the slow rate of data acquisition means that MRI images of the heart are nothing but a blurry mess unless special techniques are used to counteract the motion. 

## Goal of Cardiac MRI

The goal of a cardiac MRI scan is produce a is a series of images, showing the heart at different phases of the cardiac cycle. An example of some freeze frames taken at different points in the cardiac cycle are shown below:

![](/img/articles/cardiacmri/CINE_Frames.jpg)

These frames can be played in series to show a movie of the cardiac cycle, which is called a CINE:

![](/img/articles/cardiacmri/cardiacmricine.gif)

For the remainder of this article, I will give a basic explanation of how these CINE images are produced by combining data collected from many heartbeats to overcome the cardiac motion problem. There are several techniques for dealing with cardiac motion, but the one we will discuss here is retrospectively gated MRI.

### Some terminology

- **MRI acquisition** - the period in which the MRI scanner is running and collecting image data
- **Cardiac phase** - cardiac phase is the timing of cardiac motion. The cardiac cycle repeats with each heartbeat, moving through diastole (filling with flood), then systole (contraction).
- **Raw data** - these are the measurements that the MRI scanner makes that are eventually transformed into an image by a reconstruction algorithm.
- **Image reconstruction** - a process that converts the raw data captured by the MRI scanner and transforms it into an image.

## Retrospectively Gated MRI Acquisitions

Retrospectively gated MRI gets its name because the *MRI scanner does not react to the motion of the heart during the image aquisiton period*. Instead, the MRI scanner executes a long image aquisition sequence in which it aquires all of the raw data it needs to construct the image many times. Only during the image reconstruction process is the cardiac cycle *retrospectively* accounted for.

In a retrospectively gated cardiac MRI acquisition, the cardiac motion problem is overcome by imaging the heart repeatedly for a long period of time and capturing raw data from many different heartbeats. The idea is that while the MRI scanner does not have enough time to capture a complete set of raw data during any single heartbeat, a complete set of raw data can be assembled by combining and reordering data captured during many different heartbeats This technique is generally very reliable, except in the case of cardiac arrythmia. 

In order to be able to reconstruct an image of a single heartbeat from raw data captured during many heartbeats, a synchronization signal is required. In other words, the MRI scanner needs to be able to record what position the heart was in while it was collecting the raw data measurements. This synchronization signal is typically called a gating signal or triggering signal. The gating signal must correspond directly to the cardiac cycle. The most commonly used gating signal is the R-wave of ECG, but the peak of arterial blood pressure can also be used. It is also possible to generate the gating signal directly from the image data using a technique called metric optimized gating, but that's an advanced technique beyond the scope of this article. We will assume an ECG gating signal. In practice, this gating signal is measured by connecting three or four ECG leads to the patient while they lay in the MRI scanner.

This synchronization signal is usually called the **gating signal**, or *triggering signal*. The MRI scanner uses the gating signal to organize the data into bins, and the data from those bins is combined during image reconstruction. The raw data in each bin is associated with a single frame of the CINE. 

To visualize this process, an ECG gating signal is shown below. Below the ECG signal, there are five colour coded bins.  Typically a CINE would use more frames than this, but five bins are enough to explain the concept. During the image reconstruction, the raw data that was captured during the continuous acquisition is grouped into these bins. Given that the MRI acquisition is continouous, there will generally be some redundant data captured. This redundant data can be averaged, or simply discarded. 

![CINE MRI IMAGE](/img/articles/cardiacmri/Cardiac_MRI_Binning.jpg)

Once all of the data has been binned, the data in each bin is reconstructed into a single two dimensional image that makes up a single frame of the CINE. 

## Summary

To recap, retrospectively gated cardiac MRI uses a prolonged image aquisition sequence in which all of the raw data required to reconstruct and MRI image is collected many times. After the acquisition is complete, the data is reordered and sorted based on when it was aquired relative to the cardiac phase of the heart. Data that was collected during the same cardiac phase (but potentially from different heartbeats) is grouped together into bins. The data from each of these bins is reconstructed to produce a single frame of the heart. When all of the reconstructed images are arranged in sequence, they make up an animation of the cardiac cycle called a CINE.

## Further Reading

In this article, the question of what MRI raw data is, and how it is measured were ignored for the sake of simplicity. For readers who are interested in learning a little bit more about how MRI works without delving directly into quantum physics, I recommend [clinical cardiac MRI](http://www.springer.com/cn/book/9783642230349). Another good resource is [questions and answers in MRI](http://mriquestions.com/index.html).

## References
- [Bishop J et al. Retrospective gating for mouse cardiac MRI. Magnnetic Resonance in Medicine. 2006 Mar;55(3):472-7.](https://www.ncbi.nlm.nih.gov/pubmed/16450339)
- [Grace M. Nijm et al. Comparison of Self-Gated Cine MRI Retrospective Cardiac Synchronization Algorithms. Journal of Magnetic Resonance Imaging 2008 Sep; 28(3): 767–772.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2597286/)
- [MRI techniques for Cardiovascular Imaging](http://www.indiana.edu/~mri/seminars/slides/Cardiovascualr%20MRI%2020111015.pdf)