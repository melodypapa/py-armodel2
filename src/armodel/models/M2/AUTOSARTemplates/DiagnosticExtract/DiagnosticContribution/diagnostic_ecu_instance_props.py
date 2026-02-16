"""DiagnosticEcuInstanceProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class DiagnosticEcuInstanceProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEcuInstanceProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecu_instances", None, False, True, EcuInstance),  # ecuInstances
        ("obd_support", None, False, False, DiagnosticObdSupportEnum),  # obdSupport
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEcuInstanceProps."""
        super().__init__()
        self.ecu_instances: list[EcuInstance] = []
        self.obd_support: Optional[DiagnosticObdSupportEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEcuInstanceProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuInstanceProps":
        """Create DiagnosticEcuInstanceProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEcuInstanceProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEcuInstanceProps since parent returns ARObject
        return cast("DiagnosticEcuInstanceProps", obj)


class DiagnosticEcuInstancePropsBuilder:
    """Builder for DiagnosticEcuInstanceProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuInstanceProps = DiagnosticEcuInstanceProps()

    def build(self) -> DiagnosticEcuInstanceProps:
        """Build and return DiagnosticEcuInstanceProps object.

        Returns:
            DiagnosticEcuInstanceProps instance
        """
        # TODO: Add validation
        return self._obj
