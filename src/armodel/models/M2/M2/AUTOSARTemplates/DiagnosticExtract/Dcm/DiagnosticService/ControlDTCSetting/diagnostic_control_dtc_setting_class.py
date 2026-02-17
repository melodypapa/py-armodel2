"""DiagnosticControlDTCSettingClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ControlDTCSetting.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticControlDTCSettingClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticControlDTCSettingClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "control_option": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # controlOption
    }

    def __init__(self) -> None:
        """Initialize DiagnosticControlDTCSettingClass."""
        super().__init__()
        self.control_option: Optional[Boolean] = None


class DiagnosticControlDTCSettingClassBuilder:
    """Builder for DiagnosticControlDTCSettingClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlDTCSettingClass = DiagnosticControlDTCSettingClass()

    def build(self) -> DiagnosticControlDTCSettingClass:
        """Build and return DiagnosticControlDTCSettingClass object.

        Returns:
            DiagnosticControlDTCSettingClass instance
        """
        # TODO: Add validation
        return self._obj
