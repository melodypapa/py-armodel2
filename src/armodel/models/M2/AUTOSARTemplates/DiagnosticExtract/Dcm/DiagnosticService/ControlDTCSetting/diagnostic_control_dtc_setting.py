"""DiagnosticControlDTCSetting AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticControlDTCSetting(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticControlDTCSetting."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dtc_setting_class", None, False, False, any (DiagnosticControlDTC)),  # dtcSettingClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticControlDTCSetting."""
        super().__init__()
        self.dtc_setting_class: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticControlDTCSetting to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlDTCSetting":
        """Create DiagnosticControlDTCSetting from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticControlDTCSetting instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticControlDTCSetting since parent returns ARObject
        return cast("DiagnosticControlDTCSetting", obj)


class DiagnosticControlDTCSettingBuilder:
    """Builder for DiagnosticControlDTCSetting."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlDTCSetting = DiagnosticControlDTCSetting()

    def build(self) -> DiagnosticControlDTCSetting:
        """Build and return DiagnosticControlDTCSetting object.

        Returns:
            DiagnosticControlDTCSetting instance
        """
        # TODO: Add validation
        return self._obj
