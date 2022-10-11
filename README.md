# OBS_SCTE

## DISCLAIMER
**--THIS IS A PROTOTYPE AND THERE ARE MANY SETTINGS THAT CAN BE TWEAKED AND CHANGED THAT MAY WORK BETTER FOR DIFFERENT SITUATIONS--**

## Overview

This project uses [TSduck](https://tsduck.io/) to inject SCTE-35 with an OBS trigger.
SCTE is a protocol that is used by many broadcast systems for inserting dynamic ads.
TSduck is an open source project that runs in a CLI (Command line interface) for deploying and testing MPEG Transport Streams.
We use the python script inside of OBS to send the trigger over udp to TSduck to insert the SCTE

## Basic Road Map

There is a roadmap for the ts stream and a roadmap for the SCTE data

> ### Transport Stream
> 1. OBS streams to TSduck over SRT
> 2. SCTE is injected into stream
> 3. TSduck outputs to a .ts file
---
> ### SCTE data
> 1. TSduck opens a udp server to listen for XML file
> 2. OBS sends XML string over udp when scene triggers
> 3. TSduck inject SCTE data into stream

## Installation

- Install TSduck for your specific operating system (TSduck goes further into detail per operating system)
- Make sure python 3.6 is used in OBS and import obs.py into the scripts of OBS
- The current setting for OBS stream is `srt://127.0.0.2:9999?mode=listener&transtype=live&latency=3000000&ffs=128000&rcvbuf=100058624` but feel free to change them, this is just what is working for us

