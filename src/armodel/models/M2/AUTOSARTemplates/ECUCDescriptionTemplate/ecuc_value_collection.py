"""EcucValueCollection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 108)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2022)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class EcucValueCollection(ARElement):
    """AUTOSAR EcucValueCollection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_value_refs: list[Any]
    ecu_extract_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcucValueCollection."""
        super().__init__()
        self.ecuc_value_refs: list[Any] = []
        self.ecu_extract_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucValueCollection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucValueCollection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_value_refs (list to container "ECUC-VALUE-REFS")
        if self.ecuc_value_refs:
            wrapper = ET.Element("ECUC-VALUE-REFS")
            for item in self.ecuc_value_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ECUC-VALUE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_extract_ref
        if self.ecu_extract_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_extract_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-EXTRACT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValueCollection":
        """Deserialize XML element to EcucValueCollection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucValueCollection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucValueCollection, cls).deserialize(element)

        # Parse ecuc_value_refs (list from container "ECUC-VALUE-REFS")
        obj.ecuc_value_refs = []
        container = SerializationHelper.find_child_element(element, "ECUC-VALUE-REFS")
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
                    obj.ecuc_value_refs.append(child_value)

        # Parse ecu_extract_ref
        child = SerializationHelper.find_child_element(element, "ECU-EXTRACT-REF")
        if child is not None:
            ecu_extract_ref_value = ARRef.deserialize(child)
            obj.ecu_extract_ref = ecu_extract_ref_value

        return obj



class EcucValueCollectionBuilder(ARElementBuilder):
    """Builder for EcucValueCollection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucValueCollection = EcucValueCollection()


    def with_ecuc_values(self, items: list[any (EcucModule)]) -> "EcucValueCollectionBuilder":
        """Set ecuc_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_values = list(items) if items else []
        return self

    def with_ecu_extract(self, value: Optional[System]) -> "EcucValueCollectionBuilder":
        """Set ecu_extract attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_extract = value
        return self


    def add_ecuc_value(self, item: any (EcucModule)) -> "EcucValueCollectionBuilder":
        """Add a single item to ecuc_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_values.append(item)
        return self

    def clear_ecuc_values(self) -> "EcucValueCollectionBuilder":
        """Clear all items from ecuc_values list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_values = []
        return self



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


    def build(self) -> EcucValueCollection:
        """Build and return the EcucValueCollection instance with validation."""
        self._validate_instance()
        pass
        return self._obj