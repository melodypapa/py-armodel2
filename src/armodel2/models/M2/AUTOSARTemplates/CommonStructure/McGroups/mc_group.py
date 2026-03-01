"""McGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 190)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2034)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_McGroups.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.McGroups.mc_group_data_ref_set import (
    McGroupDataRefSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class McGroup(ARElement):
    """AUTOSAR McGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-GROUP"


    mc_function_refs: list[ARRef]
    ref_calprm_set_ref: Optional[ARRef]
    ref_ref: Optional[ARRef]
    sub_group_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MC-FUNCTIONS": lambda obj, elem: obj.mc_function_refs.append(ARRef.deserialize(elem)),
        "REF-CALPRM-SET-REF": lambda obj, elem: setattr(obj, "ref_calprm_set_ref", ARRef.deserialize(elem)),
        "REF-REF": lambda obj, elem: setattr(obj, "ref_ref", ARRef.deserialize(elem)),
        "SUB-GROUPS": lambda obj, elem: obj.sub_group_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize McGroup."""
        super().__init__()
        self.mc_function_refs: list[ARRef] = []
        self.ref_calprm_set_ref: Optional[ARRef] = None
        self.ref_ref: Optional[ARRef] = None
        self.sub_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize McGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mc_function_refs (list to container "MC-FUNCTION-REFS")
        if self.mc_function_refs:
            wrapper = ET.Element("MC-FUNCTION-REFS")
            for item in self.mc_function_refs:
                serialized = SerializationHelper.serialize_item(item, "McFunction")
                if serialized is not None:
                    child_elem = ET.Element("MC-FUNCTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ref_calprm_set_ref
        if self.ref_calprm_set_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ref_calprm_set_ref, "McGroupDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF-CALPRM-SET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ref_ref
        if self.ref_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ref_ref, "McGroupDataRefSet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_group_refs (list to container "SUB-GROUP-REFS")
        if self.sub_group_refs:
            wrapper = ET.Element("SUB-GROUP-REFS")
            for item in self.sub_group_refs:
                serialized = SerializationHelper.serialize_item(item, "McGroup")
                if serialized is not None:
                    child_elem = ET.Element("SUB-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McGroup":
        """Deserialize XML element to McGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "MC-FUNCTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.mc_function_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "McFunction"))
            elif tag == "REF-CALPRM-SET-REF":
                setattr(obj, "ref_calprm_set_ref", ARRef.deserialize(child))
            elif tag == "REF-REF":
                setattr(obj, "ref_ref", ARRef.deserialize(child))
            elif tag == "SUB-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sub_group_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "McGroup"))

        return obj



class McGroupBuilder(ARElementBuilder):
    """Builder for McGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McGroup = McGroup()


    def with_mc_functions(self, items: list[McFunction]) -> "McGroupBuilder":
        """Set mc_functions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_functions = list(items) if items else []
        return self

    def with_ref_calprm_set(self, value: Optional[McGroupDataRefSet]) -> "McGroupBuilder":
        """Set ref_calprm_set attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ref_calprm_set = value
        return self

    def with_ref(self, value: Optional[McGroupDataRefSet]) -> "McGroupBuilder":
        """Set ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ref = value
        return self

    def with_sub_groups(self, items: list[McGroup]) -> "McGroupBuilder":
        """Set sub_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_groups = list(items) if items else []
        return self


    def add_mc_function(self, item: McFunction) -> "McGroupBuilder":
        """Add a single item to mc_functions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_functions.append(item)
        return self

    def clear_mc_functions(self) -> "McGroupBuilder":
        """Clear all items from mc_functions list.

        Returns:
            self for method chaining
        """
        self._obj.mc_functions = []
        return self

    def add_sub_group(self, item: McGroup) -> "McGroupBuilder":
        """Add a single item to sub_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_groups.append(item)
        return self

    def clear_sub_groups(self) -> "McGroupBuilder":
        """Clear all items from sub_groups list.

        Returns:
            self for method chaining
        """
        self._obj.sub_groups = []
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


    def build(self) -> McGroup:
        """Build and return the McGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj