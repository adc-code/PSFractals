import os

print ('Making... KochSnowflake_IFS1_line_single.pdf')
os.system ('python MakeKochSnowflakeIFS_ps.py IFS1 LINE PS 5')
os.system ('ps2pdf tmp_KochSnowflake_IFS1_line_iter5.ps')
os.system ('mv tmp_KochSnowflake_IFS1_line_iter5.pdf KochSnowflake_IFS1_line_single.pdf')
print ()

print ('Making... KochSnowflake_IFS1_triangle_single.pdf')
os.system ('python MakeKochSnowflakeIFS_ps.py IFS1 TRIANGLE PS 5')
os.system ('ps2pdf tmp_KochSnowflake_IFS1_triangle_iter5.ps')
os.system ('mv tmp_KochSnowflake_IFS1_triangle_iter5.pdf KochSnowflake_IFS1_triangle_single.pdf')
print ()

print ('Making... KochSnowflake_IFS2_line_single.pdf')
os.system ('python MakeKochSnowflakeIFS_ps.py IFS2 LINE PS 4')
os.system ('ps2pdf tmp_KochSnowflake_IFS2_line_iter4.ps')
os.system ('mv tmp_KochSnowflake_IFS2_line_iter4.pdf KochSnowflake_IFS2_line_single.pdf')
print ()

print ('Making... KochSnowflake_IFS2_triangle_single.pdf')
os.system ('python MakeKochSnowflakeIFS_ps.py IFS2 TRIANGLE PS 4')
os.system ('ps2pdf tmp_KochSnowflake_IFS2_triangle_iter4.ps')
os.system ('mv tmp_KochSnowflake_IFS2_triangle_iter4.pdf KochSnowflake_IFS2_triangle_single.pdf')
print ()

print ('Making... KochSnowflake_IFS1_line_series.pdf')
for iter in range (0, 6):
    print ('    making... tmp_KochSnowflake_IFS1_line_iter' + str(iter) + '.eps')
    os.system ('python MakeKochSnowflakeIFS_ps.py IFS1 LINE EPS ' + str(iter))

f = open ('tmpKochSnowflake_IFS1_line_series.ps', 'w')

f.write ('/inch { 72 mul } def \n')
f.write ('/baselength { 2.75 inch } def \n')
f.write ('/heightEst { 2.75 1.15 mul inch } def \n\n')

f.write ('/xSpace 8.5 inch baselength 2 mul sub 3 div def \n')
f.write ('/ySpace 11 inch heightEst 3 mul sub 4 div def \n')
f.write ('/scalingfactor baselength 1 inch div def \n\n')

iter = 0
for row in range (0, 3):
    for col in range (0, 2):
        f.write ('gsave\n')
        f.write ('save\n')
        f.write ('/showpage {} def\n')
        f.write ('0 setgray 0 setlinecap 1 setlinewidth\n')
        f.write ('0 setlinejoin 10 setmiterlimit [ ] 0 setdash newpath\n')

        f.write ('xSpace ' + str(col+1) + ' mul baselength 30 sub ' + str(col) + ' mul add  11 inch heightEst ySpace add ' + str(row+1) + ' mul sub  translate\n')
        f.write ('scalingfactor dup scale\n')
        f.write ('(tmp_KochSnowflake_IFS1_line_iter' + str(iter) + '.eps) run\n')
        f.write ('restore\n')
        f.write ('grestore\n\n')

        iter += 1

f.close ()

os.system ('ps2pdf -dNOSAFER tmpKochSnowflake_IFS1_line_series.ps')
os.system ('mv tmpKochSnowflake_IFS1_line_series.pdf KochSnowflake_IFS1_line_series.pdf')

os.system ('rm tmp_KochSnowflake_IFS1_line*ps')

print ()


print ('Making... KochSnowflake_IFS1_triangle_series.pdf')
for iter in range (0, 6):
    print ('    making... tmp_KochSnowflake_IFS1_triangle_iter' + str(iter) + '.eps')
    os.system ('python MakeKochSnowflakeIFS_ps.py IFS1 TRIANGLE EPS ' + str(iter))

f = open ('tmpKochSnowflake_IFS1_triangle_series.ps', 'w')

f.write ('/inch { 72 mul } def \n')
f.write ('/baselength { 2.75 inch } def \n')
f.write ('/heightEst { 2.75 1.35 mul inch } def \n\n')

f.write ('/xSpace 8.5 inch baselength 2 mul sub 3 div def \n')
f.write ('/ySpace 11 inch heightEst 3 mul sub 4 div def \n')
f.write ('/scalingfactor baselength 1 inch div def \n\n')

iter = 0
for row in range (0, 3):
    for col in range (0, 2):
        f.write ('gsave\n')
        f.write ('save\n')
        f.write ('/showpage {} def\n')
        f.write ('0 setgray 0 setlinecap 1 setlinewidth\n')
        f.write ('0 setlinejoin 10 setmiterlimit [ ] 0 setdash newpath\n')

        f.write ('xSpace ' + str(col+1) + ' mul baselength 30 sub ' + str(col) + ' mul add  11 inch heightEst ySpace add ' + str(row+1) + ' mul sub  translate\n')
        f.write ('scalingfactor dup scale\n')
        f.write ('(tmp_KochSnowflake_IFS1_triangle_iter' + str(iter) + '.eps) run\n')
        f.write ('restore\n')
        f.write ('grestore\n\n')

        iter += 1

f.close ()

os.system ('ps2pdf -dNOSAFER tmpKochSnowflake_IFS1_triangle_series.ps')
os.system ('mv tmpKochSnowflake_IFS1_triangle_series.pdf KochSnowflake_IFS1_triangle_series.pdf')

os.system ('rm tmp_KochSnowflake_IFS1_triangle*ps')

print ()


print ('Making... KochSnowflake_IFS2_line_series.pdf')
for iter in range (0, 4):
    print ('    making... tmp_KochSnowflake_IFS2_line_iter' + str(iter) + '.eps')
    os.system ('python MakeKochSnowflakeIFS_ps.py IFS2 LINE EPS ' + str(iter))

f = open ('tmpKochSnowflake_IFS2_line_series.ps', 'w')

f.write ('/inch { 72 mul } def \n')
f.write ('/baselength { 2.75 inch } def \n')
f.write ('/heightEst { 2.75 1.15 mul inch } def \n\n')

f.write ('/xSpace 8.5 inch baselength 2 mul sub 3 div def \n')
f.write ('/ySpace 11 inch heightEst 2 mul sub 3 div def \n')
f.write ('/scalingfactor baselength 1 inch div def \n\n')

iter = 0
for row in range (0, 2):
    for col in range (0, 2):
        f.write ('gsave\n')
        f.write ('save\n')
        f.write ('/showpage {} def\n')
        f.write ('0 setgray 0 setlinecap 1 setlinewidth\n')
        f.write ('0 setlinejoin 10 setmiterlimit [ ] 0 setdash newpath\n')

        f.write ('xSpace ' + str(col+1) + ' mul baselength 30 sub ' + str(col) + ' mul add  11 inch heightEst ySpace add ' + str(row+1) + ' mul sub  translate\n')
        f.write ('scalingfactor dup scale\n')
        f.write ('(tmp_KochSnowflake_IFS2_line_iter' + str(iter) + '.eps) run\n')
        f.write ('restore\n')
        f.write ('grestore\n\n')

        iter += 1

f.close ()

os.system ('ps2pdf -dNOSAFER tmpKochSnowflake_IFS2_line_series.ps')
os.system ('mv tmpKochSnowflake_IFS2_line_series.pdf KochSnowflake_IFS2_line_series.pdf')

os.system ('rm tmp_KochSnowflake_IFS2_line*ps')

print ()


print ('Making... KochSnowflake_IFS2_triangle_series.pdf')
for iter in range (0, 4):
    print ('    making... tmp_KochSnowflake_IFS2_triangle_iter' + str(iter) + '.eps')
    os.system ('python MakeKochSnowflakeIFS_ps.py IFS2 TRIANGLE EPS ' + str(iter))

f = open ('tmpKochSnowflake_IFS2_triangle_series.ps', 'w')

f.write ('/inch { 72 mul } def \n')
f.write ('/baselength { 2.75 inch } def \n')
f.write ('/heightEst { 2.75 1.35 mul inch } def \n\n')

f.write ('/xSpace 8.5 inch baselength 2 mul sub 3 div def \n')
f.write ('/ySpace 11 inch heightEst 2 mul sub 3 div def \n')
f.write ('/scalingfactor baselength 1 inch div def \n\n')

iter = 0
for row in range (0, 2):
    for col in range (0, 2):
        f.write ('gsave\n')
        f.write ('save\n')
        f.write ('/showpage {} def\n')
        f.write ('0 setgray 0 setlinecap 1 setlinewidth\n')
        f.write ('0 setlinejoin 10 setmiterlimit [ ] 0 setdash newpath\n')

        f.write ('xSpace ' + str(col+1) + ' mul baselength 30 sub ' + str(col) + ' mul add  11 inch heightEst ySpace add ' + str(row+1) + ' mul sub  translate\n')
        f.write ('scalingfactor dup scale\n')
        f.write ('(tmp_KochSnowflake_IFS2_triangle_iter' + str(iter) + '.eps) run\n')
        f.write ('restore\n')
        f.write ('grestore\n\n')

        iter += 1

f.close ()

os.system ('ps2pdf -dNOSAFER tmpKochSnowflake_IFS2_triangle_series.ps')
os.system ('mv tmpKochSnowflake_IFS2_triangle_series.pdf KochSnowflake_IFS2_triangle_series.pdf')

os.system ('rm tmp_KochSnowflake_IFS2_triangle*ps')

print ()




