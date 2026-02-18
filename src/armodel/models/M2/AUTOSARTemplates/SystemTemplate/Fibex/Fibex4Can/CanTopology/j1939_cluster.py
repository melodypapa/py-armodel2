"""J1939Cluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class J1939Cluster(ARObject):
    """AUTOSAR J1939Cluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network_id: Optional[PositiveInteger]
    request2_support: Optional[Boolean]
    uses_address: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize J1939Cluster."""
        super().__init__()
        self.network_id: Optional[PositiveInteger] = None
        self.request2_support: Optional[Boolean] = None
        self.uses_address: Optional[Boolean] = None


class J1939ClusterBuilder:
    """Builder for J1939Cluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939Cluster = J1939Cluster()

    def build(self) -> J1939Cluster:
        """Build and return J1939Cluster object.

        Returns:
            J1939Cluster instance
        """
        # TODO: Add validation
        return self._obj
