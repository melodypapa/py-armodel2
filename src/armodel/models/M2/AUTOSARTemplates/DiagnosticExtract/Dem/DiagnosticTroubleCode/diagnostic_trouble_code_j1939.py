"""DiagnosticTroubleCodeJ1939 AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)


class DiagnosticTroubleCodeJ1939(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeJ1939."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dtc_props_props", None, False, False, DiagnosticTroubleCode),  # dtcPropsProps
        ("fmi", None, True, False, None),  # fmi
        ("kind", None, False, False, DiagnosticTroubleCode),  # kind
        ("node", None, False, False, DiagnosticJ1939Node),  # node
        ("spn", None, False, False, DiagnosticJ1939Spn),  # spn
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeJ1939."""
        super().__init__()
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.fmi: Optional[PositiveInteger] = None
        self.kind: Optional[DiagnosticTroubleCode] = None
        self.node: Optional[DiagnosticJ1939Node] = None
        self.spn: Optional[DiagnosticJ1939Spn] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTroubleCodeJ1939 to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeJ1939":
        """Create DiagnosticTroubleCodeJ1939 from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTroubleCodeJ1939 instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTroubleCodeJ1939 since parent returns ARObject
        return cast("DiagnosticTroubleCodeJ1939", obj)


class DiagnosticTroubleCodeJ1939Builder:
    """Builder for DiagnosticTroubleCodeJ1939."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeJ1939 = DiagnosticTroubleCodeJ1939()

    def build(self) -> DiagnosticTroubleCodeJ1939:
        """Build and return DiagnosticTroubleCodeJ1939 object.

        Returns:
            DiagnosticTroubleCodeJ1939 instance
        """
        # TODO: Add validation
        return self._obj
