
import sys
from urllib.request import urlopen
import html_to_json


def main(args):

      years = ["2018","2019","2020"]

      for year in years:
            paper_list = []
            file = open("acm-hri" + year + ".txt", "w")
            file.write("{title}\n")
            file.write("====\n")

            with open("bibitems-hri" + year + ".bib") as bibitems:
                  for line in bibitems:
                        if line.startswith("title"):
                              i = line.index('{')
                              title = line[i+1:-3]
                              paper_list.append(title)
                              file.write(title + '.\n')


            file.close()
            print("Number of papers in HRI " + year + ": " + str(len(paper_list)))

if __name__ == "__main__":
   main(sys.argv[1:])