"""ArrayValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 434)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import CompositeValueSpecificationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ArrayValueSpecification(CompositeValueSpecification):
    """AUTOSAR ArrayValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ARRAY-VALUE-SPECIFICATION"


    elements: list[ValueSpecification]
    intended_partial: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ELEMENTS": ("_POLYMORPHIC_LIST", "elements", ["AbstractRuleBasedValueSpecification", "ApplicationValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "INTENDED-PARTIAL": lambda obj, elem: setattr(obj, "intended_partial", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ArrayValueSpecification."""
        super().__init__()
        self.elements: list[ValueSpecification] = []
        self.intended_partial: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ArrayValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ArrayValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize elements (list to container "ELEMENTS")
        if self.elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self.elements:
                serialized = SerializationHelper.serialize_item(item, "ValueSpecification")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize intended_partial
        if self.intended_partial is not None:
            serialized = SerializationHelper.serialize_item(self.intended_partial, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTENDED-PARTIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArrayValueSpecification":
        """Deserialize XML element to ArrayValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArrayValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ArrayValueSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ELEMENTS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        obj.elements.append(SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "INTENDED-PARTIAL":
                setattr(obj, "intended_partial", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ArrayValueSpecificationBuilder(CompositeValueSpecificationBuilder):
    """Builder for ArrayValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ArrayValueSpecification = ArrayValueSpecification()


    def with_elements(self, items: list[ValueSpecification]) -> "ArrayValueSpecificationBuilder":
        """Set elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.elements = list(items) if items else []
        return self

    def with_intended_partial(self, value: Optional[PositiveInteger]) -> "ArrayValueSpecificationBuilder":
        """Set intended_partial attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.intended_partial = value
        return self


    def add_element(self, item: ValueSpecification) -> "ArrayValueSpecificationBuilder":
        """Add a single item to elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.elements.append(item)
        return self

    def clear_elements(self) -> "ArrayValueSpecificationBuilder":
        """Clear all items from elements list.

        Returns:
            self for method chaining
        """
        self._obj.elements = []
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


    def build(self) -> ArrayValueSpecification:
        """Build and return the ArrayValueSpecification instance with validation."""
        self._validate_instance()
        pass
        return self._obj