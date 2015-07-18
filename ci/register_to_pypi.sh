#!/bin/bash

HERE=$(cd "$(dirname $0)" && pwd)
BASE_DIR=$(cd "${HERE}/.." && pwd)

cd "${BASE_DIR}"

python setup.py bdist
python setup.py register -r pypi