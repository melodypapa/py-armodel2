"""SecureCommunicationPropsSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class SecureCommunicationPropsSet(FibexElement):
    """AUTOSAR SecureCommunicationPropsSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentications", None, False, True, any (SecureCommunication)),  # authentications
        ("freshness_propses", None, False, True, any (SecureCommunication)),  # freshnessPropses
    ]

    def __init__(self) -> None:
        """Initialize SecureCommunicationPropsSet."""
        super().__init__()
        self.authentications: list[Any] = []
        self.freshness_propses: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecureCommunicationPropsSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationPropsSet":
        """Create SecureCommunicationPropsSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecureCommunicationPropsSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecureCommunicationPropsSet since parent returns ARObject
        return cast("SecureCommunicationPropsSet", obj)


class SecureCommunicationPropsSetBuilder:
    """Builder for SecureCommunicationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationPropsSet = SecureCommunicationPropsSet()

    def build(self) -> SecureCommunicationPropsSet:
        """Build and return SecureCommunicationPropsSet object.

        Returns:
            SecureCommunicationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
