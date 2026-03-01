"""DiagnosticMemoryDestinationUserDefined AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import DiagnosticMemoryDestinationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticMemoryDestinationUserDefined(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationUserDefined."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED"


    auth_role_refs: list[ARRef]
    memory_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "AUTH-ROLE-REFS": lambda obj, elem: [obj.auth_role_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MEMORY-ID": lambda obj, elem: setattr(obj, "memory_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationUserDefined."""
        super().__init__()
        self.auth_role_refs: list[ARRef] = []
        self.memory_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryDestinationUserDefined to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryDestinationUserDefined, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auth_role_refs (list to container "AUTH-ROLE-REFS")
        if self.auth_role_refs:
            wrapper = ET.Element("AUTH-ROLE-REFS")
            for item in self.auth_role_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticAuthRole")
                if serialized is not None:
                    child_elem = ET.Element("AUTH-ROLE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize memory_id
        if self.memory_id is not None:
            serialized = SerializationHelper.serialize_item(self.memory_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestinationUserDefined":
        """Deserialize XML element to DiagnosticMemoryDestinationUserDefined object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryDestinationUserDefined object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryDestinationUserDefined, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTH-ROLE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.auth_role_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MEMORY-ID":
                setattr(obj, "memory_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticMemoryDestinationUserDefinedBuilder(DiagnosticMemoryDestinationBuilder):
    """Builder for DiagnosticMemoryDestinationUserDefined with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticMemoryDestinationUserDefined = DiagnosticMemoryDestinationUserDefined()


    def with_auth_roles(self, items: list[DiagnosticAuthRole]) -> "DiagnosticMemoryDestinationUserDefinedBuilder":
        """Set auth_roles list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.auth_roles = list(items) if items else []
        return self

    def with_memory_id(self, value: Optional[PositiveInteger]) -> "DiagnosticMemoryDestinationUserDefinedBuilder":
        """Set memory_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.memory_id = value
        return self


    def add_auth_role(self, item: DiagnosticAuthRole) -> "DiagnosticMemoryDestinationUserDefinedBuilder":
        """Add a single item to auth_roles list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.auth_roles.append(item)
        return self

    def clear_auth_roles(self) -> "DiagnosticMemoryDestinationUserDefinedBuilder":
        """Clear all items from auth_roles list.

        Returns:
            self for method chaining
        """
        self._obj.auth_roles = []
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


    def build(self) -> DiagnosticMemoryDestinationUserDefined:
        """Build and return the DiagnosticMemoryDestinationUserDefined instance with validation."""
        self._validate_instance()
        pass
        return self._obj