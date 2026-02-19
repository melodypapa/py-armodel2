"""TDCpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TDCpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR TDCpSoftwareClusterMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    td_cp_softwares: list[Any]
    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMappingSet."""
        super().__init__()
        self.td_cp_softwares: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterMappingSet":
        """Deserialize XML element to TDCpSoftwareClusterMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterMappingSet, cls).deserialize(element)

        # Parse td_cp_softwares (list from container "TD-CP-SOFTWARES")
        obj.td_cp_softwares = []
        container = ARObject._find_child_element(element, "TD-CP-SOFTWARES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.td_cp_softwares.append(child_value)

        return obj



class TDCpSoftwareClusterMappingSetBuilder:
    """Builder for TDCpSoftwareClusterMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDCpSoftwareClusterMappingSet = TDCpSoftwareClusterMappingSet()

    def build(self) -> TDCpSoftwareClusterMappingSet:
        """Build and return TDCpSoftwareClusterMappingSet object.

        Returns:
            TDCpSoftwareClusterMappingSet instance
        """
        # TODO: Add validation
        return self._obj
