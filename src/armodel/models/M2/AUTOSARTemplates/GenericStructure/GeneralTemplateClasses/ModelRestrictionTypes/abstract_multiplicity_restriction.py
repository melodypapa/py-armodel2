"""AbstractMultiplicityRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class AbstractMultiplicityRestriction(ARObject, ABC):
    """AUTOSAR AbstractMultiplicityRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    lower_multiplicity: Optional[PositiveInteger]
    upper_multiplicity: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize AbstractMultiplicityRestriction."""
        super().__init__()
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractMultiplicityRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractMultiplicityRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_multiplicity
        if self.lower_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.lower_multiplicity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_multiplicity
        if self.upper_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.upper_multiplicity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractMultiplicityRestriction":
        """Deserialize XML element to AbstractMultiplicityRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractMultiplicityRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractMultiplicityRestriction, cls).deserialize(element)

        # Parse lower_multiplicity
        child = SerializationHelper.find_child_element(element, "LOWER-MULTIPLICITY")
        if child is not None:
            lower_multiplicity_value = child.text
            obj.lower_multiplicity = lower_multiplicity_value

        # Parse upper_multiplicity
        child = SerializationHelper.find_child_element(element, "UPPER-MULTIPLICITY")
        if child is not None:
            upper_multiplicity_value = child.text
            obj.upper_multiplicity = upper_multiplicity_value

        return obj



class AbstractMultiplicityRestrictionBuilder(BuilderBase, ABC):
    """Builder for AbstractMultiplicityRestriction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractMultiplicityRestriction = AbstractMultiplicityRestriction()


    def with_lower_multiplicity(self, value: Optional[PositiveInteger]) -> "AbstractMultiplicityRestrictionBuilder":
        """Set lower_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lower_multiplicity = value
        return self

    def with_upper_multiplicity(self, value: Optional[Boolean]) -> "AbstractMultiplicityRestrictionBuilder":
        """Set upper_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upper_multiplicity = value
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


    @abstractmethod
    def build(self) -> AbstractMultiplicityRestriction:
        """Build and return the AbstractMultiplicityRestriction instance (abstract)."""
        raise NotImplementedError