import subprocess
import os


def repair():
    # takes about 18s
    print("repairing sequences")
    subprocess.call(
        [
            "repair.sh",
            "in1=in1.fastq",
            "in2=in2.fastq",
            "out1=repaired1.fastq",
            "out2=repaired2.fastq",
            "outs=garbage",
        ]
    )
    # subprocess.call(["rm", "garbage"])


def quality_control():

    # takes about 2 mins
    subprocess.call(["fastqc", "repaired1.fastq"])
    subprocess.call(["fastqc", "repaired2.fastq"])

    subprocess.call(["unzip", "repaired1_fastqc.zip"])
    subprocess.call(["unzip", "repaired2_fastqc.zip"])


def extract_adapters():
    pass


def run(args):

    # read inputs
    in1, in2 = args.fastq1, args.fastq2
    print("Inputs:", in1, in2)
    if in1.split(".")[-1] != "fastq" or in2.split(".")[-1] != "fastq":
        print("invalid file extensions")
        return

    # make a copy of input files with simpler name
    # subprocess.call(["cp", in1, "in1.fastq"])
    # subprocess.call(["cp", in2, "in2.fastq"])

    # repair()
    # quality_control()
    extract_adapters()

    return

    # check qualities of sequences
    print("quality control of sequences")

    # subprocess.call(["fastqc", out1])
    # subprocess.call(["fastqc", out2])

    zipout1 = "_".join(out1.rsplit(".", 1)) + "c"
    zipout2 = "_".join(out2.rsplit(".", 1)) + "c"

    # subprocess.call(["unzip", zipout1])
    # subprocess.call(["unzip", zipout2])
