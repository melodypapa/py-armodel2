"""DiagnosticAuthTransmitCertificateEvaluation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class DiagnosticAuthTransmitCertificateEvaluation(Identifiable):
    """AUTOSAR DiagnosticAuthTransmitCertificateEvaluation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("evaluation_id", None, True, False, None),  # evaluationId
        ("function", None, True, False, None),  # function
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateEvaluation."""
        super().__init__()
        self.evaluation_id: Optional[PositiveInteger] = None
        self.function: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthTransmitCertificateEvaluation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificateEvaluation":
        """Create DiagnosticAuthTransmitCertificateEvaluation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthTransmitCertificateEvaluation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthTransmitCertificateEvaluation since parent returns ARObject
        return cast("DiagnosticAuthTransmitCertificateEvaluation", obj)


class DiagnosticAuthTransmitCertificateEvaluationBuilder:
    """Builder for DiagnosticAuthTransmitCertificateEvaluation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificateEvaluation = DiagnosticAuthTransmitCertificateEvaluation()

    def build(self) -> DiagnosticAuthTransmitCertificateEvaluation:
        """Build and return DiagnosticAuthTransmitCertificateEvaluation object.

        Returns:
            DiagnosticAuthTransmitCertificateEvaluation instance
        """
        # TODO: Add validation
        return self._obj
