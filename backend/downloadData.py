import urllib.request
import bs4 as bs

def call_back():
    toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t '))
    # Fetch the html file
    response = urllib.request.urlopen(
        'https://www.studyadda.com/sample-papers/neet-sample-test-paper-83_q1/1296/403162')
    html_doc = response.read()

    # Parse the html file
    soup = bs.BeautifulSoup(html_doc, 'lxml')

    # Get question ans. data
    details_ques_ans = soup.find(class_="details_ques_ans")

    for line in details_ques_ans.find_all("span"):
        #print(line.get_text(), len(line.get_text()))
        if(len(line.get_text()) >= 1):
            print(line.contents, type(line.contents))
    answer = soup.find(class_="ans_panel")
    print(answer.get_text())

if _name_ == "_main_":
    call_back()
