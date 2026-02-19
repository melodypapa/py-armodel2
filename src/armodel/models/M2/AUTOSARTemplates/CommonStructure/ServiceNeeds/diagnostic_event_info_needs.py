"""DiagnosticEventInfoNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 760)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventInfoNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    obd_dtc_number: Optional[PositiveInteger]
    uds_dtc_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticEventInfoNeeds."""
        super().__init__()
        self.obd_dtc_number: Optional[PositiveInteger] = None
        self.uds_dtc_number: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventInfoNeeds":
        """Deserialize XML element to DiagnosticEventInfoNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventInfoNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse obd_dtc_number
        child = ARObject._find_child_element(element, "OBD-DTC-NUMBER")
        if child is not None:
            obd_dtc_number_value = child.text
            obj.obd_dtc_number = obd_dtc_number_value

        # Parse uds_dtc_number
        child = ARObject._find_child_element(element, "UDS-DTC-NUMBER")
        if child is not None:
            uds_dtc_number_value = child.text
            obj.uds_dtc_number = uds_dtc_number_value

        return obj



class DiagnosticEventInfoNeedsBuilder:
    """Builder for DiagnosticEventInfoNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventInfoNeeds = DiagnosticEventInfoNeeds()

    def build(self) -> DiagnosticEventInfoNeeds:
        """Build and return DiagnosticEventInfoNeeds object.

        Returns:
            DiagnosticEventInfoNeeds instance
        """
        # TODO: Add validation
        return self._obj
