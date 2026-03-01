"""DiagnosticContributionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 56)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticContributionSet(ARElement):
    """AUTOSAR DiagnosticContributionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-CONTRIBUTION-SET"


    common: Optional[Any]
    element_refs: list[Any]
    service_table_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMMON": lambda obj, elem: setattr(obj, "common", SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticCommon)")),
        "ELEMENT-REFS": lambda obj, elem: obj.element_refs.append(ARRef.deserialize(elem)),
        "SERVICE-TABLE-REFS": lambda obj, elem: obj.service_table_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticContributionSet."""
        super().__init__()
        self.common: Optional[Any] = None
        self.element_refs: list[Any] = []
        self.service_table_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticContributionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticContributionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize common
        if self.common is not None:
            serialized = SerializationHelper.serialize_item(self.common, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_refs (list to container "ELEMENT-REFS")
        if self.element_refs:
            wrapper = ET.Element("ELEMENT-REFS")
            for item in self.element_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_table_refs (list to container "SERVICE-TABLE-REFS")
        if self.service_table_refs:
            wrapper = ET.Element("SERVICE-TABLE-REFS")
            for item in self.service_table_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticServiceTable")
                if serialized is not None:
                    child_elem = ET.Element("SERVICE-TABLE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticContributionSet":
        """Deserialize XML element to DiagnosticContributionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticContributionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticContributionSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMON":
                setattr(obj, "common", SerializationHelper.deserialize_by_tag(child, "any (DiagnosticCommon)"))
            elif tag == "ELEMENT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.element_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (DiagnosticCommon)"))
            elif tag == "SERVICE-TABLE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.service_table_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticServiceTable"))

        return obj



class DiagnosticContributionSetBuilder(ARElementBuilder):
    """Builder for DiagnosticContributionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticContributionSet = DiagnosticContributionSet()


    def with_common(self, value: Optional[any (DiagnosticCommon)]) -> "DiagnosticContributionSetBuilder":
        """Set common attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.common = value
        return self

    def with_elements(self, items: list[any (DiagnosticCommon)]) -> "DiagnosticContributionSetBuilder":
        """Set elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.elements = list(items) if items else []
        return self

    def with_service_tables(self, items: list[DiagnosticServiceTable]) -> "DiagnosticContributionSetBuilder":
        """Set service_tables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_tables = list(items) if items else []
        return self


    def add_element(self, item: any (DiagnosticCommon)) -> "DiagnosticContributionSetBuilder":
        """Add a single item to elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.elements.append(item)
        return self

    def clear_elements(self) -> "DiagnosticContributionSetBuilder":
        """Clear all items from elements list.

        Returns:
            self for method chaining
        """
        self._obj.elements = []
        return self

    def add_service_table(self, item: DiagnosticServiceTable) -> "DiagnosticContributionSetBuilder":
        """Add a single item to service_tables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_tables.append(item)
        return self

    def clear_service_tables(self) -> "DiagnosticContributionSetBuilder":
        """Clear all items from service_tables list.

        Returns:
            self for method chaining
        """
        self._obj.service_tables = []
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


    def build(self) -> DiagnosticContributionSet:
        """Build and return the DiagnosticContributionSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj