"""SdgAbstractForeignReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MetaClassName,
)


class SdgAbstractForeignReference(SdgElementWithGid):
    """AUTOSAR SdgAbstractForeignReference."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dest_meta_class", None, True, False, None),  # destMetaClass
    ]

    def __init__(self) -> None:
        """Initialize SdgAbstractForeignReference."""
        super().__init__()
        self.dest_meta_class: Optional[MetaClassName] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgAbstractForeignReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAbstractForeignReference":
        """Create SdgAbstractForeignReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgAbstractForeignReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgAbstractForeignReference since parent returns ARObject
        return cast("SdgAbstractForeignReference", obj)


class SdgAbstractForeignReferenceBuilder:
    """Builder for SdgAbstractForeignReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAbstractForeignReference = SdgAbstractForeignReference()

    def build(self) -> SdgAbstractForeignReference:
        """Build and return SdgAbstractForeignReference object.

        Returns:
            SdgAbstractForeignReference instance
        """
        # TODO: Add validation
        return self._obj
