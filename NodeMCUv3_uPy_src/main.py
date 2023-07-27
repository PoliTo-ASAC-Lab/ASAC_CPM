from machine import Pin
import time
import cmd

dev_to_pin = {
    1: Pin(16, mode=Pin.OUT, value=1), #D0
    2: Pin(5, mode=Pin.OUT, value=1),  #D1
    3: Pin(4, mode=Pin.OUT, value=1),  #D2
    4: Pin(0, mode=Pin.OUT, value=1),  #D3
    5: Pin(14, mode=Pin.OUT, value=1), #D5
    6: Pin(12, mode=Pin.OUT, value=1), #D6
    7: Pin(13, mode=Pin.OUT, value=1), #D7
    8: Pin(15, mode=Pin.OUT, value=1), #D8
}

class Shell(cmd.Cmd):

    #prompt = "you@world:/$ "
    prompt = "# "

    @staticmethod
    def _check_dev(dev):

        if dev == "all":
            return -1 

        try:
            dev = int(dev)
        except:
            print("Error: argument #1 must be a number")
            return None

        if not dev in dev_to_pin:
            print("Error: device #" + str(dev) + " out of bound")
            return None

        return dev

    def do_EOF(self, line):
        print()
        return True

    def do_exit(self, line):
        return self.do_EOF(line)

    def do_y(self, dev):
        dev = Shell._check_dev(dev)
        if dev == None:
            return False

        # if -1 means all devices
        act_devs = [dev] if dev != -1 else dev_to_pin.keys()

        for dev in act_devs:
            print("Turning ON  dev #" + str(dev) + "... ", end="")
            dev_to_pin[dev].value(1)
            print("OK.")

    def do_k(self, dev):
        dev = Shell._check_dev(dev)
        if dev == None:
            return False

        act_devs = [dev] if dev != -1 else dev_to_pin.keys()

        for dev in act_devs:
            print("Turning OFF dev #" + str(dev) + "... ", end="")
            dev_to_pin[dev].value(0)
            print("OK.")

    def do_r(self, dev):
        dev = Shell._check_dev(dev)
        if dev == None:
            return False

        act_devs = [dev] if dev != -1 else dev_to_pin.keys()

        for dev in act_devs:
            print("Switching dev #" + str(dev))
            dev_to_pin[dev].value(0)

        time.sleep(1)

        for dev in act_devs:
            dev_to_pin[dev].value(1)


    def do_s(self, line):

        print()
        sorted_keys = sorted(dev_to_pin.keys())
        header = "".join(["{:^5}".format("#" + str(p)) for p in sorted_keys])

        print(header)
        print("-" * len(header))

        for k in sorted_keys:
            print("{:^5}".format("ON" if dev_to_pin[k].value() == 1 else "OFF"), end="")

        #state = "".join(["{:^5}".format("ON" if p.value() == 1 else "OFF") for p in dev_to_pin.values()])
        #print(state)

        print()
        print()

    def do_test(self, line):
        pin = Pin(5, Pin.OUT)
        pin.value(pin.value() ^ 1)
        print("New value is " + str(pin.value()))

def do_loop():
    Shell().cmdloop()

do_loop()