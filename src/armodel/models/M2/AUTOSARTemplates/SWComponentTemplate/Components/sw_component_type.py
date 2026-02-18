"""SwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2060)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 245)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 22)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 466)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
    ConsistencyNeeds,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation.sw_component_documentation import (
    SwComponentDocumentation,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit_group import (
    UnitGroup,
)
from abc import ABC, abstractmethod


class SwComponentType(ARElement, ABC):
    """AUTOSAR SwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    consistency_needses: list[ConsistencyNeeds]
    port_refs: list[ARRef]
    port_group_refs: list[ARRef]
    swc_mapping_refs: list[ARRef]
    sw_component_documentation: Optional[SwComponentDocumentation]
    unit_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SwComponentType."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []
        self.port_refs: list[ARRef] = []
        self.port_group_refs: list[ARRef] = []
        self.swc_mapping_refs: list[ARRef] = []
        self.sw_component_documentation: Optional[SwComponentDocumentation] = None
        self.unit_group_refs: list[ARRef] = []


class SwComponentTypeBuilder:
    """Builder for SwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentType = SwComponentType()

    def build(self) -> SwComponentType:
        """Build and return SwComponentType object.

        Returns:
            SwComponentType instance
        """
        # TODO: Add validation
        return self._obj
