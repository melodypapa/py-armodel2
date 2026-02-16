"""EcucInstanceReferenceValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucInstanceReferenceValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, False, False, AtpFeature),  # value
    ]

    def __init__(self) -> None:
        """Initialize EcucInstanceReferenceValue."""
        super().__init__()
        self.value: Optional[AtpFeature] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucInstanceReferenceValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucInstanceReferenceValue":
        """Create EcucInstanceReferenceValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucInstanceReferenceValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucInstanceReferenceValue since parent returns ARObject
        return cast("EcucInstanceReferenceValue", obj)


class EcucInstanceReferenceValueBuilder:
    """Builder for EcucInstanceReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucInstanceReferenceValue = EcucInstanceReferenceValue()

    def build(self) -> EcucInstanceReferenceValue:
        """Build and return EcucInstanceReferenceValue object.

        Returns:
            EcucInstanceReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
