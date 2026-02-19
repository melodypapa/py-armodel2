"""BswDirectCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswDirectCallPoint(BswModuleCallPoint):
    """AUTOSAR BswDirectCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    called_entry: Optional[BswModuleEntry]
    called_from: Optional[ExclusiveAreaNestingOrder]
    def __init__(self) -> None:
        """Initialize BswDirectCallPoint."""
        super().__init__()
        self.called_entry: Optional[BswModuleEntry] = None
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDirectCallPoint":
        """Deserialize XML element to BswDirectCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswDirectCallPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswDirectCallPoint, cls).deserialize(element)

        # Parse called_entry
        child = ARObject._find_child_element(element, "CALLED-ENTRY")
        if child is not None:
            called_entry_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.called_entry = called_entry_value

        # Parse called_from
        child = ARObject._find_child_element(element, "CALLED-FROM")
        if child is not None:
            called_from_value = ARObject._deserialize_by_tag(child, "ExclusiveAreaNestingOrder")
            obj.called_from = called_from_value

        return obj



class BswDirectCallPointBuilder:
    """Builder for BswDirectCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDirectCallPoint = BswDirectCallPoint()

    def build(self) -> BswDirectCallPoint:
        """Build and return BswDirectCallPoint object.

        Returns:
            BswDirectCallPoint instance
        """
        # TODO: Add validation
        return self._obj
