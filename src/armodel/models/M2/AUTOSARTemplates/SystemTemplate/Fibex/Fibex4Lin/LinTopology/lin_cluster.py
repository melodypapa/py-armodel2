"""LinCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class LinCluster(ARObject):
    """AUTOSAR LinCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize LinCluster."""
        super().__init__()


class LinClusterBuilder:
    """Builder for LinCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCluster = LinCluster()

    def build(self) -> LinCluster:
        """Build and return LinCluster object.

        Returns:
            LinCluster instance
        """
        # TODO: Add validation
        return self._obj
