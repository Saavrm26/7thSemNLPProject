import asyncio
import argparse
import commands

def fetch_cve():
    asyncio.run(commands.fetch_cve())


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.add_parser(
        "fetch_cve", help="Fetch NSIT CVE database and save to artifacts"
    ).set_defaults(func=fetch_cve)

    args = parser.parse_args()
    args.func()



if __name__ == "__main__":
    main()
