# NE 204 Report Lab0

This repo contains all the files necessary to build the lab report for NE 204 Lab O

# Energy Calibration

Data was collected with a Coaxial HPGe detector with Co-60, Am-241, and Eu-152 sources.

A python script was written to conduct a two-point linear energy calibration using the 59.541 keV peak from 241Am and
the 661.657 keV peak from 137Cs, to apply the linear calibration model to the 133Ba dataset, and quantify the difference between
the calibrated peak locations and the expected peak locations based on the literature.

Instructions for running the lab report are posted below:

## File instructions

### Downloading the data

Use the makefile to download the data for the lab:

```
make data

```
### Validate data is not corrupted

```
make validate
```

### Run Test on analysis code

```
make test
```

### Generating the final report in pdf format

```
make
```
