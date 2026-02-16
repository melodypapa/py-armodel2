"""J1939NmCluster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class J1939NmCluster(NmCluster):
    """AUTOSAR J1939NmCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "address_claim": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # addressClaim
        "uses_dynamic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # usesDynamic
    }

    def __init__(self) -> None:
        """Initialize J1939NmCluster."""
        super().__init__()
        self.address_claim: Optional[Boolean] = None
        self.uses_dynamic: Optional[Boolean] = None


class J1939NmClusterBuilder:
    """Builder for J1939NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmCluster = J1939NmCluster()

    def build(self) -> J1939NmCluster:
        """Build and return J1939NmCluster object.

        Returns:
            J1939NmCluster instance
        """
        # TODO: Add validation
        return self._obj
