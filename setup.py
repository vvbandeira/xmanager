# Copyright 2021 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup configuration specifying XManager dependencies."""

from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name='xmanager',
    version='1.0.0',
    description='A framework for managing experiments',
    author='DeepMind Technologies Limited',
    packages=find_namespace_packages(),
    include_package_data=True,
    package_data={'': ['*.sh']},
    python_requires='>=3.6',
    install_requires=[
        'absl-py',
        'async_generator',
        'attrs',
        'caliban==0.4.1',
        'docker',
        'immutabledict',
        'google-api-python-client',
        'google-auth',
        'google-cloud-storage',
        'kubernetes',
        'termcolor',
    ],
    entry_points={
        'console_scripts': ['xmanager = xmanager.cli.cli:Entrypoint',],
    },
)