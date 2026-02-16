"""EcucReferenceValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class EcucReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucReferenceValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, False, False, Referrable),  # value
    ]

    def __init__(self) -> None:
        """Initialize EcucReferenceValue."""
        super().__init__()
        self.value: Optional[Referrable] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucReferenceValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucReferenceValue":
        """Create EcucReferenceValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucReferenceValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucReferenceValue since parent returns ARObject
        return cast("EcucReferenceValue", obj)


class EcucReferenceValueBuilder:
    """Builder for EcucReferenceValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucReferenceValue = EcucReferenceValue()

    def build(self) -> EcucReferenceValue:
        """Build and return EcucReferenceValue object.

        Returns:
            EcucReferenceValue instance
        """
        # TODO: Add validation
        return self._obj
