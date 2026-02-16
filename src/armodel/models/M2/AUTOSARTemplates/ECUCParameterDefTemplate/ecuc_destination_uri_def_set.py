"""EcucDestinationUriDefSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucDestinationUriDefSet(ARElement):
    """AUTOSAR EcucDestinationUriDefSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_uri_defs", None, False, True, EcucDestinationUriDef),  # destinationUriDefs
    ]

    def __init__(self) -> None:
        """Initialize EcucDestinationUriDefSet."""
        super().__init__()
        self.destination_uri_defs: list[EcucDestinationUriDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucDestinationUriDefSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDefSet":
        """Create EcucDestinationUriDefSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucDestinationUriDefSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucDestinationUriDefSet since parent returns ARObject
        return cast("EcucDestinationUriDefSet", obj)


class EcucDestinationUriDefSetBuilder:
    """Builder for EcucDestinationUriDefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDefSet = EcucDestinationUriDefSet()

    def build(self) -> EcucDestinationUriDefSet:
        """Build and return EcucDestinationUriDefSet object.

        Returns:
            EcucDestinationUriDefSet instance
        """
        # TODO: Add validation
        return self._obj
