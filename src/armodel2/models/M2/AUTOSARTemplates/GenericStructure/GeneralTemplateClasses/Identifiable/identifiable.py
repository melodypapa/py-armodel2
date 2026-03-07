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

    category: Optional[CategoryString]
    admin_data: Optional[AdminData]
    annotations: list[Annotation]
    desc: Optional[MultiLanguageOverviewParagraph]
    introduction: Optional[DocumentationBlock]
    _uuid: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "CategoryString")),
        "ADMIN-DATA": lambda obj, elem: setattr(obj, "admin_data", SerializationHelper.deserialize_by_tag(elem, "AdminData")),
        "ANNOTATIONS": lambda obj, elem: obj.annotations.append(SerializationHelper.deserialize_by_tag(elem, "Annotation")),
        "DESC": lambda obj, elem: setattr(obj, "desc", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageOverviewParagraph")),
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
    }


    def __init__(self) -> None:
        """Initialize Identifiable."""
        super().__init__()
        self.category: Optional[CategoryString] = None
        self.admin_data: Optional[AdminData] = None
        self.annotations: list[Annotation] = []
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
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

        # Parse uuid from XML attribute
        if "UUID" in element.attrib:
            obj.uuid = element.attrib["UUID"]

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "CategoryString"))
            elif tag == "ADMIN-DATA":
                setattr(obj, "admin_data", SerializationHelper.deserialize_by_tag(child, "AdminData"))
            elif tag == "ANNOTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.annotations.append(SerializationHelper.deserialize_by_tag(item_elem, "Annotation"))
            elif tag == "DESC":
                setattr(obj, "desc", SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph"))
            elif tag == "INTRODUCTION":
                setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))

        return obj



class IdentifiableBuilder(MultilanguageReferrableBuilder):
    """Builder for Identifiable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Identifiable = Identifiable()


    def with_category(self, value: Optional[CategoryString]) -> "IdentifiableBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'category' is required and cannot be None")
        self._obj.category = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "IdentifiableBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'admin_data' is required and cannot be None")
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
            raise ValueError("Attribute 'desc' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "IdentifiableBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'introduction' is required and cannot be None")
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
            raise ValueError("Attribute 'uuid' is required and cannot be None")
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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "adminData",
        "annotation",
        "category",
        "desc",
        "introduction",
        "uuid",
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
    def build(self) -> Identifiable:
        """Build and return the Identifiable instance (abstract)."""
        raise NotImplementedError