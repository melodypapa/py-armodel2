"""HwPin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class HwPin(Identifiable):
    """AUTOSAR HwPin."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_names: list[String]
    packaging_pin: Optional[String]
    pin_number: Optional[Integer]
    def __init__(self) -> None:
        """Initialize HwPin."""
        super().__init__()
        self.function_names: list[String] = []
        self.packaging_pin: Optional[String] = None
        self.pin_number: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize HwPin to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPin, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_names (list to container "FUNCTION-NAMES")
        if self.function_names:
            wrapper = ET.Element("FUNCTION-NAMES")
            for item in self.function_names:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("FUNCTION-NAME")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize packaging_pin
        if self.packaging_pin is not None:
            serialized = SerializationHelper.serialize_item(self.packaging_pin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGING-PIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pin_number
        if self.pin_number is not None:
            serialized = SerializationHelper.serialize_item(self.pin_number, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PIN-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPin":
        """Deserialize XML element to HwPin object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPin object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPin, cls).deserialize(element)

        # Parse function_names (list from container "FUNCTION-NAMES")
        obj.function_names = []
        container = SerializationHelper.find_child_element(element, "FUNCTION-NAMES")
        if container is not None:
            for child in container:
                # Extract primitive value (String) as text
                child_value = child.text
                if child_value is not None:
                    obj.function_names.append(child_value)

        # Parse packaging_pin
        child = SerializationHelper.find_child_element(element, "PACKAGING-PIN")
        if child is not None:
            packaging_pin_value = child.text
            obj.packaging_pin = packaging_pin_value

        # Parse pin_number
        child = SerializationHelper.find_child_element(element, "PIN-NUMBER")
        if child is not None:
            pin_number_value = child.text
            obj.pin_number = pin_number_value

        return obj



class HwPinBuilder:
    """Builder for HwPin."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPin = HwPin()

    def build(self) -> HwPin:
        """Build and return HwPin object.

        Returns:
            HwPin instance
        """
        # TODO: Add validation
        return self._obj
