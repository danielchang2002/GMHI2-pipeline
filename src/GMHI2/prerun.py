import subprocess
import os
from . import utils


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
        print(bcolors.WARNING + tool, "not found on path or wrong version")
        print(
            'please run: "conda install -c bioconda',
            tool + "=" + gt + '"',
            bcolors.ENDC,
        )
    print()
    return correct


def check_versions():
    print(
        "-" * 5,
        "Version checks",
        "-" * 5,
    )
    any_failed = False
    for tool in version_dict:
        if not check_tool(tool):
            any_failed = True
    if any_failed:
        print(
            bcolors.FAIL,
            "Please (re)install dependencies with above instructions and rerun",
            bcolors.ENDC,
        )
    else:
        print(
            bcolors.GREEN,
            "All dependencies up to date",
            bcolors.ENDC,
        )
    print("-" * 5, "Version checks done", "-" * 5, "\n")
    return not any_failed


def check_and_install_databases():
    print("-" * 5, "Database checks", "-" * 5)
    database = "GRCh38_noalt_as"
    print(database)
    try:
        proc = subprocess.Popen(
            [
                "md5sum",
                "-c",
                os.path.join(utils.DEFAULT_DB_FOLDER, "GRCh38_noalt_as.chk"),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output = proc.stdout.read().decode("ASCII")
        print(output[:-1])
        correct = [line[-2:] == "OK" or line[-2:] == "" for line in output.split("\n")]
        correct = all(correct)
    except:
        correct = False
    print_check_message(correct)
    if not correct:
        print(
            bcolors.WARNING, database, "database not found or corrupted", bcolors.ENDC
        )
    print("-" * 5, "Database checks done", "-" * 5, "\n")
