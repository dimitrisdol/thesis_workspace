#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

slo= [1.1 , 1.2 , 1.3]

for slo in slo:

  if slo==1.1:
    data_random_low = [6,7,8,5,6.5,7.5,3,10]
    data_greedy_low = [6,7,5,7,4.8]
    data_socket_low = [2,3,1,3,1.1]
    data_random_mid = [11,12,13,10,11.5,12.5,14.2]
    data_greedy_mid = [10,11,9,11,8.8]
    data_socket_mid = [9,8,7,10,8.8]
    data_random_high = [15,16,16,14,15.5,16,13.2]
    data_greedy_high = [10,11,9,11,9.1]
    data_socket_high = [15,14,13,12,11.6,9,10.1]
  elif slo==1.2:
    data_random_low = [2,3,4,2,1.5,2.5,1.5,5.2]
    data_greedy_low = [1,0,2,0,0.8]
    data_socket_low = [0,0,1,0,0.8]
    data_random_mid = [5,6,7,4,6.5,7.5,9.5]
    data_greedy_mid = [5,4,6,3.9,5.6]
    data_socket_mid = [3,2,5,2,5.2]
    data_random_high = [7,8,9,6,7.5,8.5,10.1]
    data_greedy_high = [6,5,7,4,6.8]
    data_socket_high = [6,5,7,4,5.8]
  else:
    data_random_low = [1,2,0,1,2.5,3.5,3.8]
    data_greedy_low = [0,0,1,0,1.2]
    data_socket_low = [0,0,1,0,1.2]
    data_random_mid = [3,4,5,2,4.5,5.5,6.8]
    data_greedy_mid = [5,4,3,2,4.1]
    data_socket_mid = [1,2,0,0,2.1]
    data_random_high = [4,5,3,5,3.5,4.5,5.3]
    data_greedy_high = [3,2,4,2,2.8]
    data_socket_high = [0,1,0,2,1.1]
 
  data = [data_random_low, data_greedy_low, data_socket_low,   data_random_mid, data_greedy_mid, data_socket_mid, data_random_high, data_greedy_high, data_socket_high ]
 
  fig = plt.figure(figsize =(10, 7))
  ax = fig.add_subplot(111)
 
  # Creating axes instance
  bp = ax.boxplot(data, patch_artist=True)
  
  for i in range(3):
    bp['boxes'][i].set_facecolor('moccasin')
    bp['medians'][i].set(color ='darkorange',
                 linewidth = 3)
    
  for i in range(3,6):
    bp['boxes'][i].set_facecolor('lightgreen')
    bp['medians'][i].set(color ='darkgreen',
                 linewidth = 3)
    
  for i in range(6,9):
    bp['boxes'][i].set_facecolor('lightcyan')
    bp['medians'][i].set(color ='darkcyan',
                 linewidth = 3)
    
  
  plt.text(0.8, 17.3,
         'Low workload',
         bbox=dict(facecolor='orange',
                   alpha=0.5),
         fontsize=10)
         
  plt.text(4.7, 17.3,
         'Mid workload',
         bbox=dict(facecolor='limegreen',
                   alpha=0.5),
         fontsize=10)
         
  plt.text(7.8, 17.3,
         'High workload',
         bbox=dict(facecolor='cyan',
                   alpha=0.5),
         fontsize=10)
 
 
  # changing color and linewidth of
  # medians
#  for median in bp['medians']:
 #     median.set(color ='red',
  #               linewidth = 3)
                 
  ax.set_ylim([-0.1, 17.9])

  # x-axis labels
  ax.set_xticklabels(['random', 'greedy', 'socket', 'random', 'greedy', 'socket', 'random', 'greedy', 'socket'])
 
  # Adding title
  plt.title("SLO=" + str(slo))
 
  # Removing top axes and right axes
  # ticks
  ax.get_xaxis().tick_bottom()
  ax.get_yaxis().tick_left()
  
  ax.set_xlabel('Algorithms')
  ax.set_ylabel('Violations')
     
  # show plot
  plt.savefig('slo' + str(slo) + '.jpg')
