
from urllib.request import urlopen
import html_to_json

url = "https://dblp.org/db/conf/hri/hri2020.html"
  
response = urlopen(url)
output_html = response.read()
output_json = html_to_json.convert(output_html)

paper_list = []
file = open("hri2020.txt", "w")
file.write("{title}\n")
file.write("====\n")

for ul in output_json['html'][0]['body'][0]['div'][1]['ul']:
      for li in ul['li']:
            if 'inproceedings' in li['_attributes']['class']:
                  paper_attr = li['cite'][0]['span']
                  for data in paper_attr:
                        if 'class' in data['_attributes']:
                              title = data['_value']
                              paper_list.append(title)
                              file.write(title + '\n')


file.close()
print("Number of papers: " + str(len(paper_list)))
