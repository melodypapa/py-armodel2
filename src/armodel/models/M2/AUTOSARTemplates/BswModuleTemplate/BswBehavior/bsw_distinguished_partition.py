"""BswDistinguishedPartition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class BswDistinguishedPartition(Referrable):
    """AUTOSAR BswDistinguishedPartition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BswDistinguishedPartition."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswDistinguishedPartition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDistinguishedPartition":
        """Create BswDistinguishedPartition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswDistinguishedPartition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswDistinguishedPartition since parent returns ARObject
        return cast("BswDistinguishedPartition", obj)


class BswDistinguishedPartitionBuilder:
    """Builder for BswDistinguishedPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDistinguishedPartition = BswDistinguishedPartition()

    def build(self) -> BswDistinguishedPartition:
        """Build and return BswDistinguishedPartition object.

        Returns:
            BswDistinguishedPartition instance
        """
        # TODO: Add validation
        return self._obj
