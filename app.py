import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask('')


@app.route('/')
def display_student_info():
    studentName = scrape_student_info()
    return render_template('umpsa-directory.html', studentName=studentName)


def scrape_student_info():
    url = 'https://apps02.ump.edu.my/semakan/Matric_Card.jsp?std_id=CB20100'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        rows = soup.find_all('tr', bgcolor='#CCCCCC')
        img_tag = soup.find('img', id='cropbox')

        for row in rows:
            if 'NAMA' in row.get_text():
                name = row.find_all('td')[1].get_text(strip=True).split(": ")[1]
                return name

        return "Student Name Not Found"

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)


if __name__ == '__main__':
    app.run(debug=True)
