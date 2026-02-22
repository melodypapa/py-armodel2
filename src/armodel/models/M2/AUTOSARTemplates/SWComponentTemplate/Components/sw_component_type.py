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

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
    ports: list[PortPrototype]
    port_groups: list[PortGroup]
    swc_mapping_constraint_refs: list[ARRef]
    sw_component_documentation: Optional[SwComponentDocumentation]
    unit_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SwComponentType."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []
        self.ports: list[PortPrototype] = []
        self.port_groups: list[PortGroup] = []
        self.swc_mapping_constraint_refs: list[ARRef] = []
        self.sw_component_documentation: Optional[SwComponentDocumentation] = None
        self.unit_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consistency_needses (list to container "CONSISTENCY-NEEDSES")
        if self.consistency_needses:
            wrapper = ET.Element("CONSISTENCY-NEEDSES")
            for item in self.consistency_needses:
                serialized = SerializationHelper.serialize_item(item, "ConsistencyNeeds")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ports (list to container "PORTS")
        if self.ports:
            wrapper = ET.Element("PORTS")
            for item in self.ports:
                serialized = SerializationHelper.serialize_item(item, "PortPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize port_groups (list to container "PORT-GROUPS")
        if self.port_groups:
            wrapper = ET.Element("PORT-GROUPS")
            for item in self.port_groups:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_mapping_constraint_refs (list to container "SWC-MAPPING-CONSTRAINT-REFS")
        if self.swc_mapping_constraint_refs:
            wrapper = ET.Element("SWC-MAPPING-CONSTRAINT-REFS")
            for item in self.swc_mapping_constraint_refs:
                serialized = SerializationHelper.serialize_item(item, "SwComponentMappingConstraints")
                if serialized is not None:
                    child_elem = ET.Element("SWC-MAPPING-CONSTRAINT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_component_documentation
        if self.sw_component_documentation is not None:
            serialized = SerializationHelper.serialize_item(self.sw_component_documentation, "SwComponentDocumentation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT-DOCUMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit_group_refs (list to container "UNIT-GROUP-REFS")
        if self.unit_group_refs:
            wrapper = ET.Element("UNIT-GROUP-REFS")
            for item in self.unit_group_refs:
                serialized = SerializationHelper.serialize_item(item, "UnitGroup")
                if serialized is not None:
                    child_elem = ET.Element("UNIT-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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
        container = SerializationHelper.find_child_element(element, "CONSISTENCY-NEEDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consistency_needses.append(child_value)

        # Parse ports (list from container "PORTS")
        obj.ports = []
        container = SerializationHelper.find_child_element(element, "PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ports.append(child_value)

        # Parse port_groups (list from container "PORT-GROUPS")
        obj.port_groups = []
        container = SerializationHelper.find_child_element(element, "PORT-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_groups.append(child_value)

        # Parse swc_mapping_constraint_refs (list from container "SWC-MAPPING-CONSTRAINT-REFS")
        obj.swc_mapping_constraint_refs = []
        container = SerializationHelper.find_child_element(element, "SWC-MAPPING-CONSTRAINT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_mapping_constraint_refs.append(child_value)

        # Parse sw_component_documentation
        child = SerializationHelper.find_child_element(element, "SW-COMPONENT-DOCUMENTATION")
        if child is not None:
            sw_component_documentation_value = SerializationHelper.deserialize_by_tag(child, "SwComponentDocumentation")
            obj.sw_component_documentation = sw_component_documentation_value

        # Parse unit_group_refs (list from container "UNIT-GROUP-REFS")
        obj.unit_group_refs = []
        container = SerializationHelper.find_child_element(element, "UNIT-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.unit_group_refs.append(child_value)

        return obj



