"""BswAsynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 80)

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


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    called_entry_entry: Optional[BswModuleClientServerEntry]
    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallPoint."""
        super().__init__()
        self.called_entry_entry: Optional[BswModuleClientServerEntry] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallPoint":
        """Deserialize XML element to BswAsynchronousServerCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswAsynchronousServerCallPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswAsynchronousServerCallPoint, cls).deserialize(element)

        # Parse called_entry_entry
        child = ARObject._find_child_element(element, "CALLED-ENTRY-ENTRY")
        if child is not None:
            called_entry_entry_value = ARObject._deserialize_by_tag(child, "BswModuleClientServerEntry")
            obj.called_entry_entry = called_entry_entry_value

        return obj



class BswAsynchronousServerCallPointBuilder:
    """Builder for BswAsynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallPoint = BswAsynchronousServerCallPoint()

    def build(self) -> BswAsynchronousServerCallPoint:
        """Build and return BswAsynchronousServerCallPoint object.

        Returns:
            BswAsynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
