"""SdgTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgTailoring(RestrictionWithSeverity):
    """AUTOSAR SdgTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sdg_class", None, False, False, SdgClass),  # sdgClass
    ]

    def __init__(self) -> None:
        """Initialize SdgTailoring."""
        super().__init__()
        self.sdg_class: Optional[SdgClass] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgTailoring":
        """Create SdgTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgTailoring since parent returns ARObject
        return cast("SdgTailoring", obj)


class SdgTailoringBuilder:
    """Builder for SdgTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgTailoring = SdgTailoring()

    def build(self) -> SdgTailoring:
        """Build and return SdgTailoring object.

        Returns:
            SdgTailoring instance
        """
        # TODO: Add validation
        return self._obj
