import re
import json
import json
from dataclasses import dataclass


@dataclass
class IRTT:
    ts: list[int]
    rtt: list[float]
    upstream: list[float]
    downstream: list[float]
    packet_loss: float
    upstream_loss: float
    downstream_loss: float


@dataclass
class Ping:
    ts: list[float]
    rtt: list[float]


def load_irtt(filename: str) -> IRTT:
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
            stats = data["stats"]
            
            v_IRTT = IRTT(
                ts=[],
                rtt=[],
                upstream=[],
                downstream=[],
                packet_loss=stats["packet_loss_percent"],
                upstream_loss=stats["upstream_loss_percent"],
                downstream_loss=stats["downstream_loss_percent"],
            )
            for round in data["round_trips"]:
                v_IRTT.ts.append(round["timestamps"]["client"]["send"]["wall"])
                if round["lost"] == "true":
                    v_IRTT.rtt.append(-1)
                    v_IRTT.upstream.append(0)
                    v_IRTT.downstream.append(0)
                elif round["lost"] == "true_up":
                    v_IRTT.rtt.append(0)
                    v_IRTT.upstream.append(-1)
                    v_IRTT.downstream.append(0)
                elif round["lost"] == "true_down":
                    v_IRTT.rtt.append(0)
                    v_IRTT.upstream.append(0)
                    v_IRTT.downstream.append(-1)
                else:
                    v_IRTT.rtt.append(float(round["delay"]["rtt"])/1000000)
                    v_IRTT.downstream.append(float(round["delay"]["receive"])/1000000)
                    v_IRTT.upstream.append(float(round["delay"]["send"])/1000000)
        return v_IRTT

    except Exception as e:
        print(str(e))
        

def load_ping(filename: str) -> Ping:
    with open(filename, "r") as f:
        count = 0
        v_Ping = Ping(ts=[], rtt=[])
        for line in f.readlines():
            match = re.search(r"\[(\d+\.\d+)\].*icmp_seq=(\d+).*time=(\d+(\.\d+)?)", line)
            if match:
                count += 1
                timestamp = float(match.group(1))
                rtt = float(match.group(3))
                v_Ping.ts.append(timestamp)
                v_Ping.rtt.append(rtt)

        assert (len(v_Ping.ts) == len(v_Ping.rtt))
        return v_Ping
