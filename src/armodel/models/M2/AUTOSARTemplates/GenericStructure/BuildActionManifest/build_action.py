"""BuildAction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 366)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 172)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_entity import (
    BuildActionEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_io_element import (
    BuildActionIoElement,
)


class BuildAction(BuildActionEntity):
    """AUTOSAR BuildAction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    created_datas: list[BuildActionIoElement]
    follow_up_actions: list[BuildAction]
    input_datas: list[BuildActionIoElement]
    modified_datas: list[BuildActionIoElement]
    predecessors: list[BuildAction]
    required: BuildActionEnvironment
    def __init__(self) -> None:
        """Initialize BuildAction."""
        super().__init__()
        self.created_datas: list[BuildActionIoElement] = []
        self.follow_up_actions: list[BuildAction] = []
        self.input_datas: list[BuildActionIoElement] = []
        self.modified_datas: list[BuildActionIoElement] = []
        self.predecessors: list[BuildAction] = []
        self.required: BuildActionEnvironment = None


class BuildActionBuilder:
    """Builder for BuildAction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildAction = BuildAction()

    def build(self) -> BuildAction:
        """Build and return BuildAction object.

        Returns:
            BuildAction instance
        """
        # TODO: Add validation
        return self._obj
