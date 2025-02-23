from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox(options=Options())

def main():
    driver.get('https://www.tibia.com/community/?subtopic=highscores')
    tbody = driver.find_element(By.XPATH, '//*[@id="highscores"]/div[5]/div/div/div/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td/div/table/tbody')

    data = []

    for tr in tbody.find_elements(By.XPATH, '//tr'):
        row = [item.text for item in tr.find_elements(By.XPATH,'.//td')]
        data.append(row)

    i = 8
    dados = ''
    while i <= len(data) - 2:
        dados += ';'.join(data[i]) + '\n'
        i += 1

    f = open("highscores.csv", "w")
    f.write(dados)
    f.close()

if __name__ == '__main__':
    main()