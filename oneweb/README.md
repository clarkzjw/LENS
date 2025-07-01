# OneWeb Dataset

## Dish Locations

The `iowa` directory contains the measurement data collected from a Hughes HL-1120W OneWeb user terminal located in Ames, Iowa, USA, supported by Iowa State University, at the Wilson Hall site.

To get access to the dish and conduct custom experiments, please check the [ARA User Manual](https://arawireless.readthedocs.io/en/latest/ara_experiments/arahaul_experiments/oneweb_basic.html).

## Monthly Snapshots

The dataset is split into monthly snapshots. Each can be retrieved from Zenodo using the links below.

### `iowa`

| Monthly Snapshots | Type | Link                                                        | Compressed Size  |
|-------------------|------|-------------------------------------------------------------|------------------|
| 2025-05           | RAW  | [202505.tar.zst](https://zenodo.org/records/15786387)       | 22GB             |
| 2025-04           | RAW  | [202504.tar.zst](https://zenodo.org/records/15786377)       | 30GB             |
| 2025-03           | RAW  | [202503.tar.zst](https://zenodo.org/records/15786375)       | 25GB             |
| 2025-02           | RAW  | [202502.tar.zst](https://zenodo.org/records/15786369)       | 1.9GB            |
| 2025-01           | RAW  | [202501.tar.zst](https://zenodo.org/records/15786348)       | 371MB            |
| 2024              | RAW  | [2024.tar.zst](https://zenodo.org/records/15786332)         | 321MB            |

Please check each subdirectory in [`iowa`](./iowa) for the list of files in each snapshot. Note that snapshots before `2025-03` are significantly smaller, as they do not contain `irtt` measurements.

## Dataset Format

The `RAW` dataset contains four subdirectories:

```
.
├── aim
│   └── 202503
├── irtt
│   └── 202503.tar.zst
├── ping
│   └── 202503
└── tle
    └── 202503
```

`irtt` and `ping` contains similar latency measurements as described in the Starlink dataset. See the [README](https://github.com/clarkzjw/LENS?tab=readme-ov-file#raw-dataset) for more details.

`aim` contains the user terminal antenna tracking logs, which are stored in CSV formats with the following columns:

```
head AIM_355866000274220_2025_03_01_00_58_55.csv

TIMESTAMP,AVERAGE_SINR,TRACK_ID,SATELLITE_ID,UT_MODEL,PROCESS_RESET_COUNT,IF_PATH,TARGET_COORD_SYS,ACTUAL_COORD_SYS,A0_TARGET_COORD0,A0_TARGET_COORD1,A0_ACTUAL_COORD0,A0_ACTUAL_COORD1,RCM_TX_ACTUAL,RCM_RX_ACTUAL,A0_TRUE_NORTH,A0_ROLL,A0_PITCH,INTEGRATOR_PARAMS
2025-03-01T00:58:37.530Z,3.69,332923286,406,HL1120W,2,0,HCS,APT,285.212,53.404,267.592,35.255,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":3.90,"POINTING_SCORE":98.9,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:37.730Z,3.75,332923286,406,HL1120W,2,0,HCS,APT,285.308,53.396,267.493,35.246,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":3.90,"POINTING_SCORE":98.9,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:37.930Z,3.84,332923286,406,HL1120W,2,0,HCS,APT,285.404,53.388,267.393,35.238,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.00,"POINTING_SCORE":99.0,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:38.130Z,3.87,332923286,406,HL1120W,2,0,HCS,APT,285.500,53.380,267.294,35.230,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.00,"POINTING_SCORE":99.0,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:38.330Z,3.85,332923286,406,HL1120W,2,0,HCS,APT,285.596,53.372,267.194,35.221,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.00,"POINTING_SCORE":99.1,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:38.530Z,3.99,332923286,406,HL1120W,2,0,HCS,APT,285.690,53.362,267.095,35.215,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.20,"POINTING_SCORE":99.2,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:38.730Z,4.09,332923286,406,HL1120W,2,0,HCS,APT,285.784,53.352,266.997,35.209,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.40,"POINTING_SCORE":99.2,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:38.930Z,3.99,332923286,406,HL1120W,2,0,HCS,APT,285.878,53.342,266.898,35.203,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.20,"POINTING_SCORE":99.1,"POINTING_STATE":"Tracking"}}
2025-03-01T00:58:39.130Z,3.96,332923286,406,HL1120W,2,0,HCS,APT,285.972,53.332,266.799,35.197,14217200000,11075000000,-178.861,-0.203,-9.597,{"INTEGRATOR_PARAMS":{"CALIBRATION_STATUS":"Fine","MAX_SINR":4.30,"POINTING_SCORE":99.1,"POINTING_STATE":"Tracking"}}
```

`tle` contains historical TLE data for the OneWeb satellites, obtained from the [Celestrak](https://celestrak.org/) website daily.

# License

The OneWeb dataset shares the same license as the main LENS dataset under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

# Citation

If you use this OneWeb dataset in your research, please consider citing the following paper:


**Measuring the OneWeb Satellite Network**, Jinwei Zhao, Owen Perrin, Ali Ahangarpour, Jianping Pan, 2025 Network Traffic Measurement and Analysis Conference (TMA'25) (*doi to be added*)

and

```
@inproceedings{10.1145/3625468.3652170,
author = {Zhao, Jinwei and Pan, Jianping},
title = {LENS: A LEO Satellite Network Measurement Dataset},
year = {2024},
isbn = {9798400704123},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3625468.3652170},
doi = {10.1145/3625468.3652170},
booktitle = {Proceedings of the 15th ACM Multimedia Systems Conference},
pages = {278–284},
numpages = {7},
keywords = {Dataset, Inter-Satellite Links, LEO, Latency, Network Measurement},
location = {Bari, Italy},
series = {MMSys '24}
}
```