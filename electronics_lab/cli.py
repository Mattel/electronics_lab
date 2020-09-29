#!/usr/local/bin/python3.8
import argparse

# Uncomment if we ever get it working as a package..
# from electronics_lab.drivers import SiglentSPD3303X
from drivers import SiglentSPD3303X

IP_ADDR = "192.168.0.187"


def str_to_opt(option):
    option = option.lower()
    if option == 'voltage':
        option = SiglentSPD3303X.voltage
    elif option == 'current':
        option = SiglentSPD3303X.current
    elif option == 'power':
        option = SiglentSPD3303X.power
    elif option == 'out':
        option = SiglentSPD3303X.out

    return option


def get(option, channel):
    psu = SiglentSPD3303X(IP_ADDR)

    option = str_to_opt(option)
    print("Getting option {0} on channel {1}".format(option, channel))
    return psu.get_measurement(meas_type=option, channel=channel)


def set(option, channel, value):
    psu = SiglentSPD3303X(IP_ADDR)

    option = str_to_opt(option)
    psu.set_param(param=option, channel=channel, value=value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control Siglent Power Supply")
    parser.add_argument('--get', dest='get_mode', type=str, default=None,
                        help="Get info from power supply (Options: voltage, current, power, out)")
    parser.add_argument('--set', dest='set_mode', type=str, default=None,
                        help="Configure power supply (Options: voltage, current, power, out)")
    parser.add_argument('--channel', dest='channel', default=1, type=int, help="Channel 1 or 2 (default: 1)")
    parser.add_argument('--value', dest='value', help="Value to set parameter to (for use with --set)")

    args = vars(parser.parse_args())
    if not any(args.values()):
        parser.error("No get/set mode set")
    if all(args.values()):
        parser.error("--get and --set are exclusive. Only use one!")

    if args['get_mode']:
        val = get(args['get_mode'], args['channel'])
        exit(not val)

    elif args['set_mode']:
        if not args['value']:
            parser.error("Please use --value param when configuring power supply")
        set(args['set_mode'], args['channel'], args['value'])
