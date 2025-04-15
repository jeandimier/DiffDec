from dacite import from_dict
from dtos import GeneralConfiguration, ReactionBasedSlicingConfig
from reaction_based_slicing import ReactionBasedSlicer

from utils.enums import RunningModeEnum


class Manager:
    def __init__(self, configuration: GeneralConfiguration):
        self._configuration = configuration
        self._running_mode = RunningModeEnum()

    def _reaction_based_slicing(self):
        config = from_dict(
            data_class=ReactionBasedSlicingConfig, data=self._configuration.parameters
        )
        slicer = ReactionBasedSlicer(config)
        slicer.run()

    def run(self):
        registry = {
            self._running_mode.REACTION_BASED_SLICING: self._reaction_based_slicing,
        }

        run_type = registry.get(self._configuration.run_type, lambda: TypeError)
        run_type()
