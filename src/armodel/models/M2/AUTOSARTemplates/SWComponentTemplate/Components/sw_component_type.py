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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentType":
        """Deserialize XML element to SwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentType, cls).deserialize(element)

        # Parse consistency_needses (list from container "CONSISTENCY-NEEDSES")
        obj.consistency_needses = []
        container = ARObject._find_child_element(element, "CONSISTENCY-NEEDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consistency_needses.append(child_value)

        # Parse port_refs (list from container "PORTS")
        obj.port_refs = []
        container = ARObject._find_child_element(element, "PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_refs.append(child_value)

        # Parse port_group_refs (list from container "PORT-GROUPS")
        obj.port_group_refs = []
        container = ARObject._find_child_element(element, "PORT-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_group_refs.append(child_value)

        # Parse swc_mapping_refs (list from container "SWC-MAPPINGS")
        obj.swc_mapping_refs = []
        container = ARObject._find_child_element(element, "SWC-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_mapping_refs.append(child_value)

        # Parse sw_component_documentation
        child = ARObject._find_child_element(element, "SW-COMPONENT-DOCUMENTATION")
        if child is not None:
            sw_component_documentation_value = ARObject._deserialize_by_tag(child, "SwComponentDocumentation")
            obj.sw_component_documentation = sw_component_documentation_value

        # Parse unit_group_refs (list from container "UNIT-GROUPS")
        obj.unit_group_refs = []
        container = ARObject._find_child_element(element, "UNIT-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.unit_group_refs.append(child_value)

        return obj



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
