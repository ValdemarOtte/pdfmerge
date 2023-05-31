import argparse
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from pypdf import PdfMerger
import sys


def merger_pdfs(pdfs: list[str], output_path: Path) -> None:
    """
    Merge pdfs to one pdf

    Parameters
        pdfs: A list of complet path to the PDFs
        output_path: Path to output directory where the merge PDF will be located
    """
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()


def get_files(path: Path) -> list[str]:
    """
    Get the complet path to PDFs from a directory

    Parameters
        path: Path to directory

    Returns
        pdfs: A list of complet path to the PDFs in directory
    """
    all_files = [file for file in listdir(path) if isfile(join(path, file))]
    incomplete_pdfs = [file for file in all_files if file[-4:] == ".pdf"]
    pdfs = [f"{path}\\" + pdf for pdf in incomplete_pdfs]

    if len(pdfs) == 0:
        sys.exit("Den valgte mappe indenholder ingen PDf'er")

    return pdfs


if __name__ == "__main__":
    # -------------------------
    # Argsparse
    # -------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", help="Path to directory where PDFs are located"
    )
    parser.add_argument(
        "-o", "--output", help="Path where the merge PDF will be located"
    )
    args = parser.parse_args()

    if args.output:
        output_path = args.output + r"\result.pdf"
    else:
        # Default output path
        output_path = os.path.join(sys.path[0], r"result\result.pdf")

    if args.input:
        input_path = args.input
    else:
        # Default output path
        input_path = os.path.join(sys.path[0], r"PDFs")

    # -------------------------
    # Main
    # -------------------------
    pdfs = get_files(input_path)
    merger_pdfs(pdfs, output_path)
