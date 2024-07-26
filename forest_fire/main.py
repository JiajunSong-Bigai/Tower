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
        for fact in facts:
            self.prolog.assertz(fact)

    def query(self, q):
        result = list(self.prolog.query(q))
        return result if result else "false"


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

    for q in queries:
        result = dd.query(q)
        print("Query:", q, " => ", result)


if __name__ == "__main__":
    fire.Fire(main)
