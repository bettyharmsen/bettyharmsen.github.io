import os
import os.path

dependencies = [
    ('../thimblekit.html', ['page.py', 'thimblekit.py'], 'thimblekit.py'),
    ('../twodollarbill.html', ['page.py', 'twodollarbill.py'], 'twodollarbill.py')
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
