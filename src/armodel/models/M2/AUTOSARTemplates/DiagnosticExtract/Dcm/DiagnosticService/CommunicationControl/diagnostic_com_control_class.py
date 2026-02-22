"""DiagnosticComControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticComControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    all_channelse_refs: list[ARRef]
    all_physical_refs: list[Any]
    specific_channels: list[DiagnosticComControl]
    sub_nodes: list[DiagnosticComControl]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelse_refs: list[ARRef] = []
        self.all_physical_refs: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComControlClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComControlClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize all_channelse_refs (list to container "ALL-CHANNELSE-REFS")
        if self.all_channelse_refs:
            wrapper = ET.Element("ALL-CHANNELSE-REFS")
            for item in self.all_channelse_refs:
                serialized = SerializationHelper.serialize_item(item, "CommunicationCluster")
                if serialized is not None:
                    child_elem = ET.Element("ALL-CHANNELSE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize all_physical_refs (list to container "ALL-PHYSICAL-REFS")
        if self.all_physical_refs:
            wrapper = ET.Element("ALL-PHYSICAL-REFS")
            for item in self.all_physical_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ALL-PHYSICAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize specific_channels (list to container "SPECIFIC-CHANNELS")
        if self.specific_channels:
            wrapper = ET.Element("SPECIFIC-CHANNELS")
            for item in self.specific_channels:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_nodes (list to container "SUB-NODES")
        if self.sub_nodes:
            wrapper = ET.Element("SUB-NODES")
            for item in self.sub_nodes:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticComControl")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlClass":
        """Deserialize XML element to DiagnosticComControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticComControlClass, cls).deserialize(element)

        # Parse all_channelse_refs (list from container "ALL-CHANNELSE-REFS")
        obj.all_channelse_refs = []
        container = SerializationHelper.find_child_element(element, "ALL-CHANNELSE-REFS")
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
                    obj.all_channelse_refs.append(child_value)

        # Parse all_physical_refs (list from container "ALL-PHYSICAL-REFS")
        obj.all_physical_refs = []
        container = SerializationHelper.find_child_element(element, "ALL-PHYSICAL-REFS")
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
                    obj.all_physical_refs.append(child_value)

        # Parse specific_channels (list from container "SPECIFIC-CHANNELS")
        obj.specific_channels = []
        container = SerializationHelper.find_child_element(element, "SPECIFIC-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.specific_channels.append(child_value)

        # Parse sub_nodes (list from container "SUB-NODES")
        obj.sub_nodes = []
        container = SerializationHelper.find_child_element(element, "SUB-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_nodes.append(child_value)

        return obj



class DiagnosticComControlClassBuilder:
    """Builder for DiagnosticComControlClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DiagnosticComControlClass = DiagnosticComControlClass()


    def with_short_name(self, value: Identifier) -> "DiagnosticComControlClassBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DiagnosticComControlClassBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DiagnosticComControlClassBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "DiagnosticComControlClassBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "DiagnosticComControlClassBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DiagnosticComControlClassBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "DiagnosticComControlClassBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DiagnosticComControlClassBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "DiagnosticComControlClassBuilder":
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

    def with_all_channelses(self, items: list[CommunicationCluster]) -> "DiagnosticComControlClassBuilder":
        """Set all_channelses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.all_channelses = list(items) if items else []
        return self

    def with_all_physicals(self, items: list[any (EthernetPhysical)]) -> "DiagnosticComControlClassBuilder":
        """Set all_physicals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.all_physicals = list(items) if items else []
        return self

    def with_specific_channels(self, items: list[DiagnosticComControl]) -> "DiagnosticComControlClassBuilder":
        """Set specific_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.specific_channels = list(items) if items else []
        return self

    def with_sub_nodes(self, items: list[DiagnosticComControl]) -> "DiagnosticComControlClassBuilder":
        """Set sub_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_nodes = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DiagnosticComControlClassBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DiagnosticComControlClassBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_all_channelse(self, item: CommunicationCluster) -> "DiagnosticComControlClassBuilder":
        """Add a single item to all_channelses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.all_channelses.append(item)
        return self

    def clear_all_channelses(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from all_channelses list.

        Returns:
            self for method chaining
        """
        self._obj.all_channelses = []
        return self

    def add_all_physical(self, item: any (EthernetPhysical)) -> "DiagnosticComControlClassBuilder":
        """Add a single item to all_physicals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.all_physicals.append(item)
        return self

    def clear_all_physicals(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from all_physicals list.

        Returns:
            self for method chaining
        """
        self._obj.all_physicals = []
        return self

    def add_specific_channel(self, item: DiagnosticComControl) -> "DiagnosticComControlClassBuilder":
        """Add a single item to specific_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.specific_channels.append(item)
        return self

    def clear_specific_channels(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from specific_channels list.

        Returns:
            self for method chaining
        """
        self._obj.specific_channels = []
        return self

    def add_sub_node(self, item: DiagnosticComControl) -> "DiagnosticComControlClassBuilder":
        """Add a single item to sub_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_nodes.append(item)
        return self

    def clear_sub_nodes(self) -> "DiagnosticComControlClassBuilder":
        """Clear all items from sub_nodes list.

        Returns:
            self for method chaining
        """
        self._obj.sub_nodes = []
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


    def build(self) -> DiagnosticComControlClass:
        """Build and return the DiagnosticComControlClass instance with validation."""
        self._validate_instance()
        pass
        return self._obj