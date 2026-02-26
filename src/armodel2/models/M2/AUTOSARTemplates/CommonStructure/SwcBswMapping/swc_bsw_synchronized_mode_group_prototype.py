"""SwcBswSynchronizedModeGroupPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """AUTOSAR SwcBswSynchronizedModeGroupPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_mode_group_prototype_ref: Optional[ARRef]
    swc_mode_group_swc_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedModeGroupPrototype."""
        super().__init__()
        self.bsw_mode_group_prototype_ref: Optional[ARRef] = None
        self.swc_mode_group_swc_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcBswSynchronizedModeGroupPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcBswSynchronizedModeGroupPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_mode_group_prototype_ref
        if self.bsw_mode_group_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_mode_group_prototype_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODE-GROUP-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_mode_group_swc_instance_ref
        if self.swc_mode_group_swc_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_mode_group_swc_instance_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-MODE-GROUP-SWC-INSTANCE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswSynchronizedModeGroupPrototype":
        """Deserialize XML element to SwcBswSynchronizedModeGroupPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswSynchronizedModeGroupPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcBswSynchronizedModeGroupPrototype, cls).deserialize(element)

        # Parse bsw_mode_group_prototype_ref
        child = SerializationHelper.find_child_element(element, "BSW-MODE-GROUP-PROTOTYPE-REF")
        if child is not None:
            bsw_mode_group_prototype_ref_value = ARRef.deserialize(child)
            obj.bsw_mode_group_prototype_ref = bsw_mode_group_prototype_ref_value

        # Parse swc_mode_group_swc_instance_ref
        child = SerializationHelper.find_child_element(element, "SWC-MODE-GROUP-SWC-INSTANCE-REF-REF")
        if child is not None:
            swc_mode_group_swc_instance_ref_value = ARRef.deserialize(child)
            obj.swc_mode_group_swc_instance_ref = swc_mode_group_swc_instance_ref_value

        return obj



class SwcBswSynchronizedModeGroupPrototypeBuilder(BuilderBase):
    """Builder for SwcBswSynchronizedModeGroupPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcBswSynchronizedModeGroupPrototype = SwcBswSynchronizedModeGroupPrototype()


    def with_bsw_mode_group_prototype(self, value: Optional[ModeDeclarationGroup]) -> "SwcBswSynchronizedModeGroupPrototypeBuilder":
        """Set bsw_mode_group_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_mode_group_prototype = value
        return self

    def with_swc_mode_group_swc_instance_ref(self, value: Optional[ModeDeclarationGroup]) -> "SwcBswSynchronizedModeGroupPrototypeBuilder":
        """Set swc_mode_group_swc_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_mode_group_swc_instance_ref = value
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


    def build(self) -> SwcBswSynchronizedModeGroupPrototype:
        """Build and return the SwcBswSynchronizedModeGroupPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj