"""CpSoftwareClusterResourcePool AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CpSoftwareClusterResourcePool(ARElement):
    """AUTOSAR CpSoftwareClusterResourcePool."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecu_scopes", None, False, True, EcuInstance),  # ecuScopes
        ("resources", None, False, True, CpSoftwareCluster),  # resources
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourcePool."""
        super().__init__()
        self.ecu_scopes: list[EcuInstance] = []
        self.resources: list[CpSoftwareCluster] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterResourcePool to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResourcePool":
        """Create CpSoftwareClusterResourcePool from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterResourcePool instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterResourcePool since parent returns ARObject
        return cast("CpSoftwareClusterResourcePool", obj)


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
