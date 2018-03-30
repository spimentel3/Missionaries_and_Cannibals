import pdb
import sys

adj_list = {'MMMCCCB|': ["MMCC|BMC", "MMMCC|BC", "MMMC|BCC"],
            'MMCC|BMC': ["MMMCCCB|", "MMMCCB|C"],
            'MMMCC|BC': ["MMMCCCB|"],
            'MMMC|BCC': ["MMMCCCB|", "MMMCCB|C"],
            'MMMCCB|C': ["MMM|BCCC"],
            'MMM|BCCC': ["MMMCCB|C", "MMMCB|CC"],
            'MMMCB|CC': ["MMM|BCCC", "MC|BMMCC"],
            'MC|BMMCC': ["MMMCB|CC", "MMCCB|MC"],
            'MMCCB|MC': ["MC|BMMCC", "CC|BMMMC"],
            'CC|BMMMC': ["MMCCB|MC", "CCCB|MMM"],
            'CCCB|MMM': ["CC|BMMMC", "C|BMMMCC"],
            'C|BMMMCC': ["CCCB|MMM", "MCB|MMCC", "CCB|MMMC"],
            'MCB|MMCC': ["C|BMMMCC", "|BMMMCCC"],
            'CCB|MMMC': ["C|BMMMCC", "|BMMMCCC"],
            '|BMMMCCC': ["MCB|MMCC", "CCB|MMMC"]}

def search(path):
    for possible_path in adj_list[path[-1]]:
        if possible_path == "|BMMMCCC":
            path.append(possible_path)
            done_searching = True
            print path
            sys.exit()
        if possible_path not in path:
            path.append(possible_path)
            search(path)

done_searching = False
path = [];
path.append("MMMCCCB|") # starting state
search(path)
