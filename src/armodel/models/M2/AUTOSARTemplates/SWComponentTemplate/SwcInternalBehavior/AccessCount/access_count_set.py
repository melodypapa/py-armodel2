"""AccessCountSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
    AccessCount,
)


class AccessCountSet(ARObject):
    """AUTOSAR AccessCountSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access_counts", None, False, True, AccessCount),  # accessCounts
        ("count_profile", None, True, False, None),  # countProfile
    ]

    def __init__(self) -> None:
        """Initialize AccessCountSet."""
        super().__init__()
        self.access_counts: list[AccessCount] = []
        self.count_profile: Optional[NameToken] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AccessCountSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AccessCountSet":
        """Create AccessCountSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AccessCountSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AccessCountSet since parent returns ARObject
        return cast("AccessCountSet", obj)


class AccessCountSetBuilder:
    """Builder for AccessCountSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCountSet = AccessCountSet()

    def build(self) -> AccessCountSet:
        """Build and return AccessCountSet object.

        Returns:
            AccessCountSet instance
        """
        # TODO: Add validation
        return self._obj
