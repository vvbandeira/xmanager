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
"""Convenience adapter for the standard client."""

import functools
from typing import Mapping, Sequence

from absl import logging
import docker
from docker.models import containers


@functools.lru_cache()
def instance() -> 'DockerAdapter':
  """Returns a thread-safe singleton adapter derived from the environment.

  Allows the user to ignore the complexities of the underlying library, and
  focus on a concrete small subset of required actions.
  """
  return DockerAdapter(docker.from_env())


class DockerAdapter(object):
  """Convenience adapter for the standard client."""

  def __init__(self, client: docker.DockerClient) -> None:
    self._client = client

  def get_client(self) -> docker.DockerClient:
    return self._client

  def load_image(self, path: str) -> str:
    with open(path, 'rb') as data:
      images = self._client.images.load(data.read())
      if len(images) != 1:
        raise ValueError('{} must contain precisely one image.'.format(path))
      return images[0].id

  def run_container(
      self,
      image_id: str,
      args: Sequence[str],
      env_vars: Mapping[str, str],
  ) -> containers.Container:
    return self._client.containers.run(
        image_id,
        detach=True,
        remove=True,
        command=args,
        environment=env_vars,
    )

  def stop_container(self, container_id: str) -> None:
    try:
      self._client.containers.get(container_id).stop()
    except docker.errors.NotFound:
      logging.warning('Container %s is already stopped.', container_id)