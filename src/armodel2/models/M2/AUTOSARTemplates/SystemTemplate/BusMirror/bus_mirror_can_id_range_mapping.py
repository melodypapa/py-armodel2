"""BusMirrorCanIdRangeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BusMirrorCanIdRangeMapping(ARObject):
    """AUTOSAR BusMirrorCanIdRangeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_base: Optional[PositiveInteger]
    source_can_id_code: Optional[PositiveInteger]
    source_can_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BusMirrorCanIdRangeMapping."""
        super().__init__()
        self.destination_base: Optional[PositiveInteger] = None
        self.source_can_id_code: Optional[PositiveInteger] = None
        self.source_can_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorCanIdRangeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorCanIdRangeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_base
        if self.destination_base is not None:
            serialized = SerializationHelper.serialize_item(self.destination_base, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_can_id_code
        if self.source_can_id_code is not None:
            serialized = SerializationHelper.serialize_item(self.source_can_id_code, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CAN-ID-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_can_id
        if self.source_can_id is not None:
            serialized = SerializationHelper.serialize_item(self.source_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdRangeMapping":
        """Deserialize XML element to BusMirrorCanIdRangeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdRangeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorCanIdRangeMapping, cls).deserialize(element)

        # Parse destination_base
        child = SerializationHelper.find_child_element(element, "DESTINATION-BASE")
        if child is not None:
            destination_base_value = child.text
            obj.destination_base = destination_base_value

        # Parse source_can_id_code
        child = SerializationHelper.find_child_element(element, "SOURCE-CAN-ID-CODE")
        if child is not None:
            source_can_id_code_value = child.text
            obj.source_can_id_code = source_can_id_code_value

        # Parse source_can_id
        child = SerializationHelper.find_child_element(element, "SOURCE-CAN-ID")
        if child is not None:
            source_can_id_value = child.text
            obj.source_can_id = source_can_id_value

        return obj



class BusMirrorCanIdRangeMappingBuilder(BuilderBase):
    """Builder for BusMirrorCanIdRangeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BusMirrorCanIdRangeMapping = BusMirrorCanIdRangeMapping()


    def with_destination_base(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdRangeMappingBuilder":
        """Set destination_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_base = value
        return self

    def with_source_can_id_code(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdRangeMappingBuilder":
        """Set source_can_id_code attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_can_id_code = value
        return self

    def with_source_can_id(self, value: Optional[PositiveInteger]) -> "BusMirrorCanIdRangeMappingBuilder":
        """Set source_can_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_can_id = value
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


    def build(self) -> BusMirrorCanIdRangeMapping:
        """Build and return the BusMirrorCanIdRangeMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj