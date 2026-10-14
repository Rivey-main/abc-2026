algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]

# Открываем файл на запись
with open('algoritm.csv', 'w', encoding='utf-8') as f:
    for i, name in enumerate(algoritm, 1):
        
        f.write(f'{i}) "{name}"\n')
