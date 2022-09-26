import pdfplumber
import os


def get_paper_title(file_path):
    if file_path[-3:] != 'pdf':
        return
    with pdfplumber.open(file_path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text().split('\n')
        info = []
        for t in text:
            if 'Abstract' in t:
                break
            info.append(t)
        info = ' '.join(info)
        print(info)


def get_all_papers(root='./'):

    def is_paper(pth):
        return len(pth) > 3 and pth[-3:] == 'pdf'

    all_papers = []
    confs = os.listdir(root)
    for conf in confs:
        conf_dir = os.path.join(root,conf)
        if os.path.isdir(conf_dir):
            papers = os.listdir(conf_dir)
            for p in papers:
                name = os.path.join(conf_dir, p)
                if is_paper(name):
                    all_papers.append(name)

    return all_papers


for p in get_all_papers():
    title = get_paper_title(p)
    print(title)