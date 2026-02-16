"""DiagnosticPowertrainFreezeFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticPowertrainFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticPowertrainFreezeFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("pids", None, False, True, DiagnosticParameter),  # pids
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticPowertrainFreezeFrame."""
        super().__init__()
        self.pids: list[DiagnosticParameter] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticPowertrainFreezeFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticPowertrainFreezeFrame":
        """Create DiagnosticPowertrainFreezeFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticPowertrainFreezeFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticPowertrainFreezeFrame since parent returns ARObject
        return cast("DiagnosticPowertrainFreezeFrame", obj)


class DiagnosticPowertrainFreezeFrameBuilder:
    """Builder for DiagnosticPowertrainFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPowertrainFreezeFrame = DiagnosticPowertrainFreezeFrame()

    def build(self) -> DiagnosticPowertrainFreezeFrame:
        """Build and return DiagnosticPowertrainFreezeFrame object.

        Returns:
            DiagnosticPowertrainFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
