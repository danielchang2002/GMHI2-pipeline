import subprocess
import os

# get the directory that contains this script
gmhi2_script_install_folder = os.path.dirname(os.path.abspath(__file__))
# get the default database folder
DEFAULT_DB_FOLDER = os.path.join(gmhi2_script_install_folder, "gmhi2_databases")

def run_GMHI2():
    proc = subprocess.Popen(["cat", os.path.join(DEFAULT_DB_FOLDER, "TruSeq3-PE.fa")], 
            stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print("Running GMHI2!!")
    print("Cat result:")
    print(output)

if __name__ == "__main__":
    run_GMHI2()
