"""EcuPartition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcuPartition(Identifiable):
    """AUTOSAR EcuPartition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("exec_in_user", None, True, False, None),  # execInUser
    ]

    def __init__(self) -> None:
        """Initialize EcuPartition."""
        super().__init__()
        self.exec_in_user: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcuPartition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuPartition":
        """Create EcuPartition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcuPartition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcuPartition since parent returns ARObject
        return cast("EcuPartition", obj)


class EcuPartitionBuilder:
    """Builder for EcuPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuPartition = EcuPartition()

    def build(self) -> EcuPartition:
        """Build and return EcuPartition object.

        Returns:
            EcuPartition instance
        """
        # TODO: Add validation
        return self._obj
