"""DiagnosticControlEnableMaskBit AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticControlEnableMaskBit(ARObject):
    """AUTOSAR DiagnosticControlEnableMaskBit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bit_number", None, True, False, None),  # bitNumber
        ("controlled_datas", None, False, True, DiagnosticDataElement),  # controlledDatas
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticControlEnableMaskBit."""
        super().__init__()
        self.bit_number: Optional[PositiveInteger] = None
        self.controlled_datas: list[DiagnosticDataElement] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticControlEnableMaskBit to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlEnableMaskBit":
        """Create DiagnosticControlEnableMaskBit from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticControlEnableMaskBit instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticControlEnableMaskBit since parent returns ARObject
        return cast("DiagnosticControlEnableMaskBit", obj)


class DiagnosticControlEnableMaskBitBuilder:
    """Builder for DiagnosticControlEnableMaskBit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlEnableMaskBit = DiagnosticControlEnableMaskBit()

    def build(self) -> DiagnosticControlEnableMaskBit:
        """Build and return DiagnosticControlEnableMaskBit object.

        Returns:
            DiagnosticControlEnableMaskBit instance
        """
        # TODO: Add validation
        return self._obj
