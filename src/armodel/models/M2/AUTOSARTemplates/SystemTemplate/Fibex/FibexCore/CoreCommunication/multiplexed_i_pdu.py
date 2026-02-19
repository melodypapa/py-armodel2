"""MultiplexedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 408)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part import (
    DynamicPart,
)


class MultiplexedIPdu(IPdu):
    """AUTOSAR MultiplexedIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_part: Optional[DynamicPart]
    selector_field: Optional[Integer]
    unused_bit: Optional[Integer]
    def __init__(self) -> None:
        """Initialize MultiplexedIPdu."""
        super().__init__()
        self.dynamic_part: Optional[DynamicPart] = None
        self.selector_field: Optional[Integer] = None
        self.unused_bit: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize MultiplexedIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultiplexedIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_part
        if self.dynamic_part is not None:
            serialized = ARObject._serialize_item(self.dynamic_part, "DynamicPart")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-PART")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize selector_field
        if self.selector_field is not None:
            serialized = ARObject._serialize_item(self.selector_field, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SELECTOR-FIELD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unused_bit
        if self.unused_bit is not None:
            serialized = ARObject._serialize_item(self.unused_bit, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplexedIPdu":
        """Deserialize XML element to MultiplexedIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiplexedIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiplexedIPdu, cls).deserialize(element)

        # Parse dynamic_part
        child = ARObject._find_child_element(element, "DYNAMIC-PART")
        if child is not None:
            dynamic_part_value = ARObject._deserialize_by_tag(child, "DynamicPart")
            obj.dynamic_part = dynamic_part_value

        # Parse selector_field
        child = ARObject._find_child_element(element, "SELECTOR-FIELD")
        if child is not None:
            selector_field_value = child.text
            obj.selector_field = selector_field_value

        # Parse unused_bit
        child = ARObject._find_child_element(element, "UNUSED-BIT")
        if child is not None:
            unused_bit_value = child.text
            obj.unused_bit = unused_bit_value

        return obj



class MultiplexedIPduBuilder:
    """Builder for MultiplexedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplexedIPdu = MultiplexedIPdu()

    def build(self) -> MultiplexedIPdu:
        """Build and return MultiplexedIPdu object.

        Returns:
            MultiplexedIPdu instance
        """
        # TODO: Add validation
        return self._obj
