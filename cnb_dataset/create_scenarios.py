import yaml
import random

from config import SCENARIOS_ALL, SCENARIOS_DATA_ALL, SCENARIOS, SCENARIOS_DATA

def main():
    with open(SCENARIOS_ALL, "r") as file:
        scenarios_all = yaml.safe_load(file.read())
    with open(SCENARIOS_DATA_ALL, "r") as file:
        scenarios_data_all = yaml.safe_load(file.read())
    
    scenario_ids = random.sample(scenarios_all.keys(), 100)
    scenarios = { scenario_id: scenarios_all[scenario_id] for scenario_id in scenario_ids }
    scenarios_data = { scenario_id: scenarios_data_all[scenario_id] for scenario_id in scenario_ids }

    with open(SCENARIOS, "w+") as file:
        file.write(yaml.dump(scenarios, default_flow_style=None))
    with open(SCENARIOS_DATA, "w+") as file:
        file.write(yaml.dump(scenarios_data, default_flow_style=None))


if __name__ == "__main__":
    main()