"""BswCalledEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 74)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)


class BswCalledEntity(BswModuleEntity):
    """AUTOSAR BswCalledEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize BswCalledEntity."""
        super().__init__()


class BswCalledEntityBuilder:
    """Builder for BswCalledEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCalledEntity = BswCalledEntity()

    def build(self) -> BswCalledEntity:
        """Build and return BswCalledEntity object.

        Returns:
            BswCalledEntity instance
        """
        # TODO: Add validation
        return self._obj
