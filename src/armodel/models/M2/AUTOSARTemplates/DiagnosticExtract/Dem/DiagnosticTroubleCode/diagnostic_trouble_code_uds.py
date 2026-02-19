"""DiagnosticTroubleCodeUds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticUdsSeverityEnum,
    DiagnosticWwhObdDtcClassEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consider_pto: Optional[Boolean]
    dtc_props_props: Optional[DiagnosticTroubleCode]
    event_readiness: Optional[EventObdReadinessGroup]
    functional_unit: Optional[PositiveInteger]
    obd_dtc: Optional[PositiveInteger]
    severity: Optional[DiagnosticUdsSeverityEnum]
    uds_dtc_value: Optional[PositiveInteger]
    wwh_obd_dtc: Optional[DiagnosticWwhObdDtcClassEnum]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeUds":
        """Deserialize XML element to DiagnosticTroubleCodeUds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeUds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse consider_pto
        child = ARObject._find_child_element(element, "CONSIDER-PTO")
        if child is not None:
            consider_pto_value = child.text
            obj.consider_pto = consider_pto_value

        # Parse dtc_props_props
        child = ARObject._find_child_element(element, "DTC-PROPS-PROPS")
        if child is not None:
            dtc_props_props_value = ARObject._deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.dtc_props_props = dtc_props_props_value

        # Parse event_readiness
        child = ARObject._find_child_element(element, "EVENT-READINESS")
        if child is not None:
            event_readiness_value = ARObject._deserialize_by_tag(child, "EventObdReadinessGroup")
            obj.event_readiness = event_readiness_value

        # Parse functional_unit
        child = ARObject._find_child_element(element, "FUNCTIONAL-UNIT")
        if child is not None:
            functional_unit_value = child.text
            obj.functional_unit = functional_unit_value

        # Parse obd_dtc
        child = ARObject._find_child_element(element, "OBD-DTC")
        if child is not None:
            obd_dtc_value = child.text
            obj.obd_dtc = obd_dtc_value

        # Parse severity
        child = ARObject._find_child_element(element, "SEVERITY")
        if child is not None:
            severity_value = child.text
            obj.severity = severity_value

        # Parse uds_dtc_value
        child = ARObject._find_child_element(element, "UDS-DTC-VALUE")
        if child is not None:
            uds_dtc_value_value = child.text
            obj.uds_dtc_value = uds_dtc_value_value

        # Parse wwh_obd_dtc
        child = ARObject._find_child_element(element, "WWH-OBD-DTC")
        if child is not None:
            wwh_obd_dtc_value = child.text
            obj.wwh_obd_dtc = wwh_obd_dtc_value

        return obj



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
