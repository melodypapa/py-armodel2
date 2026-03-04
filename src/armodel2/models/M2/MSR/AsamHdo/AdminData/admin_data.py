"""AdminData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 288)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 969)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1994)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 72)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 84)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
)
from armodel2.models.M2.MSR.AsamHdo.AdminData.doc_revision import (
    DocRevision,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
    MultiLanguagePlainText,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AdminData(ARObject):
    """AUTOSAR AdminData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ADMIN-DATA"


    doc_revisions: list[DocRevision]
    language: Optional[LEnum]
    sdgs: list[Sdg]
    used_languages: Optional[MultiLanguagePlainText]
    _DESERIALIZE_DISPATCH = {
        "DOC-REVISIONS": lambda obj, elem: obj.doc_revisions.append(SerializationHelper.deserialize_by_tag(elem, "DocRevision")),
        "LANGUAGE": lambda obj, elem: setattr(obj, "language", LEnum.deserialize(elem)),
        "SDGS": lambda obj, elem: obj.sdgs.append(SerializationHelper.deserialize_by_tag(elem, "Sdg")),
        "USED-LANGUAGES": lambda obj, elem: setattr(obj, "used_languages", SerializationHelper.deserialize_by_tag(elem, "MultiLanguagePlainText")),
    }


    def __init__(self) -> None:
        """Initialize AdminData."""
        super().__init__()
        self.doc_revisions: list[DocRevision] = []
        self.language: Optional[LEnum] = None
        self.sdgs: list[Sdg] = []
        self.used_languages: Optional[MultiLanguagePlainText] = None

    def serialize(self) -> ET.Element:
        """Serialize AdminData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AdminData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize doc_revisions (list to container "DOC-REVISIONS")
        if self.doc_revisions:
            wrapper = ET.Element("DOC-REVISIONS")
            for item in self.doc_revisions:
                serialized = SerializationHelper.serialize_item(item, "DocRevision")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize language
        if self.language is not None:
            serialized = SerializationHelper.serialize_item(self.language, "LEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LANGUAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = SerializationHelper.serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize used_languages
        if self.used_languages is not None:
            serialized = SerializationHelper.serialize_item(self.used_languages, "MultiLanguagePlainText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-LANGUAGES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AdminData":
        """Deserialize XML element to AdminData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AdminData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AdminData, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DOC-REVISIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.doc_revisions.append(SerializationHelper.deserialize_by_tag(item_elem, "DocRevision"))
            elif tag == "LANGUAGE":
                setattr(obj, "language", LEnum.deserialize(child))
            elif tag == "SDGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sdgs.append(SerializationHelper.deserialize_by_tag(item_elem, "Sdg"))
            elif tag == "USED-LANGUAGES":
                setattr(obj, "used_languages", SerializationHelper.deserialize_by_tag(child, "MultiLanguagePlainText"))

        return obj



class AdminDataBuilder(BuilderBase):
    """Builder for AdminData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AdminData = AdminData()


    def with_doc_revisions(self, items: list[DocRevision]) -> "AdminDataBuilder":
        """Set doc_revisions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.doc_revisions = list(items) if items else []
        return self

    def with_language(self, value: Optional[LEnum]) -> "AdminDataBuilder":
        """Set language attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.language = value
        return self

    def with_sdgs(self, items: list[Sdg]) -> "AdminDataBuilder":
        """Set sdgs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdgs = list(items) if items else []
        return self

    def with_used_languages(self, value: Optional[MultiLanguagePlainText]) -> "AdminDataBuilder":
        """Set used_languages attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_languages = value
        return self


    def add_doc_revision(self, item: DocRevision) -> "AdminDataBuilder":
        """Add a single item to doc_revisions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.doc_revisions.append(item)
        return self

    def clear_doc_revisions(self) -> "AdminDataBuilder":
        """Clear all items from doc_revisions list.

        Returns:
            self for method chaining
        """
        self._obj.doc_revisions = []
        return self

    def add_sdg(self, item: Sdg) -> "AdminDataBuilder":
        """Add a single item to sdgs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdgs.append(item)
        return self

    def clear_sdgs(self) -> "AdminDataBuilder":
        """Clear all items from sdgs list.

        Returns:
            self for method chaining
        """
        self._obj.sdgs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "docRevision",
        "language",
        "sdg",
        "usedLanguages",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AdminData:
        """Build and return the AdminData instance with validation."""
        self._validate_instance()
        return self._obj