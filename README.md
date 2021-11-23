# GMHI2: Gut Microbiome Health Index 2

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



### Description
Gut Microbiome Health Index 2 (GMHI2) is a robust index for evaluating 
health status based on the species-level taxonomic profile of a stool 
shotgun metagenome (gut microbiome) sample.


### Installation
To avoid dependency conflicts, create an isolated conda environment and
install gmhi2

1. Install via conda
```sh
$ conda create --name gmhi2_env -c danielchang2002 python=3.7 gmhi2
```

2. Activate environment
```sh
$ conda activate gmhi2_env
```

### Usage
```sh
usage: gmhi2 [-h] [-o OUTPUT] --fastq1 FASTQ1 --fastq2 FASTQ2

DESCRIPTION:
GMHI2 version 1.0
Gut Microbiome Health Index 2 (GMHI2) is a robust index for evaluating 
health status based on the species-level taxonomic profile of a stool 
shotgun metagenome (gut microbiome) sample.

AUTHORS:
Daniel Chang, Vinod Gupta, Jaeyun Sung

USAGE:
GMHI2 is a pipeline that takes as input two raw fastq files generated 
from a paired end sequence, performs quality control, estimates microbial 
abundances, and returns as output a health index score.

* Profiling a metagenome from raw reads:
$ gmhi2 --fastq1 metagenome1.fastq --fastq2 metagenome2.fastq

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name

required named arguments:
  --fastq1 FASTQ1       first input fastq file
  --fastq2 FASTQ2       second input fastq file
```

### Example
Directory structure:
```sh
.
├── metagenome1.fastq
└── metagenome2.fastq
```

Command:
```sh
$ gmhi2 --fastq1 metagenome1.fastq --fastq2 metagenome2.fastq -o GMHI2.txt
```

Result:
```sh
.
├── GMHI2.txt
├── abundance.txt
├── metagenome1.fastq
└── metagenome2.fastq
```
where GMHI2.txt is a text file with a single line containing the health index
score of the metagenome, and abundance.txt is a tsv containing the estimated
microbial abundances.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/danielchang2002/GMHI2/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/danielchang2002/GMHI2/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/danielchang2002/GMHI2/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/danielchang2002/GMHI2/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/daniel-chang-b93473204/
[product-screenshot]: images/screenshot.png
