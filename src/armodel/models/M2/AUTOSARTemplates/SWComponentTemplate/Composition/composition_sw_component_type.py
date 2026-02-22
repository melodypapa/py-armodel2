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

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification_mapping_set import (
    ConstantSpecificationMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension_mapping_set import (
    PhysicalDimensionMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
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

    components: list[SwComponentPrototype]
    connectors: list[SwConnector]
    constant_value_mapping_refs: list[ARRef]
    data_type_mapping_refs: list[ARRef]
    instantiation_rte_event_props: list[InstantiationRTEEventProps]
    physical_dimension_mapping_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse components (list from container "COMPONENTS")
        obj.components = []
        container = SerializationHelper.find_child_element(element, "COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.components.append(child_value)

        # Parse connectors (list from container "CONNECTORS")
        obj.connectors = []
        container = SerializationHelper.find_child_element(element, "CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connectors.append(child_value)

        # Parse constant_value_mapping_refs (list from container "CONSTANT-VALUE-MAPPING-REFS")
        obj.constant_value_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "CONSTANT-VALUE-MAPPING-REFS")
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
                    obj.constant_value_mapping_refs.append(child_value)

        # Parse data_type_mapping_refs (list from container "DATA-TYPE-MAPPING-REFS")
        obj.data_type_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-TYPE-MAPPING-REFS")
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
                    obj.data_type_mapping_refs.append(child_value)

        # Parse instantiation_rte_event_props (list from container "INSTANTIATION-RTE-EVENT-PROPS")
        obj.instantiation_rte_event_props = []
        container = SerializationHelper.find_child_element(element, "INSTANTIATION-RTE-EVENT-PROPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_rte_event_props.append(child_value)

        # Parse physical_dimension_mapping_ref
        child = SerializationHelper.find_child_element(element, "PHYSICAL-DIMENSION-MAPPING-REF")
        if child is not None:
            physical_dimension_mapping_ref_value = ARRef.deserialize(child)
            obj.physical_dimension_mapping_ref = physical_dimension_mapping_ref_value

        return obj



class CompositionSwComponentTypeBuilder:
    """Builder for CompositionSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: CompositionSwComponentType = CompositionSwComponentType()


    def with_short_name(self, value: Identifier) -> "CompositionSwComponentTypeBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "CompositionSwComponentTypeBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "CompositionSwComponentTypeBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "CompositionSwComponentTypeBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "CompositionSwComponentTypeBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "CompositionSwComponentTypeBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "CompositionSwComponentTypeBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "CompositionSwComponentTypeBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "CompositionSwComponentTypeBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_consistency_needses(self, items: list[ConsistencyNeeds]) -> "CompositionSwComponentTypeBuilder":
        """Set consistency_needses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = list(items) if items else []
        return self

    def with_ports(self, items: list[PortPrototype]) -> "CompositionSwComponentTypeBuilder":
        """Set ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ports = list(items) if items else []
        return self

    def with_port_groups(self, items: list[PortGroup]) -> "CompositionSwComponentTypeBuilder":
        """Set port_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_groups = list(items) if items else []
        return self

    def with_swc_mapping_constraints(self, items: list[SwComponentMappingConstraints]) -> "CompositionSwComponentTypeBuilder":
        """Set swc_mapping_constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints = list(items) if items else []
        return self

    def with_sw_component_documentation(self, value: Optional[SwComponentDocumentation]) -> "CompositionSwComponentTypeBuilder":
        """Set sw_component_documentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_component_documentation = value
        return self

    def with_unit_groups(self, items: list[UnitGroup]) -> "CompositionSwComponentTypeBuilder":
        """Set unit_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.unit_groups = list(items) if items else []
        return self

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_dimension_mapping = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_consistency_needse(self, item: ConsistencyNeeds) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to consistency_needses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses.append(item)
        return self

    def clear_consistency_needses(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from consistency_needses list.

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = []
        return self

    def add_port(self, item: PortPrototype) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ports.append(item)
        return self

    def clear_ports(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from ports list.

        Returns:
            self for method chaining
        """
        self._obj.ports = []
        return self

    def add_port_group(self, item: PortGroup) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to port_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_groups.append(item)
        return self

    def clear_port_groups(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from port_groups list.

        Returns:
            self for method chaining
        """
        self._obj.port_groups = []
        return self

    def add_swc_mapping_constraint(self, item: SwComponentMappingConstraints) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to swc_mapping_constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints.append(item)
        return self

    def clear_swc_mapping_constraints(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from swc_mapping_constraints list.

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints = []
        return self

    def add_unit_group(self, item: UnitGroup) -> "CompositionSwComponentTypeBuilder":
        """Add a single item to unit_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.unit_groups.append(item)
        return self

    def clear_unit_groups(self) -> "CompositionSwComponentTypeBuilder":
        """Clear all items from unit_groups list.

        Returns:
            self for method chaining
        """
        self._obj.unit_groups = []
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


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> CompositionSwComponentType:
        """Build and return the CompositionSwComponentType instance with validation."""
        self._validate_instance()
        pass
        return self._obj