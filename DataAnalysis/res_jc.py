from os import listdir
from os.path import isfile, join
import re

marks={
	'init_memory_allocate':0,
        'init_memory_initialize':0,
        'init_memory_download':0,
        'cpu_readback':0,
        'cpu_deva_readback':0,
        'cpu_devb_readback':0,
        'gpu_all_readback':0,
        'gpu_single_memcpy':0,
        'free_memory':0,
        'cpu_branch':0,
        'cpu_bound':0,
        'gpu_branch':0,
        'gpu_bound':0,
        'cpu_maximum':0,
        'cpu_label':0,
        'cpu_scan':0,
        'gpu_maximum':0,
        'gpu_label':0,
        'gpu_label_download':0,
        'gpu_scan':0,
        'gpu_label_readback':0,
        'cpu_packing':0,
        'gpu_packing':0,
        'gpu_bandb':0,
        'gpu_double_memcpy':0,
        'gpu_overlap':0
}

def dataBD(fpath):
	fl = open(fpath)
	for line in fl:
		if 'Result: init' in line or 'Result: cpu' in line or 'Result: gpu' in line or 'Result: free' in line:
			mk = re.findall(': ([a-z,_]+) [0-9]+',line)
			val = re.findall(' ([0-9,.]+)',line)
			#print(mk[0],':',val[0])
			marks[mk[0]] += float(val[0])
	#print(marks)
	init = marks['init_memory_allocate']+marks['init_memory_initialize']+marks['init_memory_download']
	cpucalc = marks['cpu_branch']+marks['cpu_bound']+marks['cpu_maximum']+marks['cpu_label']+marks['cpu_scan']+marks['cpu_packing']
	g1 = marks['gpu_overlap']
	g2= marks['gpu_maximum']+marks['gpu_label']+marks['gpu_scan']+marks['gpu_packing']
	#gpucalc = marks['gpu_bandb']
	singledw = marks['gpu_single_memcpy']
	cpumrb = marks['cpu_deva_readback'] + marks['cpu_devb_readback']
	ft = marks['free_memory']
	print('Init Time, Preparation of Memories:',init)
	print('CPU Calculation Time:',cpucalc)
	#print('GPU Calculation Time:',gpucalc)
	print('GPU Calculation Time detail1:',g1)
	print('GPU Calculation Time detail2:',g2)
	print('GPU-singlemode Download Time:',singledw)
	print('CPU-mode Readback Time:',cpumrb)
	print('Free Memory Time:',ft)
	print('Total:',init+cpucalc+g1+g2+singledw+cpumrb+ft)
	
mypath = 'script_data/' 
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in files:
	dataBD(f)
