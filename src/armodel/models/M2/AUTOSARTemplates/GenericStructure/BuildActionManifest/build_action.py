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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildAction, cls).deserialize(element)

        # Parse created_datas (list from container "CREATED-DATAS")
        obj.created_datas = []
        container = ARObject._find_child_element(element, "CREATED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.created_datas.append(child_value)

        # Parse follow_up_actions (list from container "FOLLOW-UP-ACTIONS")
        obj.follow_up_actions = []
        container = ARObject._find_child_element(element, "FOLLOW-UP-ACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.follow_up_actions.append(child_value)

        # Parse input_datas (list from container "INPUT-DATAS")
        obj.input_datas = []
        container = ARObject._find_child_element(element, "INPUT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.input_datas.append(child_value)

        # Parse modified_datas (list from container "MODIFIED-DATAS")
        obj.modified_datas = []
        container = ARObject._find_child_element(element, "MODIFIED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.modified_datas.append(child_value)

        # Parse predecessors (list from container "PREDECESSORS")
        obj.predecessors = []
        container = ARObject._find_child_element(element, "PREDECESSORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.predecessors.append(child_value)

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
