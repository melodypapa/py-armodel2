"""SwComponentPrototypeAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 894)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SwComponentPrototypeAssignment(ARObject):
    """AUTOSAR SwComponentPrototypeAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_component: Optional[Any]
    def __init__(self) -> None:
        """Initialize SwComponentPrototypeAssignment."""
        super().__init__()
        self.sw_component: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize SwComponentPrototypeAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentPrototypeAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_component
        if self.sw_component is not None:
            serialized = SerializationHelper.serialize_item(self.sw_component, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototypeAssignment":
        """Deserialize XML element to SwComponentPrototypeAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototypeAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentPrototypeAssignment, cls).deserialize(element)

        # Parse sw_component
        child = SerializationHelper.find_child_element(element, "SW-COMPONENT")
        if child is not None:
            sw_component_value = child.text
            obj.sw_component = sw_component_value

        return obj



class SwComponentPrototypeAssignmentBuilder:
    """Builder for SwComponentPrototypeAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentPrototypeAssignment = SwComponentPrototypeAssignment()

    def build(self) -> SwComponentPrototypeAssignment:
        """Build and return SwComponentPrototypeAssignment object.

        Returns:
            SwComponentPrototypeAssignment instance
        """
        # TODO: Add validation
        return self._obj
