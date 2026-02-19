"""BswInterruptEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswInterruptEvent(BswEvent):
    """AUTOSAR BswInterruptEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswInterruptEvent."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInterruptEvent":
        """Deserialize XML element to BswInterruptEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInterruptEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class BswInterruptEventBuilder:
    """Builder for BswInterruptEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInterruptEvent = BswInterruptEvent()

    def build(self) -> BswInterruptEvent:
        """Build and return BswInterruptEvent object.

        Returns:
            BswInterruptEvent instance
        """
        # TODO: Add validation
        return self._obj
