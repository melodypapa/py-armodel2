"""EcucIntegerParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 60)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

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
    UnlimitedInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucIntegerParamDef(EcucParameterDef):
    """AUTOSAR EcucIntegerParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-INTEGER-PARAM-DEF"


    default_value: Optional[UnlimitedInteger]
    max: Optional[UnlimitedInteger]
    min: Optional[UnlimitedInteger]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-VALUE": lambda obj, elem: setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
        "MAX": lambda obj, elem: setattr(obj, "max", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
        "MIN": lambda obj, elem: setattr(obj, "min", SerializationHelper.deserialize_by_tag(elem, "UnlimitedInteger")),
    }


    def __init__(self) -> None:
        """Initialize EcucIntegerParamDef."""
        super().__init__()
        self.default_value: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucIntegerParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucIntegerParamDef, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.default_value, "UnlimitedInteger")
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

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucIntegerParamDef":
        """Deserialize XML element to EcucIntegerParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucIntegerParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucIntegerParamDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEFAULT-VALUE":
                setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))
            elif tag == "MAX":
                setattr(obj, "max", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))
            elif tag == "MIN":
                setattr(obj, "min", SerializationHelper.deserialize_by_tag(child, "UnlimitedInteger"))

        return obj



class EcucIntegerParamDefBuilder(EcucParameterDefBuilder):
    """Builder for EcucIntegerParamDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucIntegerParamDef = EcucIntegerParamDef()


    def with_default_value(self, value: Optional[UnlimitedInteger]) -> "EcucIntegerParamDefBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'default_value' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_max(self, value: Optional[UnlimitedInteger]) -> "EcucIntegerParamDefBuilder":
        """Set max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max' is required and cannot be None")
        self._obj.max = value
        return self

    def with_min(self, value: Optional[UnlimitedInteger]) -> "EcucIntegerParamDefBuilder":
        """Set min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min' is required and cannot be None")
        self._obj.min = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "defaultValue",
        "max",
        "min",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucIntegerParamDef:
        """Build and return the EcucIntegerParamDef instance with validation."""
        self._validate_instance()
        return self._obj