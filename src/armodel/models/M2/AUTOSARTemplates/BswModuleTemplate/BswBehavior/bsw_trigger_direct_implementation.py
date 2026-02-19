"""BswTriggerDirectImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswTriggerDirectImplementation(ARObject):
    """AUTOSAR BswTriggerDirectImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cat2_isr: Optional[Identifier]
    mastered_trigger_ref: Optional[ARRef]
    task: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize BswTriggerDirectImplementation."""
        super().__init__()
        self.cat2_isr: Optional[Identifier] = None
        self.mastered_trigger_ref: Optional[ARRef] = None
        self.task: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTriggerDirectImplementation":
        """Deserialize XML element to BswTriggerDirectImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswTriggerDirectImplementation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cat2_isr
        child = ARObject._find_child_element(element, "CAT2-ISR")
        if child is not None:
            cat2_isr_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.cat2_isr = cat2_isr_value

        # Parse mastered_trigger_ref
        child = ARObject._find_child_element(element, "MASTERED-TRIGGER")
        if child is not None:
            mastered_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.mastered_trigger_ref = mastered_trigger_ref_value

        # Parse task
        child = ARObject._find_child_element(element, "TASK")
        if child is not None:
            task_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.task = task_value

        return obj



class BswTriggerDirectImplementationBuilder:
    """Builder for BswTriggerDirectImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTriggerDirectImplementation = BswTriggerDirectImplementation()

    def build(self) -> BswTriggerDirectImplementation:
        """Build and return BswTriggerDirectImplementation object.

        Returns:
            BswTriggerDirectImplementation instance
        """
        # TODO: Add validation
        return self._obj
