
animals_name = ["krokodyl", "slon", "orzel", "bizon", "panda", "hipopotam", "lew", "tygrys", "zebra", "zaba"]
krokodyl_dict = {"ACE": ["1","2"], "RISE": ["5","6"], "Protopnet": ["3","4"]}
slon_dict = {"ACE": ["4","5"], "RISE": ["3","6"], "Protopnet": ["1","2"]}
orzel_dict = {"ACE": ["1","2"], "RISE": ["5","6"], "Protopnet": ["3","4"]}
bizon_dict = {"ACE": ["1","2"], "RISE": ["6","7"], "Protopnet": ["3", "4", "5"]}
panda_dict = {"ACE": ["1","2"], "RISE": ["5","6"], "Protopnet": ["3","4"]}
hipopotam_dict = {"ACE": ["5","6"], "RISE": ["1","2"], "Protopnet": ["3","4"]}
lew_dict = {"ACE": ["1","2"], "RISE": ["5","6"], "Protopnet": ["3","4"]}
tygrys_dict = {"ACE": ["6","5"], "RISE": ["1","2"], "Protopnet": ["3","4"]}
zebra_dict = {"ACE": ["5","6"], "RISE": ["3","4"], "Protopnet": ["1","2"]}
zaba_dict = {"ACE": ["1","2"], "RISE": ["5","6"], "Protopnet": ["3","4", "7"]}

std_cechy = ["wiek","plec","sztuczna_inteligencja","wyjasnianie","zdjecia","edukacja"]
std_warunki = {"wiek":["<19", "19 - 26", "27 - 45", "45 -65",">65"],
           "plec":["Kobieta", "Mężczyzna"],
           "sztuczna_inteligencja":["Tak", "Nie"],
           "wyjasnianie":["Tak", "Nie"],
           "zdjecia":["Tak", "Nie"],
           "edukacja":["Tak", "Nie"]}

dict_response = {"krokodyl":[8,7], "slon":[10,7], "orzel":[8,7], "bizon":[8,8], "panda":[8,7], "hipopotam":[9,7], "lew":[9,7], "tygrys":[8,7], "zebra":[8,7], "zaba":[8,8]}

def return_animals_dict():
    animals = [krokodyl_dict, slon_dict, orzel_dict, bizon_dict, panda_dict, hipopotam_dict, lew_dict, tygrys_dict, zebra_dict, zaba_dict]
    animals_dict = dict(zip(animals_name, animals))
    return animals_dict



def ranking_ut(data, animals_dict):
    metric_dict = {name : [] for name in animals_name}
    data_metrics = data[[name + "_2" for name in animals_name]]
    data_dict = data_metrics.to_dict('list')
    keys = list(data_dict.keys())

    #iterate data by rows
    for index, row in data.iterrows():
        #iterate data by columns
        for i,(key, name) in enumerate(zip(keys, animals_name)):
            for option in animals_dict[name]["ACE"]:
                if option in str(row[key]):
                    metric_dict[name].append("ACE")
            for option in animals_dict[name]["RISE"]:
                if option in str(row[key]):
                    metric_dict[name].append("RISE")
            for option in animals_dict[name]["Protopnet"]:
                if option in str(row[key]):
                    metric_dict[name].append("Protopnet")

    metric_ranking = {name : [] for name in animals_name}
    for key, l in metric_dict.items():
        temp_dict = {"ACE": 0, "RISE": 0, "Protopnet": 0}
        for ex in l:
            if ex == "ACE":
                temp_dict["ACE"] += 1
            elif ex == "RISE":
                temp_dict["RISE"] += 1
            elif ex == "Protopnet":
                temp_dict["Protopnet"] += 1

        metric_ranking[key] = temp_dict

    return metric_ranking

def return_methods_ranking(metric_ranking):
    methods_ranking = {"ACE": 0, "RISE": 0, "Protopnet": 0}
    for key, value in metric_ranking.items():
        for method, count in value.items():
            methods_ranking[method] += count

    return methods_ranking, list(methods_ranking.values()), [ rv / sum(list(methods_ranking.values()))*100 for rv in list(methods_ranking.values())]


def ref_metric_ranking(data, animals_dict):
    metric_dict = {name : [] for name in animals_name}
    data_metrics = data[[name + "_2" for name in animals_name]]
    data_dict = data_metrics.to_dict('list')
    keys = list(data_dict.keys())

    #iterate data by rows
    for index, row in data.iterrows():
        #iterate data by columns
        for i,(key, name) in enumerate(zip(keys, animals_name)):
            for option in animals_dict[name]["ACE"]:
                if option in str(row[key]):
                    metric_dict[name].append("ACE")
            for option in animals_dict[name]["RISE"]:
                if option in str(row[key]):
                    metric_dict[name].append("RISE")
            for option in animals_dict[name]["Protopnet"]:
                if option in str(row[key]):
                    metric_dict[name].append("Protopnet")

    metric_ranking = {name : [] for name in animals_name}
    for key, l in metric_dict.items():
        temp_dict = {"ACE": 0, "RISE": 0, "Protopnet": 0}
        for ex in l:
            if ex == "ACE":
                temp_dict["ACE"] += 1
            elif ex == "RISE":
                temp_dict["RISE"] += 1
            elif ex == "Protopnet":
                temp_dict["Protopnet"] += 1
        metric_ranking[key] = temp_dict

    return metric_ranking

def count_metric_ranking(data, animals_dict, cecha, warunek):
    metric_dict = {name : [] for name in animals_name}

    #drop column without _2
    columns = [name + "_2" for name in animals_name]
    columns.append(cecha)
    data_metrics = data[columns]
    data_dict = data_metrics.to_dict('list')
    keys = list(data_dict.keys())

    #iterate data by rows
    for index, row in data.iterrows():
        #iterate data by columns
        for i,(key, name) in enumerate(zip(keys[:-1], animals_name)):
            if row[cecha] == warunek:
                for option in animals_dict[name]["ACE"]:
                    if option in str(row[key]):
                        metric_dict[name].append("ACE")
                for option in animals_dict[name]["RISE"]:
                    if option in str(row[key]):
                        metric_dict[name].append("RISE")
                for option in animals_dict[name]["Protopnet"]:
                    if option in str(row[key]):
                        metric_dict[name].append("Protopnet")

    metric_ranking = {name : [] for name in animals_name}
    for key, l in metric_dict.items():
        temp_dict = {"ACE": 0, "RISE": 0, "Protopnet": 0}
        for ex in l:
            if ex == "ACE":
                temp_dict["ACE"] += 1
            elif ex == "RISE":
                temp_dict["RISE"] += 1
            elif ex == "Protopnet":
                temp_dict["Protopnet"] += 1

        metric_ranking[key] = temp_dict

    return metric_ranking

def count_metric_ranking_two(data, animals_dict, cecha, warunek, cecha2, warunek2):
    metric_dict = {name : [] for name in animals_name}

    #drop column without _2
    columns = [name + "_2" for name in animals_name]
    columns.append(cecha)
    data_metrics = data[columns]
    data_dict = data_metrics.to_dict('list')
    keys = list(data_dict.keys())

    #iterate data by rows
    for index, row in data.iterrows():
        #iterate data by columns
        for i,(key, name) in enumerate(zip(keys[:-1], animals_name)):
            if row[cecha] == warunek and row[cecha2] == warunek2:
                for option in animals_dict[name]["ACE"]:
                    if option in str(row[key]):
                        metric_dict[name].append("ACE")
                for option in animals_dict[name]["RISE"]:
                    if option in str(row[key]):
                        metric_dict[name].append("RISE")
                for option in animals_dict[name]["Protopnet"]:
                    if option in str(row[key]):
                        metric_dict[name].append("Protopnet")

    metric_ranking = {name : [] for name in animals_name}
    for key, l in metric_dict.items():
        temp_dict = {"ACE": 0, "RISE": 0, "Protopnet": 0}
        for ex in l:
            if ex == "ACE":
                temp_dict["ACE"] += 1
            elif ex == "RISE":
                temp_dict["RISE"] += 1
            elif ex == "Protopnet":
                temp_dict["Protopnet"] += 1

        metric_ranking[key] = temp_dict
    return metric_ranking