from  pyNastran import *

line = HeadLine_16()
# line.print_list()
grid1 = GRID(1002, 0, 0.0, 0.0, 0.0, 1000.0, '', '')
line2 = HeadLine_8()
rbe = RBE2(1066, 1002, 12345, 1013, 1024)

# print(len(format(1.0,'.10g')))
print(grid1)
