"""DiagnosticTroubleCodeProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aging: Optional[DiagnosticAging]
    diagnostic_memory: Optional[Any]
    extended_datas: list[DiagnosticExtendedDataRecord]
    freeze_frames: list[DiagnosticFreezeFrame]
    immediate_nv: Optional[Boolean]
    legislated: Optional[DiagnosticDataIdentifier]
    max_number: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    significance: Optional[DiagnosticSignificanceEnum]
    snapshot: Optional[DiagnosticDataIdentifier]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeProps":
        """Deserialize XML element to DiagnosticTroubleCodeProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse aging
        child = ARObject._find_child_element(element, "AGING")
        if child is not None:
            aging_value = ARObject._deserialize_by_tag(child, "DiagnosticAging")
            obj.aging = aging_value

        # Parse diagnostic_memory
        child = ARObject._find_child_element(element, "DIAGNOSTIC-MEMORY")
        if child is not None:
            diagnostic_memory_value = child.text
            obj.diagnostic_memory = diagnostic_memory_value

        # Parse extended_datas (list)
        obj.extended_datas = []
        for child in ARObject._find_all_child_elements(element, "EXTENDED-DATAS"):
            extended_datas_value = ARObject._deserialize_by_tag(child, "DiagnosticExtendedDataRecord")
            obj.extended_datas.append(extended_datas_value)

        # Parse freeze_frames (list)
        obj.freeze_frames = []
        for child in ARObject._find_all_child_elements(element, "FREEZE-FRAMES"):
            freeze_frames_value = ARObject._deserialize_by_tag(child, "DiagnosticFreezeFrame")
            obj.freeze_frames.append(freeze_frames_value)

        # Parse immediate_nv
        child = ARObject._find_child_element(element, "IMMEDIATE-NV")
        if child is not None:
            immediate_nv_value = child.text
            obj.immediate_nv = immediate_nv_value

        # Parse legislated
        child = ARObject._find_child_element(element, "LEGISLATED")
        if child is not None:
            legislated_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.legislated = legislated_value

        # Parse max_number
        child = ARObject._find_child_element(element, "MAX-NUMBER")
        if child is not None:
            max_number_value = child.text
            obj.max_number = max_number_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse significance
        child = ARObject._find_child_element(element, "SIGNIFICANCE")
        if child is not None:
            significance_value = child.text
            obj.significance = significance_value

        # Parse snapshot
        child = ARObject._find_child_element(element, "SNAPSHOT")
        if child is not None:
            snapshot_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.snapshot = snapshot_value

        return obj



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
