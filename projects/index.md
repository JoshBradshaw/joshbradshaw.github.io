---
layout: page
title: Projects
subtitle: my personal and academic project showcase
---

This is a collection showcasing my personal and academic projects, as well as a few professional projects for which I have permission to share some project details.


---

## The Hospital for Sick Children

During university I did two co-op terms at the Hospital for Sick Children (SickKids) under the supervision of [Dr. Chris Macgowan](http://www.sickkids.ca/AboutSickKids/Directory/People/M/christopher-macgowan-staff-profile.html). While I was working there, Dr. Macgowan was primarily focused on fetal cardiac imaging using MRI.

- **[PressureTrigger: an MRI cardiac triggering system.](pressuretrigger)** One of the major challenges in cardiac MRI is synchronizing the relatively slow MRI aquisition with the patient's cardiac MRI. During my internship at the hospital for Sick Children, I was tasked with building a system that would use surgically implanted blood pressure probes to trigger the MRI scanners in real time. The system was required to be completely MRI compatible, have a maximum latency of 10ms, and be endlessly reusable without having to dispose of expensive components after surgery.

- **[Bloodtools: an image processing suite for real time fetal MRI analysis.](bloodtools)** During my second co-op term at the Hospital for Sick Children, I was assigned to assist [Sharon Portnoy](http://www.mouseimaging.ca/about/contact.html). Her research focused on developing a practical MRI aquisition protocol that would allow radiologists to non-invasively measure fetal blood oxygen saturation and hematocrit. When I arrived, her work was ready to enter the clinical testing phase. Bloodtools is a simple tool that implements some of the image processing and image analysis methods that Portnoy developed, and allowed the radiology team we were working with to do some basic data analysis while they were imaging the patients.

## Academic Projects

Throughout my engineering degree I strived to create an elaborate final project for each course. In systems design engineering at the University of Waterloo, there are two semester long team design projects in third year and a cumulative project that spans both terms in fourth year. Both of the design projects that I led in third year won their respective design symposiums. In addition, my team's cumulative 4th year design project won over $10,000 in three separate awards. My most interesting and screen friendly projects are listed here.

- **[Skeleprint - A 3D printer for bone graft prototyping](skeleprint)** was my award-winning fourth year design project at the University of Waterloo. We created Skeleprint as a novel approach to bone graft manufacturing. The printer was designed to work with a new biocompatible material developed by [Professor Thomas Willett's Biomaterial's lab](https://uwaterloo.ca/systems-design-engineering/people-profiles/thomas-willett). I worked on this project with team members Alex Upenieks, [Shubh Jagani](http://www.shubhjagani.com/), [Isaac Hunter](https://isaachunter.ca/), [Kyla Gardner](https://www.linkedin.com/in/kyla-gardner-4a267163/), and [Matt Jones](https://www.linkedin.com/in/matt--jones/). I was the team leader, and I did the majority of the hardware and firmware design for the printer itself.

- **[MRI Compatible Amplifier for Invasive Blood Pressure Probes](/pdfs/SYDE_362_IBP_Measurement_System_Final_Report.pdf)**. As my third year design project, I decided to build an extension upon the cardiac gating MRI triggering system that I built for the Hospital for Sick Children during my internship. In the original system, I used a high end blood pressure transducer from Samba sensors that cost ($13,000), because the lab happened to already have one in stock. After my internship, the Samba unit started to malfunction, so I decided to try building a simpler low cost alternative in the ($150-300) price range. I was sucessful, and this amplifier has been used in several published experiments.

- **[SMRT WATR: An Interative Water Fountain](projects/smrtwatr)** was my third year design project. Our goal was to use internet of things (IOT) technology to provide entertainment encourage social interaction in public spaces. I worked on this project with [Emma Cooper](https://www.linkedin.com/in/emmamcooper/), [Matt Jones](https://www.linkedin.com/in/matt--jones/), [Isaac Hunter](https://isaachunter.ca/), [Adam Thompson](http://adamthompson.ca/), and Shubh Jagani. Based on this goal, we decided to create a mechanized water fountain which would react dynamically while users played an online quiz game. We managed to create a fully functional (if somewhat leaky) protoype, complete with four moving water jets, and a great deal of software controllable LED lighting.

- **[Neural Simulation of Lamprey Swimming](../pdfs/LampreySwimming.pdf)** this was my final project for [SYDE 556 - Simulating Neurobiological Systems](http://compneuro.uwaterloo.ca/courses/syde-750.html). As an extension of a [paper published by Dwight Kuo and Chris Eliasmith](http://arts.uwaterloo.ca/~celiasmi/Papers/kuo.eliasmith.2004.zebrafish%20swimming.neuroc.pdf) I derived a model for the spinal cord motion of the swimming lamprey and implemented it in python using the Neural Engineering Framework.

- **[Non-contact EEG Electrodes](projects/noncontacteeg)** this was my final project for [SYDE 444 - Biomedical Measurement]. This was a relatively straightforward project, our goal was to implement the wireless non-contact EEG/ECG measurement system published by [Yu M. Chi and Gert Cauwenberghs](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.423.7050&rep=rep1&type=pdf), and evaluate its performance. To add some challenge, we attempted to cut the overall cost of manufacture of the device in half.

## Crowdlab at the University of Waterloo

- **[crowdEEG Annotation Interface.](http://crowdeeg.ca/)** I was the initial developer of crowdEEG, an online EEG annotaion interface that is used to crowdsource EEG anotation tasks. Crowdsourcing EEG anotation is desirable for building machine learning data sets.

## Electronic Art

- **[Dynamic Infinity Mirror](infinitymirror).** I built a simple square infinity mirror as a Christmas present for my friend.