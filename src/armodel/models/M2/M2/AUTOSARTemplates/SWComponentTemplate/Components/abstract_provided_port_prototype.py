"""AbstractProvidedPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)


class AbstractProvidedPortPrototype(PortPrototype):
    """AUTOSAR AbstractProvidedPortPrototype."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AbstractProvidedPortPrototype."""
        super().__init__()
        self.provided_coms: list[PPortComSpec] = []


class AbstractProvidedPortPrototypeBuilder:
    """Builder for AbstractProvidedPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractProvidedPortPrototype = AbstractProvidedPortPrototype()

    def build(self) -> AbstractProvidedPortPrototype:
        """Build and return AbstractProvidedPortPrototype object.

        Returns:
            AbstractProvidedPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
