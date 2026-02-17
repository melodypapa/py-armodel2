"""PortPrototypeBlueprint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 237)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 459)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Port.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)


class PortPrototypeBlueprint(ARElement):
    """AUTOSAR PortPrototypeBlueprint."""

    init_values: list[PortPrototypeBlueprint]
    interface: PortInterface
    provided_coms: list[PPortComSpec]
    required_coms: list[RPortComSpec]
    def __init__(self) -> None:
        """Initialize PortPrototypeBlueprint."""
        super().__init__()
        self.init_values: list[PortPrototypeBlueprint] = []
        self.interface: PortInterface = None
        self.provided_coms: list[PPortComSpec] = []
        self.required_coms: list[RPortComSpec] = []


class PortPrototypeBlueprintBuilder:
    """Builder for PortPrototypeBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototypeBlueprint = PortPrototypeBlueprint()

    def build(self) -> PortPrototypeBlueprint:
        """Build and return PortPrototypeBlueprint object.

        Returns:
            PortPrototypeBlueprint instance
        """
        # TODO: Add validation
        return self._obj
