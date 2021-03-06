import os, sys, subprocess
import kociemba
import itertools

def read():
        #subprocess.call(['./read_cube.sh'])
	#subprocess.call("sudo python process_cube.py cleaned.txt > seq.txt", shell=True)
	#file = open('seq.txt', 'r')
	#seq = file.readline()
	#file.close()
        
        process1 = subprocess.Popen('./read_cube.sh', shell=True)
        process1.wait()
	process = subprocess.Popen(['sudo python process_cube.py cleaned.txt'], shell=True, stdout=subprocess.PIPE)
        process.wait()
        seq = process.communicate()
        seq = seq[0]
        seq = seq[0:9]
        return seq 


sqrs = {'U1':0, 'U2':1, 'U3':2, 'U4':3, 'U5':4, 'U6':5, 'U7':6, 'U8':7, 'U9':8, 
        'R1':9, 'R2':10, 'R3':11, 'R4':12, 'R5':13, 'R6':14, 'R7':15, 'R8':16, 'R9':17, 
        'F1':18, 'F2':19, 'F3':20, 'F4':21, 'F5':22, 'F6':23, 'F7':24, 'F8':25, 'F9':26,
        'D1':27, 'D2':28, 'D3':29, 'D4':30, 'D5':31, 'D6':32, 'D7':33, 'D8':34, 'D9':35, 
        'L1':36, 'L2':37, 'L3':38, 'L4':39, 'L5':40, 'L6':41, 'L7':42, 'L8':43, 'L9':44, 
        'B1':45, 'B2':46, 'B3':47, 'B4':48, 'B5':49, 'B6':50, 'B7':51, 'B8':52, 'B9':53}

corner_indices = [[sqrs['U1'], sqrs['L1'], sqrs['B3']], 
                [sqrs['U3'], sqrs['R3'], sqrs['B1']], 
                [sqrs['U7'], sqrs['F1'], sqrs['L3']], 
                [sqrs['U9'], sqrs['R1'], sqrs['F3']], 
                [sqrs['R7'], sqrs['F9'], sqrs['D3']], 
                [sqrs['R9'], sqrs['D9'], sqrs['B7']], 
                [sqrs['F7'], sqrs['D1'], sqrs['L9']], 
                [sqrs['D7'], sqrs['L7'], sqrs['B9']]]

corners = ['ULB', 'URB', 'UFL', 'URF', 'RFD', 'RDB', 'FDL', 'DLB']

edge_indices = [[sqrs['U2'], sqrs['B2']], [sqrs['U4'], sqrs['L2']], 
                [sqrs['U6'], sqrs['R2']], [sqrs['U8'], sqrs['F2']], 
                [sqrs['R4'], sqrs['F6']], [sqrs['R6'], sqrs['B4']], 
                [sqrs['R8'], sqrs['D6']], [sqrs['F4'], sqrs['L6']], 
                [sqrs['F8'], sqrs['D2']], [sqrs['D4'], sqrs['L8']], 
                [sqrs['D8'], sqrs['B8']], [sqrs['L4'], sqrs['B6']]]

edges = ['UB', 'UL', 'UR', 'UF', 'RF', 'RB', 'RD', 'FL', 'FD', 'DL', 'DB', 'LB']

letters = ['B','F','U','L','D','R']

#seq = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
#seq = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
#seq = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBLB'

#seq = 'UUUUUUUUURRDLRLDRDFFFDFBRLBDFDRDBRBFLLLRLFDFFBBBDBDLDB'
#seq = 'UDUUUUUUURRDLRLDRDFFFDFBRLBDFDRDBRBFLLLRLFDFFBBBDBDLDU'

#seq = 'DDBUUUUDLUFLLRDDFLRLFLFBLDRFBFFDLDRBRBFFLDBRDURUFBRDUR'
seq = 'FFURULDBLDURLRRDDRLUBDFFBFBUUULDRRURLBFLLBUDLBUUUBBDDF' 

def counts(ss): 
        count = [0,0,0,0,0,0]
        for s in ss: 
                index = letters.index(s)
                count[index] += 1
        print count
        return count

def missings(cs): 
        missing = [] 
        for i in range(0,6):
                c = cs[i] 
                diff = 9 - c 
                if diff > 0: 
                        for j in range(0,diff): 
                                missing.append(letters[i])
        print missing
        return missing

def extras(cs): 
        extra = [] 
        for i in range(0,6):
                c = cs[i] 
                diff = c - 9 
                if diff > 0: 
                        for j in range(0,diff): 
                                extra.append(letters[i])
        print extra
        return extra


def set_seq(s): 
        global seq 
        seq = ''.join(s) 

def get_corner(indices): 
        colors = [seq[i] for i in indices]
        return colors

def get_edge(indices): 
        colors =[seq[i] for i in indices]
        return colors

def get_dup(d): 
        if d[0] == d[1] == d[2]: 
                return [d[1],d[1]]
        if d[0] == d[1]: 
                return [d[0]]
        return [d[2]]

def find_wrongs(ws, rs): 
        length = len(ws)
        found = []
        wrongs = [] 
        for i in range(0,length):
                w = ws[i]
                if w not in rs: 
                        wrongs.append(w)
                if w in found: 
                        wrongs.append(w)
                found.append(w)
        return wrongs

def D_diff(a,b): 
        return 'D' in list(set(a)-set(b)) or a.count('D') < 2

def least_diffs(bs, cs):
        lenb = len(bs)
        lenc = len(cs)
        leasts = [] 
        for i in range(0, lenb):
                b = bs[i]
                diffs = [] 
                for j in range(0, lenc):
                        c = cs[j]
                        if not D_diff(b,c):
                                leasts.append([b,c])
        print "leasts"
        print leasts

        return leasts 
                                     
                

#wrong and right not alphad
def correct_corner(position, wrong, right, sq): 
        new_color = list(set(right) - set(wrong))
        old_color = list(set(wrong) - set(right))

        if len(old_color) < len(new_color): 
                old_color += get_dup(wrong)

        wrongs = len(new_color)

        for i in range(0, wrongs): 
                indices = corner_indices[position]

                index = indices[wrong.index(old_color[i])]

                s = list(sq)
                s[index] = new_color[i]
                return ''.join(s)

def correct_edge(position, wrong, right, sq): 
        wrong_index = 0 
        new_color = right[0]
        old_color = wrong[0]
        if wrong[0] == right[0]: 
                new_color = right[1]
                old_color = wrong[1]
                wrong_index = 1

        elif wrong[0] == right[1]: 
                new_color = right[0]
                old_color = wrong[1]
                wrong_index = 1

        elif wrong[1] == right[0]: 
                new_color = right[1]
                old_color = wrong[0]
                wrong_index = 0

        indices = edge_indices[position]
        index = indices[wrong_index]

        s = list(sq)
        s[index] = new_color
        return ''.join(s)


def alpha(ar): 
        alphad = [''.join(sorted(a)) for a in ar]
        return alphad
 

def problem_areas(s):
        yellows = s.count('U')
        whites = s.count('D')
        seq = ''

def generate_seq_corner(missing_corners, wrong_corners, found_corners, sq): 
        wrong_positions = [found_corners.index(w) for w in wrong_corners]
        seq = sq 

        wrongs = len(wrong_positions)
        for i in range(0, wrongs): 
                seq = correct_corner(wrong_positions[i], 
                        wrong_corners[i], 
                        missing_corners[i], seq)
        return seq 

def generate_seq_edge(missing_edges, wrong_edges, found_edges, sq): 
        wrong_positions = [found_edges.index(w) for w in wrong_edges]
        seq = sq 

        wrongs = len(wrong_positions)
        for i in range(0, wrongs): 
                seq = correct_edge(wrong_positions[i], 
                        wrong_edges[i], 
                        missing_edges[i], seq)
        return seq 


# count = counts(seq)
# missings(count)
# extras(count)

def bookkeep(s): 
        print "Attempting to algorithmically correct misreads"
        #set the sequence 
        set_seq(s)

        #find the corners lists 
        found_corners = [''.join(get_corner(i)) for i in corner_indices]

        alpha_found_corners = alpha(found_corners)
        alpha_corners =  alpha(corners)

        alpha_missing_corners = list(set(alpha_corners) - set(alpha_found_corners))
        alpha_wrong_corners = find_wrongs(alpha_found_corners, alpha_corners)

        missing_corners = [corners[alpha_corners.index(a)] for a in alpha_missing_corners]
        wrong_corners = [found_corners[alpha_found_corners.index(a)] for a in alpha_wrong_corners]

        missing_perms_c = list(itertools.permutations(missing_corners))
        wrong_perms_c = list(itertools.permutations(wrong_corners))


        #find the edges list
        found_edges = [''.join(get_edge(i)) for i in edge_indices]

        #find the edges list 
        alpha_found_edges = alpha(found_edges)
        alpha_edges =  alpha(edges)

        alpha_missing_edges = list(set(alpha_edges) - set(alpha_found_edges))
        alpha_wrong_edges = find_wrongs(alpha_found_edges, alpha_edges)

        missing_edges = [edges[alpha_edges.index(a)] for a in alpha_missing_edges]
        wrong_edges = [found_edges[alpha_found_edges.index(a)] for a in alpha_wrong_edges]

        missing_perms_e = list(itertools.permutations(missing_edges))
        wrong_perms_e = list(itertools.permutations(wrong_edges))


        sq = seq
        m_c_count = 0 
        w_c_count = 0 
        m_e_count = 0 
        w_e_count = 0 
        simple_perms = True 

        total_wrongs = len(wrong_corners) + len(wrong_edges)
        print "misread this many corners"
        print len(missing_perms_c)
        print "misread this many edges"
        print len(missing_perms_e)

        # print missing_perms_e
        # print wrong_perms_e
        # print missing_perms_c
        # print wrong_perms_c

        if total_wrongs > 5:
                return -1 
                
        while simple_perms:
                try: 
                        # current = '(' + str(w_e_count) + ',' + str(m_e_count) + ',' + str(w_c_count) + ',' + str(w_c_count) + ')'
                        # print current 
                        sq = generate_seq_corner(missing_perms_c[m_c_count], wrong_perms_c[w_c_count], found_corners, seq)
                        sq = generate_seq_edge(missing_perms_e[m_e_count], wrong_perms_e[w_e_count], found_edges, sq)
                        solution = kociemba.solve(sq)
                        print "fixed this many wrong corners:"
                        print len(wrong_corners)
                        print "fixed this many wrong edges:"
                        print len(wrong_edges)
                        return sq
                        break
                except ValueError: 
                        
                        w_e_count += 1
                        if w_e_count >= len(wrong_perms_e): 
                                w_e_count = 0
                                m_e_count += 1
                        if m_e_count >= len(missing_perms_e):
                                m_e_count = 0 
                                w_c_count += 1
                        if w_c_count >= len(wrong_perms_c): 
                                w_c_count = 0
                                m_c_count += 1
                        if m_c_count >= len(missing_perms_c):
                                simple_perms = False   
                 


        print "Unable to correct misreads :("
        return -1 

bookkeep(seq)
