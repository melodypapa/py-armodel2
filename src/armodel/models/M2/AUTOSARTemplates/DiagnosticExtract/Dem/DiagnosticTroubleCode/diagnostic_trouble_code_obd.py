"""DiagnosticTroubleCodeObd AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)


class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeObd."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consider_pto", None, True, False, None),  # considerPto
        ("dtc_props_props", None, False, False, DiagnosticTroubleCode),  # dtcPropsProps
        ("event_readiness", None, False, False, EventObdReadinessGroup),  # eventReadiness
        ("obd_dtc_value", None, True, False, None),  # obdDTCValue
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeObd."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.obd_dtc_value: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTroubleCodeObd to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeObd":
        """Create DiagnosticTroubleCodeObd from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTroubleCodeObd instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTroubleCodeObd since parent returns ARObject
        return cast("DiagnosticTroubleCodeObd", obj)


class DiagnosticTroubleCodeObdBuilder:
    """Builder for DiagnosticTroubleCodeObd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeObd = DiagnosticTroubleCodeObd()

    def build(self) -> DiagnosticTroubleCodeObd:
        """Build and return DiagnosticTroubleCodeObd object.

        Returns:
            DiagnosticTroubleCodeObd instance
        """
        # TODO: Add validation
        return self._obj
