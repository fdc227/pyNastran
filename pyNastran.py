class Nastran:

    def __init__(self):
        pass

    print_str = []
    def print_list(self):
        for i in self.print_str:
            print(i)

    def __str__(self):
        return '\n'.join(self.print_str)

    def number_fomat_16(self, num):
        if isinstance(num, int):
            s = format(num, '.10g')
            l = 16 - len(s)
            if l < 0:
                raise Exception('length of entry exceeds 16')
            s += ' '*l
            return s
        else:
            ss = format(num, '.10g')
            s = str(float(ss))
            l = 16 - len(s)
            if l < 0:
                raise Exception('length of entry exceeds 16')
            s += ' '*l
            return s

    def number_format_8(self, num):
        if isinstance(num, int):
            s = format(num, '.8g')
            l = 8 - len(s)
            if l < 0:
                raise Exception('length of entry exceeds 8')
            s += ' '*l
            return s
        else:
            ss = format(num, '.4g')
            s = str(float(ss))
            l = 8 - len(s)
            if l < 0:
                raise Exception('length of entry exceeds 8')
            s += ' '*l
            return s

    def formatter_16(self):
        out = []
        for data in self.var_list:
            if isinstance(data, str):
                l = 16 - len(data)
                data += ' '*l
                out.append(data)
            else:
                # s = format(data, '.10g')
                # l = 16 - len(s)l
                # s += ' '*l
                # out.append(s)
                s = self.number_fomat_16(data)
                out.append(s)
        return out

    def formatter_8(self):
        out = []
        for data in self.var_list:
            if isinstance(data, str):
                l = 8 - len(data)
                data += ' '*l
                out.append(data)
            else:
                s = self.number_format_8(data)
                out.append(s)
        return out

    def formatter_short(self): 
        out = []
        local = [self.name, self.attr]
        for data in local:
            l = 8 - len(data)
            data += ' '*l
            out.append(data)
        return out

    def line_spliter_16(self):
        formatted_16 = self.formatter_16()
        formatted_16_short = self.formatter_short()
        out = []
        line = -1
        for i in range(len(formatted_16)):
            if i % 4 == 0:
                out.append([])
                line += 1
                out[line].append(formatted_16[i])
            else:
                out[line].append(formatted_16[i])
        for i in range(len(out)):
            if i == 0:
                out[i].insert(0, formatted_16_short[0])
            else:
                out[i].insert(0, formatted_16_short[1])
        return out

    def line_spliter_8(self):
        formatted_8 = self.formatter_8()
        formatted_short = self.formatter_short()
        out = []
        line = -1
        for i in range(len(formatted_8)):
            if i % 8 == 0:
                out.append([])
                line += 1
                out[line].append(formatted_8[i])
            else:
                out[line].append(formatted_8[i])
        for i in range(len(out)):
            if i == 0:
                out[i].insert(0, formatted_short[0])
            else:
                out[i].insert(0, formatted_short[1])
        return out

    def printer_local_16(self):
        var_lines = self.line_spliter_16()
        local = []
        for i in var_lines:
            local.append(''.join(i))
        # print(local)
        final_str = '\n'.join(local)
        self.print_str.append(final_str)

    def printer_local_8(self):
        var_lines = self.line_spliter_8()
        local = []
        for i in var_lines:
            local.append(''.join(i))
        # print(local)
        final_str = '\n'.join(local)
        self.print_str.append(final_str)


class HeadLine_16(Nastran):
    def __init__(self):
        self.var_list = []
        self.show = '$.1.....2...............3...............4...............5...............6.......'
        super().print_str.append(self.show)

class HeadLine_8(Nastran):
    def __init__(self):
        self.var_list = []
        self.show = '$.1.....2.......3.......4.......5.......6.......7.......8.......9.......10......'
        super().print_str.append(self.show)

class GRID(Nastran):
    def __init__(self, ID, CP, X1, X2, X3, CD, PS, SEID):
        self.name = 'GRID*'
        self.attr = '*'
        self.var_list = [ID, CP, X1, X2, X3, CD, PS, SEID]
        self.printer_local_16()

class CORD2R(Nastran):
    def __init__(self, CID, RID, A1, A2, A3, B1, B2, B3, C1, C2, C3):
        self.name = 'CORD2R*'
        self.attr = '*'
        self.var_list = [CID, RID, A1, A2, A3, B1, B2, B3, C1, C2, C3]
        self.printer_local_16()

class CBEAM(Nastran):
    def __init__(self, EID, PID, GA, GB, X1, X2, X3, OFFT, PA, PB, W1A, W2A, W3A, W1B, W2B, W3B, SA, SB):
        self.name = 'CBEAM*'
        self.attr = '*'
        self.var_list = [EID, PID, GA, GB, X1, X2, X3, OFFT, PA, PB, W1A, W2A, W3A, W1B, W2B, W3B, SA, SB]
        self.printer_local_16()

class PBEAM(Nastran):
    def __init__(self, PID, MID, AA, l1A, l2A, l12A, JA, NSMA, C1A, C2A, D1A, D2A, E1A, E2A, F1A, F2A,
                       SO, XB, A, l1, l2, l12, J, NSM, C1, C2, D1, D2, E1, E2, F1, F2,
                       K1, K2, S1, S2, NSIA, NSIB, CWA, CWB, M1A, M2A, M1B, M2B, N1A, N2A, N1B, N2B):
        self.name = 'PBEAM*'
        self.attr = '*'
        self.var_list = [PID, MID, AA, l1A, l2A, l12A, JA, NSMA, C1A, C2A, D1A, D2A, E1A, E2A, F1A, F2A,
                        SO, XB, A, l1, l2, l12, J, NSM, C1, C2, D1, D2, E1, E2, F1, F2,
                        K1, K2, S1, S2, NSIA, NSIB, CWA, CWB, M1A, M2A, M1B, M2B, N1A, N2A, N1B, N2B]
        self.printer_local_16()

class MAT1(Nastran):
    def __init__(self, MID, E, G, NU, RHO, A, TREF, GE, ST, SC, SS, MCSID):
        self.name = 'MAT1*'
        self.attr = '*'
        self.var_list = [MID, E, G, NU, RHO, A, TREF, GE, ST, SC, SS, MCSID]
        self.printer_local_16()

class RBE2(Nastran):
    def __init__(self, EID, GN, CM, *GMi):
        self.name = 'RBE2'
        self.attr = ''
        self.var_list = [EID, GN, CM, *GMi]
        self.printer_local_8()

class CAERO1(Nastran):
    def __init__(self, EID, PID, CP, NSPAN, NCHORD, LSPAN, LCHORD, IGID, X1, Y1, Z1, X12, X4, Y4, Z4, X43):
        self.name = 'CAERO1*'
        self.attr = '*'
        self.var_list = [EID, PID, CP, NSPAN, NCHORD, LSPAN, LCHORD, IGID, X1, Y1, Z1, X12, X4, Y4, Z4, X43]
        self.printer_local_16()

class CAERO2(Nastran):
    def __init__(self, EID, PID, CP, NSB, NINT, LSB, LINT, IGID, X1, Y1, Z1, X12):
        self.name = 'CAERO2*'
        self.attr = '*'
        self.var_list = [EID, PID, CP, NSB, NINT, LSB, LINT, IGID, X1, Y1, Z1, X12]
        self.printer_local_16()
    
class CAERO4(Nastran):
    def __init__(self, EID, PID, CP, NSPAN, LSPAN, X1, Y1, Z1, X12, X4, Y4, Z4, X43):
        self.name = 'CAERO4*'
        self.attr = '*'
        self.var_list = [EID, PID, CP, NSPAN, LSPAN, X1, Y1, Z1, X12, X4, Y4, Z4, X43]
        self.printer_local_16()

class PAERO1(Nastran):
    def __init__(self, PID, *Bi):
        self.name = 'PAERO1'
        self.attr = ''
        self.var_list = [PID, *Bi]
        self.printer_local_8()

class PAERO2(Nastran):
    def __init__(self, PID, ORIENT, WIDTH, AR, LRSB, LRIB, LTH1, LTH2, THI1, THN1, THI2, THN2, THI3, THN3):
        self.name = 'PAERO2'
        self.attr = ''
        self.var_list = [PID, ORIENT, WIDTH, AR, LRSB, LRIB, LTH1, LTH2, THI1, THN1, THI2, THN2, THI3, THN3]
        self.printer_local_8()

class PAERO4(Nastran):
    def __init__(self, PID, CLA, LCLA, CIRC, LCIRC, DOC1, CAOC1, GAPOC1, DOC2, CAOC2, GAPOC2, DOC3, CAOC3, GAPOC3, *etc):
        self.name = 'PAERO4*'
        self.attr = '*'
        self.var_list = [PID, CLA, LCLA, CIRC, LCIRC, DOC1, CAOC1, GAPOC1, DOC2, CAOC2, GAPOC2, DOC3, CAOC3, GAPOC3, *etc]
        self.printer_local_8()

class SET1(Nastran):
    def __init__(self, SID, *IDi):
        self.name = 'SET1'
        self.attr = ''
        self.var_list = [SID, *IDi]
        self.printer_local_8()

class AELIST(Nastran):
    def __init__(self, SID, *Ei):
        self.name = 'AELIST'
        self.attr = ''
        self.var_list = [SID, *Ei]
        self.printer_local_8()

class SPLINE2(Nastran):
    def __init__(self, EID, CAERO, ID1, ID2, SETG, DZ, DTOR, CID, DTHX, DTHY, BLANK='', USAGE='BOTH'):
        self.name = 'SPLINE2*'
        self.attr = '*'
        self.var_list = [EID, CAERO, ID1, ID2, SETG, DZ, DTOR, CID, DTHX, DTHY, BLANK, USAGE]
        self.printer_local_16()

class SPLINE5(Nastran):
    def __init__(self, SID, CAERO, AELIST, SETG, DZ, DTOR, CID, DTHX, DTHY, USAGE, METH, FTYPE, RCORE):
        self.name = 'SPLINE5*'
        self.attr = '*'
        self.var_list = [SID, CAERO, AELIST, '', SETG, DZ, DTOR, CID, DTHX, DTHY, '', USAGE, METH, '', FTYPE, RCORE]
        self.printer_local_16()

class SPLINE7(Nastran):
    def __init__(self, EID, CAERO, AELIST, SETG, DZ, DTOR, CID, USAGE, METHOD, DZR, IA2, EPSBM):
        self.name = 'SPLINE7*'
        self.attr = '*'
        self.var_list = [EID, CAERO, AELIST, '', SETG, DZ, DTOR, CID, '', '', '', USAGE, METHOD, DZR, IA2, EPSBM]
        self.printer_local_16()

class AERO(Nastran):
    def __init__(self, ACSID, VELOCITY, REFC, RHOrEF, SYMXZ, SYMXY):
        self.name = 'AERO'
        self.attr = ''
        self.var_list = [ACSID, VELOCITY, REFC, RHOrEF, SYMXZ, SYMXY]
        self.printer_local_8()

class AEROS(Nastran):
    def __init__(self, ACSID, RCSID, REFC, REFB, REFS, SYMXZ, SYMXY):
        self.name = 'AEROS'
        self.attr = ''
        self.var_list = [ACSID, RCSID, REFC, REFB, REFS, SYMXZ, SYMXY]
        self.printer_local_8()

class MKAERO1(Nastran):
    def __init__(self, m1, m2, m3, m4, m5, m6, m7, m8, k1, k2, k3, k4, k5, k6, k7, k8):
        self.name = 'MKAERO1'
        self.attr = ''
        self.var_list = [m1, m2, m3, m4, m5, m6, m7, m8, k1, k2, k3, k4, k5, k6, k7, k8]
        self.printer_local_8()

class MKAERO2(Nastran):
    def __init__(self, m1, k1, m2, k2, m3, k3, m4, k4):
        self.name = 'MKAERO2'
        self.attr = ''
        self.var_list = [m1, k1, m2, k2, m3, k3, m4, k4]
        self.printer_local_8()

class PARAM(Nastran):
    def __init__(self, N, V1, *V2):
        self.name = 'PARAM'
        self.attr = ''
        self.var_list = [N, V1, *V2]
        self.printer_local_8()

class CONM1(Nastran):
    def __init__(self, EID, G, CID, M11, M21, M31, M32, M33, M41, M42, M43, M44, M51,
                       M52, M53, M54, M55, M61, M62, M63, M64, M65, M66):
        self.name = 'CONM1*'
        self.attr = '*'
        self.var_list = [EID, G, CID, M11, M21, M31, M32, M33, M41, M42, M43, M44, M51,
                       M52, M53, M54, M55, M61, M62, M63, M64, M65, M66]
        self.printer_local_16()

class CONM2(Nastran):
    def __init__(self, EID, G, CID, M, X1, X2, X3, l11, l21, l22, I31, I32, I33):
        self.name = 'CONM2*'
        self.attr = '*'
        self.var_list = [EID, G, CID, M, X1, X2, X3, l11, l21, l22, I31, I32, I33]
        self.printer_local_16()
