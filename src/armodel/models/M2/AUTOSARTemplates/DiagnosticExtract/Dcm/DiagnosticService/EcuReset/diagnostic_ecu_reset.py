"""DiagnosticEcuReset AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset.diagnostic_ecu_reset import (
    DiagnosticEcuReset,
)


class DiagnosticEcuReset(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticEcuReset."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_sub", None, True, False, None),  # customSub
        ("ecu_reset_class", None, False, False, DiagnosticEcuReset),  # ecuResetClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEcuReset."""
        super().__init__()
        self.custom_sub: Optional[PositiveInteger] = None
        self.ecu_reset_class: Optional[DiagnosticEcuReset] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEcuReset to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuReset":
        """Create DiagnosticEcuReset from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEcuReset instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEcuReset since parent returns ARObject
        return cast("DiagnosticEcuReset", obj)


class DiagnosticEcuResetBuilder:
    """Builder for DiagnosticEcuReset."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuReset = DiagnosticEcuReset()

    def build(self) -> DiagnosticEcuReset:
        """Build and return DiagnosticEcuReset object.

        Returns:
            DiagnosticEcuReset instance
        """
        # TODO: Add validation
        return self._obj
