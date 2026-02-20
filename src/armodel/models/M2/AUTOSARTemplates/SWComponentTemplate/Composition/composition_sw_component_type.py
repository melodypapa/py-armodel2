"""CompositionSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 307)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 291)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 895)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 219)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 434)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)


class CompositionSwComponentType(SwComponentType):
    """AUTOSAR CompositionSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    components: list[Any]
    connectors: list[SwConnector]
    constant_values: list[ConstantSpecification]
    data_type_refs: list[ARRef]
    instantiation_rte_events: list[InstantiationRTEEventProps]
    physical: Optional[PhysicalDimension]
    def __init__(self) -> None:
        """Initialize CompositionSwComponentType."""
        super().__init__()
        self.components: list[Any] = []
        self.connectors: list[SwConnector] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_type_refs: list[ARRef] = []
        self.instantiation_rte_events: list[InstantiationRTEEventProps] = []
        self.physical: Optional[PhysicalDimension] = None

    def serialize(self) -> ET.Element:
        """Serialize CompositionSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompositionSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize components (list to container "COMPONENTS")
        if self.components:
            wrapper = ET.Element("COMPONENTS")
            for item in self.components:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize connectors (list to container "CONNECTORS")
        if self.connectors:
            wrapper = ET.Element("CONNECTORS")
            for item in self.connectors:
                serialized = ARObject._serialize_item(item, "SwConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constant_values (list to container "CONSTANT-VALUES")
        if self.constant_values:
            wrapper = ET.Element("CONSTANT-VALUES")
            for item in self.constant_values:
                serialized = ARObject._serialize_item(item, "ConstantSpecification")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_type_refs (list to container "DATA-TYPE-REFS")
        if self.data_type_refs:
            wrapper = ET.Element("DATA-TYPE-REFS")
            for item in self.data_type_refs:
                serialized = ARObject._serialize_item(item, "DataTypeMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_rte_events (list to container "INSTANTIATION-RTE-EVENTS")
        if self.instantiation_rte_events:
            wrapper = ET.Element("INSTANTIATION-RTE-EVENTS")
            for item in self.instantiation_rte_events:
                serialized = ARObject._serialize_item(item, "InstantiationRTEEventProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical
        if self.physical is not None:
            serialized = ARObject._serialize_item(self.physical, "PhysicalDimension")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositionSwComponentType":
        """Deserialize XML element to CompositionSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompositionSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompositionSwComponentType, cls).deserialize(element)

        # Parse components (list from container "COMPONENTS")
        obj.components = []
        container = ARObject._find_child_element(element, "COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.components.append(child_value)

        # Parse connectors (list from container "CONNECTORS")
        obj.connectors = []
        container = ARObject._find_child_element(element, "CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connectors.append(child_value)

        # Parse constant_values (list from container "CONSTANT-VALUES")
        obj.constant_values = []
        container = ARObject._find_child_element(element, "CONSTANT-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constant_values.append(child_value)

        # Parse data_type_refs (list from container "DATA-TYPE-REFS")
        obj.data_type_refs = []
        container = ARObject._find_child_element(element, "DATA-TYPE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_type_refs.append(child_value)

        # Parse instantiation_rte_events (list from container "INSTANTIATION-RTE-EVENTS")
        obj.instantiation_rte_events = []
        container = ARObject._find_child_element(element, "INSTANTIATION-RTE-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_rte_events.append(child_value)

        # Parse physical
        child = ARObject._find_child_element(element, "PHYSICAL")
        if child is not None:
            physical_value = ARObject._deserialize_by_tag(child, "PhysicalDimension")
            obj.physical = physical_value

        return obj



class CompositionSwComponentTypeBuilder:
    """Builder for CompositionSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositionSwComponentType = CompositionSwComponentType()

    def build(self) -> CompositionSwComponentType:
        """Build and return CompositionSwComponentType object.

        Returns:
            CompositionSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
