"""SpecElementReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SpecElementReference(Identifiable):
    """AUTOSAR SpecElementReference."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alternative", None, True, False, None),  # alternative
    ]

    def __init__(self) -> None:
        """Initialize SpecElementReference."""
        super().__init__()
        self.alternative: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SpecElementReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecElementReference":
        """Create SpecElementReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SpecElementReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SpecElementReference since parent returns ARObject
        return cast("SpecElementReference", obj)


class SpecElementReferenceBuilder:
    """Builder for SpecElementReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementReference = SpecElementReference()

    def build(self) -> SpecElementReference:
        """Build and return SpecElementReference object.

        Returns:
            SpecElementReference instance
        """
        # TODO: Add validation
        return self._obj
