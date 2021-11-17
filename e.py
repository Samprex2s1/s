import requests

f = open('aboba.txt', 'w')
dict = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for i in range(len(dict)):
    response = requests.get('https://rasp.omgtu.ru/api/search?term='+dict[i]+'&type=person')
    print(response.json)
    #for o in range(len(dict)):
        #f.write('https://rasp.omgtu.ru/api/search?term=%27+dict[i]+dict[o]+%27&type=person/n%27)
        #for p in range(len(dict)):
            #f.write('https://rasp.omgtu.ru/api/search?term=%27+dict[i]+dict[o]+dict[p]+%27&type=person/n%27)
f.close()