"""MultiLanguageOverviewParagraph AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 53)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 347)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import lang_prefix

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MultiLanguageOverviewParagraph(ARObject):
    """AUTOSAR MultiLanguageOverviewParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH"


    _l2: list[LOverviewParagraph]
    _DESERIALIZE_DISPATCH = {
        "L2": lambda obj, elem: obj._l2.append(SerializationHelper.deserialize_by_tag(elem, "LOverviewParagraph")),
    }


    def __init__(self) -> None:
        """Initialize MultiLanguageOverviewParagraph."""
        super().__init__()
        self._l2: list[LOverviewParagraph] = []
    @property
    @lang_prefix("L-2")
    def l2(self) -> list[LOverviewParagraph]:
        """Get l2 with language-specific wrapper."""
        return self._l2

    @l2.setter
    def l2(self, value: list[LOverviewParagraph]) -> None:
        """Set l2 with language-specific wrapper."""
        self._l2 = value


    def serialize(self) -> ET.Element:
        """Serialize MultiLanguageOverviewParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultiLanguageOverviewParagraph, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize l2 (list with lang_prefix "L-2")
        for item in self.l2:
            serialized = SerializationHelper.serialize_item(item, "LOverviewParagraph")
            if serialized is not None:
                # For lang_prefix lists, wrap each item in the lang_prefix tag
                wrapped = ET.Element("L-2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageOverviewParagraph":
        """Deserialize XML element to MultiLanguageOverviewParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguageOverviewParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiLanguageOverviewParagraph, cls).deserialize(element)


        # Parse l2 (list with lang_prefix "L-2")
        for child in SerializationHelper.find_all_child_elements(element, "L-2"):
            l2_item = SerializationHelper.deserialize_by_tag(child, "LOverviewParagraph")
            obj._l2.append(l2_item)

        return obj



class MultiLanguageOverviewParagraphBuilder(BuilderBase):
    """Builder for MultiLanguageOverviewParagraph with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultiLanguageOverviewParagraph = MultiLanguageOverviewParagraph()


    def with_l2(self, value: LOverviewParagraph) -> "MultiLanguageOverviewParagraphBuilder":
        """Set l2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'l2' is required and cannot be None")
        self._obj.l2 = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "l2",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MultiLanguageOverviewParagraph:
        """Build and return the MultiLanguageOverviewParagraph instance with validation."""
        self._validate_instance()
        return self._obj