#!/bin/bash

set -e

pip install --upgrade setuptools wheel


pip_version=$(pip --version | awk '{print $2}')
required_version="24.0"

version_greater_equal() {
    printf '%s\n%s' "$1" "$2" | sort -C -V
}

if ! version_greater_equal "$pip_version" "$required_version"; then
    echo "Upgrading pip from version $pip_version to $required_version"
    pip install --upgrade pip
else
    echo "pip is already at version $pip_version, no need to upgrade."
fi

pip install -r requirements.txt

pip install .
