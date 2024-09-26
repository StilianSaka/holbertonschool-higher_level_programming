#!/usr/bin/env python3
"""
Dragon class demonstrates the use of mixins for adding swim and fly abilities.
"""


class SwimMixin:
    """Mixin to add swimming ability."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin to add flying ability."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly."""
    def roar(self):
        print("The dragon roars!")
