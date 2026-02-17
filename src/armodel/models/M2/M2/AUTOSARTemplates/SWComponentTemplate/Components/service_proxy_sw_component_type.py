"""ServiceProxySwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 661)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2056)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)


class ServiceProxySwComponentType(AtomicSwComponentType):
    """AUTOSAR ServiceProxySwComponentType."""

    def __init__(self) -> None:
        """Initialize ServiceProxySwComponentType."""
        super().__init__()


class ServiceProxySwComponentTypeBuilder:
    """Builder for ServiceProxySwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceProxySwComponentType = ServiceProxySwComponentType()

    def build(self) -> ServiceProxySwComponentType:
        """Build and return ServiceProxySwComponentType object.

        Returns:
            ServiceProxySwComponentType instance
        """
        # TODO: Add validation
        return self._obj
