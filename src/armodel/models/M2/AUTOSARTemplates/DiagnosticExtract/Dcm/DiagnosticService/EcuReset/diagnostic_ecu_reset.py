"""DiagnosticEcuReset AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset.diagnostic_ecu_reset import (
    DiagnosticEcuReset,
)


class DiagnosticEcuReset(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticEcuReset."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "custom_sub": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # customSub
        "ecu_reset_class": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEcuReset,
        ),  # ecuResetClass
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEcuReset."""
        super().__init__()
        self.custom_sub: Optional[PositiveInteger] = None
        self.ecu_reset_class: Optional[DiagnosticEcuReset] = None


class DiagnosticEcuResetBuilder:
    """Builder for DiagnosticEcuReset."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuReset = DiagnosticEcuReset()

    def build(self) -> DiagnosticEcuReset:
        """Build and return DiagnosticEcuReset object.

        Returns:
            DiagnosticEcuReset instance
        """
        # TODO: Add validation
        return self._obj
