"""DiagEventDebounceTimeBased AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 260)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 198)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 758)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceTimeBased."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    time_based_fdc: Optional[TimeValue]
    time_failed: Optional[TimeValue]
    time_passed: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DiagEventDebounceTimeBased."""
        super().__init__()
        self.time_based_fdc: Optional[TimeValue] = None
        self.time_failed: Optional[TimeValue] = None
        self.time_passed: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceTimeBased":
        """Deserialize XML element to DiagEventDebounceTimeBased object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagEventDebounceTimeBased object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse time_based_fdc
        child = ARObject._find_child_element(element, "TIME-BASED-FDC")
        if child is not None:
            time_based_fdc_value = child.text
            obj.time_based_fdc = time_based_fdc_value

        # Parse time_failed
        child = ARObject._find_child_element(element, "TIME-FAILED")
        if child is not None:
            time_failed_value = child.text
            obj.time_failed = time_failed_value

        # Parse time_passed
        child = ARObject._find_child_element(element, "TIME-PASSED")
        if child is not None:
            time_passed_value = child.text
            obj.time_passed = time_passed_value

        return obj



class DiagEventDebounceTimeBasedBuilder:
    """Builder for DiagEventDebounceTimeBased."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceTimeBased = DiagEventDebounceTimeBased()

    def build(self) -> DiagEventDebounceTimeBased:
        """Build and return DiagEventDebounceTimeBased object.

        Returns:
            DiagEventDebounceTimeBased instance
        """
        # TODO: Add validation
        return self._obj
