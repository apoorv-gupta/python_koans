#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import os

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    def __init__(self):
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, args=None):
        "Run the koans tests with a custom runner output."

        if args and len(args) >=2:
            target = args[1]
            # Accept a koan filename (with or without its directory/.py
            # suffix) as well as a fully-qualified unittest name.
            if target.endswith('.py') or os.path.sep in target or '/' in target or '\\' in target:
                target = os.path.splitext(os.path.basename(target))[0]
            if not target.startswith('koans.'):
                target = 'koans.' + target
            self.tests = unittest.TestLoader().loadTestsFromName(target)

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
