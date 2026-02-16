"""DiagnosticIumprDenominatorGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprDenominatorGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprDenominatorGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("iumprs", None, False, True, DiagnosticIumpr),  # iumprs
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIumprDenominatorGroup."""
        super().__init__()
        self.iumprs: list[DiagnosticIumpr] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIumprDenominatorGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprDenominatorGroup":
        """Create DiagnosticIumprDenominatorGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIumprDenominatorGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIumprDenominatorGroup since parent returns ARObject
        return cast("DiagnosticIumprDenominatorGroup", obj)


class DiagnosticIumprDenominatorGroupBuilder:
    """Builder for DiagnosticIumprDenominatorGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprDenominatorGroup = DiagnosticIumprDenominatorGroup()

    def build(self) -> DiagnosticIumprDenominatorGroup:
        """Build and return DiagnosticIumprDenominatorGroup object.

        Returns:
            DiagnosticIumprDenominatorGroup instance
        """
        # TODO: Add validation
        return self._obj
