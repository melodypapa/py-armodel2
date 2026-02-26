"""AliasNameAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 175)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AliasNameAssignment(ARObject):
    """AUTOSAR AliasNameAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_instance_ref: Optional[ARRef]
    identifiable_ref: Optional[ARRef]
    label: Optional[MultilanguageLongName]
    short_label: Optional[String]
    def __init__(self) -> None:
        """Initialize AliasNameAssignment."""
        super().__init__()
        self.flat_instance_ref: Optional[ARRef] = None
        self.identifiable_ref: Optional[ARRef] = None
        self.label: Optional[MultilanguageLongName] = None
        self.short_label: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize AliasNameAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AliasNameAssignment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize flat_instance_ref
        if self.flat_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flat_instance_ref, "FlatInstanceDescriptor")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identifiable_ref
        if self.identifiable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.identifiable_ref, "Identifiable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameAssignment":
        """Deserialize XML element to AliasNameAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameAssignment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AliasNameAssignment, cls).deserialize(element)

        # Parse flat_instance_ref
        child = SerializationHelper.find_child_element(element, "FLAT-INSTANCE-REF")
        if child is not None:
            flat_instance_ref_value = ARRef.deserialize(child)
            obj.flat_instance_ref = flat_instance_ref_value

        # Parse identifiable_ref
        child = SerializationHelper.find_child_element(element, "IDENTIFIABLE-REF")
        if child is not None:
            identifiable_ref_value = ARRef.deserialize(child)
            obj.identifiable_ref = identifiable_ref_value

        # Parse label
        child = SerializationHelper.find_child_element(element, "LABEL")
        if child is not None:
            label_value = SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class AliasNameAssignmentBuilder(BuilderBase):
    """Builder for AliasNameAssignment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AliasNameAssignment = AliasNameAssignment()


    def with_flat_instance(self, value: Optional[FlatInstanceDescriptor]) -> "AliasNameAssignmentBuilder":
        """Set flat_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flat_instance = value
        return self

    def with_identifiable(self, value: Optional[Identifiable]) -> "AliasNameAssignmentBuilder":
        """Set identifiable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.identifiable = value
        return self

    def with_label(self, value: Optional[MultilanguageLongName]) -> "AliasNameAssignmentBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label = value
        return self

    def with_short_label(self, value: Optional[String]) -> "AliasNameAssignmentBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
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


    def build(self) -> AliasNameAssignment:
        """Build and return the AliasNameAssignment instance with validation."""
        self._validate_instance()
        pass
        return self._obj