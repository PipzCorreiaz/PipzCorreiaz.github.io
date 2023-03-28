
import sys
from urllib.request import urlopen
import html_to_json


def main(args):

      
      year = "2019"
      url = "https://dblp.org/db/conf/hri/hri" + year + ".html"
        
      response = urlopen(url)
      output_html = response.read()
      output_json = html_to_json.convert(output_html)

      paper_list = []
      file = open("hri" + year + ".txt", "w")
      file.write("{title}\n")
      file.write("====\n")

      
      i = 0
      for h in output_json['html'][0]['body'][0]['div'][1]['header']:
            if 'h2' in h and (not 'PlenaryTalk' in h['h2'][0]['_attributes']['id']) and (not 'VideoSession' in h['h2'][0]['_attributes']['id']) and (not 'altHRIPresentations' in h['h2'][0]['_attributes']['id']) and (not 'LateBreakingTalks' in h['h2'][0]['_attributes']['id']) and (not 'Demonstrations' in h['h2'][0]['_attributes']['id']) and (not 'WorkshopPresentations' in h['h2'][0]['_attributes']['id']) and (not 'PioneerTalks' in h['h2'][0]['_attributes']['id']) and (not 'StudentDesignPresentations' in h['h2'][0]['_attributes']['id']):
                  ul = output_json['html'][0]['body'][0]['div'][1]['ul'][i]
                  for li in ul['li']:
                        if 'inproceedings' in li['_attributes']['class']:
                              paper_attr = li['cite'][0]['span']
                              for data in paper_attr:
                                    if 'class' in data['_attributes']:
                                          title = data['_value']
                                          paper_list.append(title)
                                          file.write(title + '\n')
            i += 1


      file.close()
      print("Number of papers: " + str(len(paper_list)))

if __name__ == "__main__":
   main(sys.argv[1:])