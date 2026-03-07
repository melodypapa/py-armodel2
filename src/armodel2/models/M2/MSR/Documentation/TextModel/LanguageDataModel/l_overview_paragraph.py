"""LOverviewParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 348)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LOverviewParagraph(LanguageSpecific):
    """AUTOSAR LOverviewParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "L-OVERVIEW-PARAGRAPH"


    blueprint_value: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "BLUEPRINT-VALUE": lambda obj, elem: setattr(obj, "blueprint_value", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize LOverviewParagraph."""
        super().__init__()
        self.blueprint_value: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize LOverviewParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LOverviewParagraph, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint_value
        if self.blueprint_value is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint_value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LOverviewParagraph":
        """Deserialize XML element to LOverviewParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LOverviewParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LOverviewParagraph, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLUEPRINT-VALUE":
                setattr(obj, "blueprint_value", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class LOverviewParagraphBuilder(BuilderBase):
    """Builder for LOverviewParagraph with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LOverviewParagraph = LOverviewParagraph()


    def with_blueprint_value(self, value: Optional[String]) -> "LOverviewParagraphBuilder":
        """Set blueprint_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'blueprint_value' is required and cannot be None")
        self._obj.blueprint_value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "blueprintValue",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LOverviewParagraph:
        """Build and return the LOverviewParagraph instance with validation."""
        self._validate_instance()
        return self._obj