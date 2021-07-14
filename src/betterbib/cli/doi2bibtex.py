import argparse
import sys

from unidecode import unidecode

from .. import crossref, tools
from .default_parser import get_version_parser_arguments


def _create_citekey_for_entry(entry):
    """
    Create a citekey for entry using the [author:lower][year] JabRef pattern.

    See https://retorque.re/zotero-better-bibtex/citing/

    """
    bibtex_key = ""
    if (
        entry.persons
        and "author" in entry.persons
        and entry.persons["author"]
        and entry.persons["author"][0].last()
    ):
        bibtex_key += unidecode(entry.persons["author"][0].last()[0].lower())
    if "year" in entry.fields and entry.fields["year"]:
        bibtex_key += str(entry.fields["year"])
    if not bibtex_key:
        bibtex_key = "key"
    return bibtex_key


def main(argv=None):
    parser = _get_parser()
    args = parser.parse_args(argv)
    source = crossref.Crossref()
    entry = source.get_by_doi(args.doi)
    bibtex_citekey = _create_citekey_for_entry(entry)
    string = tools.pybtex_to_bibtex_string(entry, bibtex_citekey)
    args.outfile.write(string)
    return


def _get_parser():
    parser = argparse.ArgumentParser(description="Turn a DOI into a BibTeX entry.")

    parser = get_version_parser_arguments(parser)

    parser.add_argument("doi", type=str, help="input DOI")
    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="output file (default: stdout)",
    )
    return parser
