"""DiagnosticComControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 108)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticComControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "com_control": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="DiagnosticComControl",
        ),  # comControl
        "custom_sub": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # customSub
    }

    def __init__(self) -> None:
        """Initialize DiagnosticComControl."""
        super().__init__()
        self.com_control: Optional[DiagnosticComControl] = None
        self.custom_sub: Optional[PositiveInteger] = None


class DiagnosticComControlBuilder:
    """Builder for DiagnosticComControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControl = DiagnosticComControl()

    def build(self) -> DiagnosticComControl:
        """Build and return DiagnosticComControl object.

        Returns:
            DiagnosticComControl instance
        """
        # TODO: Add validation
        return self._obj
