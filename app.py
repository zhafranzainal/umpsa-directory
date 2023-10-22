import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request

app = Flask('')


@app.route('/', methods=['GET', 'POST'])
def display_student_info():
    if request.method == 'POST':
        student_id = request.form.get('studentId').upper()
        student_name = scrape_student_info(student_id)
        return render_template('umpsa-directory.html', studentName=student_name, studentId=student_id)

    return render_template('umpsa-directory.html', studentName='student name')


def scrape_student_info(student_id):
    url = f'https://apps02.ump.edu.my/semakan/Matric_Card.jsp?std_id={student_id}'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        rows = soup.find_all('tr', bgcolor='#CCCCCC')

        for row in rows:
            if 'NAMA' in row.get_text():
                name = row.find_all('td')[1].get_text(strip=True).split(": ")[1]
                return name

        return "Student Name Not Found"

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)


if __name__ == '__main__':
    app.run(debug=True)
