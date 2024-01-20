# Python Challenges XXIVb

## OOP #2

Solve the below problem showing usage of OOP principles: inheritance, encapsulation and polymorphism.

---

Define a class called `Device`.

All devices have a battery power and a flag to say whether they are on or off. They need a method to turn off, a method to turn on. The default state is off, but the power is dependent on what device is being created (instantiated). A method named `get_power_state()` returns type: bool representing the current power state of the device.

Define a class called `Phone`. A phone can do everything a device can. But can also `make_call()` - it is not important what is contained inside this at this point. A phone also contains a phone number, which is decided when the Phone is first created.

Define a class called `Computer`. A computer can do everything a device can, but a computer can be a) on, b) off or c) on stand-by. Use the most appropriate data type to store this property and polymorphism to change the functionality of the base class.

Inside the `test()` procedure do the following:

a) Make an instance of a Phone called nokia which has a battery life of 100 and the phone number `"01234567898"`

b) Make an instance of a Computer called `linux`, and another called `mac`. _You can decide the battery power._

c) Demonstrate setting the state of the nokia to **on**, the linux to **stand-by** and the mac to **off**.