"""Prms AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_GerneralParameters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Prms(Paginateable):
    """AUTOSAR Prms."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PRMS"


    label: Optional[MultilanguageLongName]
    prm: Any
    _DESERIALIZE_DISPATCH = {
        "LABEL": lambda obj, elem: setattr(obj, "label", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
        "PRM": lambda obj, elem: setattr(obj, "prm", SerializationHelper.deserialize_by_tag(elem, "any (GeneralParameter)")),
    }


    def __init__(self) -> None:
        """Initialize Prms."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.prm: Any = None

    def serialize(self) -> ET.Element:
        """Serialize Prms to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Prms, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize prm
        if self.prm is not None:
            serialized = SerializationHelper.serialize_item(self.prm, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Prms":
        """Deserialize XML element to Prms object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Prms object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Prms, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LABEL":
                setattr(obj, "label", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))
            elif tag == "PRM":
                setattr(obj, "prm", SerializationHelper.deserialize_by_tag(child, "any (GeneralParameter)"))

        return obj



class PrmsBuilder(PaginateableBuilder):
    """Builder for Prms with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Prms = Prms()


    def with_label(self, value: Optional[MultilanguageLongName]) -> "PrmsBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'label' is required and cannot be None")
        self._obj.label = value
        return self

    def with_prm(self, value: Any) -> "PrmsBuilder":
        """Set prm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'prm' is required and cannot be None")
        self._obj.prm = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "prm",
    }
    _OPTIONAL_ATTRIBUTES = {
        "label",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "prm", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'prm' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'prm' is None", UserWarning)


    def build(self) -> Prms:
        """Build and return the Prms instance with validation."""
        self._validate_instance()
        return self._obj