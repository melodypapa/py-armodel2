"""SecureCommunicationFreshnessProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SecureCommunicationFreshnessProps(Identifiable):
    """AUTOSAR SecureCommunicationFreshnessProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("freshness", None, True, False, None),  # freshness
        ("freshness_value", None, True, False, None),  # freshnessValue
        ("use_freshness", None, True, False, None),  # useFreshness
    ]

    def __init__(self) -> None:
        """Initialize SecureCommunicationFreshnessProps."""
        super().__init__()
        self.freshness: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.use_freshness: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecureCommunicationFreshnessProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationFreshnessProps":
        """Create SecureCommunicationFreshnessProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecureCommunicationFreshnessProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecureCommunicationFreshnessProps since parent returns ARObject
        return cast("SecureCommunicationFreshnessProps", obj)


class SecureCommunicationFreshnessPropsBuilder:
    """Builder for SecureCommunicationFreshnessProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationFreshnessProps = SecureCommunicationFreshnessProps()

    def build(self) -> SecureCommunicationFreshnessProps:
        """Build and return SecureCommunicationFreshnessProps object.

        Returns:
            SecureCommunicationFreshnessProps instance
        """
        # TODO: Add validation
        return self._obj
