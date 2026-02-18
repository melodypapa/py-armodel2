"""DiagnosticDataElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 982)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class DiagnosticDataElement(Identifiable):
    """AUTOSAR DiagnosticDataElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size: Optional[ArraySizeSemanticsEnum]
    max_number_of: Optional[PositiveInteger]
    scaling_info_size: Optional[PositiveInteger]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize DiagnosticDataElement."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.scaling_info_size: Optional[PositiveInteger] = None
        self.sw_data_def: Optional[SwDataDefProps] = None


class DiagnosticDataElementBuilder:
    """Builder for DiagnosticDataElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataElement = DiagnosticDataElement()

    def build(self) -> DiagnosticDataElement:
        """Build and return DiagnosticDataElement object.

        Returns:
            DiagnosticDataElement instance
        """
        # TODO: Add validation
        return self._obj
