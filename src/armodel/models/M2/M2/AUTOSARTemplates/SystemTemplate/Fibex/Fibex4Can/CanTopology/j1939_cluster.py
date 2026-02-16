"""J1939Cluster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class J1939Cluster(ARObject):
    """AUTOSAR J1939Cluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "network_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # networkId
        "request2_support": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # request2Support
        "uses_address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # usesAddress
    }

    def __init__(self) -> None:
        """Initialize J1939Cluster."""
        super().__init__()
        self.network_id: Optional[PositiveInteger] = None
        self.request2_support: Optional[Boolean] = None
        self.uses_address: Optional[Boolean] = None


class J1939ClusterBuilder:
    """Builder for J1939Cluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939Cluster = J1939Cluster()

    def build(self) -> J1939Cluster:
        """Build and return J1939Cluster object.

        Returns:
            J1939Cluster instance
        """
        # TODO: Add validation
        return self._obj
