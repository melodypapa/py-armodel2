"""ModeDeclarationGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 113)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 233)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototype(Identifiable):
    """AUTOSAR ModeDeclarationGroupPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_calibration_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwCalibrationAccessEnum,
        ),  # swCalibrationAccess
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototype."""
        super().__init__()
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.type: Optional[ModeDeclarationGroup] = None


class ModeDeclarationGroupPrototypeBuilder:
    """Builder for ModeDeclarationGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroupPrototype = ModeDeclarationGroupPrototype()

    def build(self) -> ModeDeclarationGroupPrototype:
        """Build and return ModeDeclarationGroupPrototype object.

        Returns:
            ModeDeclarationGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj
