"""Xref AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 320)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)


class Xref(ARObject):
    """AUTOSAR Xref."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label1: Optional[SingleLanguageLongName]
    referrable_ref: Optional[ARRef]
    resolution_policy_enum: Optional[ResolutionPolicyEnum]
    show_content_enum: Optional[ShowContentEnum]
    show_resource_alias: Optional[ShowResourceAliasNameEnum]
    show_resource: Optional[ShowResourceTypeEnum]
    show_resource_long: Optional[ShowResourceLongNameEnum]
    show_resource_number: Optional[ShowResourceNumberEnum]
    show_resource_page: Optional[ShowResourcePageEnum]
    show_resource_short: Optional[ShowResourceShortNameEnum]
    show_see: Optional[ShowSeeEnum]
    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable_ref: Optional[ARRef] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Xref to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xref, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label1
        if self.label1 is not None:
            serialized = SerializationHelper.serialize_item(self.label1, "SingleLanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize referrable_ref
        if self.referrable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.referrable_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERRABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resolution_policy_enum
        if self.resolution_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.resolution_policy_enum, "ResolutionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOLUTION-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_content_enum
        if self.show_content_enum is not None:
            serialized = SerializationHelper.serialize_item(self.show_content_enum, "ShowContentEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-CONTENT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_alias
        if self.show_resource_alias is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_alias, "ShowResourceAliasNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-ALIAS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource
        if self.show_resource is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource, "ShowResourceTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_long
        if self.show_resource_long is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_long, "ShowResourceLongNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-LONG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_number
        if self.show_resource_number is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_number, "ShowResourceNumberEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_page
        if self.show_resource_page is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_page, "ShowResourcePageEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-PAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_short
        if self.show_resource_short is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_short, "ShowResourceShortNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-SHORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_see
        if self.show_see is not None:
            serialized = SerializationHelper.serialize_item(self.show_see, "ShowSeeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-SEE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xref":
        """Deserialize XML element to Xref object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xref object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xref, cls).deserialize(element)

        # Parse label1
        child = SerializationHelper.find_child_element(element, "LABEL1")
        if child is not None:
            label1_value = SerializationHelper.deserialize_by_tag(child, "SingleLanguageLongName")
            obj.label1 = label1_value

        # Parse referrable_ref
        child = SerializationHelper.find_child_element(element, "REFERRABLE-REF")
        if child is not None:
            referrable_ref_value = ARRef.deserialize(child)
            obj.referrable_ref = referrable_ref_value

        # Parse resolution_policy_enum
        child = SerializationHelper.find_child_element(element, "RESOLUTION-POLICY-ENUM")
        if child is not None:
            resolution_policy_enum_value = ResolutionPolicyEnum.deserialize(child)
            obj.resolution_policy_enum = resolution_policy_enum_value

        # Parse show_content_enum
        child = SerializationHelper.find_child_element(element, "SHOW-CONTENT-ENUM")
        if child is not None:
            show_content_enum_value = ShowContentEnum.deserialize(child)
            obj.show_content_enum = show_content_enum_value

        # Parse show_resource_alias
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-ALIAS")
        if child is not None:
            show_resource_alias_value = ShowResourceAliasNameEnum.deserialize(child)
            obj.show_resource_alias = show_resource_alias_value

        # Parse show_resource
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE")
        if child is not None:
            show_resource_value = ShowResourceTypeEnum.deserialize(child)
            obj.show_resource = show_resource_value

        # Parse show_resource_long
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-LONG")
        if child is not None:
            show_resource_long_value = ShowResourceLongNameEnum.deserialize(child)
            obj.show_resource_long = show_resource_long_value

        # Parse show_resource_number
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-NUMBER")
        if child is not None:
            show_resource_number_value = ShowResourceNumberEnum.deserialize(child)
            obj.show_resource_number = show_resource_number_value

        # Parse show_resource_page
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-PAGE")
        if child is not None:
            show_resource_page_value = ShowResourcePageEnum.deserialize(child)
            obj.show_resource_page = show_resource_page_value

        # Parse show_resource_short
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-SHORT")
        if child is not None:
            show_resource_short_value = ShowResourceShortNameEnum.deserialize(child)
            obj.show_resource_short = show_resource_short_value

        # Parse show_see
        child = SerializationHelper.find_child_element(element, "SHOW-SEE")
        if child is not None:
            show_see_value = ShowSeeEnum.deserialize(child)
            obj.show_see = show_see_value

        return obj



class XrefBuilder:
    """Builder for Xref with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: Xref = Xref()


    def with_label1(self, value: Optional[SingleLanguageLongName]) -> "XrefBuilder":
        """Set label1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label1 = value
        return self

    def with_referrable(self, value: Optional[Referrable]) -> "XrefBuilder":
        """Set referrable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.referrable = value
        return self

    def with_resolution_policy_enum(self, value: Optional[ResolutionPolicyEnum]) -> "XrefBuilder":
        """Set resolution_policy_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resolution_policy_enum = value
        return self

    def with_show_content_enum(self, value: Optional[ShowContentEnum]) -> "XrefBuilder":
        """Set show_content_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_content_enum = value
        return self

    def with_show_resource_alias(self, value: Optional[ShowResourceAliasNameEnum]) -> "XrefBuilder":
        """Set show_resource_alias attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_alias = value
        return self

    def with_show_resource(self, value: Optional[ShowResourceTypeEnum]) -> "XrefBuilder":
        """Set show_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource = value
        return self

    def with_show_resource_long(self, value: Optional[ShowResourceLongNameEnum]) -> "XrefBuilder":
        """Set show_resource_long attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_long = value
        return self

    def with_show_resource_number(self, value: Optional[ShowResourceNumberEnum]) -> "XrefBuilder":
        """Set show_resource_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_number = value
        return self

    def with_show_resource_page(self, value: Optional[ShowResourcePageEnum]) -> "XrefBuilder":
        """Set show_resource_page attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_page = value
        return self

    def with_show_resource_short(self, value: Optional[ShowResourceShortNameEnum]) -> "XrefBuilder":
        """Set show_resource_short attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_short = value
        return self

    def with_show_see(self, value: Optional[ShowSeeEnum]) -> "XrefBuilder":
        """Set show_see attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_see = value
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


    def build(self) -> Xref:
        """Build and return the Xref instance with validation."""
        self._validate_instance()
        pass
        return self._obj