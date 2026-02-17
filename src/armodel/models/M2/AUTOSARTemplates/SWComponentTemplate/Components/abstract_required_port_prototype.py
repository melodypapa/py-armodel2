"""AbstractRequiredPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)


class AbstractRequiredPortPrototype(PortPrototype):
    """AUTOSAR AbstractRequiredPortPrototype."""
    """Abstract base class - do not instantiate directly."""

    required_coms: list[RPortComSpec]
    def __init__(self) -> None:
        """Initialize AbstractRequiredPortPrototype."""
        super().__init__()
        self.required_coms: list[RPortComSpec] = []


class AbstractRequiredPortPrototypeBuilder:
    """Builder for AbstractRequiredPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRequiredPortPrototype = AbstractRequiredPortPrototype()

    def build(self) -> AbstractRequiredPortPrototype:
        """Build and return AbstractRequiredPortPrototype object.

        Returns:
            AbstractRequiredPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
