## Lorenz Attractor

This is an excellent demonstration of an **analog computer**, taken from an outstanding lesson
by Professor [Paul Horowitz](https://youtu.be/DBteowmSN8g?si=P4ycZDwNGiXzkuB8).  
The Lorenz attractor arises as the solution to a set of three coupled nonlinear differential equations, which, for certain values of
the parameters, a, b, and c, exhibit chaotic behaviour [1](https://en.wikipedia.org/wiki/Lorenz_system). 

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/equations.JPG" alt="Lorenz attractor equation" style="width:40%;"/>

## Analog Computer

The differential equations are solved using an analog computer implemented as an electronic circuit.  
Integration is performed by operational amplifiers (op-apmps) whith capacitors in their feedback loop, and the integrated signals are
multiplied using an MPY634 multiplication IC. Here is the circuit that represents the solution to the differential equations.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/lorenz_ckt_640.jpg" alt="Lorenz attractor scheme" style="width:80%;"/>

## Experimental Setup
I used two Texas Instruments general-purpose µA741CP op-amps and one TI LF411 instead of the original LF412, and, instead of the more expensive
MPY634, I used two Analog Devices AD633JNs. I also used two precision potentiometers to adjust the values of resistors R3 and R7. Here is a
picture of the circuit assembled, along with the power supply and oscilloscope.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/circuit.JPG" alt="Lorenz attractor circuit" style="width:90%;"/>

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/setup.JPG" alt="Lorenz attractor setup" style="width:50%;"/>

## Python Script

One can also model the response of this system of differential equations using a Python script (**lorenz.py**) which uses the SciPy
module **odeint** to solve ordinary differential equations.

<img src="https://github.com/Analog741/Lorenz-Attractor/blob/main/pictures/traj.png" alt="Lorenz attractor setup" style="width:60%;"/>


## Credits
Professor Paul Horowitz website:  

http://seti.harvard.edu/unusual_stuff/misc/lorenz.htm  

[The Art of Electronics 3rd Edition, P. Horowitz and W. Hill, Cambridge University Press 2015.](https://www.cambridge.org/us/universitypress/subjects/physics/electronics-physicists/art-electronics-3rd-edition)
