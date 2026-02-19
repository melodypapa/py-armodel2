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

    def serialize(self) -> ET.Element:
        """Serialize BuildAction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildAction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize created_datas (list to container "CREATED-DATAS")
        if self.created_datas:
            wrapper = ET.Element("CREATED-DATAS")
            for item in self.created_datas:
                serialized = ARObject._serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize follow_up_actions (list to container "FOLLOW-UP-ACTIONS")
        if self.follow_up_actions:
            wrapper = ET.Element("FOLLOW-UP-ACTIONS")
            for item in self.follow_up_actions:
                serialized = ARObject._serialize_item(item, "BuildAction")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize input_datas (list to container "INPUT-DATAS")
        if self.input_datas:
            wrapper = ET.Element("INPUT-DATAS")
            for item in self.input_datas:
                serialized = ARObject._serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize modified_datas (list to container "MODIFIED-DATAS")
        if self.modified_datas:
            wrapper = ET.Element("MODIFIED-DATAS")
            for item in self.modified_datas:
                serialized = ARObject._serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize predecessors (list to container "PREDECESSORS")
        if self.predecessors:
            wrapper = ET.Element("PREDECESSORS")
            for item in self.predecessors:
                serialized = ARObject._serialize_item(item, "BuildAction")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required
        if self.required is not None:
            serialized = ARObject._serialize_item(self.required, "BuildActionEnvironment")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
