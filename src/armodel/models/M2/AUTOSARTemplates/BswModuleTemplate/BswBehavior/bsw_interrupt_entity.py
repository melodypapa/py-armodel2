"""BswInterruptEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswInterruptCategory,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class BswInterruptEntity(BswModuleEntity):
    """AUTOSAR BswInterruptEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interrupt_category: Optional[BswInterruptCategory]
    interrupt_source: Optional[String]
    def __init__(self) -> None:
        """Initialize BswInterruptEntity."""
        super().__init__()
        self.interrupt_category: Optional[BswInterruptCategory] = None
        self.interrupt_source: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInterruptEntity":
        """Deserialize XML element to BswInterruptEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInterruptEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse interrupt_category
        child = ARObject._find_child_element(element, "INTERRUPT-CATEGORY")
        if child is not None:
            interrupt_category_value = child.text
            obj.interrupt_category = interrupt_category_value

        # Parse interrupt_source
        child = ARObject._find_child_element(element, "INTERRUPT-SOURCE")
        if child is not None:
            interrupt_source_value = child.text
            obj.interrupt_source = interrupt_source_value

        return obj



class BswInterruptEntityBuilder:
    """Builder for BswInterruptEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInterruptEntity = BswInterruptEntity()

    def build(self) -> BswInterruptEntity:
        """Build and return BswInterruptEntity object.

        Returns:
            BswInterruptEntity instance
        """
        # TODO: Add validation
        return self._obj
