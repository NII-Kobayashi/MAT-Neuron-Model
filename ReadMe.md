# Simulating a firing pattern of a neuron using the Multi-timescale Adaptive Threshold (MAT) model

This is the code illustrating the *Kobayashi, Tsubo and Shinomoto (2009)* and aims at reproducing a continuous variety of the firing characteristics with three parameters. The paper is available [here](https://www.frontiersin.org/articles/10.3389/neuro.10.009.2009/full).

## Requirements
- Python 3
- Matplotlib

## Getting started
The git repository can be cloned by simply using:

    git clone　https://github.com/NII-Kobayashi/MAT-Neuron-Model.git

## Usage
This directory has a code: "MAT.py".

You can run this code to produce spike times:

    python3 MAT.py <input_current> alpha1 alpha2 omega

where <input_current> is the file of the input current, alpha1 and alpha2 are the weights of the time constraints and omega is the resting value. The sampling interval of the input current is fixed at 0.1 ms.

Typical parameters for RS, IB, FS and CH neurons are as follows:
- RS neuron: alpha1 = 30, alpha2 = 2.0, omega = -45
- IB neuron: alpha1 = 7.5, alpha2 = 1.5, omega = -46
- FS neuron: alpha1 = 10, alpha2 = 0.2, omega = -55
- CH neuron: alpha1 = -0.5, alpha2 = 0.4, omega = -39

This directory also has a sample file of the input current: "current_sample.txt".

For example, you can get the same result  as the case of the RS neuron of Figure 5B in [*Kobayashi, Tsubo and Shinomoto (2009)*](https://www.frontiersin.org/articles/10.3389/neuro.10.009.2009/full):

    python3 MAT.py current_sample.txt 30 2.0 -45

After running the code, you will obtain four output files: "spiketime.txt", "voltage.txt", "spike.png" and "spike.eps".
- spiketime.txt: time [ms], model potential [mV]
- voltage.txt: spike time [ms]
- spike.png and spike.eps: figures of spikes

## License
This project is licensed under the terms of the MIT license.

Please contact [Ryota Kobayashi](http://research.nii.ac.jp/~r-koba/en/contact.html) if you want to use the code for commercial purposes.

## The program was developed by
Yuichiro Marui
