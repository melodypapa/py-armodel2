"""J1939NodeName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class J1939NodeName(ARObject):
    """AUTOSAR J1939NodeName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arbitrary_address: Optional[Any]
    ecu_instance: Optional[Integer]
    function: Optional[Integer]
    function_instance: Optional[Integer]
    identitiy_number: Optional[Integer]
    industry_group: Optional[Integer]
    manufacturer_code: Optional[Integer]
    vehicle_system: Optional[Integer]
    vehicle_system_instance: Optional[Integer]
    def __init__(self) -> None:
        """Initialize J1939NodeName."""
        super().__init__()
        self.arbitrary_address: Optional[Any] = None
        self.ecu_instance: Optional[Integer] = None
        self.function: Optional[Integer] = None
        self.function_instance: Optional[Integer] = None
        self.identitiy_number: Optional[Integer] = None
        self.industry_group: Optional[Integer] = None
        self.manufacturer_code: Optional[Integer] = None
        self.vehicle_system: Optional[Integer] = None
        self.vehicle_system_instance: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939NodeName to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939NodeName, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arbitrary_address
        if self.arbitrary_address is not None:
            serialized = SerializationHelper.serialize_item(self.arbitrary_address, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARBITRARY-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance
        if self.ecu_instance is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance, "Integer")
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

        # Serialize function
        if self.function is not None:
            serialized = SerializationHelper.serialize_item(self.function, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function_instance
        if self.function_instance is not None:
            serialized = SerializationHelper.serialize_item(self.function_instance, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identitiy_number
        if self.identitiy_number is not None:
            serialized = SerializationHelper.serialize_item(self.identitiy_number, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTITIY-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize industry_group
        if self.industry_group is not None:
            serialized = SerializationHelper.serialize_item(self.industry_group, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDUSTRY-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize manufacturer_code
        if self.manufacturer_code is not None:
            serialized = SerializationHelper.serialize_item(self.manufacturer_code, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MANUFACTURER-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vehicle_system
        if self.vehicle_system is not None:
            serialized = SerializationHelper.serialize_item(self.vehicle_system, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VEHICLE-SYSTEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vehicle_system_instance
        if self.vehicle_system_instance is not None:
            serialized = SerializationHelper.serialize_item(self.vehicle_system_instance, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VEHICLE-SYSTEM-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NodeName":
        """Deserialize XML element to J1939NodeName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939NodeName object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939NodeName, cls).deserialize(element)

        # Parse arbitrary_address
        child = SerializationHelper.find_child_element(element, "ARBITRARY-ADDRESS")
        if child is not None:
            arbitrary_address_value = child.text
            obj.arbitrary_address = arbitrary_address_value

        # Parse ecu_instance
        child = SerializationHelper.find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = child.text
            obj.ecu_instance = ecu_instance_value

        # Parse function
        child = SerializationHelper.find_child_element(element, "FUNCTION")
        if child is not None:
            function_value = child.text
            obj.function = function_value

        # Parse function_instance
        child = SerializationHelper.find_child_element(element, "FUNCTION-INSTANCE")
        if child is not None:
            function_instance_value = child.text
            obj.function_instance = function_instance_value

        # Parse identitiy_number
        child = SerializationHelper.find_child_element(element, "IDENTITIY-NUMBER")
        if child is not None:
            identitiy_number_value = child.text
            obj.identitiy_number = identitiy_number_value

        # Parse industry_group
        child = SerializationHelper.find_child_element(element, "INDUSTRY-GROUP")
        if child is not None:
            industry_group_value = child.text
            obj.industry_group = industry_group_value

        # Parse manufacturer_code
        child = SerializationHelper.find_child_element(element, "MANUFACTURER-CODE")
        if child is not None:
            manufacturer_code_value = child.text
            obj.manufacturer_code = manufacturer_code_value

        # Parse vehicle_system
        child = SerializationHelper.find_child_element(element, "VEHICLE-SYSTEM")
        if child is not None:
            vehicle_system_value = child.text
            obj.vehicle_system = vehicle_system_value

        # Parse vehicle_system_instance
        child = SerializationHelper.find_child_element(element, "VEHICLE-SYSTEM-INSTANCE")
        if child is not None:
            vehicle_system_instance_value = child.text
            obj.vehicle_system_instance = vehicle_system_instance_value

        return obj



class J1939NodeNameBuilder:
    """Builder for J1939NodeName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NodeName = J1939NodeName()

    def build(self) -> J1939NodeName:
        """Build and return J1939NodeName object.

        Returns:
            J1939NodeName instance
        """
        # TODO: Add validation
        return self._obj
