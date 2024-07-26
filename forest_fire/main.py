import logging
from typing import List

import fire
from pyswip import Prolog

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,  # Adjust the logging level as needed
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # Adjust datefmt to exclude milliseconds
)
logger = logging.getLogger(__name__)


def facts_from_file(path_to_facts):
    logger.info(f"Reading facts from file: {path_to_facts}")
    try:
        with open(path_to_facts, "r") as file:
            facts = file.readlines()
    except FileNotFoundError:
        logger.error(f"File not found: {path_to_facts}")
        return []

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
    def __init__(self, path_to_rules) -> None:
        self.prolog = Prolog()
        logger.info(f"Consulting Prolog rules from file: {path_to_rules}")
        self.prolog.consult(path_to_rules)

    def read_facts(self, facts: List[str]):
        logger.info("Asserting facts into Prolog")
        for fact in facts:
            logger.debug(f"Asserting fact: {fact}")
            self.prolog.assertz(fact)

    def query(self, q):
        logger.info(f"Querying Prolog: {q}")
        result = list(self.prolog.query(q))
        if result:
            logger.info(f"Query result: {result}")
        else:
            logger.info("Query result: false")


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

    logger.info("Executing queries")
    for q in queries:
        dd.query(q)


if __name__ == "__main__":
    fire.Fire(main)
