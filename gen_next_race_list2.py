# -*- coding: utf-8 -*-

import pprint

from ppropkg.pproxls import POHorseList
from ppropkg.pprows import get_next_race_info_id, get_next_race_info


def main():
    pohorselist = POHorseList()
    poh_list = pohorselist.get()
    poh_horse_name_list = [horse[1] for horse in poh_list]

    next_race_list = []

    info_content = get_next_race_info(get_next_race_info_id())
    paragraphs = info_content.find("h3").find_all_next("p")
    num_of_paragraphs = len(paragraphs)
    gates_paragraphs = info_content.find("h3").find_next("h3").find_all_next("p")
    num_of_gates_paragraphs = len(gates_paragraphs)

    for i in range(num_of_paragraphs - num_of_gates_paragraphs):
        if paragraphs[i].text[0] != "★":
            continue
        race_info, horses = paragraphs[i].text.split("\n")[0], paragraphs[i].text.split("\n")[1].split("、")
        race_date = race_info.split(" ")[0].strip("★")
        race_name = race_info.split(" ")[1]
        race_course = race_info.split(" ")[2]
        for horse in horses:
            horse_name = horse.strip("？").split("(")[0]
            if horse_name not in poh_horse_name_list:
                continue
            horse_index = poh_horse_name_list.index(horse_name)
            is_seal = poh_list[horse_index][3]
            if is_seal:
                continue
            owner = poh_list[horse_index][2]
            is_question = True if horse[-1] == "？" else False
            if "(" in horse:
                jockey = horse.split("(")[1].split(")")[0]
            else:
                jockey = ""

            next_race_list.append([race_date, race_name, race_course, horse_name, owner, jockey, is_question])

    pprint.pprint(next_race_list)


if __name__ == "__main__":
    main()



