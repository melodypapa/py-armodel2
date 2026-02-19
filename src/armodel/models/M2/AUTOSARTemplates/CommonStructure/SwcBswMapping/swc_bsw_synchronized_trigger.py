"""SwcBswSynchronizedTrigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class SwcBswSynchronizedTrigger(ARObject):
    """AUTOSAR SwcBswSynchronizedTrigger."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_trigger_ref: Optional[ARRef]
    swc_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedTrigger."""
        super().__init__()
        self.bsw_trigger_ref: Optional[ARRef] = None
        self.swc_trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswSynchronizedTrigger":
        """Deserialize XML element to SwcBswSynchronizedTrigger object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswSynchronizedTrigger object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_trigger_ref
        child = ARObject._find_child_element(element, "BSW-TRIGGER")
        if child is not None:
            bsw_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.bsw_trigger_ref = bsw_trigger_ref_value

        # Parse swc_trigger_ref
        child = ARObject._find_child_element(element, "SWC-TRIGGER")
        if child is not None:
            swc_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.swc_trigger_ref = swc_trigger_ref_value

        return obj



class SwcBswSynchronizedTriggerBuilder:
    """Builder for SwcBswSynchronizedTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedTrigger = SwcBswSynchronizedTrigger()

    def build(self) -> SwcBswSynchronizedTrigger:
        """Build and return SwcBswSynchronizedTrigger object.

        Returns:
            SwcBswSynchronizedTrigger instance
        """
        # TODO: Add validation
        return self._obj
