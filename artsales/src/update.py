import os
import os.path

dependencies = [
    ('../index.html', ['index.py'], 'index.py'),
    ('../Artifact0308.html', ['page.py', 'Artifact0308.py'], 'Artifact0308.py'),
    ('../Artifact1229.html', ['page.py', 'Artifact1229.py'], 'Artifact1229.py'),
    ('../Artifact1546.html', ['page.py', 'Artifact1546.py'], 'Artifact1546.py'),
    ('../Artifact2107.html', ['page.py', 'Artifact2107.py'], 'Artifact2107.py'),
    ('../Artifact2777.html', ['page.py', 'Artifact2777.py'], 'Artifact2777.py'),
    ('../Artifact3000.html', ['page.py', 'Artifact3000.py'], 'Artifact3000.py'),
    ('../Artifact3208.html', ['page.py', 'Artifact3208.py'], 'Artifact3208.py'),
    ('../Artifact3219.html', ['page.py', 'Artifact3219.py'], 'Artifact3219.py'),
    ('../Artifact3256.html', ['page.py', 'Artifact3256.py'], 'Artifact3256.py'),
    ('../Artifact3609.html', ['page.py', 'Artifact3609.py'], 'Artifact3609.py'),
    ('../Artifact3619.html', ['page.py', 'Artifact3619.py'], 'Artifact3619.py'),
    ('../Artifact3735.html', ['page.py', 'Artifact3735.py'], 'Artifact3735.py'),
    ('../Artifact3891.html', ['page.py', 'Artifact3891.py'], 'Artifact3891.py'),
    ('../Artifact3900.html', ['page.py', 'Artifact3900.py'], 'Artifact3900.py'),
    ('../Artifact3907.html', ['page.py', 'Artifact3907.py'], 'Artifact3907.py'),
    ('../Artifact4261.html', ['page.py', 'Artifact4261.py'], 'Artifact4261.py'),
    ('../Artifact4291.html', ['page.py', 'Artifact4291.py'], 'Artifact4291.py'),
    ('../Artifact4355.html', ['page.py', 'Artifact4355.py'], 'Artifact4355.py'),
    ('../Artifact4357.html', ['page.py', 'Artifact4357.py'], 'Artifact4357.py'),
    ('../Artifact4363.html', ['page.py', 'Artifact4363.py'], 'Artifact4363.py'),
    ('../Artifact4379.html', ['page.py', 'Artifact4379.py'], 'Artifact4379.py'),
    ('../Artifact4500.html', ['page.py', 'Artifact4500.py'], 'Artifact4500.py'),
    ('../Artifact4514.html', ['page.py', 'Artifact4514.py'], 'Artifact4514.py'),
    ('../Artifact4758.html', ['page.py', 'Artifact4758.py'], 'Artifact4758.py'),
    ('../Artifact4963.html', ['page.py', 'Artifact4963.py'], 'Artifact4963.py'),
    ('../Artifact4988.html', ['page.py', 'Artifact4988.py'], 'Artifact4988.py'),
    ('../Artifact5009.html', ['page.py', 'Artifact5009.py'], 'Artifact5009.py'),
    ('../Artifact5016.html', ['page.py', 'Artifact5016.py'], 'Artifact5016.py'),
    ('../Artifact5083.html', ['page.py', 'Artifact5083.py'], 'Artifact5083.py'),
    ('../Artifact5580.html', ['page.py', 'Artifact5580.py'], 'Artifact5580.py'),
    ('../Artifact5849.html', ['page.py', 'Artifact5849.py'], 'Artifact5849.py'),
    ('../Artifact5858.html', ['page.py', 'Artifact5858.py'], 'Artifact5858.py'),
    ('../Artifact6392.html', ['page.py', 'Artifact6392.py'], 'Artifact6392.py'),
    ('../Artifact7029.html', ['page.py', 'Artifact7029.py'], 'Artifact7029.py'),
    ('../Artifact7072.html', ['page.py', 'Artifact7072.py'], 'Artifact7072.py'),
    ('../Artifact7075.html', ['page.py', 'Artifact7075.py'], 'Artifact7075.py'),
    ('../Artifact8639.html', ['page.py', 'Artifact8639.py'], 'Artifact8639.py'),
    ('../Artifact8666.html', ['page.py', 'Artifact8666.py'], 'Artifact8666.py'),
    ('../Artifact8695.html', ['page.py', 'Artifact8695.py'], 'Artifact8695.py'),
    ('../Artifact8702.html', ['page.py', 'Artifact8702.py'], 'Artifact8702.py'),
    ('../Artifact_2018-05-24_15.23.57',
     ['page.py', 'Artifact_2018-05-24_15.23.57.py'],
     'Artifact_2018-05-24_15.23.57.py'),
]

for dependency in dependencies:
    requiresUpdate = (os.path.exists(dependency[0]) == False)
    if requiresUpdate == False:
        for dependedUpon in dependency[1]:
            if os.path.getmtime(dependedUpon) > os.path.getmtime(dependency[0]):
                print "'%s' is newer than '%s'" % (dependedUpon, dependency[0])
                requiresUpdate = True
                break
    if requiresUpdate != False:
        execfile(dependency[2])
