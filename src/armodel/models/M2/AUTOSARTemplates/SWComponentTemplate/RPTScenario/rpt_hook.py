"""RptHook AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class RptHook(ARObject):
    """AUTOSAR RptHook."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("code_label", None, True, False, None),  # codeLabel
        ("mcd_identifier", None, True, False, None),  # mcdIdentifier
        ("rpt_ar_hook", None, False, False, AtpFeature),  # rptArHook
        ("sdgs", None, False, True, Sdg),  # sdgs
    ]

    def __init__(self) -> None:
        """Initialize RptHook."""
        super().__init__()
        self.code_label: Optional[CIdentifier] = None
        self.mcd_identifier: Optional[NameToken] = None
        self.rpt_ar_hook: Optional[AtpFeature] = None
        self.sdgs: list[Sdg] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptHook to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptHook":
        """Create RptHook from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptHook instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptHook since parent returns ARObject
        return cast("RptHook", obj)


class RptHookBuilder:
    """Builder for RptHook."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptHook = RptHook()

    def build(self) -> RptHook:
        """Build and return RptHook object.

        Returns:
            RptHook instance
        """
        # TODO: Add validation
        return self._obj
