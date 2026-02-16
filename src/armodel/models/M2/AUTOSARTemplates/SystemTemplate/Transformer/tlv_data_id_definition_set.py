"""TlvDataIdDefinitionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
    TlvDataIdDefinition,
)


class TlvDataIdDefinitionSet(ARElement):
    """AUTOSAR TlvDataIdDefinitionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tlv_data_ids", None, False, True, TlvDataIdDefinition),  # tlvDataIds
    ]

    def __init__(self) -> None:
        """Initialize TlvDataIdDefinitionSet."""
        super().__init__()
        self.tlv_data_ids: list[TlvDataIdDefinition] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TlvDataIdDefinitionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinitionSet":
        """Create TlvDataIdDefinitionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TlvDataIdDefinitionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TlvDataIdDefinitionSet since parent returns ARObject
        return cast("TlvDataIdDefinitionSet", obj)


class TlvDataIdDefinitionSetBuilder:
    """Builder for TlvDataIdDefinitionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinitionSet = TlvDataIdDefinitionSet()

    def build(self) -> TlvDataIdDefinitionSet:
        """Build and return TlvDataIdDefinitionSet object.

        Returns:
            TlvDataIdDefinitionSet instance
        """
        # TODO: Add validation
        return self._obj
