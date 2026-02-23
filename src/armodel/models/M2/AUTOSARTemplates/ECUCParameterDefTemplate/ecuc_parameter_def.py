"""EcucParameterDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 57)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import EcucCommonAttributesBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
    EcucDerivationSpecification,
)


class EcucParameterDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucParameterDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    derivation: Optional[EcucDerivationSpecification]
    symbolic_name: Optional[Boolean]
    with_auto: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucParameterDef."""
        super().__init__()
        self.derivation: Optional[EcucDerivationSpecification] = None
        self.symbolic_name: Optional[Boolean] = None
        self.with_auto: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucParameterDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParameterDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize derivation
        if self.derivation is not None:
            serialized = SerializationHelper.serialize_item(self.derivation, "EcucDerivationSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DERIVATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbolic_name
        if self.symbolic_name is not None:
            serialized = SerializationHelper.serialize_item(self.symbolic_name, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOLIC-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize with_auto
        if self.with_auto is not None:
            serialized = SerializationHelper.serialize_item(self.with_auto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WITH-AUTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterDef":
        """Deserialize XML element to EcucParameterDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParameterDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParameterDef, cls).deserialize(element)

        # Parse derivation
        child = SerializationHelper.find_child_element(element, "DERIVATION")
        if child is not None:
            derivation_value = SerializationHelper.deserialize_by_tag(child, "EcucDerivationSpecification")
            obj.derivation = derivation_value

        # Parse symbolic_name
        child = SerializationHelper.find_child_element(element, "SYMBOLIC-NAME")
        if child is not None:
            symbolic_name_value = child.text
            obj.symbolic_name = symbolic_name_value

        # Parse with_auto
        child = SerializationHelper.find_child_element(element, "WITH-AUTO")
        if child is not None:
            with_auto_value = child.text
            obj.with_auto = with_auto_value

        return obj



class EcucParameterDefBuilder(EcucCommonAttributesBuilder):
    """Builder for EcucParameterDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucParameterDef = EcucParameterDef()


    def with_derivation(self, value: Optional[EcucDerivationSpecification]) -> "EcucParameterDefBuilder":
        """Set derivation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.derivation = value
        return self

    def with_symbolic_name(self, value: Optional[Boolean]) -> "EcucParameterDefBuilder":
        """Set symbolic_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbolic_name = value
        return self

    def with_with_auto(self, value: Optional[Boolean]) -> "EcucParameterDefBuilder":
        """Set with_auto attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.with_auto = value
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
    def build(self) -> EcucParameterDef:
        """Build and return the EcucParameterDef instance (abstract)."""
        raise NotImplementedError