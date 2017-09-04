#!/usr/bin/env python
from __future__ import division
import sys
import numpy as np
import numpy.random as rand
import numpy.linalg as linalg
# import deep2d
# import deep2d.se2 as se2
import unittest
import matplotlib.pyplot as plt
import scipy.io as io
import pandas as pd
from cubic import CreateCubicSpline
from math import sqrt

class TestCubic(unittest.TestCase):
    def test_CreateCubicSpline(self):
        d = 3
        n_pts = 7
        pts = np.zeros((d,n_pts))
        pts[:,0] = np.array([0.0, 0.0, 0.0])
        pts[:,1] = np.array([0.0, 0.2, 1.0])
        pts[:,2] = np.array([0.0, 3.0, 0.5])
        pts[:,3] = np.array([1.1, 2.0, 0.0])
        pts[:,4] = np.array([1.0, 0.0, 0.0])
        pts[:,5] = np.array([0.0, 1.0, 0.0])
        pts[:,6] = np.array([0.0, 0.0, 1.0])
        max_vel = np.ones((d,))
        max_accel = np.ones((d,))
        spline = CreateCubicSpline(pts, max_vel, max_accel, 0.001)
        # print spline.IsValid()
        T = np.zeros((132,))
        x = np.zeros((d,132))
        dx = np.zeros((d,132))
        t = 0.1
        i = 0
        # print spline.GetDuration()
        while t < spline.GetDuration():
            x_t  = spline.GetPosition(t)
            dx_t = spline.GetVelocity(t)
            T[i] = t
            x[:,i,None] = x_t
            dx[:,i,None] = dx_t
            i = i + 1
            t = t + 0.1
        x = np.asarray(x)
        dx = np.asarray(dx)

        df = pd.read_csv('test.txt', sep='\s+')

        tx = df.values[:,1:4]
        tdx = df.values[:,4:7]

        for i in range(130):
            x_t = x[:,i]
            dx_t = dx[:,i]
            tx_t = tx[i,:]
            tdx_t = tdx[i,:]
            assert linalg.norm(x_t - tx_t) < 1e-5, i
            assert linalg.norm(dx_t - tdx_t) < 1e-5, i
            # print x_t, tx_t
            # print dx_t, tdx_t

        # plt.plot(T,x[1,:],'*-')
        # plt.show()

    def test_Repeatibility(self):
        h0 = np.array([10,5,np.pi/2],dtype=np.float)
        h1 = np.array([-10,5,np.pi/2],dtype=np.float)
        h2 = np.array([ 2.5, 5., 1.57079637])
        pts = np.hstack((h0[:,None],h2[:,None]))
        max_vel = np.ones((3,))
        max_accel = np.ones((3,))
        spline = CreateCubicSpline(pts, max_vel, max_accel, 0.001)
        duration = spline.GetDuration()
        hz = 60.0
        duration = duration + 1
        num_time_steps = int(np.ceil(duration * hz) + 1)
        t = np.linspace(0, duration, num_time_steps)
        print t[-1]
        print duration
        print spline.GetPosition(duration)
        x = np.zeros((3,num_time_steps))
        v = np.zeros((3,num_time_steps))
        for i in range(len(t)):
            x[:,i,None] = spline.GetPosition(t[i])
            v[:,i,None] = spline.GetVelocity(t[i])
        plt.plot(t, x[0,:])
        plt.show()
        
        

if __name__=='__main__':
    print
    unittest.main(argv=sys.argv,verbosity=2,exit=False)
