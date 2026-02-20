"""LinCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


@atp_variant()

class LinCluster(ARObject):
    """AUTOSAR LinCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize LinCluster."""
        super().__init__()



class LinClusterBuilder:
    """Builder for LinCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCluster = LinCluster()

    def build(self) -> LinCluster:
        """Build and return LinCluster object.

        Returns:
            LinCluster instance
        """
        # TODO: Add validation
        return self._obj
