"""Identifiable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 318)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 317)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 296)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 995)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2027)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 229)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 74)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 59)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 31)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 60)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_attribute

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import MultilanguageReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    String,
)
from armodel2.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel2.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Identifiable(MultilanguageReferrable, ABC):
    """AUTOSAR Identifiable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    admin_data: Optional[AdminData]
    annotations: list[Annotation]
    desc: Optional[MultiLanguageOverviewParagraph]
    category: Optional[CategoryString]
    introduction: Optional[DocumentationBlock]
    _uuid: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "ADMIN-DATA": lambda obj, elem: setattr(obj, "admin_data", AdminData.deserialize(elem)),
        "ANNOTATIONS": lambda obj, elem: obj.annotations.append(Annotation.deserialize(elem)),
        "DESC": lambda obj, elem: setattr(obj, "desc", MultiLanguageOverviewParagraph.deserialize(elem)),
        "CATEGORY": lambda obj, elem: setattr(obj, "category", elem.text),
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", DocumentationBlock.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Identifiable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.annotations: list[Annotation] = []
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.category: Optional[CategoryString] = None
        self.introduction: Optional[DocumentationBlock] = None
        self._uuid: Optional[String] = None
    @property
    @xml_attribute
    def uuid(self) -> String:
        """Get uuid XML attribute."""
        return self._uuid

    @uuid.setter
    def uuid(self, value: String) -> None:
        """Set uuid XML attribute."""
        self._uuid = value


    def serialize(self) -> ET.Element:
        """Serialize Identifiable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Identifiable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize admin_data
        if self.admin_data is not None:
            serialized = SerializationHelper.serialize_item(self.admin_data, "AdminData")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADMIN-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize annotations (list to container "ANNOTATIONS")
        if self.annotations:
            wrapper = ET.Element("ANNOTATIONS")
            for item in self.annotations:
                serialized = SerializationHelper.serialize_item(item, "Annotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize desc
        if self.desc is not None:
            serialized = SerializationHelper.serialize_item(self.desc, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "CategoryString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize introduction
        if self.introduction is not None:
            serialized = SerializationHelper.serialize_item(self.introduction, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTRODUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uuid as XML attribute
        if self.uuid is not None:
            elem.attrib["UUID"] = str(self.uuid)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Identifiable":
        """Deserialize XML element to Identifiable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Identifiable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Identifiable, cls).deserialize(element)

        # Parse admin_data
        child = SerializationHelper.find_child_element(element, "ADMIN-DATA")
        if child is not None:
            admin_data_value = SerializationHelper.deserialize_by_tag(child, "AdminData")
            obj.admin_data = admin_data_value

        # Parse annotations (list from container "ANNOTATIONS")
        obj.annotations = []
        container = SerializationHelper.find_child_element(element, "ANNOTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.annotations.append(child_value)

        # Parse desc
        child = SerializationHelper.find_child_element(element, "DESC")
        if child is not None:
            desc_value = SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse introduction
        child = SerializationHelper.find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse uuid from XML attribute
        if "UUID" in element.attrib:
            uuid_value = element.attrib["UUID"]
            obj.uuid = uuid_value

        return obj



class IdentifiableBuilder(MultilanguageReferrableBuilder):
    """Builder for Identifiable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Identifiable = Identifiable()


    def with_admin_data(self, value: Optional[AdminData]) -> "IdentifiableBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "IdentifiableBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "IdentifiableBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "IdentifiableBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "IdentifiableBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "IdentifiableBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self


    def add_annotation(self, item: Annotation) -> "IdentifiableBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "IdentifiableBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
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


    @abstractmethod
    def build(self) -> Identifiable:
        """Build and return the Identifiable instance (abstract)."""
        raise NotImplementedError