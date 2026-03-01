"""MultilanguageReferrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 75)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MultilanguageReferrable(Referrable, ABC):
    """AUTOSAR MultilanguageReferrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    long_name: Optional[MultilanguageLongName]
    _DESERIALIZE_DISPATCH = {
        "LONG-NAME": lambda obj, elem: setattr(obj, "long_name", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
    }


    def __init__(self) -> None:
        """Initialize MultilanguageReferrable."""
        super().__init__()
        self.long_name: Optional[MultilanguageLongName] = None

    def serialize(self) -> ET.Element:
        """Serialize MultilanguageReferrable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultilanguageReferrable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize long_name
        if self.long_name is not None:
            serialized = SerializationHelper.serialize_item(self.long_name, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LONG-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageReferrable":
        """Deserialize XML element to MultilanguageReferrable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultilanguageReferrable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultilanguageReferrable, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "LONG-NAME":
                setattr(obj, "long_name", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))

        return obj



class MultilanguageReferrableBuilder(ReferrableBuilder):
    """Builder for MultilanguageReferrable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultilanguageReferrable = MultilanguageReferrable()


    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "MultilanguageReferrableBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
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
    def build(self) -> MultilanguageReferrable:
        """Build and return the MultilanguageReferrable instance (abstract)."""
        raise NotImplementedError