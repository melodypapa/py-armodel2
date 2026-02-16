"""EcucValueCollection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class EcucValueCollection(ARElement):
    """AUTOSAR EcucValueCollection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecuc_values", None, False, True, any (EcucModule)),  # ecucValues
        ("ecu_extract", None, False, False, System),  # ecuExtract
    ]

    def __init__(self) -> None:
        """Initialize EcucValueCollection."""
        super().__init__()
        self.ecuc_values: list[Any] = []
        self.ecu_extract: Optional[System] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucValueCollection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValueCollection":
        """Create EcucValueCollection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucValueCollection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucValueCollection since parent returns ARObject
        return cast("EcucValueCollection", obj)


class EcucValueCollectionBuilder:
    """Builder for EcucValueCollection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValueCollection = EcucValueCollection()

    def build(self) -> EcucValueCollection:
        """Build and return EcucValueCollection object.

        Returns:
            EcucValueCollection instance
        """
        # TODO: Add validation
        return self._obj
