---
layout: page
title: Bloodtools
subtitle: An open-source tool for MRI image analysis
---

This project is open-source and [available on Github](https://github.com/JoshBradshaw/bloodtools).

![](/img/projects/bloodtools/thumb.jpg)

*The bloodtools image processing tool. The test image shown here is a 2D slice accross a warming bath filled with vials of blood.*

## Background

In spring 2016 I was working with Sharon Portnoy on the final experiments of her PHD in the experimental medicine department at SickKids Hospital. Her PHD involved the [development of a method for measuring the oxygen saturation and hematocrit of fetal blood using MRI.](http://onlinelibrary.wiley.com/doi/10.1002/mrm.26599/abstract) This new measurement technique was useful, because it allowed radiologists the opportunity to diagnose congenital heart defects before birth that would otherwise be impossible to detect so early.

Measurement of blood oxygen saturation and hematocrit in MRI is accomplished using a technique called MR relaxometry. In relaxometry, the MRI scanner is used to measure the material's longitudinal and transverse magnetization recovery times, which are called T1 and T2 respectively. 

The measurement protocol involved:

1. Imaging the fetal heart using a specialized MRI acquisition sequence designed to capture a series of images of the blood vessel under study. These image series were specially calibrated such that they could be used to determine the T1 and T2 times of the blood in that vessel.
2. Opening each calibrated image series of the blood vessel in question and drawing regions of interest (ROIs) around the blood contained there.
3. Running a script that extracted the intensity value of each pixel in region of interest, and used a fitting algorithm to determine the T1 or T2 decay curve of the blood in the vessel.
4. Solving a system of equations to determine the blood oxygen saturation and hematocrit values that corresponded to the T1 and T2 recovery times of the tissue.

## Problem

Once the measurement protocol for blood oxygen saturation and hematocrit had been established and verified by Portnoy, a clinical research group at the hospital wanted to begin using it for experimental imaging. Their plan was to image women with high risk pregnancies, and use the measurements to estimate whether the fetuses exhibited a range of conditions including fetal anemia, hypoxia, and congenital heart defects.

While the clinical researchers were highly skilled at identifying anatomy in MRI, they did not have the software acumen to carry out the measurement protocol using the scripts that the researchers were using. It was necessary to create a commercialized version of the measurement procedure that made it as simple as possible to carry out the measurements and do the analysis while keeping up with the demanding pace of the clinical setting.

## Display Design

To design the analysis tool, I spent a day shadowing the clinical researchers while they were scanning a pregnant volunteer. I observed the way they went about locating the fetal blood vessels, and took notes on how they organized and saved the image files. During these sessions, I discovered that fetal blood vessels are difficult to spot, and that the researchers often make use of image windowing and artificial color to locate the smaller vessels. Artificial color is useful, because it makes flowing blood stand out against the background more.

Based on these observations, I built a tool that allowed the researchers to pan through the images. To make the process as efficient as possible, the image was displayed in both greyscale and  artificial color side by side. They could zoom into or pan around either image, or change the windowing to enhance the contrast.

## ROI Drawing

The researchers task was to draw a region of interest on each slice of the image series. The ROI had to encompass the blood, but not the vessel wall or the surrounding tissues. Each image in the T1 or T2 measurement series was captured with a delay of 20-100ms, which meant that in some series fetal motion would cause the blood vessel location to differ slightly in each slice. 

To handle image series with fetal motion, I made it possible for the clinical researchers to draw separate ROIs on each individual slice if necessary. They could also exclude slices if 1-2 slices of the acquisition were invalid. This was sometimes necessary if the fetus rolled out of frame towards the end of the acquisition.

The ROIs could be circular, elliptical or freeform. The circular and elliptical options were useful for drawing ROIs in blood vessels, while the freeform option was ideal for measuring pools of blood in the ventricles of the heart.

After drawing an ROI on either the grayscale or colorized image, it would automatically be mirrored over to the other display. If the image series was not affected by fetal motion, the ROI could be mirrored to all of the slices in the image series by selecting ALL SLICES.

## Fitting

The T1 and T2 fitting engine has two modes of operation. It can either run a simple least squares fit using the average intensity of each ROI, or it can perform [statistical bootstrap fitting](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) to give a more accurate fit and an uncertainty measure.

## Calculation of Blood Oxygen Saturation and Hematocrit

![](/img/projects/bloodtools/calculator.jpg)

To make it easier for the clinical researchers to solve the system of cubic equations required to compute blood oxygen saturation and hematocrit. Given a measurement of T1, T2, blood oxygen saturation, or hematocrit, the calculator can take any two measurements and output the other two using Portnoy's model of fetal blood properties. 

A full description of the calculator and how to interpret its results is available in the [user manual](/pdfs/calculator_manual.pdf).