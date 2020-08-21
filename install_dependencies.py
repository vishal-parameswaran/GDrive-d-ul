import subprocess
import sys
def install_pydrive():
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if 'PyDrive' not in installed_packages:
        reqs = subprocess.check_output("pip install httplib2==0.15.0",stderr=subprocess.STDOUT,shell=True).decode('UTF-8')
        if 'Successfully installed httplib2' in reqs:
            reqs = subprocess.check_output("pip install pydrive",stderr=subprocess.STDOUT,shell=True).decode('UTF-8')
            if 'Successfully installed pydrive' in reqs:
                return(True)
            else:
                return(False)  
        else:
            return(False)    
    else:
        return(True)