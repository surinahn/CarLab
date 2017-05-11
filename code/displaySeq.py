#import kociemba

cMap = {'U':'Y', 'R':'B', 'L':'G', 'F':'O', 'D':'W', 'B':'P'}
cMapInv = {'Y':'U', 'B':'R', 'G':'L', 'O':'F', 'W':'D', 'P':'B'}


def displayCube(seq):

    uSide = seq[0:9]
    rSide = seq[9:18]
    fSide = seq[18:27]
    dSide = seq[27:36]
    lSide = seq[36:45]
    bSide = seq[45:]


    print '          ' , cMap[uSide[0]], cMap[uSide[1]], cMap[uSide[2]]
    print '          ' , cMap[uSide[3]], cMap[uSide[4]], cMap[uSide[5]]
    print '          ' , cMap[uSide[6]], cMap[uSide[7]], cMap[uSide[8]]

    print '\n'

    print cMap[lSide[0]], cMap[lSide[1]], cMap[lSide[2]], '    ', cMap[fSide[0]], cMap[fSide[1]], cMap[fSide[2]], '    ', cMap[rSide[0]], cMap[rSide[1]], cMap[rSide[2]], '    ', cMap[bSide[0]], cMap[bSide[1]], cMap[bSide[2]]
    print cMap[lSide[3]], cMap[lSide[4]], cMap[lSide[5]], '    ', cMap[fSide[3]], cMap[fSide[4]], cMap[fSide[5]], '    ', cMap[rSide[3]], cMap[rSide[4]], cMap[rSide[5]], '    ', cMap[bSide[3]], cMap[bSide[4]], cMap[bSide[5]]
    print cMap[lSide[6]], cMap[lSide[7]], cMap[lSide[8]], '    ', cMap[fSide[6]], cMap[fSide[7]], cMap[fSide[8]], '    ', cMap[rSide[6]], cMap[rSide[7]], cMap[rSide[8]], '    ', cMap[bSide[6]], cMap[bSide[7]], cMap[bSide[8]]

    print '\n'

    print '          ' , cMap[dSide[0]], cMap[dSide[1]], cMap[dSide[2]]
    print '          ' , cMap[dSide[3]], cMap[dSide[4]], cMap[dSide[5]]
    print '          ' , cMap[dSide[6]], cMap[dSide[7]], cMap[dSide[8]]
    print '\n'


# Test

'''
seq = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'

displayCube(seq)

colorSeq = ''

for c in seq:
    colorSeq += cMap[c]

print 'Current up side: ', colorSeq[0:9]
print 'Current right side: ', colorSeq[9:18]
print 'Current front side: ', colorSeq[18:27]
print 'Current down side: ', colorSeq[27:36]
print 'Current left side: ', colorSeq[36:45]
print 'Current back side: ', colorSeq[45:]
print '\n'
userConfig = ''
userConfig += raw_input("Enter edited up side: ")
userConfig += raw_input("Enter edited right side: ")
userConfig += raw_input("Enter edited front side: ")
userConfig += raw_input("Enter edited down side: ")
userConfig += raw_input("Enter edited left side: ")
userConfig += raw_input("Enter edited back side: ")
print '\n'
editSeq = ''

for c in userConfig:
    editSeq += cMapInv[c]

displayCube(editSeq)

print 'Solution: ', kociemba.solve(editSeq)
'''
