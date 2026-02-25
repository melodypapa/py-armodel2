"""FMFeature AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 24)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 444)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_restriction import (
    FMFeatureRestriction,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_relation import (
        FMFeatureRelation,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class FMFeature(ARElement):
    """AUTOSAR FMFeature."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_deves: list[FMAttributeDef]
    decomposition_decompositions: list[FMFeature]
    maximum: Optional[BindingTimeEnum]
    minimum: Optional[BindingTimeEnum]
    relations: list[FMFeatureRelation]
    restrictions: list[FMFeatureRestriction]
    def __init__(self) -> None:
        """Initialize FMFeature."""
        super().__init__()
        self.attribute_deves: list[FMAttributeDef] = []
        self.decomposition_decompositions: list[FMFeature] = []
        self.maximum: Optional[BindingTimeEnum] = None
        self.minimum: Optional[BindingTimeEnum] = None
        self.relations: list[FMFeatureRelation] = []
        self.restrictions: list[FMFeatureRestriction] = []

    def serialize(self) -> ET.Element:
        """Serialize FMFeature to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeature, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_deves (list to container "ATTRIBUTE-DEVES")
        if self.attribute_deves:
            wrapper = ET.Element("ATTRIBUTE-DEVES")
            for item in self.attribute_deves:
                serialized = SerializationHelper.serialize_item(item, "FMAttributeDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize decomposition_decompositions (list to container "DECOMPOSITION-DECOMPOSITIONS")
        if self.decomposition_decompositions:
            wrapper = ET.Element("DECOMPOSITION-DECOMPOSITIONS")
            for item in self.decomposition_decompositions:
                serialized = SerializationHelper.serialize_item(item, "FMFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum
        if self.minimum is not None:
            serialized = SerializationHelper.serialize_item(self.minimum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize relations (list to container "RELATIONS")
        if self.relations:
            wrapper = ET.Element("RELATIONS")
            for item in self.relations:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureRelation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize restrictions (list to container "RESTRICTIONS")
        if self.restrictions:
            wrapper = ET.Element("RESTRICTIONS")
            for item in self.restrictions:
                serialized = SerializationHelper.serialize_item(item, "FMFeatureRestriction")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeature":
        """Deserialize XML element to FMFeature object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeature object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeature, cls).deserialize(element)

        # Parse attribute_deves (list from container "ATTRIBUTE-DEVES")
        obj.attribute_deves = []
        container = SerializationHelper.find_child_element(element, "ATTRIBUTE-DEVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attribute_deves.append(child_value)

        # Parse decomposition_decompositions (list from container "DECOMPOSITION-DECOMPOSITIONS")
        obj.decomposition_decompositions = []
        container = SerializationHelper.find_child_element(element, "DECOMPOSITION-DECOMPOSITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.decomposition_decompositions.append(child_value)

        # Parse maximum
        child = SerializationHelper.find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = BindingTimeEnum.deserialize(child)
            obj.maximum = maximum_value

        # Parse minimum
        child = SerializationHelper.find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = BindingTimeEnum.deserialize(child)
            obj.minimum = minimum_value

        # Parse relations (list from container "RELATIONS")
        obj.relations = []
        container = SerializationHelper.find_child_element(element, "RELATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.relations.append(child_value)

        # Parse restrictions (list from container "RESTRICTIONS")
        obj.restrictions = []
        container = SerializationHelper.find_child_element(element, "RESTRICTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.restrictions.append(child_value)

        return obj



class FMFeatureBuilder(ARElementBuilder):
    """Builder for FMFeature with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFeature = FMFeature()


    def with_attribute_deves(self, items: list[FMAttributeDef]) -> "FMFeatureBuilder":
        """Set attribute_deves list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.attribute_deves = list(items) if items else []
        return self

    def with_decomposition_decompositions(self, items: list[FMFeature]) -> "FMFeatureBuilder":
        """Set decomposition_decompositions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.decomposition_decompositions = list(items) if items else []
        return self

    def with_maximum(self, value: Optional[BindingTimeEnum]) -> "FMFeatureBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_minimum(self, value: Optional[BindingTimeEnum]) -> "FMFeatureBuilder":
        """Set minimum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum = value
        return self

    def with_relations(self, items: list[FMFeatureRelation]) -> "FMFeatureBuilder":
        """Set relations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.relations = list(items) if items else []
        return self

    def with_restrictions(self, items: list[FMFeatureRestriction]) -> "FMFeatureBuilder":
        """Set restrictions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.restrictions = list(items) if items else []
        return self


    def add_attribute_def(self, item: FMAttributeDef) -> "FMFeatureBuilder":
        """Add a single item to attribute_deves list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.attribute_deves.append(item)
        return self

    def clear_attribute_deves(self) -> "FMFeatureBuilder":
        """Clear all items from attribute_deves list.

        Returns:
            self for method chaining
        """
        self._obj.attribute_deves = []
        return self

    def add_decomposition_decomposition(self, item: FMFeature) -> "FMFeatureBuilder":
        """Add a single item to decomposition_decompositions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.decomposition_decompositions.append(item)
        return self

    def clear_decomposition_decompositions(self) -> "FMFeatureBuilder":
        """Clear all items from decomposition_decompositions list.

        Returns:
            self for method chaining
        """
        self._obj.decomposition_decompositions = []
        return self

    def add_relation(self, item: FMFeatureRelation) -> "FMFeatureBuilder":
        """Add a single item to relations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.relations.append(item)
        return self

    def clear_relations(self) -> "FMFeatureBuilder":
        """Clear all items from relations list.

        Returns:
            self for method chaining
        """
        self._obj.relations = []
        return self

    def add_restriction(self, item: FMFeatureRestriction) -> "FMFeatureBuilder":
        """Add a single item to restrictions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.restrictions.append(item)
        return self

    def clear_restrictions(self) -> "FMFeatureBuilder":
        """Clear all items from restrictions list.

        Returns:
            self for method chaining
        """
        self._obj.restrictions = []
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


    def build(self) -> FMFeature:
        """Build and return the FMFeature instance with validation."""
        self._validate_instance()
        pass
        return self._obj