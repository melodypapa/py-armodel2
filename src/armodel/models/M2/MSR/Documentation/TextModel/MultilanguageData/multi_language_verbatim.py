"""MultiLanguageVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 291)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import l_prefix

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FloatEnum,
    PgwideEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_verbatim import (
    LVerbatim,
)


class MultiLanguageVerbatim(Paginateable):
    """AUTOSAR MultiLanguageVerbatim."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allow_break: Optional[NameToken]
    float: Optional[FloatEnum]
    help_entry: Optional[String]
    _l5: list[LVerbatim]
    pgwide: Optional[PgwideEnum]
    def __init__(self) -> None:
        """Initialize MultiLanguageVerbatim."""
        super().__init__()
        self.allow_break: Optional[NameToken] = None
        self.float: Optional[FloatEnum] = None
        self.help_entry: Optional[String] = None
        self._l5: list[LVerbatim] = []
        self.pgwide: Optional[PgwideEnum] = None
    @property
    @l_prefix("L-5")
    def l5(self) -> list[LVerbatim]:
        """Get l5 with language-specific wrapper."""
        return self._l5

    @l5.setter
    def l5(self, value: list[LVerbatim]) -> None:
        """Set l5 with language-specific wrapper."""
        self._l5 = value


    def serialize(self) -> ET.Element:
        """Serialize MultiLanguageVerbatim to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultiLanguageVerbatim, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allow_break
        if self.allow_break is not None:
            serialized = ARObject._serialize_item(self.allow_break, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOW-BREAK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize float
        if self.float is not None:
            serialized = ARObject._serialize_item(self.float, "FloatEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = ARObject._serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize l5 (list with l_prefix "L-5")
        for item in self.l5:
            serialized = ARObject._serialize_item(item, "LVerbatim")
            if serialized is not None:
                # For l_prefix lists, wrap each item in the l_prefix tag
                wrapped = ET.Element("L-5")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pgwide
        if self.pgwide is not None:
            serialized = ARObject._serialize_item(self.pgwide, "PgwideEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PGWIDE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageVerbatim":
        """Deserialize XML element to MultiLanguageVerbatim object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguageVerbatim object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiLanguageVerbatim, cls).deserialize(element)

        # Parse allow_break
        child = ARObject._find_child_element(element, "ALLOW-BREAK")
        if child is not None:
            allow_break_value = child.text
            obj.allow_break = allow_break_value

        # Parse float
        child = ARObject._find_child_element(element, "FLOAT")
        if child is not None:
            float_value = FloatEnum.deserialize(child)
            obj.float = float_value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse l5 (list with l_prefix "L-5")
        obj.l5 = []
        for child in ARObject._find_all_child_elements(element, "L-5"):
            l5_value = ARObject._deserialize_by_tag(child, "LVerbatim")
            obj.l5.append(l5_value)

        # Parse pgwide
        child = ARObject._find_child_element(element, "PGWIDE")
        if child is not None:
            pgwide_value = PgwideEnum.deserialize(child)
            obj.pgwide = pgwide_value

        return obj



class MultiLanguageVerbatimBuilder:
    """Builder for MultiLanguageVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageVerbatim = MultiLanguageVerbatim()

    def build(self) -> MultiLanguageVerbatim:
        """Build and return MultiLanguageVerbatim object.

        Returns:
            MultiLanguageVerbatim instance
        """
        # TODO: Add validation
        return self._obj
