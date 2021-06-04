#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:49:24 2021

@author: ahmed
"""

from app import app

if __name__ == '__main__':
    app.run("0.0.0.0", port = 5000, debug=False)