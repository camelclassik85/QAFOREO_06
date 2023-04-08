'''7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples'''
#div:nth-child(2) > button:nth-child(3)
#//div[2]/button[3]
#(//button)[7]
#(//button)[last()-1]
#//*[text()='Gold']
#//*[contains(text(), 'Gold')]


'''7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html'''
#(//p)[last()-1]
#(//p)[5]
#(//p[@class])[5]
#(//p[@class])[last() -1]
#(//p[@class= 'card-text'])[last() -1]
#//*[text()='Fully charged cat']
#//*[contains(text(), 'Fully charged cat')]
#//*[.='Fully charged cat']

