"""DataTypeMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_map import (
        DataTypeMap,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_request_type_map import (
        ModeRequestTypeMap,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class DataTypeMappingSet(ARElement):
    """AUTOSAR DataTypeMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-TYPE-MAPPING-SET"


    data_type_maps: list[DataTypeMap]
    mode_request_type_maps: list[ModeRequestTypeMap]
    _DESERIALIZE_DISPATCH = {
        "DATA-TYPE-MAPS": lambda obj, elem: obj.data_type_maps.append(SerializationHelper.deserialize_by_tag(elem, "DataTypeMap")),
        "MODE-REQUEST-TYPE-MAPS": lambda obj, elem: obj.mode_request_type_maps.append(SerializationHelper.deserialize_by_tag(elem, "ModeRequestTypeMap")),
    }


    def __init__(self) -> None:
        """Initialize DataTypeMappingSet."""
        super().__init__()
        self.data_type_maps: list[DataTypeMap] = []
        self.mode_request_type_maps: list[ModeRequestTypeMap] = []

    def serialize(self) -> ET.Element:
        """Serialize DataTypeMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataTypeMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_type_maps (list to container "DATA-TYPE-MAPS")
        if self.data_type_maps:
            wrapper = ET.Element("DATA-TYPE-MAPS")
            for item in self.data_type_maps:
                serialized = SerializationHelper.serialize_item(item, "DataTypeMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_request_type_maps (list to container "MODE-REQUEST-TYPE-MAPS")
        if self.mode_request_type_maps:
            wrapper = ET.Element("MODE-REQUEST-TYPE-MAPS")
            for item in self.mode_request_type_maps:
                serialized = SerializationHelper.serialize_item(item, "ModeRequestTypeMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTypeMappingSet":
        """Deserialize XML element to DataTypeMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTypeMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTypeMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DATA-TYPE-MAPS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.data_type_maps.append(SerializationHelper.deserialize_by_tag(item_elem, "DataTypeMap"))
            elif tag == "MODE-REQUEST-TYPE-MAPS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.mode_request_type_maps.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeRequestTypeMap"))

        return obj



class DataTypeMappingSetBuilder(ARElementBuilder):
    """Builder for DataTypeMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataTypeMappingSet = DataTypeMappingSet()


    def with_data_type_maps(self, items: list[DataTypeMap]) -> "DataTypeMappingSetBuilder":
        """Set data_type_maps list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_type_maps = list(items) if items else []
        return self

    def with_mode_request_type_maps(self, items: list[ModeRequestTypeMap]) -> "DataTypeMappingSetBuilder":
        """Set mode_request_type_maps list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_request_type_maps = list(items) if items else []
        return self


    def add_data_type_map(self, item: DataTypeMap) -> "DataTypeMappingSetBuilder":
        """Add a single item to data_type_maps list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_type_maps.append(item)
        return self

    def clear_data_type_maps(self) -> "DataTypeMappingSetBuilder":
        """Clear all items from data_type_maps list.

        Returns:
            self for method chaining
        """
        self._obj.data_type_maps = []
        return self

    def add_mode_request_type_map(self, item: ModeRequestTypeMap) -> "DataTypeMappingSetBuilder":
        """Add a single item to mode_request_type_maps list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_request_type_maps.append(item)
        return self

    def clear_mode_request_type_maps(self) -> "DataTypeMappingSetBuilder":
        """Clear all items from mode_request_type_maps list.

        Returns:
            self for method chaining
        """
        self._obj.mode_request_type_maps = []
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


    def build(self) -> DataTypeMappingSet:
        """Build and return the DataTypeMappingSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj