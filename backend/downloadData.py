import urllib.request
from urllib.error import HTTPError, URLError
import bs4 as bs
import json, time, random, os
from socket import timeout


j_data = {"NEET_Sample_Test_Paper_84": []}

def update_json(data):
    global j_data
    j_data['NEET_Sample_Test_Paper_84'].append(data)

def call_back(myurl, num):
    toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t'))
    # Fetch the html file
    #response = urllib.request.urlopen(myurl)
    try:
        req = urllib.request.Request(myurl)
        response = urllib.request.urlopen(req, timeout=1000)
        print("I tried.")
    except:
        print("I failed.")
    # try:
    #     response = urllib.request.urlopen(myurl, timeout=100)#.read().decode('utf-8')
    # except (HTTPError, URLError) as error:
    #     print('Data not retrieved because %s\nURL: %s', error, myurl)
    # except timeout:
    #     print('socket timed out - URL %s', myurl)
    # else:
    #     print('Access successful.')
    html_doc = response.read()

    # Parse the html file
    soup = bs.BeautifulSoup(html_doc, 'lxml')

    # Get question ans. data
    details_ques_ans = soup.find(class_="details_ques_ans")
    i = 1

    for line in details_ques_ans.find_all("span"):
        #print(line.get_text(), len(line.get_text()))
        data = ""
        if(len(line.get_text()) >= 1):
            for text in line.contents:
                try:
                    text = text.translate(toremove)
                    if len(text):
                        data += text
                        # print(i, data)
                except:
                    data += str(text)
                    # print(i, data)
        #print(i, data)
        if i == 2:
            question = data
        if i == 4:
            option_A = data
        if i == 6:
            option_B = data
        if i == 8:
            option_C = data
        if i == 10:
            option_D = data
        if i == 11:
            solution = data
        i += 1
    answer = soup.find(class_="ans_panel")
    #print(i, answer.get_text().split()[-1])
    answer = answer.get_text().split()[-1]
    one = {
        "No": num,
        "Que": question,
        "O_A": option_A,
        "O_B": option_B,
        "O_C": option_C,
        "O_D": option_D,
        "Exp": solution,
        "Ans": answer,
        "Ref": myurl
    }
    update_json(one)

if __name__ == "__main__":
    for i in range(180):
        myurl = 'https://www.studyadda.com/sample-papers/neet-sample-test-paper-84_q1/1382/' + str(416717 + i)
        call_back(myurl, i+1)
        x = random.randint(1, 9)
        print(i, x)
        time.sleep(x)
    #print(j_data)
    with open("NEET_Sample_Test_Paper_84.json", "w") as outfile:
        json.dump(j_data, outfile, indent=4, sort_keys=True)
