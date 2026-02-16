"""SdgForeignReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_foreign_reference import (
    SdgAbstractForeignReference,
)


class SdgForeignReference(SdgAbstractForeignReference):
    """AUTOSAR SdgForeignReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SdgForeignReference."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgForeignReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgForeignReference":
        """Create SdgForeignReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgForeignReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgForeignReference since parent returns ARObject
        return cast("SdgForeignReference", obj)


class SdgForeignReferenceBuilder:
    """Builder for SdgForeignReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgForeignReference = SdgForeignReference()

    def build(self) -> SdgForeignReference:
        """Build and return SdgForeignReference object.

        Returns:
            SdgForeignReference instance
        """
        # TODO: Add validation
        return self._obj
