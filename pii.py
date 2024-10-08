#!/usr/bin/env python3
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

import en_core_web_lg

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

DEFAULT_ENTITIES = [
    "PHONE_NUMBER",
    "EMAIL_ADDRESS",
    "PERSON",
    "IP_ADDRESS",
]


def anonymize(text, entities=DEFAULT_ENTITIES):
    """
    Anonymize the given text, redacting the provided entities.
    """
    results = analyzer.analyze(text=text, entities=entities, language="en")
    anon = anonymizer.anonymize(text=text, analyzer_results=results)
    return anon


if __name__ == "__main__":
    # Quick command line test.
    import sys
    text = sys.stdin.read()
    result = anonymize(text)
    sys.stdout.write(result.text)
