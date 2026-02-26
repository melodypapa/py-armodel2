"""MetaDataItem AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 98)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.text_value_specification import (
    TextValueSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MetaDataItem(ARObject):
    """AUTOSAR MetaDataItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    length: Optional[PositiveInteger]
    meta_data_item: Optional[TextValueSpecification]
    def __init__(self) -> None:
        """Initialize MetaDataItem."""
        super().__init__()
        self.length: Optional[PositiveInteger] = None
        self.meta_data_item: Optional[TextValueSpecification] = None

    def serialize(self) -> ET.Element:
        """Serialize MetaDataItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MetaDataItem, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize meta_data_item
        if self.meta_data_item is not None:
            serialized = SerializationHelper.serialize_item(self.meta_data_item, "TextValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("META-DATA-ITEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItem":
        """Deserialize XML element to MetaDataItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MetaDataItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MetaDataItem, cls).deserialize(element)

        # Parse length
        child = SerializationHelper.find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        # Parse meta_data_item
        child = SerializationHelper.find_child_element(element, "META-DATA-ITEM")
        if child is not None:
            meta_data_item_value = SerializationHelper.deserialize_by_tag(child, "TextValueSpecification")
            obj.meta_data_item = meta_data_item_value

        return obj



class MetaDataItemBuilder(BuilderBase):
    """Builder for MetaDataItem with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MetaDataItem = MetaDataItem()


    def with_length(self, value: Optional[PositiveInteger]) -> "MetaDataItemBuilder":
        """Set length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.length = value
        return self

    def with_meta_data_item(self, value: Optional[TextValueSpecification]) -> "MetaDataItemBuilder":
        """Set meta_data_item attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.meta_data_item = value
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


    def build(self) -> MetaDataItem:
        """Build and return the MetaDataItem instance with validation."""
        self._validate_instance()
        pass
        return self._obj