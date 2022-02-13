# Importing stuff
import requests
import bs4
import sys
import argparse

# Setting up arguments with argparser
parser=argparse.ArgumentParser()
parser.add_argument("url",help="Enter main website URL")
parser.add_argument("-o","--output",help="To save results in output file. Specify Filename.",type=str)
parser.add_argument("-s","--status",help="To check the status of js urls",action="store_true")

args=parser.parse_args()

# Visiting main urls and storing HTML in var.
mainURL = sys.argv[1]
r = requests.get(mainURL)
data = r.text

full_js_Urls = []


def fullURLMaker():
    # Extract absolute js urls from html data.
    soup = bs4.BeautifulSoup(data, "lxml")
    script_Tag = soup.find_all("script")

    # Extracting relative urls in 'src' attr and saving it in lists.
    rel_paths = []
    for x in script_Tag:
        y = str(x.get("src"))
        rel_paths.append(y)

    def joinURLs():
        for item in rel_paths:
            if "None" in item:
                pass
            elif "http" in item:
                full_js_Urls.append(item)
            else:
                abs_url = mainURL + item
                full_js_Urls.append(abs_url)

    joinURLs()

# Return the list of js urls

def list_of_jsURLs():
    fullURLMaker()
    print("JS URLs Extracted:\n--------------------------")
    for jslink in full_js_Urls:
        print(jslink)

def output_save():
    fullURLMaker()
    fz = open(args.output, "w")
    print("JS URLs Extracted:\n--------------------------")
    for jslink in full_js_Urls:
        print(jslink)
        fz.write(f"{jslink}\n")
    fz.close()
    print(f"\nSaved has been Results to  {args.output}")

def check_status():
    fullURLMaker()
    print("JS URLs Extracted")
    for jsLink in full_js_Urls:
        r=requests.get(jsLink)
        print(f"{jsLink} >>> {r.status_code}")

#Executing functions based on arguments provided:

if args.url and not args.output and not args.status:
    list_of_jsURLs()
elif args.output:
    output_save()
elif args.status:
    check_status()
