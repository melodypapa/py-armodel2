"""PPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2041)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 234)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PPortPrototype(AbstractProvidedPortPrototype):
    """AUTOSAR PPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided: Optional[PortInterface]
    def __init__(self) -> None:
        """Initialize PPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None


class PPortPrototypeBuilder:
    """Builder for PPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortPrototype = PPortPrototype()

    def build(self) -> PPortPrototype:
        """Build and return PPortPrototype object.

        Returns:
            PPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
