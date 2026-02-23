"""FMFeatureRelation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
        FMFeature,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class FMFeatureRelation(Identifiable):
    """AUTOSAR FMFeatureRelation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    feature_refs: list[ARRef]
    restriction: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureRelation."""
        super().__init__()
        self.feature_refs: list[ARRef] = []
        self.restriction: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureRelation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureRelation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature_refs (list to container "FEATURE-REFS")
        if self.feature_refs:
            wrapper = ET.Element("FEATURE-REFS")
            for item in self.feature_refs:
                serialized = SerializationHelper.serialize_item(item, "FMFeature")
                if serialized is not None:
                    child_elem = ET.Element("FEATURE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize restriction
        if self.restriction is not None:
            serialized = SerializationHelper.serialize_item(self.restriction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESTRICTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRelation":
        """Deserialize XML element to FMFeatureRelation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureRelation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureRelation, cls).deserialize(element)

        # Parse feature_refs (list from container "FEATURE-REFS")
        obj.feature_refs = []
        container = SerializationHelper.find_child_element(element, "FEATURE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.feature_refs.append(child_value)

        # Parse restriction
        child = SerializationHelper.find_child_element(element, "RESTRICTION")
        if child is not None:
            restriction_value = child.text
            obj.restriction = restriction_value

        return obj



class FMFeatureRelationBuilder(IdentifiableBuilder):
    """Builder for FMFeatureRelation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFeatureRelation = FMFeatureRelation()


    def with_features(self, items: list[FMFeature]) -> "FMFeatureRelationBuilder":
        """Set features list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.features = list(items) if items else []
        return self

    def with_restriction(self, value: Optional[any (FMConditionByFeatures)]) -> "FMFeatureRelationBuilder":
        """Set restriction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.restriction = value
        return self


    def add_feature(self, item: FMFeature) -> "FMFeatureRelationBuilder":
        """Add a single item to features list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.features.append(item)
        return self

    def clear_features(self) -> "FMFeatureRelationBuilder":
        """Clear all items from features list.

        Returns:
            self for method chaining
        """
        self._obj.features = []
        return self



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


    def build(self) -> FMFeatureRelation:
        """Build and return the FMFeatureRelation instance with validation."""
        self._validate_instance()
        pass
        return self._obj