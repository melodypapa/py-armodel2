"""DiagnosticTroubleCodeObd AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)


class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeObd."""

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
    obd_dtc_value: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeObd."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.obd_dtc_value: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeObd":
        """Deserialize XML element to DiagnosticTroubleCodeObd object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeObd object
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

        # Parse obd_dtc_value
        child = ARObject._find_child_element(element, "OBD-DTC-VALUE")
        if child is not None:
            obd_dtc_value_value = child.text
            obj.obd_dtc_value = obd_dtc_value_value

        return obj



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
