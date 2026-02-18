"""PassThroughSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class PassThroughSwConnector(SwConnector):
    """AUTOSAR PassThroughSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided_outer: Optional[AbstractProvidedPortPrototype]
    required_outer: Optional[AbstractRequiredPortPrototype]
    def __init__(self) -> None:
        """Initialize PassThroughSwConnector."""
        super().__init__()
        self.provided_outer: Optional[AbstractProvidedPortPrototype] = None
        self.required_outer: Optional[AbstractRequiredPortPrototype] = None


class PassThroughSwConnectorBuilder:
    """Builder for PassThroughSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PassThroughSwConnector = PassThroughSwConnector()

    def build(self) -> PassThroughSwConnector:
        """Build and return PassThroughSwConnector object.

        Returns:
            PassThroughSwConnector instance
        """
        # TODO: Add validation
        return self._obj
