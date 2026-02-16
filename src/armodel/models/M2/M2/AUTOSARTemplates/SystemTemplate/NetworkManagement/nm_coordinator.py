"""NmCoordinator AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # index
        "nm_coord_sync": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCoordSync
        "nm_global": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmGlobal
        "nm_nodes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmNode,
        ),  # nmNodes
    }

    def __init__(self) -> None:
        """Initialize NmCoordinator."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.nm_coord_sync: Optional[Boolean] = None
        self.nm_global: Optional[TimeValue] = None
        self.nm_nodes: list[NmNode] = []


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
