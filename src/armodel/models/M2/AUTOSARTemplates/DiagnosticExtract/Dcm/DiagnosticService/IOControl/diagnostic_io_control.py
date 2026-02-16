"""DiagnosticIOControl AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.IOControl.diagnostic_io_control import (
    DiagnosticIOControl,
)


class DiagnosticIOControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticIOControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("control_enables", None, False, True, any (DiagnosticControl)),  # controlEnables
        ("data_identifier_identifier", None, False, False, DiagnosticDataIdentifier),  # dataIdentifierIdentifier
        ("freeze_current", None, True, False, None),  # freezeCurrent
        ("io_control_class", None, False, False, DiagnosticIOControl),  # ioControlClass
        ("reset_to_default", None, True, False, None),  # resetToDefault
        ("short_term", None, True, False, None),  # shortTerm
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIOControl."""
        super().__init__()
        self.control_enables: list[Any] = []
        self.data_identifier_identifier: Optional[DiagnosticDataIdentifier] = None
        self.freeze_current: Optional[Boolean] = None
        self.io_control_class: Optional[DiagnosticIOControl] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIOControl to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIOControl":
        """Create DiagnosticIOControl from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIOControl instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIOControl since parent returns ARObject
        return cast("DiagnosticIOControl", obj)


class DiagnosticIOControlBuilder:
    """Builder for DiagnosticIOControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIOControl = DiagnosticIOControl()

    def build(self) -> DiagnosticIOControl:
        """Build and return DiagnosticIOControl object.

        Returns:
            DiagnosticIOControl instance
        """
        # TODO: Add validation
        return self._obj
