#!/usr/bin/env python3

import os
import importlib
import ipaddress

INPUT_TYPE = os.environ["IPSU_INPUT"]
OUTPUT_TYPE = os.environ["IPSU_OUTPUT"]

input_config = dict()
output_config = dict()
for k, v in os.environ.items():
    key = k.split("_", 3)[-1].lower()
    if k.startswith(f"IPSU_INPUT_{INPUT_TYPE.upper()}_"):
        input_config[key] = v
    elif k.startswith(f"IPSU_OUTPUT_{OUTPUT_TYPE.upper()}_"):
        output_config[key] = v

input_module = importlib.import_module(f"input.{INPUT_TYPE}")
result = [ipaddress.ip_interface(i) for i in input_module.run(input_config)]

output_module = importlib.import_module(f"output.{OUTPUT_TYPE}")
output_module.run(output_config, result)
