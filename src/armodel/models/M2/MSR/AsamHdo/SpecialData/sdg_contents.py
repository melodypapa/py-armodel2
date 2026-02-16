"""SdgContents AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class SdgContents(ARObject):
    """AUTOSAR SdgContents."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sd", None, False, False, Sd),  # sd
        ("sdf", None, False, False, Sdf),  # sdf
        ("sdg", None, False, False, Sdg),  # sdg
        ("sdx", None, False, False, Referrable),  # sdx
        ("sdxf", None, False, False, Referrable),  # sdxf
    ]

    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx: Optional[Referrable] = None
        self.sdxf: Optional[Referrable] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgContents to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgContents":
        """Create SdgContents from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgContents instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgContents since parent returns ARObject
        return cast("SdgContents", obj)


class SdgContentsBuilder:
    """Builder for SdgContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgContents = SdgContents()

    def build(self) -> SdgContents:
        """Build and return SdgContents object.

        Returns:
            SdgContents instance
        """
        # TODO: Add validation
        return self._obj
