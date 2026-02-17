"""SwcExclusiveAreaPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.classes.json"""

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


class SwcExclusiveAreaPolicy(ARObject):
    """AUTOSAR SwcExclusiveAreaPolicy."""

    api_principle_enum: Optional[ApiPrincipleEnum]
    exclusive_area: Optional[ExclusiveArea]
    def __init__(self) -> None:
        """Initialize SwcExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area: Optional[ExclusiveArea] = None


class SwcExclusiveAreaPolicyBuilder:
    """Builder for SwcExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcExclusiveAreaPolicy = SwcExclusiveAreaPolicy()

    def build(self) -> SwcExclusiveAreaPolicy:
        """Build and return SwcExclusiveAreaPolicy object.

        Returns:
            SwcExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
