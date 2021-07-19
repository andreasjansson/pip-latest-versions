import time
import xmlrpc.client
from typing import List
import fileinput
import pkg_resources
import pypi_xmlrpc

def main():
    # TODO: copy source of pkg_resources.parse_requirements to include comments
    reqs = pkg_resources.parse_requirements(fileinput.input())
    for req in reqs:
        print_package_with_version(req)


def print_package_with_version(req):
    if req.specs:
        print(str(req))
    else:
        version = fetch_latest_version(req.name)
        time.sleep(1)
        print(f"{req.name}=={version}")


def fetch_latest_version(name) -> str:
    while True:
        try:
            releases: List[str] = pypi_xmlrpc.package_releases(name, show_hidden=False)
            return releases[0]
        except xmlrpc.client.Fault as e:
            if e.faultString.startswith("HTTPTooManyRequests"):
                time.sleep(1)
                continue
            raise e


if __name__ == '__main__':
    main()
