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
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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


class SwComponentType(ARElement):
    """AUTOSAR SwComponentType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "consistency_needses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConsistencyNeeds,
        ),  # consistencyNeedses
        "ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortPrototype,
        ),  # ports
        "port_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortGroup,
        ),  # portGroups
        "swc_mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwComponentMapping),
        ),  # swcMappings
        "sw_component_documentation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentDocumentation,
        ),  # swComponentDocumentation
        "unit_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=UnitGroup,
        ),  # unitGroups
    }

    def __init__(self) -> None:
        """Initialize SwComponentType."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []
        self.ports: list[PortPrototype] = []
        self.port_groups: list[PortGroup] = []
        self.swc_mappings: list[Any] = []
        self.sw_component_documentation: Optional[SwComponentDocumentation] = None
        self.unit_groups: list[UnitGroup] = []


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
