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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildAction":
        """Deserialize XML element to BuildAction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildAction object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse created_datas (list)
        obj.created_datas = []
        for child in ARObject._find_all_child_elements(element, "CREATED-DATAS"):
            created_datas_value = ARObject._deserialize_by_tag(child, "BuildActionIoElement")
            obj.created_datas.append(created_datas_value)

        # Parse follow_up_actions (list)
        obj.follow_up_actions = []
        for child in ARObject._find_all_child_elements(element, "FOLLOW-UP-ACTIONS"):
            follow_up_actions_value = ARObject._deserialize_by_tag(child, "BuildAction")
            obj.follow_up_actions.append(follow_up_actions_value)

        # Parse input_datas (list)
        obj.input_datas = []
        for child in ARObject._find_all_child_elements(element, "INPUT-DATAS"):
            input_datas_value = ARObject._deserialize_by_tag(child, "BuildActionIoElement")
            obj.input_datas.append(input_datas_value)

        # Parse modified_datas (list)
        obj.modified_datas = []
        for child in ARObject._find_all_child_elements(element, "MODIFIED-DATAS"):
            modified_datas_value = ARObject._deserialize_by_tag(child, "BuildActionIoElement")
            obj.modified_datas.append(modified_datas_value)

        # Parse predecessors (list)
        obj.predecessors = []
        for child in ARObject._find_all_child_elements(element, "PREDECESSORS"):
            predecessors_value = ARObject._deserialize_by_tag(child, "BuildAction")
            obj.predecessors.append(predecessors_value)

        # Parse required
        child = ARObject._find_child_element(element, "REQUIRED")
        if child is not None:
            required_value = ARObject._deserialize_by_tag(child, "BuildActionEnvironment")
            obj.required = required_value

        return obj



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
