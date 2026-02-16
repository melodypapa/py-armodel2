"""NmCoordinator AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)


class NmCoordinator(ARObject):
    """AUTOSAR NmCoordinator."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("index", None, True, False, None),  # index
        ("nm_coord_sync", None, True, False, None),  # nmCoordSync
        ("nm_global", None, True, False, None),  # nmGlobal
        ("nm_nodes", None, False, True, NmNode),  # nmNodes
    ]

    def __init__(self) -> None:
        """Initialize NmCoordinator."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.nm_coord_sync: Optional[Boolean] = None
        self.nm_global: Optional[TimeValue] = None
        self.nm_nodes: list[NmNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NmCoordinator to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCoordinator":
        """Create NmCoordinator from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NmCoordinator instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NmCoordinator since parent returns ARObject
        return cast("NmCoordinator", obj)


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
