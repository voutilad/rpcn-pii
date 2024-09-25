# PII Redaction with Redpanda Connect & Microsoft Presidio

## Installation

0. Clone the repo and submodule(s):

```sh
git clone https://github.com/voutilad/rpcn-pii
cd rpcn-pii
git submodule update --init --recursive
```

1. Create and activate new virtualenv:

```sh
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```sh
# Used for RP Connect Python.
pip install -U pip setuptools

# Install dependencies for Presidio.
pip install -r requirements.txt

# Download a prebuilt language model for spaCy.
python -m spacy download en_core_web_lg
```

3. Build Redpanda Connect Python:

```sh
CGO_ENABLED=0 go build -C rp-connect-python
```

## Demo / Usage

```sh
echo "My name is Dave and I like to party. Call me at (123)-456-7890!" \
    | ./rp-connect-python/rp-connect-python run pipeline.yaml
```

You should see output of JSON resembling:

```json
{
  "text": "My name is <PERSON> and I like to party. Call me at <PHONE_NUMBER>!",
  "items": [
    {
      "start": 52,
      "end": 66,
      "entity_type": "PHONE_NUMBER",
      "text": "<PHONE_NUMBER>",
      "operator": "replace"
    },
    {
      "start": 11,
      "end": 19,
      "entity_type": "PERSON",
      "text": "<PERSON>",
      "operator": "replace"
    }
  ]
}
```