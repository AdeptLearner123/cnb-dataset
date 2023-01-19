import yaml
import random

from config import CARDWORDS, SCENARIOS

from collections import Counter

def main():
    with open(CARDWORDS, "r") as file:
        cardwords = file.read().splitlines()
    
    with open(SCENARIOS, "r") as file:
        scenarios = yaml.safe_load(file.read())
    
    word_counts = Counter([ len(scenario["pos"]) + len(scenario["neg"]) for scenario in scenarios.values() ])
    print(word_counts)

    scenarios_low_count = [ (scenario_id, scenario) for scenario_id, scenario in scenarios.items() if len(scenario["pos"]) + len (scenario["neg"]) < 8 ]
    print(len(scenarios_low_count))

    for i, (scenario_id, scenario) in enumerate(scenarios_low_count):
        print(i)
        print(scenario["clue"])
        print(scenario["pos"])
        
        for i in range(8 - len(scenario["pos"]) - len(scenario["neg"])):
            possible_negs = list(set(cardwords) - set(scenario["pos"]) - set(scenario["neg"]))

            while True:
                cardword = random.choice(possible_negs)
                print(cardword)
                yes = input("y/n:") == "y"

                if yes:
                    scenario["neg"].append(cardword)
                    scenarios[scenario_id] = scenario

                    with open(SCENARIOS, "w") as file:
                        file.write(yaml.dump(scenarios, default_flow_style=None))
                    break


if __name__ == "__main__":
    main()