---
layout: page
title: 'Skeleprint'
subtitle: 'A 3D Printer for Bone Graft Prototyping'
---

![](/img/projects/skeleprint/thumb.jpg)

Here I present a short and simple explanation of the 3D printer we created. For those who want more technical details about the implementation, I have made the [complete final report](/pdfs/GENE_404_Final_Report.pdf) available.

## Problem

In September 2016, Professor Willett's biomaterials lab had just developed a promising new osteoregenerative and biocompatible material intended for bone graft production. The material was composed of hydroxyapetite and an organic matrix, and was designed to replace load bearing cortical bone in humans.

Professor Willett and his research team performed some preliminary tests with the material. They manufactured it into sample blocks and mechanically tested them to prove the material's suitability for use in bone grafts. Inititially they manufactured the material using a [freeze casting process](https://en.wikipedia.org/wiki/Freeze-casting). Then they progressed to manufacturing the material using a conventional 3D printer, and curing the material in place using high intensity UV light.

Conventional 3D printing  was not suitable for the production of bone grafts, because of the directional anisotropies produced by the 3D printing process. In a conventional 3D printer material is deposited as flat planes, and this style of layering creates inherent planes of weakness in the final product. These planes of weakness make it impossible to print cylindrical bone graft structures using a conventional 3D printer. For our fourth year design project, professor Thomas Willett tasked us with creating a new 3D printing method that would yield stronger cylindrical bone grafts than conventional 3D printing.

## Team

![photograph of the team members](/img/projects/skeleprint/team.jpg)

I built this 3D printer as my fourth year design project with team members Alex Upenieks, [Shubh Jagani](http://www.shubhjagani.com/), [Isaac Hunter](https://isaachunter.ca/), [Kyla Gardner](https://www.linkedin.com/in/kyla-gardner-4a267163/), and [Matt Jones](https://www.linkedin.com/in/matt--jones/) This project was commissioned by and funded by professor Thomas Willett. The project supervisor was Professor [Oscar Nespoli](https://uwaterloo.ca/mechanical-mechatronics-engineering/profile/oscar) from the mechanical engineering department.

## Role

I was the team leader, and responsible for the robot's controls and firmware design. This means that I was responsible for the electronics and actuators that controlled the printer's motions, and the extrusion system. I also designed the printer's frame.

## Workflow

Early in the build process, it was unclear how to improve the 3D printing process to create a stronger bone graft. We decided to use the lab's existing 3D printer, UV laser, and mechanical testing machine to create some flat test prints and compare their strength. At this point we were not trying to create cylindrical bone grafts, our goal was simply to evaulate different printing modalities. By making these simple flat test prints, we discovered that the material was strongest when the layers were were printed in opposition, similar to the alternating grain direction in plywood. The grain structure of plywood is illustrated below.

![Plywood grain structure illustration](/img/projects/skeleprint/UnderstandWood5.jpg)

Given that our goal was to print cylindrical bone grafts. We had to adapt the structure. Instead of printing flat layers with alternating grain structure, we needed to create cylinders. We opted to do this by depositing each layer as a series of helices on a rotating mandrel. Each layer is deposited by laying down a helix, shifting the print head slightly, and then laying down more adjacent helices until they form a complete cylindrical layer.


## First Prototype

We build the first prototype to figure out if extruding the ink onto a rotating mandrel was a workable concept. We opted to simply place a rotating mandrel into an existing cartesian 3D printer and use it to print some helical layers. A photograph of one of the early tests is shown below.

![Plywood grain structure illustration](/img/projects/skeleprint/prototype1.jpg)

## Specifications

Professor Willett's intention for this 3D printer was to use it to create bone graft samples for mechanical testing and verification. With this goal in mind, the accuracy and repeatability of the printer were both extremely important. The accuracy specifications for the final printer prototype were defined over the full scale range of the axis, and they are summarized in the error budget below.

### Resolution Requirements

Resolution Specification | Value (microns)
Radial | < 25 
Axial  | < 25 
Rotational | < 100 

### Error Budget

Resolution Specification | Value (microns) | Full Scale Range (mm)
Radial  | < 150 | 6000
Axial | 100 | 22000
Rotational | 200 | $2 \pi radians$ 

## Final Printer Prototype

A demo of the final printer prototype printing its first layer is shown below. This video clearly illustrates how the printer builds up cylindrical layers out of helices.

<div class="videoWrapper">
    <!-- Copy & Pasted from YouTube -->
    <iframe src="https://www.youtube-nocookie.com/embed/Q3a447J2GTI?rel=0" frameborder="0" allowfullscreen></iframe>
</div>


## Results

The final printer was fully functional. We presented it at two design symposiums and won the Baylis Medical Capstone Design Award. After we graduated, professor Willett hired two co-op students to 3D print bone grafts and evaluate their performance in a formal manner. 