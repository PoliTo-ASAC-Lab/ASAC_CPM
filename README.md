# ASC_CPM - ASC Cluster Power Manager

ASC_CPM is a Cluster Power Manager solution, to be used for testing purposes or extensive fault injection campaigns involving a cluster of devices. It can be easily adapted to be used with other kinds of board composing the cluster, like Arduino, Raspberry-Pi, others.

## HW Setup

The overall setup requires low-cost components only and can be easily adapted and scaled based on necessity. To manage the power supply of the cluster nodes (ON/OFF) a set of relay switches is controlled by a [NodeMCU Lua Lolin V3 Module](https://www.az-delivery.de/en/products/nodemcu-lolin-v3-modul-mit-esp8266), implementing a user interface accessible through USB-serial connection.
Here below is the general scheme of the hardware setup:

![HW_Setup](https://github.com/danirizziero/ASAC_CPM/assets/37268662/7e57bd38-930e-4d55-b451-e069c083dfe4)

Here below the details about the NodeMCU module pin usage:

![NodeMCU_Pinout](https://github.com/danirizziero/ASAC_CPM/assets/37268662/7e18c012-a647-45ae-8fb0-89661b3cc0cf)


>***Note***: an additional VCC >= 5V is needed to power the relay switches (!= Relay Ctrl). As can be seen in the HW Setup general scheme, the PS line could be used for this purpose.

------

Here below a photo of an ASC_CPM istance, as it has been mounted in ASC Laboratory @ DAUIN, Politecnico di Torino:

![ASC_CPM_istance](https://github.com/danirizziero/ASAC_CPM/assets/37268662/89fcbb40-c32a-4739-9b39-f2e08bb3ecb7)


>***Note***: in this model/setup, 8x TUL PYNQ-Z2 MPSoC Development boards have been used to compose the cluster. To edit each FTDI device serial name, and thus be able to manage all the boards singularly, refer to [ftdi-serial-flasher](https://github.com/EdwarDu/ftdi-serial-flasher) repository, by [@EdwarDu](https://github.com/EdwarDu).

## Getting Started

To initialize the CPM, MicroPython firmware has to be flashed on the NodeMCU module, together with some source code implementing the control interface.

0) **Install CH340 Driver**: from [this link](https://www.wch.cn/download/CH341SER_EXE.html).
1) **Installing MicroPython firmware**: follow this guide [```docs/ESP8266_uPy_guide.pdf```](docs/ESP8266_uPy_guide.pdf).

2) **Uploading the uPy source files enabling control interface**
   
    2.1) Install [adafruit-ampy](https://pypi.org/project/adafruit-ampy/) on your local machine, to upload/update source files stored in the ESP8266's flash memory.

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

   Once all is set up, you can use the CPM control interface by opening a serial connection (115200-8N1) with the NodeMCU module. If everything is good, a prompt '**#**' should appear. Here below are the available commands.

    | Command           | Description |
    | :---------------- | :------ |
    | ```s``` | Returns the current ON/OFF state of the cluster nodes.   |
    | ```y ([1-8] \| all)``` | Power ON the device **[1-8]** or **all** the devices.   |
    | ```k ([1-8] \| all)``` | Power OFF the device **[1-8]** or **all** the devices.   |
    | ```r ([1-8] \| all)``` | Power-cycle (*OFF - 1sec - ON*) the device **[1-8]** or **all** the devices.|

## Market COTS Alternatives

Here below are some Commercial-Off-The-Shelf alternatives/similar products available on the market (in July 2023):
- [Crowd Supply Programmable USB Hubs](https://mou.sr/3OBESQ7) (202.50$)
- [Microchip EVB-USB5734](https://www.microchip.com/en-us/development-tool/evb-usb5734) (536.20€)
- [Cluster Triple for Raspberry Pi Compute Modules](https://clusterctrl.com/p/Triple) (49.00$)

The total implementation cost (in July 2023) of the ASC_CPM is <ins>**around 20€**</ins> (~12.50€ for the [8x Relay Module](https://www.az-delivery.de/en/products/8-relais-modul) + ~7.50€ for the [NodeMCU V3 Module](https://www.az-delivery.de/en/products/nodemcu-lolin-v3-modul-mit-esp8266)).
