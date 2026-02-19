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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse td_cp_softwares (list)
        obj.td_cp_softwares = []
        for child in ARObject._find_all_child_elements(element, "TD-CP-SOFTWARES"):
            td_cp_softwares_value = child.text
            obj.td_cp_softwares.append(td_cp_softwares_value)

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
