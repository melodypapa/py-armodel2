"""DdsCpProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpProvidedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    local_unicast_ref: Optional[ARRef]
    minor_version: Optional[PositiveInteger]
    provided_ddses: list[DdsCpServiceInstance]
    static_remote_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DdsCpProvidedServiceInstance."""
        super().__init__()
        self.local_unicast_ref: Optional[ARRef] = None
        self.minor_version: Optional[PositiveInteger] = None
        self.provided_ddses: list[DdsCpServiceInstance] = []
        self.static_remote_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DdsCpProvidedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpProvidedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize local_unicast_ref
        if self.local_unicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.local_unicast_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-UNICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = SerializationHelper.serialize_item(self.minor_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_ddses (list to container "PROVIDED-DDSES")
        if self.provided_ddses:
            wrapper = ET.Element("PROVIDED-DDSES")
            for item in self.provided_ddses:
                serialized = SerializationHelper.serialize_item(item, "DdsCpServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize static_remote_refs (list to container "STATIC-REMOTE-REFS")
        if self.static_remote_refs:
            wrapper = ET.Element("STATIC-REMOTE-REFS")
            for item in self.static_remote_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("STATIC-REMOTE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DdsCpProvidedServiceInstance":
        """Deserialize XML element to DdsCpProvidedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpProvidedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpProvidedServiceInstance, cls).deserialize(element)

        # Parse local_unicast_ref
        child = SerializationHelper.find_child_element(element, "LOCAL-UNICAST-REF")
        if child is not None:
            local_unicast_ref_value = ARRef.deserialize(child)
            obj.local_unicast_ref = local_unicast_ref_value

        # Parse minor_version
        child = SerializationHelper.find_child_element(element, "MINOR-VERSION")
        if child is not None:
            minor_version_value = child.text
            obj.minor_version = minor_version_value

        # Parse provided_ddses (list from container "PROVIDED-DDSES")
        obj.provided_ddses = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-DDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_ddses.append(child_value)

        # Parse static_remote_refs (list from container "STATIC-REMOTE-REFS")
        obj.static_remote_refs = []
        container = SerializationHelper.find_child_element(element, "STATIC-REMOTE-REFS")
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
                    obj.static_remote_refs.append(child_value)

        return obj



class DdsCpProvidedServiceInstanceBuilder:
    """Builder for DdsCpProvidedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DdsCpProvidedServiceInstance = DdsCpProvidedServiceInstance()


    def with_short_name(self, value: Identifier) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "DdsCpProvidedServiceInstanceBuilder":
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

    def with_capabilities(self, items: list[TagWithOptionalValue]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set capabilities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.capabilities = list(items) if items else []
        return self

    def with_major_version(self, value: Optional[PositiveInteger]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set major_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.major_version = value
        return self

    def with_method(self, value: Optional[PduActivationRoutingGroup]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.method = value
        return self

    def with_routing_groups(self, items: list[SoAdRoutingGroup]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set routing_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = list(items) if items else []
        return self

    def with_dds_field_reply(self, value: Optional[DdsCpTopic]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set dds_field_reply attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_field_reply = value
        return self

    def with_dds_field(self, value: Optional[DdsCpTopic]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set dds_field attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_field = value
        return self

    def with_dds_method(self, value: Optional[DdsCpTopic]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set dds_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_method = value
        return self

    def with_dds_service_qos(self, value: Optional[DdsCpQosProfile]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set dds_service_qos attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_service_qos = value
        return self

    def with_service_instance(self, value: Optional[PositiveInteger]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set service_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_instance = value
        return self

    def with_service_interface(self, value: Optional[String]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set service_interface attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_interface = value
        return self

    def with_local_unicast(self, value: Optional[ApplicationEndpoint]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set local_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_unicast = value
        return self

    def with_minor_version(self, value: Optional[PositiveInteger]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set minor_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minor_version = value
        return self

    def with_provided_ddses(self, items: list[DdsCpServiceInstance]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set provided_ddses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_ddses = list(items) if items else []
        return self

    def with_static_remotes(self, items: list[ApplicationEndpoint]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set static_remotes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.static_remotes = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_capabilitie(self, item: TagWithOptionalValue) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to capabilities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.capabilities.append(item)
        return self

    def clear_capabilities(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from capabilities list.

        Returns:
            self for method chaining
        """
        self._obj.capabilities = []
        return self

    def add_routing_group(self, item: SoAdRoutingGroup) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to routing_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.routing_groups.append(item)
        return self

    def clear_routing_groups(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from routing_groups list.

        Returns:
            self for method chaining
        """
        self._obj.routing_groups = []
        return self

    def add_provided_ddse(self, item: DdsCpServiceInstance) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to provided_ddses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_ddses.append(item)
        return self

    def clear_provided_ddses(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from provided_ddses list.

        Returns:
            self for method chaining
        """
        self._obj.provided_ddses = []
        return self

    def add_static_remote(self, item: ApplicationEndpoint) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to static_remotes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.static_remotes.append(item)
        return self

    def clear_static_remotes(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from static_remotes list.

        Returns:
            self for method chaining
        """
        self._obj.static_remotes = []
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


    def build(self) -> DdsCpProvidedServiceInstance:
        """Build and return the DdsCpProvidedServiceInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj