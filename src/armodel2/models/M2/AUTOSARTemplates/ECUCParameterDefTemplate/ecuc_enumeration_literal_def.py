"""EcucEnumerationLiteralDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucEnumerationLiteralDef(Identifiable):
    """AUTOSAR EcucEnumerationLiteralDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-ENUMERATION-LITERAL-DEF"


    ecuc_cond: Optional[Any]
    origin: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "ECUC-COND": lambda obj, elem: setattr(obj, "ecuc_cond", SerializationHelper.deserialize_by_tag(elem, "any (EcucCondition)")),
        "ORIGIN": lambda obj, elem: setattr(obj, "origin", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize EcucEnumerationLiteralDef."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.origin: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucEnumerationLiteralDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucEnumerationLiteralDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_cond
        if self.ecuc_cond is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_cond, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-COND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize origin
        if self.origin is not None:
            serialized = SerializationHelper.serialize_item(self.origin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ORIGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationLiteralDef":
        """Deserialize XML element to EcucEnumerationLiteralDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucEnumerationLiteralDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucEnumerationLiteralDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECUC-COND":
                setattr(obj, "ecuc_cond", SerializationHelper.deserialize_by_tag(child, "any (EcucCondition)"))
            elif tag == "ORIGIN":
                setattr(obj, "origin", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class EcucEnumerationLiteralDefBuilder(IdentifiableBuilder):
    """Builder for EcucEnumerationLiteralDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucEnumerationLiteralDef = EcucEnumerationLiteralDef()


    def with_ecuc_cond(self, value: Optional[any (EcucCondition)]) -> "EcucEnumerationLiteralDefBuilder":
        """Set ecuc_cond attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc_cond = value
        return self

    def with_origin(self, value: Optional[String]) -> "EcucEnumerationLiteralDefBuilder":
        """Set origin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.origin = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ecucCond",
        "origin",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucEnumerationLiteralDef:
        """Build and return the EcucEnumerationLiteralDef instance with validation."""
        self._validate_instance()
        return self._obj