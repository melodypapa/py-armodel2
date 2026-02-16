"""SdgClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MetaClassName,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class SdgClass(SdgElementWithGid):
    """AUTOSAR SdgClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attributes", None, False, True, SdgAttribute),  # attributes
        ("caption", None, True, False, None),  # caption
        ("extends_meta", None, True, False, None),  # extendsMeta
        ("sdg_constraints", None, False, True, TraceableText),  # sdgConstraints
    ]

    def __init__(self) -> None:
        """Initialize SdgClass."""
        super().__init__()
        self.attributes: list[SdgAttribute] = []
        self.caption: Optional[Boolean] = None
        self.extends_meta: Optional[MetaClassName] = None
        self.sdg_constraints: list[TraceableText] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgClass":
        """Create SdgClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgClass since parent returns ARObject
        return cast("SdgClass", obj)


class SdgClassBuilder:
    """Builder for SdgClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgClass = SdgClass()

    def build(self) -> SdgClass:
        """Build and return SdgClass object.

        Returns:
            SdgClass instance
        """
        # TODO: Add validation
        return self._obj
