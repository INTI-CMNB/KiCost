#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_kicost
----------------------------------

Tests for `kicost` module.
"""

import unittest
import subprocess
import logging
import glob
import os

from kicost import kicost


def do_test_single(pattern):
    os.chdir('tests')
    fail = False
    try:
        for f in glob.glob(pattern):
            try:
                res = subprocess.check_output(['./test_single.sh', '--no_price', f])
                logging.info(f + ' OK')
            except subprocess.CalledProcessError:
                logging.error('Failed test: '+f)
                fail = True
                pass
    finally:
        os.chdir('..')
    return fail


def test_xmls():
    assert not do_test_single('*.xml')


def test_csvs():
    assert not do_test_single('*.csv')


class TestKicost(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
