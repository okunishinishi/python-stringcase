#!/bin/bash

HERE=$(cd "$(dirname $0)" && pwd)
BASE_DIR=$(cd "${HERE}/.." && pwd)

cd "${BASE_DIR}"

python setup.py sdist upload -r pypi

git add . -A
git commit -m 'Version up'
git push