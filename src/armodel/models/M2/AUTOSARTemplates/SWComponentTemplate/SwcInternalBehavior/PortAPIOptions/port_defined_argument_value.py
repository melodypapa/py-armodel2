"""PortDefinedArgumentValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 593)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class PortDefinedArgumentValue(ARObject):
    """AUTOSAR PortDefinedArgumentValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[ValueSpecification]
    value_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize PortDefinedArgumentValue."""
        super().__init__()
        self.value: Optional[ValueSpecification] = None
        self.value_type: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize PortDefinedArgumentValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortDefinedArgumentValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value_type
        if self.value_type is not None:
            serialized = SerializationHelper.serialize_item(self.value_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortDefinedArgumentValue":
        """Deserialize XML element to PortDefinedArgumentValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortDefinedArgumentValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortDefinedArgumentValue, cls).deserialize(element)

        # Parse value
        child = SerializationHelper.find_child_element(element, "VALUE")
        if child is not None:
            value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.value = value_value

        # Parse value_type
        child = SerializationHelper.find_child_element(element, "VALUE-TYPE")
        if child is not None:
            value_type_value = child.text
            obj.value_type = value_type_value

        return obj



class PortDefinedArgumentValueBuilder:
    """Builder for PortDefinedArgumentValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortDefinedArgumentValue = PortDefinedArgumentValue()

    def build(self) -> PortDefinedArgumentValue:
        """Build and return PortDefinedArgumentValue object.

        Returns:
            PortDefinedArgumentValue instance
        """
        # TODO: Add validation
        return self._obj
