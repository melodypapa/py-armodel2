"""SdgReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgReference(SdgAttribute):
    """AUTOSAR SdgReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dest_sdg", None, False, False, SdgClass),  # destSdg
    ]

    def __init__(self) -> None:
        """Initialize SdgReference."""
        super().__init__()
        self.dest_sdg: Optional[SdgClass] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgReference":
        """Create SdgReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgReference since parent returns ARObject
        return cast("SdgReference", obj)


class SdgReferenceBuilder:
    """Builder for SdgReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgReference = SdgReference()

    def build(self) -> SdgReference:
        """Build and return SdgReference object.

        Returns:
            SdgReference instance
        """
        # TODO: Add validation
        return self._obj
