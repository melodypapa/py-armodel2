"""BuildActionManifest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 365)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action import (
    BuildAction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)


class BuildActionManifest(ARElement):
    """AUTOSAR BuildActionManifest."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    build_actions: list[BuildActionEnvironment]
    dynamic_actions: list[BuildAction]
    start_actions: list[BuildAction]
    tear_down_actions: list[BuildAction]
    def __init__(self) -> None:
        """Initialize BuildActionManifest."""
        super().__init__()
        self.build_actions: list[BuildActionEnvironment] = []
        self.dynamic_actions: list[BuildAction] = []
        self.start_actions: list[BuildAction] = []
        self.tear_down_actions: list[BuildAction] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionManifest":
        """Deserialize XML element to BuildActionManifest object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionManifest object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionManifest, cls).deserialize(element)

        # Parse build_actions (list from container "BUILD-ACTIONS")
        obj.build_actions = []
        container = ARObject._find_child_element(element, "BUILD-ACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.build_actions.append(child_value)

        # Parse dynamic_actions (list from container "DYNAMIC-ACTIONS")
        obj.dynamic_actions = []
        container = ARObject._find_child_element(element, "DYNAMIC-ACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dynamic_actions.append(child_value)

        # Parse start_actions (list from container "START-ACTIONS")
        obj.start_actions = []
        container = ARObject._find_child_element(element, "START-ACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.start_actions.append(child_value)

        # Parse tear_down_actions (list from container "TEAR-DOWN-ACTIONS")
        obj.tear_down_actions = []
        container = ARObject._find_child_element(element, "TEAR-DOWN-ACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tear_down_actions.append(child_value)

        return obj



class BuildActionManifestBuilder:
    """Builder for BuildActionManifest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionManifest = BuildActionManifest()

    def build(self) -> BuildActionManifest:
        """Build and return BuildActionManifest object.

        Returns:
            BuildActionManifest instance
        """
        # TODO: Add validation
        return self._obj
