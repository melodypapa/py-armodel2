"""DiagnosticConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 632)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)


class DiagnosticConnection(ARElement):
    """AUTOSAR DiagnosticConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    functional_request_refs: list[ARRef]
    periodic_response_uudt_refs: list[ARRef]
    physical_request_ref: Optional[ARRef]
    response_ref: Optional[ARRef]
    response_on_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticConnection."""
        super().__init__()
        self.functional_request_refs: list[ARRef] = []
        self.periodic_response_uudt_refs: list[ARRef] = []
        self.physical_request_ref: Optional[ARRef] = None
        self.response_ref: Optional[ARRef] = None
        self.response_on_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize functional_request_refs (list to container "FUNCTIONAL-REQUEST-REFS")
        if self.functional_request_refs:
            wrapper = ET.Element("FUNCTIONAL-REQUEST-REFS")
            for item in self.functional_request_refs:
                serialized = SerializationHelper.serialize_item(item, "TpConnectionIdent")
                if serialized is not None:
                    child_elem = ET.Element("FUNCTIONAL-REQUEST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize periodic_response_uudt_refs (list to container "PERIODIC-RESPONSE-UUDT-REFS")
        if self.periodic_response_uudt_refs:
            wrapper = ET.Element("PERIODIC-RESPONSE-UUDT-REFS")
            for item in self.periodic_response_uudt_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("PERIODIC-RESPONSE-UUDT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_request_ref
        if self.physical_request_ref is not None:
            serialized = SerializationHelper.serialize_item(self.physical_request_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-REQUEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_ref
        if self.response_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_on_ref
        if self.response_on_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_on_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnection":
        """Deserialize XML element to DiagnosticConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticConnection, cls).deserialize(element)

        # Parse functional_request_refs (list from container "FUNCTIONAL-REQUEST-REFS")
        obj.functional_request_refs = []
        container = SerializationHelper.find_child_element(element, "FUNCTIONAL-REQUEST-REFS")
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
                    obj.functional_request_refs.append(child_value)

        # Parse periodic_response_uudt_refs (list from container "PERIODIC-RESPONSE-UUDT-REFS")
        obj.periodic_response_uudt_refs = []
        container = SerializationHelper.find_child_element(element, "PERIODIC-RESPONSE-UUDT-REFS")
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
                    obj.periodic_response_uudt_refs.append(child_value)

        # Parse physical_request_ref
        child = SerializationHelper.find_child_element(element, "PHYSICAL-REQUEST-REF")
        if child is not None:
            physical_request_ref_value = ARRef.deserialize(child)
            obj.physical_request_ref = physical_request_ref_value

        # Parse response_ref
        child = SerializationHelper.find_child_element(element, "RESPONSE-REF")
        if child is not None:
            response_ref_value = ARRef.deserialize(child)
            obj.response_ref = response_ref_value

        # Parse response_on_ref
        child = SerializationHelper.find_child_element(element, "RESPONSE-ON-REF")
        if child is not None:
            response_on_ref_value = ARRef.deserialize(child)
            obj.response_on_ref = response_on_ref_value

        return obj



class DiagnosticConnectionBuilder:
    """Builder for DiagnosticConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DiagnosticConnection = DiagnosticConnection()


    def with_short_name(self, value: Identifier) -> "DiagnosticConnectionBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DiagnosticConnectionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DiagnosticConnectionBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "DiagnosticConnectionBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "DiagnosticConnectionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DiagnosticConnectionBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "DiagnosticConnectionBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DiagnosticConnectionBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "DiagnosticConnectionBuilder":
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

    def with_functional_requests(self, items: list[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set functional_requests list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.functional_requests = list(items) if items else []
        return self

    def with_periodic_response_uudts(self, items: list[PduTriggering]) -> "DiagnosticConnectionBuilder":
        """Set periodic_response_uudts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.periodic_response_uudts = list(items) if items else []
        return self

    def with_physical_request(self, value: Optional[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set physical_request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_request = value
        return self

    def with_response(self, value: Optional[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set response attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response = value
        return self

    def with_response_on(self, value: Optional[TpConnectionIdent]) -> "DiagnosticConnectionBuilder":
        """Set response_on attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_on = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DiagnosticConnectionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DiagnosticConnectionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DiagnosticConnectionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DiagnosticConnectionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_functional_request(self, item: TpConnectionIdent) -> "DiagnosticConnectionBuilder":
        """Add a single item to functional_requests list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.functional_requests.append(item)
        return self

    def clear_functional_requests(self) -> "DiagnosticConnectionBuilder":
        """Clear all items from functional_requests list.

        Returns:
            self for method chaining
        """
        self._obj.functional_requests = []
        return self

    def add_periodic_response_uudt(self, item: PduTriggering) -> "DiagnosticConnectionBuilder":
        """Add a single item to periodic_response_uudts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.periodic_response_uudts.append(item)
        return self

    def clear_periodic_response_uudts(self) -> "DiagnosticConnectionBuilder":
        """Clear all items from periodic_response_uudts list.

        Returns:
            self for method chaining
        """
        self._obj.periodic_response_uudts = []
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


    def build(self) -> DiagnosticConnection:
        """Build and return the DiagnosticConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj