## Lorenz Attractor

This is a great demonstration of an **analog computer**, taken from a very nice lesson
from professor [Horowitz](https://youtu.be/DBteowmSN8g?si=P4ycZDwNGiXzkuB8).  
This is a set of three coupled linear differential equations which for some set of parameters, a, b, and c, will exhibit
a chaotic behaviour [1](https://en.wikipedia.org/wiki/Lorenz_system). 

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/equations.JPG" alt="Lorenz attractor equation" style="width:40%;"/>

## Analog Computer

The analog computer is implemented in a circuit. Integration is done by operational amplifiers whith capacitors in their feedback
loop and the integrated signals are multiplied using an MPY634 multiplexer. Here is the equivalent circuit.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/lorenz_ckt_640.jpg" alt="Lorenz attractor circuit" style="width:40%;"/>

## Experimental Setup
I used LF411 ICs instead of the original LF412 and instead of the more expensive MPY634, I used an AD633. Here is a picture of the circuit I built together
with the power supply and oscilloscope.

![Lorenz attractor circuit](https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/circuit.JPG)

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/setup.JPG" alt="Lorenz attractor setup" style="width:50%;"/>

## Python Script

One can also model the response of this system of differentail equaations using a Python script (lorenz.py) and the SciPy module to solve ordinary 
differential equations.

![Lorenz attractor solution](https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/traj.png)

## Credits
Proffesor Horowitz website:  

http://seti.harvard.edu/unusual_stuff/misc/lorenz.htm
