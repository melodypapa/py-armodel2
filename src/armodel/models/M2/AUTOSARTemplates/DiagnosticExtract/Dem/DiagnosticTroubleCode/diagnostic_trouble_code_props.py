"""DiagnosticTroubleCodeProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticSignificanceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticAging.diagnostic_aging import (
    DiagnosticAging,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticExtendedDataRecord.diagnostic_extended_data_record import (
    DiagnosticExtendedDataRecord,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame.diagnostic_freeze_frame import (
    DiagnosticFreezeFrame,
)


class DiagnosticTroubleCodeProps(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "aging": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticAging,
        ),  # aging
        "diagnostic_memory": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticMemory),
        ),  # diagnosticMemory
        "extended_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticExtendedDataRecord,
        ),  # extendedDatas
        "freeze_frames": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticFreezeFrame,
        ),  # freezeFrames
        "immediate_nv": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # immediateNv
        "legislated": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticDataIdentifier,
        ),  # legislated
        "max_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumber
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "significance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticSignificanceEnum,
        ),  # significance
        "snapshot": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticDataIdentifier,
        ),  # snapshot
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeProps."""
        super().__init__()
        self.aging: Optional[DiagnosticAging] = None
        self.diagnostic_memory: Optional[Any] = None
        self.extended_datas: list[DiagnosticExtendedDataRecord] = []
        self.freeze_frames: list[DiagnosticFreezeFrame] = []
        self.immediate_nv: Optional[Boolean] = None
        self.legislated: Optional[DiagnosticDataIdentifier] = None
        self.max_number: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.significance: Optional[DiagnosticSignificanceEnum] = None
        self.snapshot: Optional[DiagnosticDataIdentifier] = None


class DiagnosticTroubleCodePropsBuilder:
    """Builder for DiagnosticTroubleCodeProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeProps = DiagnosticTroubleCodeProps()

    def build(self) -> DiagnosticTroubleCodeProps:
        """Build and return DiagnosticTroubleCodeProps object.

        Returns:
            DiagnosticTroubleCodeProps instance
        """
        # TODO: Add validation
        return self._obj
