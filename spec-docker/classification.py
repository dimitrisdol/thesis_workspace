#! /usr/bin/python3

import numpy as np

qos=[1.2]

grid_defending = { 'zeusmp': { 'namd': '1.001', 'gobmk' : '1.001', 'omnetpp': '1.001', 'perlbench': '1.001', 'cactusADM': '1.001', 'libquantum2': '1.064', 'GemsFDTD2': '1.043', 'libquantum1': '1.023', 'soplex2': '1.05'},
         'namd': { 'zeusmp': '1.003', 'gobmk' : '1', 'omnetpp': '1', 'perlbench': '1', 'cactusADM': '1', 'libquantum2': '1.01', 'GemsFDTD2': '1.01', 'libquantum1': '1', 'soplex2': '1.003'},
         'gobmk': { 'zeusmp': '1.02', 'namd' : '1.03', 'omnetpp': '1.025', 'perlbench': '1.01', 'cactusADM': '1', 'libquantum2': '1.1', 'GemsFDTD2': '1.1', 'libquantum1': '1.05', 'soplex2': '1.06'},
         'omnetpp': { 'zeusmp': '1.04', 'namd' : '1.04', 'gobmk': '1.05', 'perlbench': '1.06', 'cactusADM': '1.04', 'libquantum2': '1.45', 'GemsFDTD2': '1.25', 'libquantum1': '1.07', 'soplex2': '1.16'},
         'perlbench': { 'zeusmp': '1.002', 'namd' : '1', 'gobmk': '1', 'omnetpp': '1.002', 'cactusADM': '1', 'libquantum2': '1.19', 'GemsFDTD2': '1.24', 'libquantum1': '1.17', 'soplex2': '1.11'},
         'cactusADM': { 'zeusmp': '1.008', 'namd' : '1.004', 'gobmk': '1', 'omnetpp': '1.009', 'perlbench': '1.005', 'libquantum2': '1.11', 'GemsFDTD2': '1.10', 'libquantum1': '1.06', 'soplex2': '1.08'},
         'libquantum2': { 'zeusmp': '1.18', 'namd' : '1.1', 'gobmk': '1.11', 'omnetpp': '1', 'perlbench': '1.07', 'cactusADM': '1.12', 'GemsFDTD2': '1.3', 'libquantum1': '1.24', 'soplex2': '1.15'},
         'GemsFDTD2': { 'zeusmp': '1.12', 'namd' : '1.03', 'gobmk': '1.01', 'omnetpp': '1.01', 'perlbench': '1.02', 'cactusADM': '1.1', 'libquantum2': '1.27', 'libquantum1': '1.16', 'soplex2': '1.16'},
         'libquantum1': { 'zeusmp': '1.01', 'namd' : '1.01', 'gobmk': '1.01', 'omnetpp': '1.025', 'perlbench': '1.025', 'cactusADM': '1.08', 'libquantum2': '1.26', 'GemsFDTD2': '1.26', 'soplex2': '1.19'},
         'soplex2': { 'zeusmp': '1.07', 'namd' : '1.05', 'gobmk': '1.08', 'omnetpp': '1.12', 'perlbench': '1.05', 'cactusADM': '1.12', 'libquantum2': '1.30', 'GemsFDTD2': '1.22', 'libquantum1': '1.17'} }
         
grid_attacking = { 'zeusmp': { 'namd': '1.003', 'gobmk' : '1.02', 'omnetpp': '1.04', 'perlbench': '1.002', 'cactusADM': '1.008', 'libquantum2': '1.18', 'GemsFDTD2': '1.12', 'libquantum1': '1.12', 'soplex2': '1.2'},
         'namd': { 'zeusmp': '1.001', 'gobmk' : '1.03', 'omnetpp': '1.04', 'perlbench': '1', 'cactusADM': '1.004', 'libquantum2': '1.1', 'GemsFDTD2': '1.03', 'libquantum1': '1.01', 'soplex2': '1.01'},
         'gobmk': { 'zeusmp': '1.01', 'namd' : '1', 'omnetpp': '1.05', 'perlbench': '1.', 'cactusADM': '1.009', 'libquantum2': '1.11', 'GemsFDTD2': '1.01', 'libquantum1': '1.01', 'soplex2': '1.05'}, 
         'omnetpp': { 'zeusmp': '1.001', 'namd' : '1', 'gobmk': '1.025', 'perlbench': '1.002', 'cactusADM': '1.009', 'libquantum2': '1', 'GemsFDTD2': '1.01', 'libquantum1': '1.025', 'soplex2': '1.05'},
         'perlbench': { 'zeusmp': '1.001', 'namd' : '1', 'gobmk': '1.01', 'omnetpp': '1.06', 'cactusADM': '1.005', 'libquantum2': '1.07', 'GemsFDTD2': '1.02', 'libquantum1': '1.025', 'soplex2': '1.03'},
         'cactusADM': { 'zeusmp': '1.024', 'namd' : '1', 'gobmk': '1.07', 'omnetpp': '1.04', 'perlbench': '1', 'libquantum2': '1.15', 'GemsFDTD2': '1.13', 'libquantum1': '1.08', 'soplex2': '1.12'},
         'libquantum2': { 'zeusmp': '1.07', 'namd' : '1.01', 'gobmk': '1.1', 'omnetpp': '1.45', 'perlbench': '1.16', 'cactusADM': '1.1', 'GemsFDTD2': '1.27', 'libquantum1': '1.26', 'soplex2': '1.30'},
         'GemsFDTD2': { 'zeusmp': '1.043', 'namd' : '1.01', 'gobmk': '1.1', 'omnetpp': '1.25', 'perlbench': '1.14', 'cactusADM': '1.04', 'libquantum2': '1.3', 'libquantum1': '1.26', 'soplex2': '1.28'},
         'libquantum1': { 'zeusmp': '1.023', 'namd' : '1', 'gobmk': '1.05', 'omnetpp': '1.07', 'perlbench': '1.17', 'cactusADM': '1.06', 'libquantum2': '1.24', 'GemsFDTD2': '1.16', 'soplex2': '1.17'},
         'soplex2': { 'zeusmp': '1.03', 'namd' : '1.03', 'gobmk': '1.06', 'omnetpp': '1.19', 'perlbench': '1.11', 'cactusADM': '1.08', 'libquantum2': '1.16', 'GemsFDTD2': '1.21', 'libquantum1': '1.19'} }


def qos_class(qos, slowdown):
	try:
		class_ = qos.index(min([x for x in qos if x > slowdown]))
	except:
		class_ = len(qos)
	return class_

def classes(grid, qos, class_num = 2):
	clos = dict()
	whiskers = dict()
	quartiles3 = dict()
	for bench in grid.keys():
		if not grid[bench]: continue
		measures = list(map(float, grid[bench].values()))
		quartile3 = np.percentile(measures,75)
		quartile1 = np.percentile(measures,25)
		iqr = quartile3 - quartile1
		whisker_lim = quartile3 + 1.5 * iqr
		whisker = max([x for x in measures if x <= whisker_lim])
		if class_num == 2:
			clos[bench] = qos_class(qos, whisker)
		whiskers[bench] = whisker
		quartiles3[bench] = quartile3
	return (clos, whiskers, quartiles3)
	
if __name__ == '__main__':
	sensitivity = classes(grid_defending,qos,2)
	print(sensitivity)
	
	print("-------------------")
	
	contensiousness = classes(grid_attacking,qos,2)
	print(contensiousness)
	


