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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataElement":
        """Deserialize XML element to DiagnosticDataElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse array_size
        child = ARObject._find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = child.text
            obj.array_size = array_size_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse scaling_info_size
        child = ARObject._find_child_element(element, "SCALING-INFO-SIZE")
        if child is not None:
            scaling_info_size_value = child.text
            obj.scaling_info_size = scaling_info_size_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



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
