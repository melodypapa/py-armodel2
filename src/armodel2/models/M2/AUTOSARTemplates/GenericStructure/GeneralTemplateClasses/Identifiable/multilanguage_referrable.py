"""MultilanguageReferrable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 75)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MultilanguageReferrable(Referrable, ABC):
    """AUTOSAR MultilanguageReferrable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    long_name: Optional[MultilanguageLongName]
    _DESERIALIZE_DISPATCH = {
        "LONG-NAME": lambda obj, elem: setattr(obj, "long_name", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
    }


    def __init__(self) -> None:
        """Initialize MultilanguageReferrable."""
        super().__init__()
        self.long_name: Optional[MultilanguageLongName] = None

    def serialize(self) -> ET.Element:
        """Serialize MultilanguageReferrable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultilanguageReferrable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize long_name
        if self.long_name is not None:
            serialized = SerializationHelper.serialize_item(self.long_name, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LONG-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageReferrable":
        """Deserialize XML element to MultilanguageReferrable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultilanguageReferrable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultilanguageReferrable, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LONG-NAME":
                setattr(obj, "long_name", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))

        return obj



class MultilanguageReferrableBuilder(ReferrableBuilder):
    """Builder for MultilanguageReferrable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultilanguageReferrable = MultilanguageReferrable()


    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "MultilanguageReferrableBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'long_name' is required and cannot be None")
        self._obj.long_name = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "longName",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> MultilanguageReferrable:
        """Build and return the MultilanguageReferrable instance (abstract)."""
        raise NotImplementedError