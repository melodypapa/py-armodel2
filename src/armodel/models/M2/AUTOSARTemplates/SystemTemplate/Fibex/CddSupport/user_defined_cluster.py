"""UserDefinedCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedCluster(ARObject):
    """AUTOSAR UserDefinedCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedCluster."""
        super().__init__()


class UserDefinedClusterBuilder:
    """Builder for UserDefinedCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCluster = UserDefinedCluster()

    def build(self) -> UserDefinedCluster:
        """Build and return UserDefinedCluster object.

        Returns:
            UserDefinedCluster instance
        """
        # TODO: Add validation
        return self._obj
