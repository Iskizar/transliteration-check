import json


def transliteration_check(eng_name: str, scan_name):
    with open("dict.json", 'r', encoding='utf-8') as f:  # открыли файл
        options = json.load(f)  # загнали все из файла в переменную

    l_result = [{"name": "", "passed": 0}]
    n_result = [{"name": "", "passed": 0}]
    scan_name = scan_name.lower()
    for i in range(len(scan_name)):
        for r in range(len(l_result)):
            for j in range(len(options[scan_name[i]])):
                if i < len(scan_name) - 1:
                    if scan_name[i] + scan_name[i + 1] in options:
                        for k in range(len(options[scan_name[i] + scan_name[i + 1]])):
                            result = l_result[r]["name"]
                            what_find = result + options[scan_name[i] + scan_name[i + 1]][k]
                            where_end = len(what_find)
                            if eng_name.lower().find(what_find, 0, where_end) == 0:
                                result += options[scan_name[i] + scan_name[i + 1]][k]
                                y = 0
                                for t in range(len(n_result)): # проверка на наличие этого результата в списке результатов
                                    if n_result[t] == result:
                                       y+=1
                                for t in range(len(n_result)): # проверка на наличие этого результата в списке результатов
                                    if n_result[t] == result:
                                       y+=1
                                if y == 0:
                                    passed = l_result[r]["passed"]+2
                                    n_result.append({"name": result, "passed": passed})
                result = l_result[r]["name"]
                what_find = result + options[scan_name[i]][j]
                where_end = len(what_find)
                if eng_name.lower().find(what_find, 0, where_end) == 0:
                    result += options[scan_name[i]][j]
                    y=0
                    for t in range(len(n_result)):  # проверка на наличие этого результата в списке результатов
                        if n_result[t] == result:
                            y += 1
                    for t in range(len(n_result)):  # проверка на наличие этого результата в списке результатов
                        if n_result[t] == result:
                            y += 1
                    if y == 0:
                        passed = l_result[r]["passed"] + 1
                        n_result.append({"name": result, "passed": passed})
        if len(n_result) > 0:
            l_result += n_result
            n_result = [{"name": "", "passed": 0}]
        #тут должна быть проверка l_result на мелкие passed
        t_res = []
        for t in range(len(l_result)):
            if l_result[t]["passed"] == i+1 or l_result[t]["passed"] == i+2:
                t_res.append(l_result[t])
        l_result = t_res
        if i == len(scan_name) - 1: # сравнение перевода и eng_name
            for t in range(len(l_result)):
                if len(scan_name) == l_result[t]["passed"]:
                    if eng_name.lower() == l_result[t]["name"]:
                        return True
            return False

# Пример запроса
# print(transliteration_check("SOLOVYOV", "СОЛОВЬЁВ"))
