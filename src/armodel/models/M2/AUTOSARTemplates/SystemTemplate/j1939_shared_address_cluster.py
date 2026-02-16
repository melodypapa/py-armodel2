"""J1939SharedAddressCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.j1939_cluster import (
    J1939Cluster,
)


class J1939SharedAddressCluster(Identifiable):
    """AUTOSAR J1939SharedAddressCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("participatings", None, False, True, J1939Cluster),  # participatings
    ]

    def __init__(self) -> None:
        """Initialize J1939SharedAddressCluster."""
        super().__init__()
        self.participatings: list[J1939Cluster] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert J1939SharedAddressCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939SharedAddressCluster":
        """Create J1939SharedAddressCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            J1939SharedAddressCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to J1939SharedAddressCluster since parent returns ARObject
        return cast("J1939SharedAddressCluster", obj)


class J1939SharedAddressClusterBuilder:
    """Builder for J1939SharedAddressCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939SharedAddressCluster = J1939SharedAddressCluster()

    def build(self) -> J1939SharedAddressCluster:
        """Build and return J1939SharedAddressCluster object.

        Returns:
            J1939SharedAddressCluster instance
        """
        # TODO: Add validation
        return self._obj
