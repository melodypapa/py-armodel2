"""DiagnosticParameterIdent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 37)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import (
    IdentCaption,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.ident_caption import IdentCaptionBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticParameterIdent(IdentCaption):
    """AUTOSAR DiagnosticParameterIdent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-PARAMETER-IDENT"


    sub_elements: list[DiagnosticParameter]
    _DESERIALIZE_DISPATCH = {
        "SUB-ELEMENTS": lambda obj, elem: obj.sub_elements.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdent."""
        super().__init__()
        self.sub_elements: list[DiagnosticParameter] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterIdent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameterIdent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sub_elements (list to container "SUB-ELEMENTS")
        if self.sub_elements:
            wrapper = ET.Element("SUB-ELEMENTS")
            for item in self.sub_elements:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterIdent":
        """Deserialize XML element to DiagnosticParameterIdent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterIdent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameterIdent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SUB-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sub_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameter"))

        return obj



class DiagnosticParameterIdentBuilder(IdentCaptionBuilder):
    """Builder for DiagnosticParameterIdent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticParameterIdent = DiagnosticParameterIdent()


    def with_sub_elements(self, items: list[DiagnosticParameter]) -> "DiagnosticParameterIdentBuilder":
        """Set sub_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = list(items) if items else []
        return self


    def add_sub_element(self, item: DiagnosticParameter) -> "DiagnosticParameterIdentBuilder":
        """Add a single item to sub_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_elements.append(item)
        return self

    def clear_sub_elements(self) -> "DiagnosticParameterIdentBuilder":
        """Clear all items from sub_elements list.

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "subElement",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticParameterIdent:
        """Build and return the DiagnosticParameterIdent instance with validation."""
        self._validate_instance()
        return self._obj