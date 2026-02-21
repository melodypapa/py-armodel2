"""Xref AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 320)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)


class Xref(ARObject):
    """AUTOSAR Xref."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label1: Optional[SingleLanguageLongName]
    referrable_ref: Optional[ARRef]
    resolution_policy_enum: Optional[ResolutionPolicyEnum]
    show_content_enum: Optional[ShowContentEnum]
    show_resource_alias: Optional[ShowResourceAliasNameEnum]
    show_resource: Optional[ShowResourceTypeEnum]
    show_resource_long: Optional[ShowResourceLongNameEnum]
    show_resource_number: Optional[ShowResourceNumberEnum]
    show_resource_page: Optional[ShowResourcePageEnum]
    show_resource_short: Optional[ShowResourceShortNameEnum]
    show_see: Optional[ShowSeeEnum]
    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable_ref: Optional[ARRef] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Xref to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xref, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label1
        if self.label1 is not None:
            serialized = SerializationHelper.serialize_item(self.label1, "SingleLanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize referrable_ref
        if self.referrable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.referrable_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERRABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resolution_policy_enum
        if self.resolution_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.resolution_policy_enum, "ResolutionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOLUTION-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_content_enum
        if self.show_content_enum is not None:
            serialized = SerializationHelper.serialize_item(self.show_content_enum, "ShowContentEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-CONTENT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_alias
        if self.show_resource_alias is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_alias, "ShowResourceAliasNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-ALIAS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource
        if self.show_resource is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource, "ShowResourceTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_long
        if self.show_resource_long is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_long, "ShowResourceLongNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-LONG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_number
        if self.show_resource_number is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_number, "ShowResourceNumberEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_page
        if self.show_resource_page is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_page, "ShowResourcePageEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-PAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_short
        if self.show_resource_short is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_short, "ShowResourceShortNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-SHORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_see
        if self.show_see is not None:
            serialized = SerializationHelper.serialize_item(self.show_see, "ShowSeeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-SEE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xref":
        """Deserialize XML element to Xref object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xref object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xref, cls).deserialize(element)

        # Parse label1
        child = SerializationHelper.find_child_element(element, "LABEL1")
        if child is not None:
            label1_value = SerializationHelper.deserialize_by_tag(child, "SingleLanguageLongName")
            obj.label1 = label1_value

        # Parse referrable_ref
        child = SerializationHelper.find_child_element(element, "REFERRABLE-REF")
        if child is not None:
            referrable_ref_value = ARRef.deserialize(child)
            obj.referrable_ref = referrable_ref_value

        # Parse resolution_policy_enum
        child = SerializationHelper.find_child_element(element, "RESOLUTION-POLICY-ENUM")
        if child is not None:
            resolution_policy_enum_value = ResolutionPolicyEnum.deserialize(child)
            obj.resolution_policy_enum = resolution_policy_enum_value

        # Parse show_content_enum
        child = SerializationHelper.find_child_element(element, "SHOW-CONTENT-ENUM")
        if child is not None:
            show_content_enum_value = ShowContentEnum.deserialize(child)
            obj.show_content_enum = show_content_enum_value

        # Parse show_resource_alias
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-ALIAS")
        if child is not None:
            show_resource_alias_value = ShowResourceAliasNameEnum.deserialize(child)
            obj.show_resource_alias = show_resource_alias_value

        # Parse show_resource
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE")
        if child is not None:
            show_resource_value = ShowResourceTypeEnum.deserialize(child)
            obj.show_resource = show_resource_value

        # Parse show_resource_long
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-LONG")
        if child is not None:
            show_resource_long_value = ShowResourceLongNameEnum.deserialize(child)
            obj.show_resource_long = show_resource_long_value

        # Parse show_resource_number
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-NUMBER")
        if child is not None:
            show_resource_number_value = ShowResourceNumberEnum.deserialize(child)
            obj.show_resource_number = show_resource_number_value

        # Parse show_resource_page
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-PAGE")
        if child is not None:
            show_resource_page_value = ShowResourcePageEnum.deserialize(child)
            obj.show_resource_page = show_resource_page_value

        # Parse show_resource_short
        child = SerializationHelper.find_child_element(element, "SHOW-RESOURCE-SHORT")
        if child is not None:
            show_resource_short_value = ShowResourceShortNameEnum.deserialize(child)
            obj.show_resource_short = show_resource_short_value

        # Parse show_see
        child = SerializationHelper.find_child_element(element, "SHOW-SEE")
        if child is not None:
            show_see_value = ShowSeeEnum.deserialize(child)
            obj.show_see = show_see_value

        return obj



class XrefBuilder:
    """Builder for Xref."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xref = Xref()

    def build(self) -> Xref:
        """Build and return Xref object.

        Returns:
            Xref instance
        """
        # TODO: Add validation
        return self._obj
