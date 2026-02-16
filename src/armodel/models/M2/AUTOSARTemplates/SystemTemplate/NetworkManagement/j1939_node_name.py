"""J1939NodeName AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class J1939NodeName(ARObject):
    """AUTOSAR J1939NodeName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arbitrary_address", None, False, False, any (BooleanCapable)),  # arbitraryAddress
        ("ecu_instance", None, True, False, None),  # ecuInstance
        ("function", None, True, False, None),  # function
        ("function_instance", None, True, False, None),  # functionInstance
        ("identitiy_number", None, True, False, None),  # identitiyNumber
        ("industry_group", None, True, False, None),  # industryGroup
        ("manufacturer_code", None, True, False, None),  # manufacturerCode
        ("vehicle_system", None, True, False, None),  # vehicleSystem
        ("vehicle_system_instance", None, True, False, None),  # vehicleSystemInstance
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939NodeName to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NodeName":
        """Create J1939NodeName from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939NodeName instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939NodeName since parent returns ARObject
        return cast("J1939NodeName", obj)


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
