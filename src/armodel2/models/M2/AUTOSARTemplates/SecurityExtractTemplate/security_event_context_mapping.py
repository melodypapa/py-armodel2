"""SecurityEventContextMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import (
    IdsMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import IdsMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_instance import (
    IdsmInstance,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventContextMapping(IdsMapping, ABC):
    """AUTOSAR SecurityEventContextMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    filter_chain_ref: Optional[Any]
    idsm_instance_ref: Optional[ARRef]
    mapped_securities: list[Any]
    _DESERIALIZE_DISPATCH = {
        "FILTER-CHAIN-REF": lambda obj, elem: setattr(obj, "filter_chain_ref", ARRef.deserialize(elem)),
        "IDSM-INSTANCE-REF": lambda obj, elem: setattr(obj, "idsm_instance_ref", ARRef.deserialize(elem)),
        "MAPPED-SECURITYS": lambda obj, elem: obj.mapped_securities.append(SerializationHelper.deserialize_by_tag(elem, "any (SecurityEventContext)")),
    }


    def __init__(self) -> None:
        """Initialize SecurityEventContextMapping."""
        super().__init__()
        self.filter_chain_ref: Optional[Any] = None
        self.idsm_instance_ref: Optional[ARRef] = None
        self.mapped_securities: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize filter_chain_ref
        if self.filter_chain_ref is not None:
            serialized = SerializationHelper.serialize_item(self.filter_chain_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-CHAIN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize idsm_instance_ref
        if self.idsm_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.idsm_instance_ref, "IdsmInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDSM-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_securities (list to container "MAPPED-SECURITYS")
        if self.mapped_securities:
            wrapper = ET.Element("MAPPED-SECURITYS")
            for item in self.mapped_securities:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMapping":
        """Deserialize XML element to SecurityEventContextMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FILTER-CHAIN-REF":
                setattr(obj, "filter_chain_ref", ARRef.deserialize(child))
            elif tag == "IDSM-INSTANCE-REF":
                setattr(obj, "idsm_instance_ref", ARRef.deserialize(child))
            elif tag == "MAPPED-SECURITYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mapped_securities.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SecurityEventContext)"))

        return obj



class SecurityEventContextMappingBuilder(IdsMappingBuilder):
    """Builder for SecurityEventContextMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventContextMapping = SecurityEventContextMapping()


    def with_filter_chain(self, value: Optional[any (SecurityEventFilter)]) -> "SecurityEventContextMappingBuilder":
        """Set filter_chain attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter_chain = value
        return self

    def with_idsm_instance(self, value: Optional[IdsmInstance]) -> "SecurityEventContextMappingBuilder":
        """Set idsm_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.idsm_instance = value
        return self

    def with_mapped_securities(self, items: list[any (SecurityEventContext)]) -> "SecurityEventContextMappingBuilder":
        """Set mapped_securities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mapped_securities = list(items) if items else []
        return self


    def add_mapped_security(self, item: any (SecurityEventContext)) -> "SecurityEventContextMappingBuilder":
        """Add a single item to mapped_securities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mapped_securities.append(item)
        return self

    def clear_mapped_securities(self) -> "SecurityEventContextMappingBuilder":
        """Clear all items from mapped_securities list.

        Returns:
            self for method chaining
        """
        self._obj.mapped_securities = []
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
    def build(self) -> SecurityEventContextMapping:
        """Build and return the SecurityEventContextMapping instance (abstract)."""
        raise NotImplementedError