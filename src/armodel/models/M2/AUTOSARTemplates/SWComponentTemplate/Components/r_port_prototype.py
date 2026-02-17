"""RPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 237)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 460)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class RPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR RPortPrototype."""

    def __init__(self) -> None:
        """Initialize RPortPrototype."""
        super().__init__()
        self.may_be: Optional[Boolean] = None
        self.required: Optional[PortInterface] = None


class RPortPrototypeBuilder:
    """Builder for RPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortPrototype = RPortPrototype()

    def build(self) -> RPortPrototype:
        """Build and return RPortPrototype object.

        Returns:
            RPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
