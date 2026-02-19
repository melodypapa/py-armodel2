"""HardwareConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class HardwareConfiguration(ARObject):
    """AUTOSAR HardwareConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    additional: Optional[String]
    processor_mode: Optional[String]
    processor_speed: Optional[String]
    def __init__(self) -> None:
        """Initialize HardwareConfiguration."""
        super().__init__()
        self.additional: Optional[String] = None
        self.processor_mode: Optional[String] = None
        self.processor_speed: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize HardwareConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize additional
        if self.additional is not None:
            serialized = ARObject._serialize_item(self.additional, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDITIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processor_mode
        if self.processor_mode is not None:
            serialized = ARObject._serialize_item(self.processor_mode, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSOR-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processor_speed
        if self.processor_speed is not None:
            serialized = ARObject._serialize_item(self.processor_speed, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSOR-SPEED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HardwareConfiguration":
        """Deserialize XML element to HardwareConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HardwareConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse additional
        child = ARObject._find_child_element(element, "ADDITIONAL")
        if child is not None:
            additional_value = child.text
            obj.additional = additional_value

        # Parse processor_mode
        child = ARObject._find_child_element(element, "PROCESSOR-MODE")
        if child is not None:
            processor_mode_value = child.text
            obj.processor_mode = processor_mode_value

        # Parse processor_speed
        child = ARObject._find_child_element(element, "PROCESSOR-SPEED")
        if child is not None:
            processor_speed_value = child.text
            obj.processor_speed = processor_speed_value

        return obj



class HardwareConfigurationBuilder:
    """Builder for HardwareConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HardwareConfiguration = HardwareConfiguration()

    def build(self) -> HardwareConfiguration:
        """Build and return HardwareConfiguration object.

        Returns:
            HardwareConfiguration instance
        """
        # TODO: Add validation
        return self._obj
