"""LifeCycleInfo AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lc_object_ref: ARRef
    lc_state: Optional[LifeCycleState]
    period_begin: Optional[LifeCyclePeriod]
    period_end: Optional[LifeCyclePeriod]
    remark: Optional[DocumentationBlock]
    use_instead_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object_ref: ARRef = None
        self.lc_state: Optional[LifeCycleState] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_instead_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfo":
        """Deserialize XML element to LifeCycleInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfo object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lc_object_ref
        child = ARObject._find_child_element(element, "LC-OBJECT")
        if child is not None:
            lc_object_ref_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.lc_object_ref = lc_object_ref_value

        # Parse lc_state
        child = ARObject._find_child_element(element, "LC-STATE")
        if child is not None:
            lc_state_value = ARObject._deserialize_by_tag(child, "LifeCycleState")
            obj.lc_state = lc_state_value

        # Parse period_begin
        child = ARObject._find_child_element(element, "PERIOD-BEGIN")
        if child is not None:
            period_begin_value = ARObject._deserialize_by_tag(child, "LifeCyclePeriod")
            obj.period_begin = period_begin_value

        # Parse period_end
        child = ARObject._find_child_element(element, "PERIOD-END")
        if child is not None:
            period_end_value = ARObject._deserialize_by_tag(child, "LifeCyclePeriod")
            obj.period_end = period_end_value

        # Parse remark
        child = ARObject._find_child_element(element, "REMARK")
        if child is not None:
            remark_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.remark = remark_value

        # Parse use_instead_refs (list)
        obj.use_instead_refs = []
        for child in ARObject._find_all_child_elements(element, "USE-INSTEADS"):
            use_instead_refs_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.use_instead_refs.append(use_instead_refs_value)

        return obj



class LifeCycleInfoBuilder:
    """Builder for LifeCycleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfo = LifeCycleInfo()

    def build(self) -> LifeCycleInfo:
        """Build and return LifeCycleInfo object.

        Returns:
            LifeCycleInfo instance
        """
        # TODO: Add validation
        return self._obj
