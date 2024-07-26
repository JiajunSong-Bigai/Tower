from typing import List

import fire
from pyswip import Prolog


def facts_from_file(path_to_facts):
    facts = open(path_to_facts).readlines()
    return_facts = []
    for fact in facts:
        fact = fact.strip()

        if fact.startswith("%") or not fact:
            continue

        if fact.endswith("."):
            fact = fact[:-1]

        return_facts.append(fact)

    return return_facts


class DD:
    def __init__(
        self,
        path_to_rules,
    ) -> None:
        self.prolog = Prolog()
        self.prolog.consult(path_to_rules)

    def read_facts(self, facts: List[str]):
        print("FACTS\n" + "=" * 50)
        for fact in facts:
            print(fact)
            self.prolog.assertz(fact)

    def query(self, q):
        print(f"q: {q}\n", end="=> ")
        result = list(self.prolog.query(q))
        if result:
            print(result, end="\n\n")
        else:
            print("false")


def main(path_to_rules="rules.pl", path_to_facts="facts.pl"):
    facts = facts_from_file(path_to_facts)

    # Define queries
    queries = [
        "fire_spread_area(current, SpreadArea)",
        "fire_size(Size)",
        "take_action(current)",
    ]

    # Define Deductive Database
    dd = DD(path_to_rules=path_to_rules)
    dd.read_facts(facts)

    print("\n\nQUERIES\n" + "=" * 50)
    for q in queries:
        dd.query(q)


if __name__ == "__main__":
    fire.Fire(main)
