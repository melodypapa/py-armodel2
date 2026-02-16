"""DiagnosticIumprGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr_group import (
    DiagnosticIumprGroup,
)


class DiagnosticIumprGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("iumprs", None, False, True, DiagnosticIumpr),  # iumprs
        ("iumpr_group", None, False, False, DiagnosticIumprGroup),  # iumprGroup
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroup."""
        super().__init__()
        self.iumprs: list[DiagnosticIumpr] = []
        self.iumpr_group: Optional[DiagnosticIumprGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIumprGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprGroup":
        """Create DiagnosticIumprGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIumprGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIumprGroup since parent returns ARObject
        return cast("DiagnosticIumprGroup", obj)


class DiagnosticIumprGroupBuilder:
    """Builder for DiagnosticIumprGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprGroup = DiagnosticIumprGroup()

    def build(self) -> DiagnosticIumprGroup:
        """Build and return DiagnosticIumprGroup object.

        Returns:
            DiagnosticIumprGroup instance
        """
        # TODO: Add validation
        return self._obj
