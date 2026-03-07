"""VariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1010)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2078)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 80)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 226)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 39)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class VariationPoint(ARObject):
    """AUTOSAR VariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VARIATION-POINT"


    blueprint: Optional[DocumentationBlock]
    sw_syscond: Optional[ConditionByFormula]
    _DESERIALIZE_DISPATCH = {
        "BLUEPRINT": lambda obj, elem: setattr(obj, "blueprint", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "SW-SYSCOND": lambda obj, elem: setattr(obj, "sw_syscond", SerializationHelper.deserialize_by_tag(elem, "ConditionByFormula")),
    }


    def __init__(self) -> None:
        """Initialize VariationPoint."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.sw_syscond: Optional[ConditionByFormula] = None

    def serialize(self) -> ET.Element:
        """Serialize VariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint
        if self.blueprint is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_syscond
        if self.sw_syscond is not None:
            serialized = SerializationHelper.serialize_item(self.sw_syscond, "ConditionByFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-SYSCOND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationPoint":
        """Deserialize XML element to VariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariationPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLUEPRINT":
                setattr(obj, "blueprint", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "SW-SYSCOND":
                setattr(obj, "sw_syscond", SerializationHelper.deserialize_by_tag(child, "ConditionByFormula"))

        return obj



class VariationPointBuilder(BuilderBase):
    """Builder for VariationPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariationPoint = VariationPoint()


    def with_blueprint(self, value: Optional[DocumentationBlock]) -> "VariationPointBuilder":
        """Set blueprint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'blueprint' is required and cannot be None")
        self._obj.blueprint = value
        return self

    def with_sw_syscond(self, value: Optional[ConditionByFormula]) -> "VariationPointBuilder":
        """Set sw_syscond attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_syscond' is required and cannot be None")
        self._obj.sw_syscond = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "blueprint",
        "swSyscond",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> VariationPoint:
        """Build and return the VariationPoint instance with validation."""
        self._validate_instance()
        return self._obj