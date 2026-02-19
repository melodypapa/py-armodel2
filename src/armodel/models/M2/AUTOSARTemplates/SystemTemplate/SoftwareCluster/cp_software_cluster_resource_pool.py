"""CpSoftwareClusterResourcePool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CpSoftwareClusterResourcePool(ARElement):
    """AUTOSAR CpSoftwareClusterResourcePool."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_scopes: list[EcuInstance]
    resources: list[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourcePool."""
        super().__init__()
        self.ecu_scopes: list[EcuInstance] = []
        self.resources: list[CpSoftwareCluster] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResourcePool":
        """Deserialize XML element to CpSoftwareClusterResourcePool object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResourcePool object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecu_scopes (list)
        obj.ecu_scopes = []
        for child in ARObject._find_all_child_elements(element, "ECU-SCOPES"):
            ecu_scopes_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_scopes.append(ecu_scopes_value)

        # Parse resources (list)
        obj.resources = []
        for child in ARObject._find_all_child_elements(element, "RESOURCES"):
            resources_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.resources.append(resources_value)

        return obj



class CpSoftwareClusterResourcePoolBuilder:
    """Builder for CpSoftwareClusterResourcePool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResourcePool = CpSoftwareClusterResourcePool()

    def build(self) -> CpSoftwareClusterResourcePool:
        """Build and return CpSoftwareClusterResourcePool object.

        Returns:
            CpSoftwareClusterResourcePool instance
        """
        # TODO: Add validation
        return self._obj
