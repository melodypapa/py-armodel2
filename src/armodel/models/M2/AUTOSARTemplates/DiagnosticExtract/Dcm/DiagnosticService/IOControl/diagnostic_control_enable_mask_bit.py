"""DiagnosticControlEnableMaskBit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticControlEnableMaskBit(ARObject):
    """AUTOSAR DiagnosticControlEnableMaskBit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_number: Optional[PositiveInteger]
    controlled_datas: list[DiagnosticDataElement]
    def __init__(self) -> None:
        """Initialize DiagnosticControlEnableMaskBit."""
        super().__init__()
        self.bit_number: Optional[PositiveInteger] = None
        self.controlled_datas: list[DiagnosticDataElement] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlEnableMaskBit":
        """Deserialize XML element to DiagnosticControlEnableMaskBit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticControlEnableMaskBit object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bit_number
        child = ARObject._find_child_element(element, "BIT-NUMBER")
        if child is not None:
            bit_number_value = child.text
            obj.bit_number = bit_number_value

        # Parse controlled_datas (list from container "CONTROLLED-DATAS")
        obj.controlled_datas = []
        container = ARObject._find_child_element(element, "CONTROLLED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.controlled_datas.append(child_value)

        return obj



class DiagnosticControlEnableMaskBitBuilder:
    """Builder for DiagnosticControlEnableMaskBit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlEnableMaskBit = DiagnosticControlEnableMaskBit()

    def build(self) -> DiagnosticControlEnableMaskBit:
        """Build and return DiagnosticControlEnableMaskBit object.

        Returns:
            DiagnosticControlEnableMaskBit instance
        """
        # TODO: Add validation
        return self._obj
