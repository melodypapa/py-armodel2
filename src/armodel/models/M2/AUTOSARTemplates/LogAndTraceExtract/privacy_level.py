"""PrivacyLevel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PrivacyLevel(ARObject):
    """AUTOSAR PrivacyLevel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_method", None, False, False, CompuMethod),  # compuMethod
        ("privacy_level", None, True, False, None),  # privacyLevel
    ]

    def __init__(self) -> None:
        """Initialize PrivacyLevel."""
        super().__init__()
        self.compu_method: Optional[CompuMethod] = None
        self.privacy_level: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PrivacyLevel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrivacyLevel":
        """Create PrivacyLevel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PrivacyLevel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PrivacyLevel since parent returns ARObject
        return cast("PrivacyLevel", obj)


class PrivacyLevelBuilder:
    """Builder for PrivacyLevel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrivacyLevel = PrivacyLevel()

    def build(self) -> PrivacyLevel:
        """Build and return PrivacyLevel object.

        Returns:
            PrivacyLevel instance
        """
        # TODO: Add validation
        return self._obj
