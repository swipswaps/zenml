#  Copyright (c) maiot GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

import importlib.util

from zenml.core.steps.trainer.base_trainer import BaseTrainerStep

spec = importlib.util.find_spec('torch')
if spec is None:
    raise AssertionError("torch integration not installed. Please install "
                         "zenml[torch] via `pip install zenml[pytorch]`")


class TorchBaseTrainerStep(BaseTrainerStep):
    """
    Base class for all PyTorch based trainer steps. All pytorch based
    trainings should use this as the base class. An example is available
    with torch_ff_trainer.FeedForwardTrainer.
    """
    pass
