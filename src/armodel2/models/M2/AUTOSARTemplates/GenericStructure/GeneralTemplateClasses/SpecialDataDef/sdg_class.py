"""SdgClass AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import SdgElementWithGidBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MetaClassName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SdgClass(SdgElementWithGid):
    """AUTOSAR SdgClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG-CLASS"


    attributes: list[SdgAttribute]
    caption: Optional[Boolean]
    extends_meta: Optional[MetaClassName]
    sdg_constraint_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ATTRIBUTES": ("_POLYMORPHIC_LIST", "attributes", ["SdgAbstractForeignReference", "SdgAbstractPrimitiveAttribute", "SdgAggregationWithVariation", "Sdg"]),
        "CAPTION": lambda obj, elem: setattr(obj, "caption", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "EXTENDS-META": lambda obj, elem: setattr(obj, "extends_meta", SerializationHelper.deserialize_by_tag(elem, "MetaClassName")),
        "SDG-CONSTRAINTS": lambda obj, elem: obj.sdg_constraint_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SdgClass."""
        super().__init__()
        self.attributes: list[SdgAttribute] = []
        self.caption: Optional[Boolean] = None
        self.extends_meta: Optional[MetaClassName] = None
        self.sdg_constraint_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SdgClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attributes (list to container "ATTRIBUTES")
        if self.attributes:
            wrapper = ET.Element("ATTRIBUTES")
            for item in self.attributes:
                serialized = SerializationHelper.serialize_item(item, "SdgAttribute")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize caption
        if self.caption is not None:
            serialized = SerializationHelper.serialize_item(self.caption, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extends_meta
        if self.extends_meta is not None:
            serialized = SerializationHelper.serialize_item(self.extends_meta, "MetaClassName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXTENDS-META")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg_constraint_refs (list to container "SDG-CONSTRAINT-REFS")
        if self.sdg_constraint_refs:
            wrapper = ET.Element("SDG-CONSTRAINT-REFS")
            for item in self.sdg_constraint_refs:
                serialized = SerializationHelper.serialize_item(item, "TraceableText")
                if serialized is not None:
                    child_elem = ET.Element("SDG-CONSTRAINT-REF")
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
    def deserialize(cls, element: ET.Element) -> "SdgClass":
        """Deserialize XML element to SdgClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgClass, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ATTRIBUTES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "SDG-ABSTRACT-FOREIGN-REFERENCE":
                        obj.attributes.append(SerializationHelper.deserialize_by_tag(child[0], "SdgAbstractForeignReference"))
                    elif concrete_tag == "SDG-ABSTRACT-PRIMITIVE-ATTRIBUTE":
                        obj.attributes.append(SerializationHelper.deserialize_by_tag(child[0], "SdgAbstractPrimitiveAttribute"))
                    elif concrete_tag == "SDG-AGGREGATION-WITH-VARIATION":
                        obj.attributes.append(SerializationHelper.deserialize_by_tag(child[0], "SdgAggregationWithVariation"))
                    elif concrete_tag == "SDG":
                        obj.attributes.append(SerializationHelper.deserialize_by_tag(child[0], "Sdg"))
            elif tag == "CAPTION":
                setattr(obj, "caption", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "EXTENDS-META":
                setattr(obj, "extends_meta", SerializationHelper.deserialize_by_tag(child, "MetaClassName"))
            elif tag == "SDG-CONSTRAINTS":
                obj.sdg_constraint_refs.append(ARRef.deserialize(child))

        return obj



class SdgClassBuilder(SdgElementWithGidBuilder):
    """Builder for SdgClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgClass = SdgClass()


    def with_attributes(self, items: list[SdgAttribute]) -> "SdgClassBuilder":
        """Set attributes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.attributes = list(items) if items else []
        return self

    def with_caption(self, value: Optional[Boolean]) -> "SdgClassBuilder":
        """Set caption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.caption = value
        return self

    def with_extends_meta(self, value: Optional[MetaClassName]) -> "SdgClassBuilder":
        """Set extends_meta attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.extends_meta = value
        return self

    def with_sdg_constraints(self, items: list[TraceableText]) -> "SdgClassBuilder":
        """Set sdg_constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdg_constraints = list(items) if items else []
        return self


    def add_attribute(self, item: SdgAttribute) -> "SdgClassBuilder":
        """Add a single item to attributes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.attributes.append(item)
        return self

    def clear_attributes(self) -> "SdgClassBuilder":
        """Clear all items from attributes list.

        Returns:
            self for method chaining
        """
        self._obj.attributes = []
        return self

    def add_sdg_constraint(self, item: TraceableText) -> "SdgClassBuilder":
        """Add a single item to sdg_constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdg_constraints.append(item)
        return self

    def clear_sdg_constraints(self) -> "SdgClassBuilder":
        """Clear all items from sdg_constraints list.

        Returns:
            self for method chaining
        """
        self._obj.sdg_constraints = []
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


    def build(self) -> SdgClass:
        """Build and return the SdgClass instance with validation."""
        self._validate_instance()
        pass
        return self._obj