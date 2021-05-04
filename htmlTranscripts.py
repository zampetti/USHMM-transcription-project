import os
import csv
from bs4 import BeautifulSoup

cwd = os.getcwd()
path = cwd  + r"\USHMM_GaborToth\USHMM"
files = os.listdir(path)

problem_docs = []

for file in files:
    try:
        file_root = file.split('.html')[0]
        txt_file = os.path.join(path, file_root + '.txt')

        with open(txt_file, 'w') as txtFile:

            html_file = os.path.join(path, file)

            with open(html_file, "r", encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                for data in soup.find_all('p'):
                    print(data.get_text())
                    txtFile.write(data.get_text()+'\n')

    except Exception as e:
            print(e)
            problem_docs.append(file)

for prob_doc in problem_docs:
    with open('entry_problem_log.csv', mode='w', newline='') as prob_csv_file:
        try:
            prob_fieldnames = ['Problematic Doc']
            prob_writer = csv.DictWriter(prob_csv_file, fieldnames=prob_fieldnames)
            prob_writer.writeheader()
            prob_writer.writerow({'Problematic Doc': prob_doc})
        except Exception as e:
            print(e)
            continue
