import asyncio
import argparse
import commands

import config

def fetch_cve():
    asyncio.run(commands.fetch_cve())

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.add_parser(
        "fetch_cve", help="Fetch NSIT CVE database and save to artifacts"
    ).set_defaults(func=fetch_cve)

    subparsers.add_parser(
        "ingest_data", help="Ingest data from artifacts"
    ).set_defaults(func=lambda : commands.bulk_ingest_from_directory())

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    main()
