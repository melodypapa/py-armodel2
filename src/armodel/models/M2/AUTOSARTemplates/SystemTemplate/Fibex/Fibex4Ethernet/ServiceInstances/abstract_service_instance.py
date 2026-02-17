"""AbstractServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue.tag_with_optional_value import (
    TagWithOptionalValue,
)


class AbstractServiceInstance(Identifiable):
    """AUTOSAR AbstractServiceInstance."""
    """Abstract base class - do not instantiate directly."""

    capabilities: list[TagWithOptionalValue]
    major_version: Optional[PositiveInteger]
    method: Optional[PduActivationRoutingGroup]
    routing_groups: list[SoAdRoutingGroup]
    def __init__(self) -> None:
        """Initialize AbstractServiceInstance."""
        super().__init__()
        self.capabilities: list[TagWithOptionalValue] = []
        self.major_version: Optional[PositiveInteger] = None
        self.method: Optional[PduActivationRoutingGroup] = None
        self.routing_groups: list[SoAdRoutingGroup] = []


class AbstractServiceInstanceBuilder:
    """Builder for AbstractServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractServiceInstance = AbstractServiceInstance()

    def build(self) -> AbstractServiceInstance:
        """Build and return AbstractServiceInstance object.

        Returns:
            AbstractServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
