# -*- coding: utf-8 -*-

import pprint

from ppropkg.pproxls import POHorseList
from ppropkg.pprows import get_next_race_info_id, get_next_race_info


def main():
    poh_list = POHorseList()

    info_content = get_next_race_info(get_next_race_info_id())
    paragraphs = info_content.find("h3").find_all_next("p")
    num_of_paragraphs = len(paragraphs)
    gates_paragraphs = get_next_race_info(get_next_race_info_id().find("h3").find_next("h3").find_all_next("p"))
    num_of_gates_paragraphs = len(gates_paragraphs)

    for i in range(num_of_paragraphs - num_of_gates_paragraphs):
        if paragraphs[i].text[0] != "★":
            continue
        race_info, horses = paragraphs.split("\n")[0], paragraphs.split("\n")[1].split("、")
        race_date = race_info.split("\s")[0].strip("★")
        race_name = race_info.split("\s")[1]
        race_course = race_info.split("\s")[2]
        for horse in horses:



