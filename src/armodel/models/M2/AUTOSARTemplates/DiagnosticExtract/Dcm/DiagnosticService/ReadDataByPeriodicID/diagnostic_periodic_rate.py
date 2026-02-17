"""DiagnosticPeriodicRate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticPeriodicRate(ARObject):
    """AUTOSAR DiagnosticPeriodicRate."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # period
        "periodic_rate": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticPeriodicRate,
        ),  # periodicRate
    }

    def __init__(self) -> None:
        """Initialize DiagnosticPeriodicRate."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.periodic_rate: Optional[DiagnosticPeriodicRate] = None


class DiagnosticPeriodicRateBuilder:
    """Builder for DiagnosticPeriodicRate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPeriodicRate = DiagnosticPeriodicRate()

    def build(self) -> DiagnosticPeriodicRate:
        """Build and return DiagnosticPeriodicRate object.

        Returns:
            DiagnosticPeriodicRate instance
        """
        # TODO: Add validation
        return self._obj
