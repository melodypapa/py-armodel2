"""DiagnosticComControl AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticComControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("com_control", None, False, False, DiagnosticComControl),  # comControl
        ("custom_sub", None, True, False, None),  # customSub
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticComControl."""
        super().__init__()
        self.com_control: Optional[DiagnosticComControl] = None
        self.custom_sub: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticComControl to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControl":
        """Create DiagnosticComControl from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticComControl instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticComControl since parent returns ARObject
        return cast("DiagnosticComControl", obj)


class DiagnosticComControlBuilder:
    """Builder for DiagnosticComControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControl = DiagnosticComControl()

    def build(self) -> DiagnosticComControl:
        """Build and return DiagnosticComControl object.

        Returns:
            DiagnosticComControl instance
        """
        # TODO: Add validation
        return self._obj
