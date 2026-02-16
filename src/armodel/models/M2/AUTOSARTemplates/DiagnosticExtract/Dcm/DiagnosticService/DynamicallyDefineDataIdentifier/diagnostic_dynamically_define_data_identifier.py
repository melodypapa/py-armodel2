"""DiagnosticDynamicallyDefineDataIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_dynamic_data_identifier import (
    DiagnosticDynamicDataIdentifier,
)


class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_identifier", None, False, False, DiagnosticDynamicDataIdentifier),  # dataIdentifier
        ("dynamically", None, False, False, any (DiagnosticDynamically)),  # dynamically
        ("max_source", None, True, False, None),  # maxSource
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticDynamicDataIdentifier] = None
        self.dynamically: Optional[Any] = None
        self.max_source: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDynamicallyDefineDataIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """Create DiagnosticDynamicallyDefineDataIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDynamicallyDefineDataIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDynamicallyDefineDataIdentifier since parent returns ARObject
        return cast("DiagnosticDynamicallyDefineDataIdentifier", obj)


class DiagnosticDynamicallyDefineDataIdentifierBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifier = DiagnosticDynamicallyDefineDataIdentifier()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        """Build and return DiagnosticDynamicallyDefineDataIdentifier object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
