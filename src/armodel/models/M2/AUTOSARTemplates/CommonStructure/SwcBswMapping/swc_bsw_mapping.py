"""SwcBswMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 656)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcBswMapping(ARElement):
    """AUTOSAR SwcBswMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_behavior: Optional[BswInternalBehavior]
    runnable_mapping_refs: list[ARRef]
    swc_behavior: Optional[SwcInternalBehavior]
    synchronizeds: list[Any]
    def __init__(self) -> None:
        """Initialize SwcBswMapping."""
        super().__init__()
        self.bsw_behavior: Optional[BswInternalBehavior] = None
        self.runnable_mapping_refs: list[ARRef] = []
        self.swc_behavior: Optional[SwcInternalBehavior] = None
        self.synchronizeds: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswMapping":
        """Deserialize XML element to SwcBswMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_behavior
        child = ARObject._find_child_element(element, "BSW-BEHAVIOR")
        if child is not None:
            bsw_behavior_value = ARObject._deserialize_by_tag(child, "BswInternalBehavior")
            obj.bsw_behavior = bsw_behavior_value

        # Parse runnable_mapping_refs (list)
        obj.runnable_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "RUNNABLE-MAPPINGS"):
            runnable_mapping_refs_value = ARObject._deserialize_by_tag(child, "SwcBswRunnableMapping")
            obj.runnable_mapping_refs.append(runnable_mapping_refs_value)

        # Parse swc_behavior
        child = ARObject._find_child_element(element, "SWC-BEHAVIOR")
        if child is not None:
            swc_behavior_value = ARObject._deserialize_by_tag(child, "SwcInternalBehavior")
            obj.swc_behavior = swc_behavior_value

        # Parse synchronizeds (list)
        obj.synchronizeds = []
        for child in ARObject._find_all_child_elements(element, "SYNCHRONIZEDS"):
            synchronizeds_value = child.text
            obj.synchronizeds.append(synchronizeds_value)

        return obj



class SwcBswMappingBuilder:
    """Builder for SwcBswMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswMapping = SwcBswMapping()

    def build(self) -> SwcBswMapping:
        """Build and return SwcBswMapping object.

        Returns:
            SwcBswMapping instance
        """
        # TODO: Add validation
        return self._obj
