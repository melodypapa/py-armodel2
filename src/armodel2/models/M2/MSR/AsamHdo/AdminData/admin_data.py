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
        "DOC-REVISIONS": lambda obj, elem: obj.doc_revisions.append(DocRevision.deserialize(elem)),
        "LANGUAGE": lambda obj, elem: setattr(obj, "language", LEnum.deserialize(elem)),
        "SDGS": lambda obj, elem: obj.sdgs.append(Sdg.deserialize(elem)),
        "USED-LANGUAGES": lambda obj, elem: setattr(obj, "used_languages", MultiLanguagePlainText.deserialize(elem)),
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

        # Parse doc_revisions (list from container "DOC-REVISIONS")
        obj.doc_revisions = []
        container = SerializationHelper.find_child_element(element, "DOC-REVISIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.doc_revisions.append(child_value)

        # Parse language
        child = SerializationHelper.find_child_element(element, "LANGUAGE")
        if child is not None:
            language_value = LEnum.deserialize(child)
            obj.language = language_value

        # Parse sdgs (list from container "SDGS")
        obj.sdgs = []
        container = SerializationHelper.find_child_element(element, "SDGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdgs.append(child_value)

        # Parse used_languages
        child = SerializationHelper.find_child_element(element, "USED-LANGUAGES")
        if child is not None:
            used_languages_value = SerializationHelper.deserialize_by_tag(child, "MultiLanguagePlainText")
            obj.used_languages = used_languages_value

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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> AdminData:
        """Build and return the AdminData instance with validation."""
        self._validate_instance()
        pass
        return self._obj