"""BswSynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswSynchronousServerCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    called_entry_entry: Optional[BswModuleClientServerEntry]
    called_from: Optional[ExclusiveAreaNestingOrder]
    def __init__(self) -> None:
        """Initialize BswSynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry: Optional[BswModuleClientServerEntry] = None
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswSynchronousServerCallPoint":
        """Deserialize XML element to BswSynchronousServerCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswSynchronousServerCallPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswSynchronousServerCallPoint, cls).deserialize(element)

        # Parse called_entry_entry
        child = ARObject._find_child_element(element, "CALLED-ENTRY-ENTRY")
        if child is not None:
            called_entry_entry_value = ARObject._deserialize_by_tag(child, "BswModuleClientServerEntry")
            obj.called_entry_entry = called_entry_entry_value

        # Parse called_from
        child = ARObject._find_child_element(element, "CALLED-FROM")
        if child is not None:
            called_from_value = ARObject._deserialize_by_tag(child, "ExclusiveAreaNestingOrder")
            obj.called_from = called_from_value

        return obj



class BswSynchronousServerCallPointBuilder:
    """Builder for BswSynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswSynchronousServerCallPoint = BswSynchronousServerCallPoint()

    def build(self) -> BswSynchronousServerCallPoint:
        """Build and return BswSynchronousServerCallPoint object.

        Returns:
            BswSynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
