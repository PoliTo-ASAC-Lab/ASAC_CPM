# FI-playground

Code and documentation for FPGA/MPSoC cluster management architecture, to be used for testing purposes or extensive fault injection campaigns. It can be easily adapted to be used with other kinds of board composing the cluster, like Arduino, Raspberry-Pi, others.

------

## HW Setup

The overall setup requires low-cost components only and can be easily adapted and scaled based on necessity. To manage the power supply of the cluster nodes (ON/OFF) a set of relay switches is controlled by a [NodeMCU Lua Lolin V3 Module](https://www.az-delivery.de/en/products/nodemcu-lolin-v3-modul-mit-esp8266), implementing a user interface accessible through USB-serial connection.
Here below is the general scheme of the hardware setup:



![Picture1](https://github.com/danirizziero/FI-playground/assets/37268662/8c61bbd2-a9d0-40e4-949e-3d9695153d4c)
Here below the details about the NodeMCU module pin usage:

![pinout_detail](https://github.com/danirizziero/FI-playground/assets/37268662/065e586b-f8ef-446f-b161-7249cee2d9b2)


>***Note***: an additional VCC >= 5V is needed to power the relay switches (!= Relay Ctrl). As can be seen in the general scheme, the PS line could be used for this purpose.

------

Here below are some photos of an ASAC_FI_playground istance, mounted in ASAC Laboratory @ Politecnico di Torino:
<center>PHOTOS<br>PHOTOS<br>PHOTOS<br>PHOTOS<br> </center>

>***Note***: in this model/setup, 8x TUL PYNQ-Z2 MPSoC Development boards have been used to compose the cluster. To edit each FTDI device serial name, and thus be able to manage all the boards singularly, refer to [ftdi-serial-flasher](https://github.com/EdwarDu/ftdi-serial-flasher) repository, by @EdwarDu.

## Getting Started

To initialize the cluster control system, MicroPython has to be installed on the NodeMCU module, together with some source code implementing the control features.

1) **Installing MicroPython firmware**: you can refer to [this guide](docs/ESP8266_uPy_guide.pdf).

2) **Uploading the source files enabling control interface**
   
    2.1) Install [adafruit-ampy](https://pypi.org/project/adafruit-ampy/) to upload/update source files stored in the ESP8266's flash memory.

    ```sh
    pip install adafruit-ampy
    ```

    2.2) ```ampy``` can now be used to upload, download, list files and create directories inside the on-board flash memory. To upload the source files for the control interface (find them in [```/NodeMCUv3_uPy_src```](NodeMCUv3_uPy_src) folder), execute the following commands in a terminal:

    ```bash
    PORT="/dev/ttyUSB0"
    ampy -p $PORT put main.py
    ampy -p $PORT put boot.py
    ampy -p $PORT mkdir lib
    ampy -p $PORT put lib/cmd.mpy
    ampy -p $PORT ls
    ```

4) **Use the control interface**

   Once all is set up, you can try the cluster control in interface by opening a serial connection (9600-8N1) with the NodeMCU module. If everything is good, a prompt '**#**' should appear. Here below are the available commands.

    | Command           | Description |
    | :---------------- | :------ |
    | ```s``` | Returns the current ON/OFF state of the cluster nodes.   |
    | ```y ([1-8] \| all)``` | Power ON the device **[1-8]** or **all** the devices.   |
    | ```k ([1-8] \| all)``` | Power OFF the device **[1-8]** or **all** the devices.   |
    | ```r ([1-8] \| all)``` | Power-cycle (*OFF - 1sec - ON*) the device **[1-8]** or **all** the devices.|
