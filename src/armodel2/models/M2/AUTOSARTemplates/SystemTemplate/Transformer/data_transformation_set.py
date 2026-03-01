"""DataTransformationSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 762)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_technology import (
    TransformationTechnology,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataTransformationSet(ARElement):
    """AUTOSAR DataTransformationSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-TRANSFORMATION-SET"


    datas: list[DataTransformation]
    transformation_technologies: list[TransformationTechnology]
    _DESERIALIZE_DISPATCH = {
        "DATAS": lambda obj, elem: obj.datas.append(SerializationHelper.deserialize_by_tag(elem, "DataTransformation")),
        "TRANSFORMATION-TECHNOLOGIES": lambda obj, elem: obj.transformation_technologies.append(SerializationHelper.deserialize_by_tag(elem, "TransformationTechnology")),
    }


    def __init__(self) -> None:
        """Initialize DataTransformationSet."""
        super().__init__()
        self.datas: list[DataTransformation] = []
        self.transformation_technologies: list[TransformationTechnology] = []

    def serialize(self) -> ET.Element:
        """Serialize DataTransformationSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataTransformationSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize datas (list to container "DATAS")
        if self.datas:
            wrapper = ET.Element("DATAS")
            for item in self.datas:
                serialized = SerializationHelper.serialize_item(item, "DataTransformation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transformation_technologies (list to container "TRANSFORMATION-TECHNOLOGIES")
        if self.transformation_technologies:
            wrapper = ET.Element("TRANSFORMATION-TECHNOLOGIES")
            for item in self.transformation_technologies:
                serialized = SerializationHelper.serialize_item(item, "TransformationTechnology")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformationSet":
        """Deserialize XML element to DataTransformationSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTransformationSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTransformationSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.datas.append(SerializationHelper.deserialize_by_tag(item_elem, "DataTransformation"))
            elif tag == "TRANSFORMATION-TECHNOLOGIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.transformation_technologies.append(SerializationHelper.deserialize_by_tag(item_elem, "TransformationTechnology"))

        return obj



class DataTransformationSetBuilder(ARElementBuilder):
    """Builder for DataTransformationSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataTransformationSet = DataTransformationSet()


    def with_datas(self, items: list[DataTransformation]) -> "DataTransformationSetBuilder":
        """Set datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.datas = list(items) if items else []
        return self

    def with_transformation_technologies(self, items: list[TransformationTechnology]) -> "DataTransformationSetBuilder":
        """Set transformation_technologies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_technologies = list(items) if items else []
        return self


    def add_data(self, item: DataTransformation) -> "DataTransformationSetBuilder":
        """Add a single item to datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.datas.append(item)
        return self

    def clear_datas(self) -> "DataTransformationSetBuilder":
        """Clear all items from datas list.

        Returns:
            self for method chaining
        """
        self._obj.datas = []
        return self

    def add_transformation_technology(self, item: TransformationTechnology) -> "DataTransformationSetBuilder":
        """Add a single item to transformation_technologies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_technologies.append(item)
        return self

    def clear_transformation_technologies(self) -> "DataTransformationSetBuilder":
        """Clear all items from transformation_technologies list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_technologies = []
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


    def build(self) -> DataTransformationSet:
        """Build and return the DataTransformationSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj