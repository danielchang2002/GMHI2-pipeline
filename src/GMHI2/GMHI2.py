import subprocess
import os

# get the directory that contains this script
gmhi2_script_install_folder = os.path.dirname(os.path.abspath(__file__))
# get the default database folder
DEFAULT_DB_FOLDER = os.path.join(gmhi2_script_install_folder, "gmhi2_databases")

def tests():
    # proc = subprocess.Popen(["cat", os.path.join(DEFAULT_DB_FOLDER, "TruSeq3-PE.fa")], 
    #         stdout=subprocess.PIPE)
    # output = proc.stdout.read().decode('ASCII')
    print("Testing GMHI2!!")

    print("-"*5, "Version checks", "-" * 5)

    print("repair.sh version: 38.90")
    print("Actual:")
    proc = subprocess.Popen(["repair.sh"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("fastqc version: 0.11.8")
    print("Actual:")
    proc = subprocess.Popen(["fastqc", "--version"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("bowtie2 version: 2.4.4")
    print("Actual:")
    proc = subprocess.Popen(["bowtie2", "--version"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("samtools version: 1.9")
    print("Actual:")
    proc = subprocess.Popen(["samtools", "--version"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("bedtools version: 2.27.1")
    print("Actual:")
    proc = subprocess.Popen(["bedtools", "--version"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("trimmomatic version: 0.39")
    print("Actual:")
    proc = subprocess.Popen(["trimmomatic", "-version"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("metaphlan version: 3.0.13")
    print("Actual:")
    proc = subprocess.Popen(["metaphlan", "--version"], stdout=subprocess.PIPE)
    output = proc.stdout.read().decode('ASCII')
    print(output)

    print("-" * 5, "Version checks done", "-" * 5)

    print("-" * 5, "Database checks", "-" * 5)



def main():
    tests()

if __name__ == "__main__":
    main()
