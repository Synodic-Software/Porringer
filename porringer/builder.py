"""Builder"""

from importlib import metadata
from inspect import getmodule
from logging import Logger

from porringer_core.plugin_schema.environment import Environment
from synodic_utilities.exception import PluginError
from synodic_utilities.utility import canonicalize_type


class Builder:
    """Helper class for building Porringer projects"""

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def find_environments(self) -> list[type[Environment]]:
        """Searches for registered environment plugins

        Raises:
            PluginError: Raised if there is no plugin found

        Returns:
            A list of loaded plugins
        """

        group_name = "environment"
        plugin_types: list[type[Environment]] = []

        # Filter entries by type
        for entry_point in list(metadata.entry_points(group=f"porringer.{group_name}")):
            loaded_type = entry_point.load()
            if not issubclass(loaded_type, Environment):
                self.logger.warning(
                    f"Found incompatible plugin. The '{canonicalize_type(loaded_type).name}' plugin must be an instance"
                    f" of '{group_name}'"
                )
            else:
                self.logger.warning(
                    f"{group_name} plugin found: {canonicalize_type(loaded_type).name} from {getmodule(loaded_type)}"
                )
                plugin_types.append(loaded_type)

        if not plugin_types:
            raise PluginError(f"No {group_name} plugin was found")

        return plugin_types
