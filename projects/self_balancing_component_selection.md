---
layout: page
title: Self Balancing Robot
subtitle: Hardware Design
date: December 27, 2017
---

Over the winter break my I decided to build a self-balancing robot. Self-balancing robots are classic robotics problem that forces you to work with mechanics, electronics, software and control theory. 

## Goal

The goal was to create a self balancing robot that was capable of driving forward, backwards, turning and going up and down gentle slopes. We did not want our project to be too derivative. We wanted to design the hardware and software ourselves.

## Theory of Operation

![](img/projects/invertedpendulum/cart_pendulum.png)

Self balancing robots are a variation on the classic [inverted pendulum problem](https://en.wikipedia.org/wiki/Inverted_pendulum#Essentials_of_stabilization). The mathematics are actually described very clearly on wikipedia, so I won't rehash them here. 

This is a highly unstable and non-linear system. Making the robot move backwards and forwards is a particularly challenging problem.

## Component Selection

This project was just for fun, so the two primary requirements for the components were that they should be simple and cheap.

I chose:

1. IMU: MPU6050 
2. Motors: Generic Nema-17 Steppers
3. Motor Drivers: DRV8225
4. MCU: Teensy 3.2
5. Communication: Electronic Brick HC06 Serial Bluetooth Module (Slave)
6. DC-DC Converter: LM2596
7. Battery: 11.1V 2200mAh LiPo Battery w/ Star Plug

## Component Selection Rationale

The reason we decided to choose these particular components, was mainly to avoid common pitfalls that I observed in other self-balancing robots. Using stepper motors makes it easy to make the wheels move in synchrony, so the robot will not turn unintentionally. Stepper motors also make it easy to implement a second order velocity loop.

I chose the 