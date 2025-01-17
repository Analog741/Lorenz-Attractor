## Lorenz Attractor

This is a great demonstration of an **analog computer**, taken from a very nice lesson
from professor [Paul Horowitz](https://youtu.be/DBteowmSN8g?si=P4ycZDwNGiXzkuB8).  
The Lorenz attractor araises as the solution of a set of three coupled non-linear differential equations which for some set of
parameters, a, b, and c, will exhibit a chaotic behaviour [1](https://en.wikipedia.org/wiki/Lorenz_system). 

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/equations.JPG" alt="Lorenz attractor equation" style="width:40%;"/>

## Analog Computer

The differential equations are solved using an analog computer implemented as an electronic circuit.  
Integration is done by operational amplifiers (op-apmps) whith capacitors in their feedback loop and the integrated signals are
multiplied using an MPY634 multiplication IC. Here is the circuit which represents the solution to the differential equations.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/lorenz_ckt_640.jpg" alt="Lorenz attractor scheme" style="width:80%;"/>

## Experimental Setup
I used two 741 op-amps  LF411 ICs instead of the original LF412 and instead of the more expensive MPY634, I used an AD633.   
Here is a picture of the circuit built together with the power supply and oscilloscope.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/circuit.JPG" alt="Lorenz attractor circuit" style="width:90%;"/>

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/setup.JPG" alt="Lorenz attractor setup" style="width:50%;"/>

## Python Script

One can also model the response of this system of differential equations using a Python script (**lorenz.py**) which usess the SciPy
module **odeint** to solve ordinary differential equations.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/traj.png" alt="Lorenz attractor setup" style="width:60%;"/>


## Credits
Professor Paul Horowitz website:  

http://seti.harvard.edu/unusual_stuff/misc/lorenz.htm  

[The Art of Electronics 3rd Edition, P. Horowitz and W. Hill, Cambridge University Press 2015.](https://www.cambridge.org/us/universitypress/subjects/physics/electronics-physicists/art-electronics-3rd-edition)
