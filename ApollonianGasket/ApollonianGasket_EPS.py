import cmath
import math
import sys


# Note:
# Use python for all the calculations and (encapsulated) Postscript purely for output/display purposes


if len(sys.argv) != 6:
    
    print ('Error: Not enough command line arguments!')
    print ()
    print ('Usage: ' + sys.argv[0] + ' <Radius in Inches> <A value> <B value> <Max Iterations> <Output Name>')
    print ()
   
    sys.exit ()
 

MIN_SIZE       = 0.5
INCHES_TO_PTS  = 72


R  = float(sys.argv[1]) * INCHES_TO_PTS
A  = float(sys.argv[2]) * R 
B  = float(sys.argv[3]) * R 

MAX_LEVEL = int(sys.argv[4])

OutputFile = sys.argv[5]




def DrawCircle (file, pos, rad):

    # print ('  --> DrawCircle ', pos.real, ', ', pos.imag, ',  rad: ', rad)

    outputTxt  = str (pos.real)
    outputTxt += ' '
    outputTxt += str (pos.imag)
    outputTxt += ' '
    outputTxt += str (rad)
    outputTxt += ' 0 360 arc stroke \n'

    file.write (outputTxt)



def SolveForB4 (b1, b2, b3):

    s = b1 + b2 + b3
    r = 2 * math.sqrt ( b1*b2 + b1*b3 + b2*b3 )

    return  s + r


def CalcCircleCoords (b1, z1, b2, z2, b3, z3):

    # Using the formula to determine z4:
    # (b1z1)^2 + (b2z2)^2 + (b3z3)^2 + (b4z4)^2 = 1/2 (b1z1 + b2z2 + b4z4 + b4z4)^2
    #
    # Note b4z4 can be solved by:
    # b4z4 = (b1z1 + b2z2 + b3z3) +/- 2 sqrt ( b1b2z1z2 + b1b3z1z3 + b2b3z2z3 )

    b1z1 = b1 * z1
    b2z2 = b2 * z2
    b3z3 = b3 * z3

    b4 = SolveForB4 (b1, b2, b3)
    
    # solve for b4z4... 
    z4 = ( ( b1z1 + b2z2 + b3z3 ) + 2 * cmath.sqrt ( b1z1*b2z2 + b1z1*b3z3 + b2z2*b3z3 ) ) / b4

    return [ b4, z4 ]


def SolveForB4Prime (b1, z1, b2, z2, b3, z3, b4, z4):

    # Recall... (similar with the complex versions)
    # b4 + b4' = 2 ( b1 + b2 + b3 )
    #      b4' = 2 ( b1 + b2 + b3 ) - b4

    b4prime = 2 * ( b1 + b2 + b3 ) - b4

    b1z1 = b1 * z1
    b2z2 = b2 * z2
    b3z3 = b3 * z3
    b4z4 = b4 * z4

    z4prime = ( 2 * ( b1z1 + b2z2 + b3z3 ) - b4z4 ) / b4prime

    return [ b4prime, z4prime ]


def RecursivelySolve (b1, z1, b2, z2, b3, z3, b4, z4, level):

    if (level < 0):
        return

    b2prime, z2prime = SolveForB4Prime (b1, z1,  b3, z3,  b4, z4,  b2, z2)
    b3prime, z3prime = SolveForB4Prime (b1, z1,  b2, z2,  b4, z4,  b3, z3)
    b4prime, z4prime = SolveForB4Prime (b1, z1,  b2, z2,  b3, z3,  b4, z4)

    if (abs(1 / b2prime) > MIN_SIZE):
        DrawCircle (psFile, z2prime, abs(1 / b2prime))

    if (abs(1 / b3prime) > MIN_SIZE):
        DrawCircle (psFile, z3prime, abs(1 / b3prime))

    if (abs(1 / b4prime) > MIN_SIZE):
        DrawCircle (psFile, z4prime, abs(1 / b4prime))

    RecursivelySolve (b2prime, z2prime,  b1, z1,  b3, z3,  b4, z4,  level - 1)
    RecursivelySolve (b3prime, z3prime,  b1, z1,  b2, z2,  b4, z4,  level - 1)
    RecursivelySolve (b4prime, z4prime,  b1, z1,  b2, z2,  b3, z3,  level - 1)


def MakeApollonianGasket (b1, z1, b2, z2, b3, z3):

    b4, z4           = CalcCircleCoords (b1, z1,  b2, z2,  b3, z3)
    b4prime, z4prime = SolveForB4Prime  (b1, z1,  b2, z2,  b3, z3,  b4, z4)

    # Draw the three base 
    DrawCircle (psFile, z1, abs(1 / b1))
    DrawCircle (psFile, z2, abs(1 / b2))
    DrawCircle (psFile, z3, abs(1 / b3))

    
    DrawCircle (psFile, z4,      abs(1 / b4))
    DrawCircle (psFile, z4prime, abs(1 / b4prime))

    RecursivelySolve (b1, z1,  b2, z2,  b3, z3,  b4, z4,  MAX_LEVEL)
    RecursivelySolve (b1, z1,  b2, z2,  b3, z3,  b4prime, z4prime,  MAX_LEVEL)
    #RecursivelySolve (b4prime, z4prime,  b2, z2,  b3, z3,  b4, z4,  MAX_LEVEL)



RA = R - A
RB = R - B

Theta = math.acos ( ( A ** 2  +  B ** 2  -  (RA + RB) ** 2 ) / ( 2*A*B ) )

offsetX = 0    #72 * 3.5
offsetY = 0    #72 * 2

z1 = complex (0 + offsetX, 0 + offsetY)
b1 = -1 / R

z2 = complex (A + offsetX, 0 + offsetY)
b2 = 1 / RA

z3 = complex (B * math.cos(Theta) + offsetX, B * math.sin(Theta) + offsetY)
b3 = 1 / RB


llx = -R  # 4.25 * INCHES_TO_PTS - R
lly = -R  # 5.5  * INCHES_TO_PTS - R
urx =  R  # 4.25 * INCHES_TO_PTS + R
ury =  R  # 5.5  * INCHES_TO_PTS + R

# open a file to write to...
psFile = open (OutputFile, 'w')

psFile.write ('%!PS-Adobe-3.0 EPSF-3.0\n')
psFile.write ('%%BoundingBox: ' + str(llx) + ' ' + str(lly) + ' ' + str(urx) + ' ' + str(ury) + '\n')

psFile.write ('\n')

psFile.write ('1 setlinewidth\n')


MakeApollonianGasket (b1, z1, b2, z2, b3, z3)


# psFile.write ('showpage\n')

psFile.close ()



