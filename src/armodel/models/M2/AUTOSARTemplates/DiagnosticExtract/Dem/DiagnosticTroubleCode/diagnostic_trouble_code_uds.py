"""DiagnosticTroubleCodeUds AUTOSAR element."""

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


class DiagnosticTroubleCodeUds(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeUds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consider_pto", None, True, False, None),  # considerPto
        ("dtc_props_props", None, False, False, DiagnosticTroubleCode),  # dtcPropsProps
        ("event_readiness", None, False, False, EventObdReadinessGroup),  # eventReadiness
        ("functional_unit", None, True, False, None),  # functionalUnit
        ("obd_dtc", None, True, False, None),  # obdDtc
        ("severity", None, False, False, DiagnosticUdsSeverityEnum),  # severity
        ("uds_dtc_value", None, True, False, None),  # udsDtcValue
        ("wwh_obd_dtc", None, False, False, DiagnosticWwhObdDtcClassEnum),  # wwhObdDtc
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUds."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.functional_unit: Optional[PositiveInteger] = None
        self.obd_dtc: Optional[PositiveInteger] = None
        self.severity: Optional[DiagnosticUdsSeverityEnum] = None
        self.uds_dtc_value: Optional[PositiveInteger] = None
        self.wwh_obd_dtc: Optional[DiagnosticWwhObdDtcClassEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTroubleCodeUds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeUds":
        """Create DiagnosticTroubleCodeUds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTroubleCodeUds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTroubleCodeUds since parent returns ARObject
        return cast("DiagnosticTroubleCodeUds", obj)


class DiagnosticTroubleCodeUdsBuilder:
    """Builder for DiagnosticTroubleCodeUds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeUds = DiagnosticTroubleCodeUds()

    def build(self) -> DiagnosticTroubleCodeUds:
        """Build and return DiagnosticTroubleCodeUds object.

        Returns:
            DiagnosticTroubleCodeUds instance
        """
        # TODO: Add validation
        return self._obj
