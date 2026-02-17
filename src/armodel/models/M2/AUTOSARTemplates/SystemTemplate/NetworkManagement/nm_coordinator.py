"""NmCoordinator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
        NmNode,
    )



class NmCoordinator(ARObject):
    """AUTOSAR NmCoordinator."""

    index: Optional[Integer]
    nm_coord_sync: Optional[Boolean]
    nm_global: Optional[TimeValue]
    nm_nodes: list[NmNode]
    def __init__(self) -> None:
        """Initialize NmCoordinator."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.nm_coord_sync: Optional[Boolean] = None
        self.nm_global: Optional[TimeValue] = None
        self.nm_nodes: list[NmNode] = []


class NmCoordinatorBuilder:
    """Builder for NmCoordinator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmCoordinator = NmCoordinator()

    def build(self) -> NmCoordinator:
        """Build and return NmCoordinator object.

        Returns:
            NmCoordinator instance
        """
        # TODO: Add validation
        return self._obj
