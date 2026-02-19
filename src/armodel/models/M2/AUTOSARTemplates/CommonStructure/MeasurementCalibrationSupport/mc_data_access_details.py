"""McDataAccessDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )



class McDataAccessDetails(ARObject):
    """AUTOSAR McDataAccessDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_refs: list[RTEEvent]
    variable_accesses: list[VariableAccess]
    def __init__(self) -> None:
        """Initialize McDataAccessDetails."""
        super().__init__()
        self.rte_event_refs: list[RTEEvent] = []
        self.variable_accesses: list[VariableAccess] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataAccessDetails":
        """Deserialize XML element to McDataAccessDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McDataAccessDetails object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rte_event_refs (list)
        obj.rte_event_refs = []
        for child in ARObject._find_all_child_elements(element, "RTE-EVENT-REFS"):
            rte_event_refs_value = ARObject._deserialize_by_tag(child, "RTEEvent")
            obj.rte_event_refs.append(rte_event_refs_value)

        # Parse variable_accesses (list)
        obj.variable_accesses = []
        for child in ARObject._find_all_child_elements(element, "VARIABLE-ACCESSES"):
            variable_accesses_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.variable_accesses.append(variable_accesses_value)

        return obj



class McDataAccessDetailsBuilder:
    """Builder for McDataAccessDetails."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McDataAccessDetails = McDataAccessDetails()

    def build(self) -> McDataAccessDetails:
        """Build and return McDataAccessDetails object.

        Returns:
            McDataAccessDetails instance
        """
        # TODO: Add validation
        return self._obj
