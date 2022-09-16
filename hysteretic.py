# Initial method with incremental calculation an edge detection

# #import matplotlib
# from math import exp
# import numpy as np

# vdd = 3.3

# R = 68200
# R1 = 100000
# R2 = 200
# C = 0.000001

# vplusup = (vdd/2)* (R2/(R1 + R2)) + (vdd)*(R1/(R1+R2))
# vplusdown = (vdd/2)* (R2/(R1 + R2))

# vout = [vdd]
# vplus = vplusup
# vminus = [0]
# rising_edge = []

# dir = True
# curr_time = 0
# asymp_stx = 0
# asymp_sty = 0
# asymp_scale = vdd

# for i in range(10000000):
#     curr_time = i / 1000000

#     if dir:
#         if vminus[-1] > vplus:
#             asymp_stx = curr_time
#             asymp_sty = vminus[-1]
#             asymp_scale = vplusup
#             #print(f"{i}, {curr_time}, {vminus[-1]}, {vplus}, {asymp_stx}, {asymp_sty}, {asymp_scale}")
#             vplus = vplusdown
#             dir = False
#         else:
#             next_vmin = asymp_scale*(1-exp(-1*(curr_time-asymp_stx)/(R*C)))+asymp_sty
#             vminus.append(next_vmin)
#             continue
    
#     if not dir:
#         if vminus[-1] < vplus:
#             asymp_stx = curr_time
#             asymp_sty = vminus[-1]
#             asymp_scale = vdd - vplusdown
#             #print(f"{i}, {curr_time}, {vminus[-1]}, {vplus}, {asymp_stx}, {asymp_sty}")
#             rising_edge.append(curr_time)
#             vplus = vplusup
#             dir = True
#         else:
#             next_vmin = asymp_scale*(exp(-1*(curr_time-asymp_stx)/(R*C)))
#             #print(next_vmin)
#             vminus.append(next_vmin)
#             continue

# period = np.diff(rising_edge)

# print(period)


# Secondary method that uses the equation for period
from math import log

VDD = 3.3
VDD2 = 1.65

R_vals = [10, 11, 12.7, 14.3, 15.8, 20, 30.1, 31.6, 40.2, 47.5, 49.9, 60.4, 63.4, 69.8, 80.6, 90.9, 95.3]
C_vals = [0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001]

for value in R_vals:
    if len(R_vals) == 86: break
    R_vals.append(value * 10)

R_vals.extend([2000000, 3010000, 10000000])

valid_params = []

for c in C_vals:
    for r in R_vals:
        tau = r * c
        for r1 in R_vals:
            for r2 in R_vals:
                alpha = r1 / (r1 + r2)
                t1 = (VDD - alpha*(VDD/2))/(alpha*(VDD/2))
                t2 = (VDD - alpha*(VDD/2))/(alpha*(VDD/2))
                period = tau * log(t1*t2)
                if 0.9997 < period < 1.0003:
                    period = round(period, 6)
                    param_list = (c, r, r1, r2, period)
                    valid_params.append(param_list)

print(valid_params)