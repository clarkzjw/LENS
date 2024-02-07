import os
import sys
import csv
import time
from pathlib import Path
from multiprocessing import Pool
from util import load_irtt, load_ping


csv_dir = ""
raw_dir = ""


def convert_irtt_csv(file_path: str) -> None:
    print(file_path)
    outfile_path = Path(str(file_path).replace(raw_dir, csv_dir))
    if os.path.isfile(outfile_path.with_suffix(".csv")):
        return
    v_irtt = load_irtt(file_path)
    if v_irtt == None:
        print("error: ", file_path)
        sys.exit(1)
    with open(outfile_path.with_suffix(".csv"), 'w', newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames = ["timestamp", "rtt", "uplink", "downlink"])
        writer.writeheader()

        writer.writerows({"timestamp": v_irtt.ts[i], "rtt": v_irtt.rtt[i], "uplink": v_irtt.upstream[i], "downlink": v_irtt.downstream[i]} for i in range(len(v_irtt.ts)))


def convert_ping_csv(file_path: str) -> None:
    print(file_path)
    outfile_path = Path(str(file_path).replace(raw_dir, csv_dir))
    if os.path.isfile(outfile_path.with_suffix(".csv")):
        return
    v_ping = load_ping(file_path)
    if v_ping == None:
        print("error: ", file_path)
        sys.exit(1)
    with open(outfile_path.with_suffix(".csv"), 'w', newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames = ["timestamp", "rtt"])
        writer.writeheader()

        writer.writerows({"timestamp": v_ping.ts[i], "rtt": v_ping.rtt[i]} for i in range(len(v_ping.ts)))


def copy_folder_tree(raw_dir: str, csv_dir: str) -> None:
    for dirpath, dirnames, files in os.walk(raw_dir):
        structure = os.path.join(csv_dir, os.path.relpath(dirpath, raw_dir))
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            print("{} already exists".format(structure))
    

if __name__ == "__main__":
    p = Pool(24)
    irtt_job = []
    ping_job = []
    copy_folder_tree(raw_dir, csv_dir)

    path = Path(raw_dir)
    for dirpath, dirnames, files in os.walk(path):
        if len(files) != 0:
            for f in files:
                if f.endswith(".txt") and f.startswith("ping"):
                    ping_job.append(str(Path(dirpath).joinpath(f)))
                if f.endswith(".json") and f.startswith("irtt"):
                    irtt_job.append(str(Path(dirpath).joinpath(f)))

    irtt_job.sort(key=str.lower)
    ping_job.sort(key=str.lower)
    start = time.time()
    p.map(convert_ping_csv, ping_job)
    p.map(convert_irtt_csv, irtt_job)
    print("{} seconds elapsed".format(time.time() - start))
