#!/usr/bin/env python3
"""
FlyingFish combines Fish and Bird behaviors using multiple inheritance.
"""


class Fish:
    """Represents a fish with swimming ability."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying ability."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A fish that can also fly, inheriting from both Fish and Bird."""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
