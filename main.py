from  pyNastran import *
from math_kernel import *

# line = HeadLine_16()
# # line.print_list()
# grid1 = GRID(1002, 0, 0.0, 0.0, 0.0, 1000.0, '', '')
# line2 = HeadLine_8()
# rbe = RBE2(1066, 1002, 12345, 1013, 1024)

# # print(len(format(1.0,'.10g')))
# print(grid1)


line1 = HeadLine_16()
cord1 = CORD2R(1000, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0)
cord2 = CORD2R(1001, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0)
line2 = HeadLine_16()

grid_list = []

for i in range(11):
    grid_list.append(GRID(1002+i, 0, 0.0, float(i), 0.0, 1000, '', ''))
for i in range(11):
    grid_list.append(GRID(1013+i, 0, -.5, float(i), 0.0, 0, '', ''))
for i in range(11):
    grid_list.append(GRID(1024+i, 0, .5, float(i), 0.0, 0, '', ''))

beam_list = []
for i in range(10):
    beam_list.append(CBEAM(1035+i, 1055+i, 1002+i, 1003+i, 0.0, 1.0, 0.0, '', '', '', 0.0, 0.0, 0.0, 
                            0.0, 0.0, 0.0, '', ''))

pb_list = pbeam_gen(.1, 7800.0, 1, .4, Sbeam, Mslab)
# print(pb_list)

pbeam_list = []
for i in range(10):
    pbeam_list.append(PBEAM(1055+i, 1065, *pb_list))

print(cord1)

