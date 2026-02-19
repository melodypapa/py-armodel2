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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse build_actions (list)
        obj.build_actions = []
        for child in ARObject._find_all_child_elements(element, "BUILD-ACTIONS"):
            build_actions_value = ARObject._deserialize_by_tag(child, "BuildActionEnvironment")
            obj.build_actions.append(build_actions_value)

        # Parse dynamic_actions (list)
        obj.dynamic_actions = []
        for child in ARObject._find_all_child_elements(element, "DYNAMIC-ACTIONS"):
            dynamic_actions_value = ARObject._deserialize_by_tag(child, "BuildAction")
            obj.dynamic_actions.append(dynamic_actions_value)

        # Parse start_actions (list)
        obj.start_actions = []
        for child in ARObject._find_all_child_elements(element, "START-ACTIONS"):
            start_actions_value = ARObject._deserialize_by_tag(child, "BuildAction")
            obj.start_actions.append(start_actions_value)

        # Parse tear_down_actions (list)
        obj.tear_down_actions = []
        for child in ARObject._find_all_child_elements(element, "TEAR-DOWN-ACTIONS"):
            tear_down_actions_value = ARObject._deserialize_by_tag(child, "BuildAction")
            obj.tear_down_actions.append(tear_down_actions_value)

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
