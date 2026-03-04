"""EcucEnumerationParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 66)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import EcucParameterDefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_enumeration_literal_def import (
    EcucEnumerationLiteralDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucEnumerationParamDef(EcucParameterDef):
    """AUTOSAR EcucEnumerationParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-ENUMERATION-PARAM-DEF"


    default_value: Optional[Identifier]
    literals: list[EcucEnumerationLiteralDef]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-VALUE": lambda obj, elem: setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "LITERALS": lambda obj, elem: obj.literals.append(SerializationHelper.deserialize_by_tag(elem, "EcucEnumerationLiteralDef")),
    }


    def __init__(self) -> None:
        """Initialize EcucEnumerationParamDef."""
        super().__init__()
        self.default_value: Optional[Identifier] = None
        self.literals: list[EcucEnumerationLiteralDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucEnumerationParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucEnumerationParamDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize literals (list to container "LITERALS")
        if self.literals:
            wrapper = ET.Element("LITERALS")
            for item in self.literals:
                serialized = SerializationHelper.serialize_item(item, "EcucEnumerationLiteralDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationParamDef":
        """Deserialize XML element to EcucEnumerationParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucEnumerationParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucEnumerationParamDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEFAULT-VALUE":
                setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "LITERALS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.literals.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucEnumerationLiteralDef"))

        return obj



class EcucEnumerationParamDefBuilder(EcucParameterDefBuilder):
    """Builder for EcucEnumerationParamDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucEnumerationParamDef = EcucEnumerationParamDef()


    def with_default_value(self, value: Optional[Identifier]) -> "EcucEnumerationParamDefBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_literals(self, items: list[EcucEnumerationLiteralDef]) -> "EcucEnumerationParamDefBuilder":
        """Set literals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.literals = list(items) if items else []
        return self


    def add_literal(self, item: EcucEnumerationLiteralDef) -> "EcucEnumerationParamDefBuilder":
        """Add a single item to literals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.literals.append(item)
        return self

    def clear_literals(self) -> "EcucEnumerationParamDefBuilder":
        """Clear all items from literals list.

        Returns:
            self for method chaining
        """
        self._obj.literals = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "defaultValue",
        "literal",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucEnumerationParamDef:
        """Build and return the EcucEnumerationParamDef instance with validation."""
        self._validate_instance()
        return self._obj