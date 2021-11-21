import subprocess
import os


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_check_message(boolean):
    print(
        bcolors.OKGREEN + "passed" + bcolors.ENDC
        if boolean
        else bcolors.FAIL + "failed" + bcolors.ENDC
    )


version_dict = {
    "repair.sh": "38.90",
    "fastqc": "0.11.8",
    "bowtie2": "2.4.4",
    "samtools": "1.9",
    "bedtools": "2.27.1",
    "trimmomatic": "0.39",
    "metaphlan": "3.0.13",
}


def check_tool(tool):
    gt = version_dict[tool]
    print(tool, "version:", gt)
    flag = "--version" if not tool == "trimmomatic" else "-version"

    try:
        if not tool == "repair.sh":
            proc = subprocess.Popen([tool, flag], stdout=subprocess.PIPE)
            output = proc.stdout.read().decode("ASCII")
        else:
            proc = subprocess.Popen(["repair.sh", "--version"], stderr=subprocess.PIPE)
            output = proc.stderr.read().decode("ASCII")
        correct = gt in output
    except:
        correct = False
    print_check_message(correct)
    if not correct:
        print(
            bcolors.WARNING + tool,
            'not found on path or wrong version, please run: "conda install -c bioconda',
            tool + "=" + gt + '"',
            bcolors.ENDC,
        )


def check_versions():
    for tool in version_dict:
        check_tool(tool)


def check_databases():

    print("Checking GRCh38_noalt_as")
    try:
        proc = subprocess.Popen(
            ["md5sum", "-c", "gmhi2_databases/GRCh38_noalt_as.chk"],
            stdout=subprocess.PIPE,
        )
        output = proc.stdout.read().decode("ASCII")
        print(output)
        correct = [line[-2:] == "OK" or line[-2:] == "" for line in output.split("\n")]
        correct = all(correct)
    except:
        print("Error with gRCh38_noalt_as database")
    print_check_message(correct)


def checks():
    print("Testing Dependencies", "\n")

    print("-" * 5, "Version checks", "-" * 5)
    check_versions()
    print("-" * 5, "Version checks done", "-" * 5, "\n")
    return

    print("-" * 5, "Database checks", "-" * 5)
    check_databases()
    print("-" * 5, "Database checks done", "-" * 5, "\n")
