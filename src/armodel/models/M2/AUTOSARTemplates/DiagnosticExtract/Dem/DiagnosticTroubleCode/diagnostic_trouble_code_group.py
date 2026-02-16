"""DiagnosticTroubleCodeGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dtcs", None, False, True, DiagnosticTroubleCode),  # dtcs
        ("group_number", None, True, False, None),  # groupNumber
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeGroup."""
        super().__init__()
        self.dtcs: list[DiagnosticTroubleCode] = []
        self.group_number: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTroubleCodeGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeGroup":
        """Create DiagnosticTroubleCodeGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTroubleCodeGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTroubleCodeGroup since parent returns ARObject
        return cast("DiagnosticTroubleCodeGroup", obj)


class DiagnosticTroubleCodeGroupBuilder:
    """Builder for DiagnosticTroubleCodeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeGroup = DiagnosticTroubleCodeGroup()

    def build(self) -> DiagnosticTroubleCodeGroup:
        """Build and return DiagnosticTroubleCodeGroup object.

        Returns:
            DiagnosticTroubleCodeGroup instance
        """
        # TODO: Add validation
        return self._obj
