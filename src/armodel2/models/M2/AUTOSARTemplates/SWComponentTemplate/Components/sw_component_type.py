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

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation.sw_component_documentation import (
    SwComponentDocumentation,
)
from armodel2.models.M2.MSR.AsamHdo.Units.unit_group import (
    UnitGroup,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
        ConsistencyNeeds,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
        PortGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "CONSISTENCY-NEEDSES": lambda obj, elem: obj.consistency_needses.append(ConsistencyNeeds.deserialize(elem)),
        "PORTS": lambda obj, elem: obj.ports.append(PortPrototype.deserialize(elem)),
        "PORT-GROUPS": lambda obj, elem: obj.port_groups.append(PortGroup.deserialize(elem)),
        "SWC-MAPPING-CONSTRAINTS": lambda obj, elem: obj.swc_mapping_constraint_refs.append(ARRef.deserialize(elem)),
        "SW-COMPONENT-DOCUMENTATION": lambda obj, elem: setattr(obj, "sw_component_documentation", SwComponentDocumentation.deserialize(elem)),
        "UNIT-GROUPS": lambda obj, elem: obj.unit_group_refs.append(ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.unit_group_refs.append(child_value)

        return obj



class SwComponentTypeBuilder(ARElementBuilder):
    """Builder for SwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwComponentType = SwComponentType()


    def with_consistency_needses(self, items: list[ConsistencyNeeds]) -> "SwComponentTypeBuilder":
        """Set consistency_needses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = list(items) if items else []
        return self

    def with_ports(self, items: list[PortPrototype]) -> "SwComponentTypeBuilder":
        """Set ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ports = list(items) if items else []
        return self

    def with_port_groups(self, items: list[PortGroup]) -> "SwComponentTypeBuilder":
        """Set port_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_groups = list(items) if items else []
        return self

    def with_swc_mapping_constraints(self, items: list[SwComponentMappingConstraints]) -> "SwComponentTypeBuilder":
        """Set swc_mapping_constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints = list(items) if items else []
        return self

    def with_sw_component_documentation(self, value: Optional[SwComponentDocumentation]) -> "SwComponentTypeBuilder":
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

    def with_unit_groups(self, items: list[UnitGroup]) -> "SwComponentTypeBuilder":
        """Set unit_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.unit_groups = list(items) if items else []
        return self


    def add_consistency_needs(self, item: ConsistencyNeeds) -> "SwComponentTypeBuilder":
        """Add a single item to consistency_needses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses.append(item)
        return self

    def clear_consistency_needses(self) -> "SwComponentTypeBuilder":
        """Clear all items from consistency_needses list.

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = []
        return self

    def add_port(self, item: PortPrototype) -> "SwComponentTypeBuilder":
        """Add a single item to ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ports.append(item)
        return self

    def clear_ports(self) -> "SwComponentTypeBuilder":
        """Clear all items from ports list.

        Returns:
            self for method chaining
        """
        self._obj.ports = []
        return self

    def add_port_group(self, item: PortGroup) -> "SwComponentTypeBuilder":
        """Add a single item to port_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_groups.append(item)
        return self

    def clear_port_groups(self) -> "SwComponentTypeBuilder":
        """Clear all items from port_groups list.

        Returns:
            self for method chaining
        """
        self._obj.port_groups = []
        return self

    def add_swc_mapping_constraint(self, item: SwComponentMappingConstraints) -> "SwComponentTypeBuilder":
        """Add a single item to swc_mapping_constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints.append(item)
        return self

    def clear_swc_mapping_constraints(self) -> "SwComponentTypeBuilder":
        """Clear all items from swc_mapping_constraints list.

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints = []
        return self

    def add_unit_group(self, item: UnitGroup) -> "SwComponentTypeBuilder":
        """Add a single item to unit_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.unit_groups.append(item)
        return self

    def clear_unit_groups(self) -> "SwComponentTypeBuilder":
        """Clear all items from unit_groups list.

        Returns:
            self for method chaining
        """
        self._obj.unit_groups = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    @abstractmethod
    def build(self) -> SwComponentType:
        """Build and return the SwComponentType instance (abstract)."""
        raise NotImplementedError