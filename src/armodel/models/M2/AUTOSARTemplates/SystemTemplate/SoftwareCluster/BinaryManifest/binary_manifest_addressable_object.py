"""BinaryManifestAddressableObject AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    SymbolString,
)


class BinaryManifestAddressableObject(Identifiable):
    """AUTOSAR BinaryManifestAddressableObject."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("address", None, True, False, None),  # address
        ("symbol", None, True, False, None),  # symbol
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestAddressableObject."""
        super().__init__()
        self.address: Optional[Address] = None
        self.symbol: Optional[SymbolString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestAddressableObject to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestAddressableObject":
        """Create BinaryManifestAddressableObject from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestAddressableObject instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestAddressableObject since parent returns ARObject
        return cast("BinaryManifestAddressableObject", obj)


class BinaryManifestAddressableObjectBuilder:
    """Builder for BinaryManifestAddressableObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestAddressableObject = BinaryManifestAddressableObject()

    def build(self) -> BinaryManifestAddressableObject:
        """Build and return BinaryManifestAddressableObject object.

        Returns:
            BinaryManifestAddressableObject instance
        """
        # TODO: Add validation
        return self._obj
