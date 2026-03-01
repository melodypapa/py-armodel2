"""FMFeatureMapElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
        FMFeatureMap,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class FMFeatureMapElement(Identifiable):
    """AUTOSAR FMFeatureMapElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "F-M-FEATURE-MAP-ELEMENT"


    assertions: list[FMFeatureMap]
    conditions: list[FMFeatureMap]
    post_build_variant_refs: list[Any]
    sw_value_set_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ASSERTIONS": lambda obj, elem: obj.assertions.append(SerializationHelper.deserialize_by_tag(elem, "FMFeatureMap")),
        "CONDITIONS": lambda obj, elem: obj.conditions.append(SerializationHelper.deserialize_by_tag(elem, "FMFeatureMap")),
        "POST-BUILD-VARIANTS": lambda obj, elem: obj.post_build_variant_refs.append(ARRef.deserialize(elem)),
        "SW-VALUE-SETS": lambda obj, elem: obj.sw_value_set_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize FMFeatureMapElement."""
        super().__init__()
        self.assertions: list[FMFeatureMap] = []
        self.conditions: list[FMFeatureMap] = []
        self.post_build_variant_refs: list[Any] = []
        self.sw_value_set_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureMapElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureMapElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assertions (list to container "ASSERTIONS")
        if self.assertions:
            wrapper = ET.Element("ASSERTIONS")
            for item in self.assertions:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize conditions (list to container "CONDITIONS")
        if self.conditions:
            wrapper = ET.Element("CONDITIONS")
            for item in self.conditions:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize post_build_variant_refs (list to container "POST-BUILD-VARIANT-REFS")
        if self.post_build_variant_refs:
            wrapper = ET.Element("POST-BUILD-VARIANT-REFS")
            for item in self.post_build_variant_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("POST-BUILD-VARIANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_value_set_refs (list to container "SW-VALUE-SET-REFS")
        if self.sw_value_set_refs:
            wrapper = ET.Element("SW-VALUE-SET-REFS")
            for item in self.sw_value_set_refs:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("SW-VALUE-SET-REF")
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
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapElement":
        """Deserialize XML element to FMFeatureMapElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureMapElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureMapElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ASSERTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.assertions.append(SerializationHelper.deserialize_by_tag(item_elem, "FMFeatureMap"))
            elif tag == "CONDITIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.conditions.append(SerializationHelper.deserialize_by_tag(item_elem, "FMFeatureMap"))
            elif tag == "POST-BUILD-VARIANTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.post_build_variant_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (PostBuildVariant)"))
            elif tag == "SW-VALUE-SETS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.sw_value_set_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "SwSystemconstantValueSet"))

        return obj



class FMFeatureMapElementBuilder(IdentifiableBuilder):
    """Builder for FMFeatureMapElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFeatureMapElement = FMFeatureMapElement()


    def with_assertions(self, items: list[FMFeatureMap]) -> "FMFeatureMapElementBuilder":
        """Set assertions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assertions = list(items) if items else []
        return self

    def with_conditions(self, items: list[FMFeatureMap]) -> "FMFeatureMapElementBuilder":
        """Set conditions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.conditions = list(items) if items else []
        return self

    def with_post_build_variants(self, items: list[any (PostBuildVariant)]) -> "FMFeatureMapElementBuilder":
        """Set post_build_variants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants = list(items) if items else []
        return self

    def with_sw_value_sets(self, items: list[SwSystemconstantValueSet]) -> "FMFeatureMapElementBuilder":
        """Set sw_value_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_value_sets = list(items) if items else []
        return self


    def add_assertion(self, item: FMFeatureMap) -> "FMFeatureMapElementBuilder":
        """Add a single item to assertions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assertions.append(item)
        return self

    def clear_assertions(self) -> "FMFeatureMapElementBuilder":
        """Clear all items from assertions list.

        Returns:
            self for method chaining
        """
        self._obj.assertions = []
        return self

    def add_condition(self, item: FMFeatureMap) -> "FMFeatureMapElementBuilder":
        """Add a single item to conditions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.conditions.append(item)
        return self

    def clear_conditions(self) -> "FMFeatureMapElementBuilder":
        """Clear all items from conditions list.

        Returns:
            self for method chaining
        """
        self._obj.conditions = []
        return self

    def add_post_build_variant(self, item: any (PostBuildVariant)) -> "FMFeatureMapElementBuilder":
        """Add a single item to post_build_variants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants.append(item)
        return self

    def clear_post_build_variants(self) -> "FMFeatureMapElementBuilder":
        """Clear all items from post_build_variants list.

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants = []
        return self

    def add_sw_value_set(self, item: SwSystemconstantValueSet) -> "FMFeatureMapElementBuilder":
        """Add a single item to sw_value_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_value_sets.append(item)
        return self

    def clear_sw_value_sets(self) -> "FMFeatureMapElementBuilder":
        """Clear all items from sw_value_sets list.

        Returns:
            self for method chaining
        """
        self._obj.sw_value_sets = []
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


    def build(self) -> FMFeatureMapElement:
        """Build and return the FMFeatureMapElement instance with validation."""
        self._validate_instance()
        pass
        return self._obj