#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
slo= [1, 2, 3] #1 = greedy, 2 = socket , 3 = sparing

for slo in slo:

  if slo==1:
    data_random_low = 4.2
    data_greedy_low = 2.6
    data_greedy_low2 = 2.1
    data_random_mid = 7.9
    data_greedy_mid = 5.6
    data_greedy_mid2 = 4.9
    data_random_high = 10.2
    data_greedy_high = 7.2
    data_greedy_high2 = 6.7
    #data = [ data_random_low, data_greedy_low, data_greedy_low2, data_random_mid, data_greedy_mid, data_greedy_mid2, data_random_high, data_greedy_high, data_greedy_high2 ]
    algos = [data_greedy_low,data_greedy_mid, data_greedy_high]
    pinned =[data_greedy_low2,data_greedy_mid2, data_greedy_high2]
    val_color = 'moccasin'
  elif slo==2:
    data_random_low = 4.2
    data_socket_low = 1.4
    data_socket_low2 = 1.1
    data_random_mid = 7.9
    data_socket_mid = 4.4
    data_socket_mid2 = 3.8
    data_random_high = 10.2
    data_socket_high = 6.8
    data_socket_high2 = 6.3  
    #data = [ data_random_low, data_socket_low, data_socket_low2, data_random_mid, data_socket_mid, data_socket_mid2, data_random_high, data_socket_high, data_socket_high2 ]
    algos = [data_socket_low,data_socket_mid, data_socket_high]
    pinned =[data_socket_low2,data_socket_mid2, data_socket_high2]
    val_color = 'lightgreen'
  else:
    data_random_low = 4.2
    data_sparing_low = 2.2
    data_sparing_low2 = 1.6
    data_random_mid = 7.9
    data_sparing_mid =4.8
    data_sparing_mid2 = 4.1
    data_random_high = 10.2
    data_sparing_high = 7.5
    data_sparing_high2 = 6.8
    #data = [ data_random_low, data_sparing_low, data_sparing_low2, data_random_mid, data_sparing_mid, data_sparing_mid2, data_random_high, data_sparing_high, data_sparing_high2 ]
    algos = [data_sparing_low,data_sparing_mid, data_sparing_high]
    pinned =[data_sparing_low2,data_sparing_mid2, data_sparing_high2]
    val_color = 'lightcyan'
 
  fig = plt.figure(figsize =(10, 7))
  ax = fig.add_subplot(111)
  
  bars = ('low', 'mid', 'high')
  
  randoms = [data_random_low, data_random_mid, data_random_high]
 
  x_pos = np.arange(len(bars))
  width = 0.25
  
  fig, ax = plt.subplots()
  rects1 = ax.bar(x_pos - width, randoms, width=0.25, label ='Random')
  rects2 = ax.bar(x_pos, algos, width=0.25, label = 'No CPU pin')
  rects3 = ax.bar(x_pos + width, pinned, width=0.25, label = 'CPU-pinned')

 
  # Adding title
  if slo == 1:
    ax.set_title("Random vs Greedy vs Greedy with CPU pin")
  elif slo == 2:
    ax.set_title("Random vs Socket vs Socket with CPU pin")
  else:
    ax.set_title("Random vs Sparing vs Sparing with CPU pin")
 
  # Removing top axes and right axes
  # ticks
  ax.get_xaxis().tick_bottom()
  ax.get_yaxis().tick_left()
  ax.legend()
  
  ax.set_xlabel('Workloads')
  ax.set_ylabel('Average Violations')
  
  ax.set_xticks(x_pos)
  ax.set_xticklabels(bars)
  
  ax.bar_label(rects1, padding = 3)
  ax.bar_label(rects2, padding = 3)
  ax.bar_label(rects3, padding = 3)
     
  # show plot
  plt.savefig('cpupinning' + str(slo) + '.jpg')
