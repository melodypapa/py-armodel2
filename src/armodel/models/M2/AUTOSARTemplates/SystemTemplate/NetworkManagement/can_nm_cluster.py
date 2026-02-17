"""CanNmCluster AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanNmCluster(NmCluster):
    """AUTOSAR CanNmCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize CanNmCluster."""
        super().__init__()


class CanNmClusterBuilder:
    """Builder for CanNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmCluster = CanNmCluster()

    def build(self) -> CanNmCluster:
        """Build and return CanNmCluster object.

        Returns:
            CanNmCluster instance
        """
        # TODO: Add validation
        return self._obj
