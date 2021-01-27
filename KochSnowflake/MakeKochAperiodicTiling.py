#
# MakeKochAperiodicTiling.py
# One off program used to make Aperiodic recursive tilings of the Koch snowflake curve.
#

print ('Writing to file... tmpKochAPeriodicTiling.ps')

f = open ('tmpKochAPeriodicTiling.ps', 'w')

f.write ('/level 0 def \n')
f.write ('/Inc_level { /level level 1 add def } def \n')
f.write ('/Dec_level { /level level 1 sub def } def \n')
f.write ('/inch { 72 mul } def \n')
f.write ('/baselength { 1 inch } def\n\n')

f.write ('0 setlinecap\n\n')

f.write ('/DrawF { baselength 0 rlineto } def \n\n')

f.write ('/Minus { -60 rotate } def \n')
f.write ('/Plus  {  60 rotate } def \n\n')

f.write ('/RuleF \n')
f.write ('{\n')
f.write ('   level 0 gt\n')
f.write ('   {\n')
f.write ('       Dec_level\n')
f.write ('       % F -> F-F++F-F\n')
f.write ('       RuleF Minus RuleF Plus Plus RuleF Minus RuleF \n')
f.write ('       Inc_level\n')
f.write ('   }\n')
f.write ('   {\n')
f.write ('       DrawF\n')
f.write ('   } ifelse\n')
f.write ('} def\n\n')

f.write ('/Axiom\n')
f.write ('{\n')
f.write ('   % F++F++F\n')
f.write ('   RuleF Plus Plus RuleF Plus Plus RuleF\n')
f.write ('} def\n\n')

f.write ('/MakeKochSnowflake\n')
f.write ('{\n')
f.write ('    gsave\n')
f.write ('        newpath\n')
f.write ('            0 0 moveto\n')
f.write ('            Axiom\n') 
f.write ('        closepath\n')
f.write ('        gsave 0 setgray stroke grestore fill\n')
f.write ('    grestore\n')
f.write ('} def\n\n')

f.write ('/len 2.5 def\n/width len inch def\n/height width 2 3 sqrt div mul def\n')
f.write ('/xOffset width 2 div -1 mul def\n')
f.write ('/yOffset height 4 div -1 mul def\n')

f.write ('/xCenter 8.5 inch 2 div def\n/yCenter 11 inch 2 div def\n\n')

f.write ('/level 4 def\n\n')

f.write ('xCenter yCenter translate\n')

# note for now we are just using a preset set of colours
colors = [ [ 204, 239, 255 ], [ 128, 215, 255 ], [ 51, 190, 255], [ 0, 157, 230 ], [ 0, 105, 153], [ 0, 52, 77], [ 0, 17, 26] ]
#colors.reverse ()

normColors = []
for col in colors:
    normCol = []
    for values in col:
        normCol.append (values / 255)
    normColors.append (normCol)

level = 1

def DoIt (angle, iter, isLast):
    if iter == 0:
        return

    f.write ('% ' + str(angle) + '  ' + str(iter) + '\n')

    f.write ('gsave\n')          
    f.write ('    ' + str(angle) + ' rotate\n')
    f.write ('    width 2 3 div mul 0 translate\n')
    f.write ('    gsave\n')     
    f.write ('        ' + str(iter * 90) + ' setlinewidth\n')

    if iter % 2 == 0:
        f.write ('        ' + str(30) + ' rotate\n')
    else:
        f.write ('        ' + str(-30) + ' rotate\n')

    f.write ('        1 3 sqrt div dup scale\n')
    f.write ('        gsave\n') 
    f.write ('            xOffset  yOffset  translate\n')
    f.write ('            1 3 div level exp len mul dup scale\n')

    if iter == 1: 
        f.write ('            MakeKochSnowflake\n')

    f.write ('        grestore\n') 

    for a in [ -60, 0, 60 ]:
        DoIt (a, iter-1, False)

    f.write ('    grestore\n')  
    f.write ('grestore\n')     


# Make all the iterations and layer them on top of each other
for i in range (5, 0, -1):
    f.write ('            ' + str(normColors [i][0]) + ' ' + str(normColors [i][1]) + ' ' + str(normColors [i][2]) + ' setrgbcolor\n')
    for angle in [ 0, 60, 120, 180, 240, 300 ]: 
        isLast = False
        DoIt (angle, i, isLast)

# Make another snowflake in the center... this is the zero iteration case
f.write ('            ' + str(normColors [0][0]) + ' ' + str(normColors [0][1]) + ' ' + str(normColors [0][2]) + ' setrgbcolor\n')
f.write ('gsave\n')
f.write ('    80 setlinewidth\n')
f.write ('    gsave\n')
f.write ('        xOffset  yOffset  translate\n')
f.write ('        1 3 div level exp len mul dup scale\n')
f.write ('        MakeKochSnowflake\n')
f.write ('    grestore\n')
f.write ('grestore\n')

f.write ('showpage\n')

f.close ()



