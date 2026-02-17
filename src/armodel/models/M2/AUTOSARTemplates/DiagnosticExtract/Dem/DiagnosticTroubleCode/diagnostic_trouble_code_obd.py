"""DiagnosticTroubleCodeObd AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "consider_pto": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # considerPto
        "dtc_props_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTroubleCode,
        ),  # dtcPropsProps
        "event_readiness": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EventObdReadinessGroup,
        ),  # eventReadiness
        "obd_dtc_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # obdDTCValue
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeObd."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.obd_dtc_value: Optional[PositiveInteger] = None


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
