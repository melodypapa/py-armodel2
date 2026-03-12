"""RuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    Numerical,
    VerbatimString,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_arguments import (
    RuleArguments,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RuleBasedValueSpecification(ARObject):
    """AUTOSAR RuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RULE-BASED-VALUE-SPECIFICATION"


    arguments: Optional[RuleArguments]
    v: Optional[Numerical]
    vf: Optional[Numerical]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    max_size_to_fill: Optional[Integer]
    rule: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENTS": lambda obj, elem: setattr(obj, "arguments", SerializationHelper.deserialize_by_tag(elem, "RuleArguments")),
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "VF": lambda obj, elem: setattr(obj, "vf", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "VT": lambda obj, elem: setattr(obj, "vt", SerializationHelper.deserialize_by_tag(elem, "VerbatimString")),
        "VTF": lambda obj, elem: setattr(obj, "vtf", SerializationHelper.deserialize_by_tag(elem, "NumericalOrText")),
        "MAX-SIZE-TO-FILL": lambda obj, elem: setattr(obj, "max_size_to_fill", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "RULE": lambda obj, elem: setattr(obj, "rule", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize RuleBasedValueSpecification."""
        super().__init__()
        self.arguments: Optional[RuleArguments] = None
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None
        self.max_size_to_fill: Optional[Integer] = None
        self.rule: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RuleBasedValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments (atp_mixed - append children directly)
        if self.arguments is not None:
            serialized = SerializationHelper.serialize_item(self.arguments, "RuleArguments")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize v
        if self.v is not None:
            serialized = SerializationHelper.serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vf
        if self.vf is not None:
            serialized = SerializationHelper.serialize_item(self.vf, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vt
        if self.vt is not None:
            serialized = SerializationHelper.serialize_item(self.vt, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vtf
        if self.vtf is not None:
            serialized = SerializationHelper.serialize_item(self.vtf, "NumericalOrText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VTF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_size_to_fill
        if self.max_size_to_fill is not None:
            serialized = SerializationHelper.serialize_item(self.max_size_to_fill, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SIZE-TO-FILL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rule
        if self.rule is not None:
            serialized = SerializationHelper.serialize_item(self.rule, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueSpecification":
        """Deserialize XML element to RuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleBasedValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RuleBasedValueSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARGUMENTS":
                setattr(obj, "arguments", SerializationHelper.deserialize_by_tag(child, "RuleArguments"))
            elif tag == "V":
                setattr(obj, "v", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "VF":
                setattr(obj, "vf", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "VT":
                setattr(obj, "vt", SerializationHelper.deserialize_by_tag(child, "VerbatimString"))
            elif tag == "VTF":
                setattr(obj, "vtf", SerializationHelper.deserialize_by_tag(child, "NumericalOrText"))
            elif tag == "MAX-SIZE-TO-FILL":
                setattr(obj, "max_size_to_fill", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "RULE":
                setattr(obj, "rule", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class RuleBasedValueSpecificationBuilder(BuilderBase):
    """Builder for RuleBasedValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RuleBasedValueSpecification = RuleBasedValueSpecification()


    def with_arguments(self, value: Optional[RuleArguments]) -> "RuleBasedValueSpecificationBuilder":
        """Set arguments attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'arguments' is required and cannot be None")
        self._obj.arguments = value
        return self

    def with_v(self, value: Optional[Numerical]) -> "RuleBasedValueSpecificationBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'v' is required and cannot be None")
        self._obj.v = value
        return self

    def with_vf(self, value: Optional[Numerical]) -> "RuleBasedValueSpecificationBuilder":
        """Set vf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vf' is required and cannot be None")
        self._obj.vf = value
        return self

    def with_vt(self, value: Optional[VerbatimString]) -> "RuleBasedValueSpecificationBuilder":
        """Set vt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vt' is required and cannot be None")
        self._obj.vt = value
        return self

    def with_vtf(self, value: Optional[NumericalOrText]) -> "RuleBasedValueSpecificationBuilder":
        """Set vtf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'vtf' is required and cannot be None")
        self._obj.vtf = value
        return self

    def with_max_size_to_fill(self, value: Optional[Integer]) -> "RuleBasedValueSpecificationBuilder":
        """Set max_size_to_fill attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_size_to_fill' is required and cannot be None")
        self._obj.max_size_to_fill = value
        return self

    def with_rule(self, value: Optional[Identifier]) -> "RuleBasedValueSpecificationBuilder":
        """Set rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rule' is required and cannot be None")
        self._obj.rule = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "arguments",
        "maxSizeToFill",
        "rule",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RuleBasedValueSpecification:
        """Build and return the RuleBasedValueSpecification instance with validation."""
        self._validate_instance()
        return self._obj