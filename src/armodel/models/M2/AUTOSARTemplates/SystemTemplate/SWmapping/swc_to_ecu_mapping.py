"""SwcToEcuMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    components: list[Any]
    controlled_hw: Optional[HwElement]
    ecu_instance: Optional[EcuInstance]
    processing_unit: Optional[HwElement]
    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self.components: list[Any] = []
        self.controlled_hw: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.processing_unit: Optional[HwElement] = None
    def serialize(self) -> ET.Element:
        """Serialize SwcToEcuMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToEcuMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize components (list to container "COMPONENTS")
        if self.components:
            wrapper = ET.Element("COMPONENTS")
            for item in self.components:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize controlled_hw
        if self.controlled_hw is not None:
            serialized = ARObject._serialize_item(self.controlled_hw, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLED-HW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance
        if self.ecu_instance is not None:
            serialized = ARObject._serialize_item(self.ecu_instance, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processing_unit
        if self.processing_unit is not None:
            serialized = ARObject._serialize_item(self.processing_unit, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToEcuMapping":
        """Deserialize XML element to SwcToEcuMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToEcuMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToEcuMapping, cls).deserialize(element)

        # Parse components (list from container "COMPONENTS")
        obj.components = []
        container = ARObject._find_child_element(element, "COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.components.append(child_value)

        # Parse controlled_hw
        child = ARObject._find_child_element(element, "CONTROLLED-HW")
        if child is not None:
            controlled_hw_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.controlled_hw = controlled_hw_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse processing_unit
        child = ARObject._find_child_element(element, "PROCESSING-UNIT")
        if child is not None:
            processing_unit_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.processing_unit = processing_unit_value

        return obj



class SwcToEcuMappingBuilder:
    """Builder for SwcToEcuMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToEcuMapping = SwcToEcuMapping()

    def build(self) -> SwcToEcuMapping:
        """Build and return SwcToEcuMapping object.

        Returns:
            SwcToEcuMapping instance
        """
        # TODO: Add validation
        return self._obj
