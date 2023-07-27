# FI-playground
Code and documentation for FPGA/MPSoC cluster management architecture, to be used for testing purposes or fault injection.

------
To upload/update source files stored in the esp's flash memory, you can use [adafruit-ampy](https://pypi.org/project/adafruit-ampy/). Simply install it with
```sh
pip install adafruit-ampy
```

Once installed, ampy can be used to upload, download, list files and create directories. For example, to perform the first upload you can execute the following commands:
```bash
PORT="/dev/ttyUSB0"
ampy -p $PORT put main.py
ampy -p $PORT put boot.py
ampy -p $PORT mkdir lib
ampy -p $PORT put lib/cmd.mpy
ampy -p $PORT ls
```
