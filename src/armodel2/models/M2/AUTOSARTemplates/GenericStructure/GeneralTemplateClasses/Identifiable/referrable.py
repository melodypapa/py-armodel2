"""Referrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 63)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1002)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2049)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 31)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 66)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.short_name_fragment import (
    ShortNameFragment,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Referrable(ARObject, ABC):
    """AUTOSAR Referrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    short_name: Identifier
    short_name_fragments: list[ShortNameFragment]
    _DESERIALIZE_DISPATCH = {
        "SHORT-NAME": lambda obj, elem: setattr(obj, "short_name", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SHORT-NAME-FRAGMENTS": lambda obj, elem: obj.short_name_fragments.append(SerializationHelper.deserialize_by_tag(elem, "ShortNameFragment")),
    }


    def __init__(self) -> None:
        """Initialize Referrable."""
        super().__init__()
        self.short_name: Identifier = None
        self.short_name_fragments: list[ShortNameFragment] = []

    def serialize(self) -> ET.Element:
        """Serialize Referrable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Referrable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize short_name
        if self.short_name is not None:
            serialized = SerializationHelper.serialize_item(self.short_name, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_name_fragments (list to container "SHORT-NAME-FRAGMENTS")
        if self.short_name_fragments:
            wrapper = ET.Element("SHORT-NAME-FRAGMENTS")
            for item in self.short_name_fragments:
                serialized = SerializationHelper.serialize_item(item, "ShortNameFragment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Referrable":
        """Deserialize XML element to Referrable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Referrable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Referrable, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SHORT-NAME":
                setattr(obj, "short_name", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SHORT-NAME-FRAGMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.short_name_fragments.append(SerializationHelper.deserialize_by_tag(item_elem, "ShortNameFragment"))

        return obj



class ReferrableBuilder(BuilderBase, ABC):
    """Builder for Referrable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Referrable = Referrable()


    def with_short_name(self, value: Identifier) -> "ReferrableBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'short_name' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "ReferrableBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "ReferrableBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "ReferrableBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "shortName",
    }
    _OPTIONAL_ATTRIBUTES = {
        "shortNameFragment",
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
        if getattr(self._obj, "shortName", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'shortName' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'shortName' is None", UserWarning)


    @abstractmethod
    def build(self) -> Referrable:
        """Build and return the Referrable instance (abstract)."""
        raise NotImplementedError