"""AliasNameSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_assignment import (
    AliasNameAssignment,
)


class AliasNameSet(ARElement):
    """AUTOSAR AliasNameSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alias_names", None, False, True, AliasNameAssignment),  # aliasNames
    ]

    def __init__(self) -> None:
        """Initialize AliasNameSet."""
        super().__init__()
        self.alias_names: list[AliasNameAssignment] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AliasNameSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameSet":
        """Create AliasNameSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AliasNameSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AliasNameSet since parent returns ARObject
        return cast("AliasNameSet", obj)


class AliasNameSetBuilder:
    """Builder for AliasNameSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameSet = AliasNameSet()

    def build(self) -> AliasNameSet:
        """Build and return AliasNameSet object.

        Returns:
            AliasNameSet instance
        """
        # TODO: Add validation
        return self._obj
