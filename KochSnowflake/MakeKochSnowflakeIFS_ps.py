#
# MakeKochSnowflakeIFS_ps.py
# script ised to make Koch Snowflakes based on two different IFS rules
# note that there are a few hard coded and heuristic elements such as line thickness
#


import numpy as np
import math
import sys


# 
# key variables to change (to reduce confusion, they have been capitalized)
#
SHAPE    = 1   # 1... line  2... triangle
IFS      = 0   # 0... first set of rules   1... second set of rules
ITERS    = 3   # number of iterations
FILETYPE = 0   # 1... PS file  2... EPS file


#
# geometry related
#
lineStartPoint = np.array ( [0, 0] )
lineEndPoint   = np.array ( [1, 0] )

triangleStartPoint = np.array ( [0, 0] )
triangleEndPoint   = np.array ( [1, 0] )
triangleMidPoint   = np.array ( [1/2, math.sqrt(3)/2] )

line       = [ lineStartPoint, lineEndPoint ]
triangle   = [ triangleStartPoint, triangleMidPoint, triangleEndPoint ]

#
# other variables...
#
ScalingFactor = 7
Rules = [ [ 1, 2, 3, 4, 5, 6, 7 ], 
          [ 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14 ] ]


#
# inchesToPoints: utility function used to convert inches to (postscript) point size
#
def inchesToPoints (length):
    return length * 72


#
# TransformPoint: all the various rules used to transform the points for both IFSes
#
def TransformPoint ( point, rule ):

    if rule == 1:
 
        trans  = np.array ( [ [ -1/6, math.sqrt(3)/6 ], 
                              [ -1*math.sqrt(3)/6, -1/6 ] ] )
        offset = np.array ( [ 1/6, math.sqrt(3)/6 ] ) 
        
        return np.matmul (trans, point) + offset

    elif rule == 2:

        trans  = np.array ( [ [ 1/6, -1*math.sqrt(3)/6 ], 
                              [ math.sqrt(3)/6, 1/6 ] ] )
        offset = np.array ( [ 1/6, math.sqrt(3)/6 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 3:

        trans  = np.array ( [ [ 1/3, 0 ], 
                              [ 0, 1/3 ] ] )
        offset = np.array ( [ 1/3, math.sqrt(3)/3 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 4:

        trans  = np.array ( [ [ 1/6, math.sqrt(3)/6 ], 
                              [ -1*math.sqrt(3)/6, 1/6 ] ] )
        offset = np.array ( [ 2/3, math.sqrt(3)/3 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 5:

        trans  = np.array ( [ [ 1/2, -1*math.sqrt(3)/6 ], 
                              [ math.sqrt(3)/6, 1/2 ] ] )
        offset = np.array ( [ 1/3, 0 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 6:

        trans  = np.array ( [ [ -1/3, 0 ], 
                              [ 0, -1/3 ] ] )
        offset = np.array ( [ 2/3, 0 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 7:

        trans  = np.array ( [ [ 1/3, 0 ], 
                              [ 0, 1/3 ] ] )
        offset = np.array ( [ 2/3, 0 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 8:

        trans  = np.array ( [ [ -1/6, -1*math.sqrt(3)/18 ], 
                              [ math.sqrt(3)/18, -1/6 ] ] )
        offset = np.array ( [ 5/6, math.sqrt(3)/6 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 9:

        trans  = np.array ( [ [ 1/6, math.sqrt(3)/18 ], 
                              [ -1*math.sqrt(3)/18, 1/6 ] ] )
        offset = np.array ( [ 1/2, 5*math.sqrt(3)/18 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 10:

        trans  = np.array ( [ [ 1/6, -1*math.sqrt(3)/18 ], 
                              [ math.sqrt(3)/18, 1/6 ] ] )
        offset = np.array ( [ 1/3, 2*math.sqrt(3)/9 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 11:

        trans  = np.array ( [ [ 0, -math.sqrt(3)/9 ], 
                              [ math.sqrt(3)/9, 0 ] ] )
        offset = np.array ( [ 1/3, math.sqrt(3)/9 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 12:

        trans  = np.array ( [ [ 1/3, 0 ], 
                              [ 0, 1/3 ] ] )
        offset = np.array ( [ 1/3, math.sqrt(3)/9 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 13:

        trans  = np.array ( [ [ -1/6, math.sqrt(3)/18 ], 
                              [ -1*math.sqrt(3)/18, -1/6 ] ] )
        offset = np.array ( [ 2/3, math.sqrt(3)/9 ] )
        
        return np.matmul (trans, point) + offset

    elif rule == 14:

        trans  = np.array ( [ [ 1/6, -1*math.sqrt(3)/18 ], 
                              [ 1*math.sqrt(3)/18, 1/6 ] ] )
        offset = np.array ( [ 1/3, 0 ] )
        
        return np.matmul (trans, point) + offset


#
# TransformShape: transform each point in the shape using a specific rule
#
def TransformShape ( shape, rule ):

    transformedPoints = []
    for point in shape:
        p = TransformPoint ( point, rule )
        transformedPoints.append ( p )

    return transformedPoints


#
# WriteShapeToFile: used to write the shape information to the ps or eps file
#
def WriteShapeToFile ( file, shape ):

    # if line...
    if SHAPE == 1:  

        file.write ('gsave\n')
        #file.write ('    54  252  translate\n')
        #file.write ('    10  160  translate\n')
        file.write ('    ' + str( xOffset ) + ' ' + str( yOffset ) + ' translate\n')
        file.write ('    ' + str( inchesToPoints (ScalingFactor * shape[0][0]) ) + ' ' + str( inchesToPoints (ScalingFactor * shape[0][1]) ) + ' moveto \n')
        file.write ('    ' + str( inchesToPoints (ScalingFactor * shape[1][0]) ) + ' ' + str( inchesToPoints (ScalingFactor * shape[1][1]) ) + ' lineto \n')
        file.write ('    stroke \n')
        file.write ('grestore \n')

    # if triangle...
    elif SHAPE == 2:  

        file.write ('gsave\n')
        #file.write ('    54  252  translate\n')
        #file.write ('    10  160  translate\n')
        file.write ('    ' + str( xOffset ) + ' ' + str( yOffset ) + ' translate\n')
        file.write ('    ' + str( inchesToPoints (ScalingFactor * shape[0][0]) ) + ' ' + str( inchesToPoints (ScalingFactor * shape[0][1]) ) + ' moveto \n')
        file.write ('    ' + str( inchesToPoints (ScalingFactor * shape[1][0]) ) + ' ' + str( inchesToPoints (ScalingFactor * shape[1][1]) ) + ' lineto \n')
        file.write ('    ' + str( inchesToPoints (ScalingFactor * shape[2][0]) ) + ' ' + str( inchesToPoints (ScalingFactor * shape[2][1]) ) + ' lineto \n')
        file.write ('    fill \n')
        file.write ('grestore \n')



xLimits = [ 9e9, -9e9 ]
yLimits = [ 9e9, -9e9 ]

#
# UpdateBBoxLimits: Utility function used to function determine the bounding box of the results
#
def UpdateBBoxLimits (shape):

    startX = inchesToPoints (ScalingFactor * line[0][0])
    startY = inchesToPoints (ScalingFactor * line[0][1])
    endX   = inchesToPoints (ScalingFactor * line[1][0])
    endY   = inchesToPoints (ScalingFactor * line[1][1])
    
    if startX < xLimits [0]:
        xLimits [0] = startX
    elif startX > xLimits [1]:
        xLimits [1] = startX
        
    if startY < yLimits [0]:
        yLimits [0] = startY
    elif startY > yLimits [1]:
        yLimits [1] = startY
        
    if endX < xLimits [0]:
        xLimits [0] = endX
    elif endX > xLimits [1]:
        xLimits [1] = endX
        
    if endY < yLimits [0]:
        yLimits [0] = endY
    elif endY > yLimits [1]:
        yLimits [1] = endY
        

#
# MakeCurve: does the work to make the resulting fractal object
#
def MakeCurve ( file, shape, iter ):

    # simply do nothing (just return) for the root case
    if iter == 0:
        return

    # go through all the rules for the particular IFS
    for ruleNum in Rules [IFS]:

        # transform the shape...
        transformedShape = TransformShape ( shape, ruleNum )

        # repeat this process recursively for the results...
        MakeCurve ( file, transformedShape, iter-1)

        # finally for the bottom most or final iteration, write it to
        # the file
        if iter == 1:
            WriteShapeToFile (file, transformedShape)


#
# Main program...
#
if __name__ == '__main__':

    # uncomment for debugging
    # print (len (sys.argv))
    # for i in range(len(sys.argv)):
    #     print (i, sys.argv[i])

    if len (sys.argv) != 5:
        print ('Error: incorrect number of parameters!!!')
        print ()
        print ('Usage: ', sys.argv[0], '  [IFS1 | IFS2]  [LINE | TRIANGLE]  [PS | EPS]  [Number Of Iterations]')
        print ()
        sys.exit ()

    # Note... should really check these parameters a bit better.  For now, this program is only used another 
    # program so we are not going to be too rigorous with checking anything
    IFSStr = sys.argv[1]
    if sys.argv[1] == 'IFS2':
        IFS = 1

    geometry    = line
    geometryStr = 'line'
    if sys.argv[2] == 'TRIANGLE':
        SHAPE = 2
        geometry = triangle
        geometryStr = 'triangle'

    FileTypeStr = '.ps'
    if sys.argv[3] == 'EPS':
        FILETYPE = 2
        FileTypeStr = '.eps'

    numIters = int(sys.argv[4])
    if numIters < 0 or numIters > 7:
        ITERS = 3
    else:
        ITERS = numIters

    fileName = 'tmp_KochSnowflake_' + IFSStr + '_' + geometryStr + '_iter' + str(ITERS) + FileTypeStr
    # print ('Writing to file: ', fileName)
    f = open (fileName, 'w')

    width     = round (inchesToPoints (ScalingFactor), 1)
    height    = round (inchesToPoints (ScalingFactor) * 2 / math.sqrt(3), 1)
    lowerPart = height / 4
    xOffset = round ((inchesToPoints (8.5) - width) / 2, 1)
    yOffset = round ((inchesToPoints (11) - height) / 2 + lowerPart, 1)
    lineWidth = 1
    
    if FILETYPE == 2:

        ScalingFactor = 1

        width     = round (inchesToPoints (ScalingFactor), 1)
        height    = round (inchesToPoints (ScalingFactor) * 2 / math.sqrt(3), 1)
        lowerPart = height / 4
        xOffset   = 10
        yOffset   = lowerPart + 10  

        if IFS == 0: 
            lineWidth = 3 - 2.9/5 * ITERS
        else:
            lineWidth = 3 - 2.5/3 * ITERS

        f.write ('%!PS-Adobe-3.0 EPSF-3.0\n')
        f.write ('%%BoundingBox: 0 10 ' + str(width) + ' ' + str(height) + '\n')

    # uncomment for debugging
    # print (width, height)
    # print (xOffset, yOffset)   

    f.write (str(lineWidth) + ' setlinewidth\n')
    f.write ('1 setlinecap\n')
    f.write ('0 0 0.5 setrgbcolor\n')

    if ITERS > 0:
        MakeCurve (f, geometry, ITERS)
    else:
        # if we have 0 iterations just write out the shape
        WriteShapeToFile (f, geometry)

    f.close ()



