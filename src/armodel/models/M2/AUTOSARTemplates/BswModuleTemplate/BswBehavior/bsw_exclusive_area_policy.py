"""BswExclusiveAreaPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ApiPrincipleEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class BswExclusiveAreaPolicy(ARObject):
    """AUTOSAR BswExclusiveAreaPolicy."""

    api_principle_enum: Optional[ApiPrincipleEnum]
    exclusive_area: Optional[ExclusiveArea]
    def __init__(self) -> None:
        """Initialize BswExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area: Optional[ExclusiveArea] = None


class BswExclusiveAreaPolicyBuilder:
    """Builder for BswExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswExclusiveAreaPolicy = BswExclusiveAreaPolicy()

    def build(self) -> BswExclusiveAreaPolicy:
        """Build and return BswExclusiveAreaPolicy object.

        Returns:
            BswExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
