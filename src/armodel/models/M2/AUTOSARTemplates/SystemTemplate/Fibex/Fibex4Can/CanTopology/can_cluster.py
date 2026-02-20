"""CanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


@atp_variant()

class CanCluster(ARObject):
    """AUTOSAR CanCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanCluster."""
        super().__init__()



class CanClusterBuilder:
    """Builder for CanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCluster = CanCluster()

    def build(self) -> CanCluster:
        """Build and return CanCluster object.

        Returns:
            CanCluster instance
        """
        # TODO: Add validation
        return self._obj
