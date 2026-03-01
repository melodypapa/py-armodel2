"""DiagnosticCapabilityElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 236)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 753)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticAudienceEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagRequirementIdString,
    PositiveInteger,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """AUTOSAR DiagnosticCapabilityElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    audiences: list[DiagnosticAudienceEnum]
    diag: Optional[DiagRequirementIdString]
    security_access: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "AUDIENCES": lambda obj, elem: obj.audiences.append(DiagnosticAudienceEnum.deserialize(elem)),
        "DIAG": lambda obj, elem: setattr(obj, "diag", SerializationHelper.deserialize_by_tag(elem, "DiagRequirementIdString")),
        "SECURITY-ACCESS": lambda obj, elem: setattr(obj, "security_access", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticCapabilityElement."""
        super().__init__()
        self.audiences: list[DiagnosticAudienceEnum] = []
        self.diag: Optional[DiagRequirementIdString] = None
        self.security_access: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCapabilityElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCapabilityElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize audiences (list to container "AUDIENCES")
        if self.audiences:
            wrapper = ET.Element("AUDIENCES")
            for item in self.audiences:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticAudienceEnum")
                if serialized is not None:
                    child_elem = ET.Element("AUDIENCE")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize diag
        if self.diag is not None:
            serialized = SerializationHelper.serialize_item(self.diag, "DiagRequirementIdString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_access
        if self.security_access is not None:
            serialized = SerializationHelper.serialize_item(self.security_access, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCapabilityElement":
        """Deserialize XML element to DiagnosticCapabilityElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCapabilityElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticCapabilityElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUDIENCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.audiences.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticAudienceEnum"))
            elif tag == "DIAG":
                setattr(obj, "diag", SerializationHelper.deserialize_by_tag(child, "DiagRequirementIdString"))
            elif tag == "SECURITY-ACCESS":
                setattr(obj, "security_access", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticCapabilityElementBuilder(ServiceNeedsBuilder):
    """Builder for DiagnosticCapabilityElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticCapabilityElement = DiagnosticCapabilityElement()


    def with_audiences(self, items: list[DiagnosticAudienceEnum]) -> "DiagnosticCapabilityElementBuilder":
        """Set audiences list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.audiences = list(items) if items else []
        return self

    def with_diag(self, value: Optional[DiagRequirementIdString]) -> "DiagnosticCapabilityElementBuilder":
        """Set diag attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diag = value
        return self

    def with_security_access(self, value: Optional[PositiveInteger]) -> "DiagnosticCapabilityElementBuilder":
        """Set security_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.security_access = value
        return self


    def add_audience(self, item: DiagnosticAudienceEnum) -> "DiagnosticCapabilityElementBuilder":
        """Add a single item to audiences list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.audiences.append(item)
        return self

    def clear_audiences(self) -> "DiagnosticCapabilityElementBuilder":
        """Clear all items from audiences list.

        Returns:
            self for method chaining
        """
        self._obj.audiences = []
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


    @abstractmethod
    def build(self) -> DiagnosticCapabilityElement:
        """Build and return the DiagnosticCapabilityElement instance (abstract)."""
        raise NotImplementedError