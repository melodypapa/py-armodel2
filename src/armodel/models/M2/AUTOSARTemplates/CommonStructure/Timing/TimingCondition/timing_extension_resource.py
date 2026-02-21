"""TimingExtensionResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)


class TimingExtensionResource(Identifiable):
    """AUTOSAR TimingExtensionResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timing_arguments: list[AutosarOperationArgumentInstance]
    timing_modes: list[TimingModeInstance]
    timing_variables: list[Any]
    def __init__(self) -> None:
        """Initialize TimingExtensionResource."""
        super().__init__()
        self.timing_arguments: list[AutosarOperationArgumentInstance] = []
        self.timing_modes: list[TimingModeInstance] = []
        self.timing_variables: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TimingExtensionResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingExtensionResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_arguments (list to container "TIMING-ARGUMENTS")
        if self.timing_arguments:
            wrapper = ET.Element("TIMING-ARGUMENTS")
            for item in self.timing_arguments:
                serialized = SerializationHelper.serialize_item(item, "AutosarOperationArgumentInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_modes (list to container "TIMING-MODES")
        if self.timing_modes:
            wrapper = ET.Element("TIMING-MODES")
            for item in self.timing_modes:
                serialized = SerializationHelper.serialize_item(item, "TimingModeInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_variables (list to container "TIMING-VARIABLES")
        if self.timing_variables:
            wrapper = ET.Element("TIMING-VARIABLES")
            for item in self.timing_variables:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtensionResource":
        """Deserialize XML element to TimingExtensionResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingExtensionResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingExtensionResource, cls).deserialize(element)

        # Parse timing_arguments (list from container "TIMING-ARGUMENTS")
        obj.timing_arguments = []
        container = SerializationHelper.find_child_element(element, "TIMING-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_arguments.append(child_value)

        # Parse timing_modes (list from container "TIMING-MODES")
        obj.timing_modes = []
        container = SerializationHelper.find_child_element(element, "TIMING-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_modes.append(child_value)

        # Parse timing_variables (list from container "TIMING-VARIABLES")
        obj.timing_variables = []
        container = SerializationHelper.find_child_element(element, "TIMING-VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_variables.append(child_value)

        return obj



class TimingExtensionResourceBuilder:
    """Builder for TimingExtensionResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingExtensionResource = TimingExtensionResource()

    def build(self) -> TimingExtensionResource:
        """Build and return TimingExtensionResource object.

        Returns:
            TimingExtensionResource instance
        """
        # TODO: Add validation
        return self._obj
