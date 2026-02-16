"""TDCpSoftwareClusterMappingSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class TDCpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR TDCpSoftwareClusterMappingSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("td_cp_softwares", None, False, True, any (TDCpSoftwareCluster)),  # tdCpSoftwares
    ]

    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMappingSet."""
        super().__init__()
        self.td_cp_softwares: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDCpSoftwareClusterMappingSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterMappingSet":
        """Create TDCpSoftwareClusterMappingSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDCpSoftwareClusterMappingSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDCpSoftwareClusterMappingSet since parent returns ARObject
        return cast("TDCpSoftwareClusterMappingSet", obj)


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
