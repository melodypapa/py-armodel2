"""RuleBasedValueCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RuleBasedValueCont(ARObject):
    """AUTOSAR RuleBasedValueCont."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RULE-BASED-VALUE-CONT"


    rule_based: Optional[Any]
    v: Optional[Numerical]
    unit_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RULE-BASED": lambda obj, elem: setattr(obj, "rule_based", SerializationHelper.deserialize_by_tag(elem, "any (RuleBasedValue)")),
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "UNIT-REF": lambda obj, elem: setattr(obj, "unit_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RuleBasedValueCont."""
        super().__init__()
        self.rule_based: Optional[Any] = None
        self.v: Optional[Numerical] = None
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RuleBasedValueCont to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RuleBasedValueCont, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rule_based
        if self.rule_based is not None:
            serialized = SerializationHelper.serialize_item(self.rule_based, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE-BASED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueCont":
        """Deserialize XML element to RuleBasedValueCont object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleBasedValueCont object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RuleBasedValueCont, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RULE-BASED":
                setattr(obj, "rule_based", SerializationHelper.deserialize_by_tag(child, "any (RuleBasedValue)"))
            elif tag == "V":
                setattr(obj, "v", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "UNIT-REF":
                setattr(obj, "unit_ref", ARRef.deserialize(child))

        return obj



class RuleBasedValueContBuilder(BuilderBase):
    """Builder for RuleBasedValueCont with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RuleBasedValueCont = RuleBasedValueCont()


    def with_rule_based(self, value: Optional[any (RuleBasedValue)]) -> "RuleBasedValueContBuilder":
        """Set rule_based attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rule_based = value
        return self

    def with_v(self, value: Optional[Numerical]) -> "RuleBasedValueContBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.v = value
        return self

    def with_unit(self, value: Optional[Unit]) -> "RuleBasedValueContBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ruleBased",
        "swArraysize",
        "unit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RuleBasedValueCont:
        """Build and return the RuleBasedValueCont instance with validation."""
        self._validate_instance()
        return self._obj