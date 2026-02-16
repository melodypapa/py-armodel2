"""DiagnosticReadDataByPeriodicIDClass AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate import (
    DiagnosticPeriodicRate,
)


class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByPeriodicIDClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_periodic_did": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxPeriodicDid
        "periodic_rates": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticPeriodicRate,
        ),  # periodicRates
        "scheduler_max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # schedulerMax
    }

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicIDClass."""
        super().__init__()
        self.max_periodic_did: Optional[PositiveInteger] = None
        self.periodic_rates: list[DiagnosticPeriodicRate] = []
        self.scheduler_max: Optional[PositiveInteger] = None


class DiagnosticReadDataByPeriodicIDClassBuilder:
    """Builder for DiagnosticReadDataByPeriodicIDClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicIDClass = DiagnosticReadDataByPeriodicIDClass()

    def build(self) -> DiagnosticReadDataByPeriodicIDClass:
        """Build and return DiagnosticReadDataByPeriodicIDClass object.

        Returns:
            DiagnosticReadDataByPeriodicIDClass instance
        """
        # TODO: Add validation
        return self._obj
