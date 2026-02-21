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

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    String,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from abc import ABC, abstractmethod


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
    uuid: Optional[String]
    def __init__(self) -> None:
        """Initialize Identifiable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.annotations: list[Annotation] = []
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.category: Optional[CategoryString] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.uuid: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize Identifiable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Serialize uuid
        if self.uuid is not None:
            serialized = SerializationHelper.serialize_item(self.uuid, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UUID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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
            desc_value = SerializationHelper.deserialize_with_type(child, "MultiLanguageOverviewParagraph")
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

        # Parse uuid
        child = SerializationHelper.find_child_element(element, "UUID")
        if child is not None:
            uuid_value = child.text
            obj.uuid = uuid_value

        return obj



class IdentifiableBuilder:
    """Builder for Identifiable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Identifiable = Identifiable()

    def build(self) -> Identifiable:
        """Build and return Identifiable object.

        Returns:
            Identifiable instance
        """
        # TODO: Add validation
        return self._obj
