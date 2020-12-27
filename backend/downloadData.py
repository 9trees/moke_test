import urllib.request
import bs4 as bs
import json, time, random


j_data = {"NEET_Sample_Test_Paper_83": []}

def update_json(data):
    global j_data
    j_data['NEET_Sample_Test_Paper_83'].append(data)

def call_back(myurl, num):
    toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t'))
    # Fetch the html file
    response = urllib.request.urlopen(myurl)
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
        print(i)

        myurl = 'https://www.studyadda.com/sample-papers/neet-sample-test-paper-83_q1/1296/' + str(403162 + i)
        call_back(myurl, i+1)
        time.sleep(random.randint(1, 9))
    #print(jdata)
    with open("NEET_Sample_Test_Paper_83.json", "w") as outfile:
        json.dump(j_data, outfile, indent=4, sort_keys=True)
