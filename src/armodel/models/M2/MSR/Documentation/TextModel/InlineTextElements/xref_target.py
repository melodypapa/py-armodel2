"""XrefTarget AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)


class XrefTarget(SingleLanguageReferrable):
    """AUTOSAR XrefTarget."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize XrefTarget."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert XrefTarget to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "XrefTarget":
        """Create XrefTarget from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            XrefTarget instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to XrefTarget since parent returns ARObject
        return cast("XrefTarget", obj)


class XrefTargetBuilder:
    """Builder for XrefTarget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: XrefTarget = XrefTarget()

    def build(self) -> XrefTarget:
        """Build and return XrefTarget object.

        Returns:
            XrefTarget instance
        """
        # TODO: Add validation
        return self._obj
