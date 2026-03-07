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
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import SwComponentTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification_mapping_set import (
    ConstantSpecificationMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel2.models.M2.MSR.AsamHdo.Units.physical_dimension_mapping_set import (
    PhysicalDimensionMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompositionSwComponentType(SwComponentType):
    """AUTOSAR CompositionSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMPOSITION-SW-COMPONENT-TYPE"


    components: list[SwComponentPrototype]
    connectors: list[SwConnector]
    constant_value_mapping_refs: list[ARRef]
    data_type_mapping_refs: list[ARRef]
    instantiation_rte_event_props: list[InstantiationRTEEventProps]
    physical_dimension_mapping_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMPONENTS": lambda obj, elem: obj.components.append(SerializationHelper.deserialize_by_tag(elem, "SwComponentPrototype")),
        "CONNECTORS": ("_POLYMORPHIC_LIST", "connectors", ["AssemblySwConnector", "DelegationSwConnector", "PassThroughSwConnector"]),
        "CONSTANT-VALUE-MAPPING-REFS": lambda obj, elem: [obj.constant_value_mapping_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "DATA-TYPE-MAPPING-REFS": lambda obj, elem: [obj.data_type_mapping_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "INSTANTIATION-RTE-EVENT-PROPS": ("_POLYMORPHIC_LIST", "instantiation_rte_event_props", ["InstantiationTimingEventProps"]),
        "PHYSICAL-DIMENSION-MAPPING-REF": lambda obj, elem: setattr(obj, "physical_dimension_mapping_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CompositionSwComponentType."""
        super().__init__()
        self.components: list[SwComponentPrototype] = []
        self.connectors: list[SwConnector] = []
        self.constant_value_mapping_refs: list[ARRef] = []
        self.data_type_mapping_refs: list[ARRef] = []
        self.instantiation_rte_event_props: list[InstantiationRTEEventProps] = []
        self.physical_dimension_mapping_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CompositionSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompositionSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize components (list to container "COMPONENTS")
        if self.components:
            wrapper = ET.Element("COMPONENTS")
            for item in self.components:
                serialized = SerializationHelper.serialize_item(item, "SwComponentPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize connectors (list to container "CONNECTORS")
        if self.connectors:
            wrapper = ET.Element("CONNECTORS")
            for item in self.connectors:
                serialized = SerializationHelper.serialize_item(item, "SwConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constant_value_mapping_refs (list to container "CONSTANT-VALUE-MAPPING-REFS")
        if self.constant_value_mapping_refs:
            wrapper = ET.Element("CONSTANT-VALUE-MAPPING-REFS")
            for item in self.constant_value_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "ConstantSpecificationMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("CONSTANT-VALUE-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_type_mapping_refs (list to container "DATA-TYPE-MAPPING-REFS")
        if self.data_type_mapping_refs:
            wrapper = ET.Element("DATA-TYPE-MAPPING-REFS")
            for item in self.data_type_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "DataTypeMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_rte_event_props (list to container "INSTANTIATION-RTE-EVENT-PROPS")
        if self.instantiation_rte_event_props:
            wrapper = ET.Element("INSTANTIATION-RTE-EVENT-PROPS")
            for item in self.instantiation_rte_event_props:
                serialized = SerializationHelper.serialize_item(item, "InstantiationRTEEventProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_dimension_mapping_ref
        if self.physical_dimension_mapping_ref is not None:
            serialized = SerializationHelper.serialize_item(self.physical_dimension_mapping_ref, "PhysicalDimensionMappingSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-DIMENSION-MAPPING-REF")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPONENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.components.append(SerializationHelper.deserialize_by_tag(item_elem, "SwComponentPrototype"))
            elif tag == "CONNECTORS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ASSEMBLY-SW-CONNECTOR":
                        obj.connectors.append(SerializationHelper.deserialize_by_tag(item_elem, "AssemblySwConnector"))
                    elif concrete_tag == "DELEGATION-SW-CONNECTOR":
                        obj.connectors.append(SerializationHelper.deserialize_by_tag(item_elem, "DelegationSwConnector"))
                    elif concrete_tag == "PASS-THROUGH-SW-CONNECTOR":
                        obj.connectors.append(SerializationHelper.deserialize_by_tag(item_elem, "PassThroughSwConnector"))
            elif tag == "CONSTANT-VALUE-MAPPING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.constant_value_mapping_refs.append(ARRef.deserialize(item_elem))
            elif tag == "DATA-TYPE-MAPPING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_type_mapping_refs.append(ARRef.deserialize(item_elem))
            elif tag == "INSTANTIATION-RTE-EVENT-PROPS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "INSTANTIATION-TIMING-EVENT-PROPS":
                        obj.instantiation_rte_event_props.append(SerializationHelper.deserialize_by_tag(item_elem, "InstantiationTimingEventProps"))
            elif tag == "PHYSICAL-DIMENSION-MAPPING-REF":
                setattr(obj, "physical_dimension_mapping_ref", ARRef.deserialize(child))

        return obj



class CompositionSwComponentTypeBuilder(SwComponentTypeBuilder):
    """Builder for CompositionSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompositionSwComponentType = CompositionSwComponentType()


    def with_components(self, items: list[SwComponentPrototype]) -> "CompositionSwComponentTypeBuilder":
        """Set components list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.components = list(items) if items else []
        return self

    def with_connectors(self, items: list[SwConnector]) -> "CompositionSwComponentTypeBuilder":
        """Set connectors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.connectors = list(items) if items else []
        return self

    def with_constant_value_mappings(self, items: list[ConstantSpecificationMappingSet]) -> "CompositionSwComponentTypeBuilder":
        """Set constant_value_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = list(items) if items else []
        return self

    def with_data_type_mappings(self, items: list[DataTypeMappingSet]) -> "CompositionSwComponentTypeBuilder":
        """Set data_type_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = list(items) if items else []
        return self

    def with_instantiation_rte_event_props(self, items: list[InstantiationRTEEventProps]) -> "CompositionSwComponentTypeBuilder":
        """Set instantiation_rte_event_props list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instantiation_rte_event_props = list(items) if items else []
        return self

    def with_physical_dimension_mapping(self, value: Optional[PhysicalDimensionMappingSet]) -> "CompositionSwComponentTypeBuilder":
        """Set physical_dimension_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'physical_dimension_mapping' is required and cannot be None")
        self._obj.physical_dimension_mapping = value
        return self


    def add_component(self, item: SwComponentPrototype) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to components list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.components.append(item)
        return self

    def clear_components(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from components list.

        Returns:
            self for method chaining
        """
        self._obj.components = []
        return self

    def add_connector(self, item: SwConnector) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to connectors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.connectors.append(item)
        return self

    def clear_connectors(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from connectors list.

        Returns:
            self for method chaining
        """
        self._obj.connectors = []
        return self

    def add_constant_value_mapping(self, item: ConstantSpecificationMappingSet) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to constant_value_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings.append(item)
        return self

    def clear_constant_value_mappings(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from constant_value_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = []
        return self

    def add_data_type_mapping(self, item: DataTypeMappingSet) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to data_type_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings.append(item)
        return self

    def clear_data_type_mappings(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from data_type_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = []
        return self

    def add_instantiation_rte_event_prop(self, item: InstantiationRTEEventProps) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to instantiation_rte_event_props list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instantiation_rte_event_props.append(item)
        return self

    def clear_instantiation_rte_event_props(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from instantiation_rte_event_props list.

        Returns:
            self for method chaining
        """
        self._obj.instantiation_rte_event_props = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "component",
        "connector",
        "constantValueMapping",
        "dataTypeMapping",
        "instantiationRTEEventProp",
        "physicalDimensionMapping",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompositionSwComponentType:
        """Build and return the CompositionSwComponentType instance with validation."""
        self._validate_instance()
        return self._obj