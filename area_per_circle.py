#!/usr/bin/env python3
# Created by: Xiaohan Tian
# Created on: Mar 5, 2025
# This program is to area and the circumference of circle.

import math


def main():
    # input of from the user
    radius = int(input("Enter the radius of the circle (cm): "))
    circumference = math.pi * radius * 2
    area = math.pi * radius**2
    # output the results
    print("")
    print("Circumference = {:.2f} cm".format(circumference))
    print("Area = {:.2f} cm²".format(area))


if __name__ == "__main__":
    main()
