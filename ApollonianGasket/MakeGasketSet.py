import os

# 1. open a file
# 2. in two for loops 
# 3. make gasket... and write out stuff to file
# 4. close file.


def ConvertToStr (value):
    
    return ''.join (str(value).split('.'))


OutputFile = 'ApollonianGasket_Set.ps'

# open a file to write to...
psFile = open (OutputFile, 'w')

psFile.write ('%!PS-Adobe-2.0\n')
psFile.write ('\n')

psFile.write ('/inch { 72 mul } def\n')
psFile.write ('\n')


Radius  =  0.9
MaxIter = 10 

for i in range (0, 4):

    for j in range (0, 5):

        A = 0.5 + 0.15 * i
        B = 0.5 + 0.1  * j

        EPSFileName = 'tmp_AG_' + ConvertToStr(Radius) + \
                            '_' + ConvertToStr(A) + \
                            '_' + ConvertToStr(B) + \
                            '_' + str(MaxIter) + '.eps'

        strCmd = 'python ApollonianGasket_EPS.py ' + str(Radius) + \
                            ' ' + str(A) + ' ' + str(B) + \
                            ' ' + str(MaxIter) + \
                            ' ' + EPSFileName; 

        os.system (strCmd)

        xOffset = 1.25 + 2 * i
        yOffset = 9.5  - 2 * j

        psFile.write ('gsave\n')
        psFile.write ('save\n')
        psFile.write ('/showpage {} def\n')
        psFile.write ('0 setgray 0 setlinecap 1 setlinewidth\n')
        psFile.write ('0 setlinejoin 10 setmiterlimit [ ] 0 setdash newpath\n')
        psFile.write (str(xOffset) + ' inch ' + str(yOffset) + ' inch translate\n')
        psFile.write ('(' + EPSFileName + ') run\n')
        psFile.write ('restore\n')
        psFile.write ('grestore\n')
        psFile.write ('\n')



psFile.write ('showpage\n')

psFile.close ()

