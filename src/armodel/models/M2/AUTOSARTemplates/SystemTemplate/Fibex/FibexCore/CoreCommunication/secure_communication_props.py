"""SecureCommunicationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecureCommunicationProps(ARObject):
    """AUTOSAR SecureCommunicationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("auth_data", None, True, False, None),  # authData
        ("authentication", None, True, False, None),  # authentication
        ("data_id", None, True, False, None),  # dataId
        ("freshness_value", None, True, False, None),  # freshnessValue
        ("message_link", None, True, False, None),  # messageLink
        ("secondary", None, True, False, None),  # secondary
        ("secured_area", None, True, False, None),  # securedArea
    ]

    def __init__(self) -> None:
        """Initialize SecureCommunicationProps."""
        super().__init__()
        self.auth_data: Optional[PositiveInteger] = None
        self.authentication: Optional[PositiveInteger] = None
        self.data_id: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.message_link: Optional[PositiveInteger] = None
        self.secondary: Optional[PositiveInteger] = None
        self.secured_area: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecureCommunicationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationProps":
        """Create SecureCommunicationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecureCommunicationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecureCommunicationProps since parent returns ARObject
        return cast("SecureCommunicationProps", obj)


class SecureCommunicationPropsBuilder:
    """Builder for SecureCommunicationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationProps = SecureCommunicationProps()

    def build(self) -> SecureCommunicationProps:
        """Build and return SecureCommunicationProps object.

        Returns:
            SecureCommunicationProps instance
        """
        # TODO: Add validation
        return self._obj
