import argparse
from requests import get

def download(args):
    url = args.download[0]
    file_name = args.download[1]
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

def main():
    parser = argparse.ArgumentParser(description="Download a file which python, wow")

    parser.add_argument("-d", "--download", type = str, nargs=2,
    metavar = ("url", "file_name"), default= None,
    help = "Download a file.")

    args = parser.parse_args()

    if args.download != None:
        download(args)


if __name__ == "__main__":
    main()
