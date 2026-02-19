"""SwRecordLayoutGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 422)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2066)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AsamRecordLayoutSemantics,
    RecordLayoutIteratorPoint,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutGroup(ARObject):
    """AUTOSAR SwRecordLayoutGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[AsamRecordLayoutSemantics]
    desc: Optional[MultiLanguageOverviewParagraph]
    short_label: Optional[Identifier]
    sw_generic_axis_param: Optional[SwGenericAxisParam]
    sw_record: Optional[RecordLayoutIteratorPoint]
    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroup."""
        super().__init__()
        self.category: Optional[AsamRecordLayoutSemantics] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None
        self.sw_record: Optional[RecordLayoutIteratorPoint] = None
    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = ARObject._serialize_item(self.category, "AsamRecordLayoutSemantics")
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

        # Serialize desc
        if self.desc is not None:
            serialized = ARObject._serialize_item(self.desc, "MultiLanguageOverviewParagraph")
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

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_generic_axis_param
        if self.sw_generic_axis_param is not None:
            serialized = ARObject._serialize_item(self.sw_generic_axis_param, "SwGenericAxisParam")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS-PARAM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record
        if self.sw_record is not None:
            serialized = ARObject._serialize_item(self.sw_record, "RecordLayoutIteratorPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroup":
        """Deserialize XML element to SwRecordLayoutGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse desc
        child = ARObject._find_child_element(element, "DESC")
        if child is not None:
            desc_value = ARObject._deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse sw_generic_axis_param
        child = ARObject._find_child_element(element, "SW-GENERIC-AXIS-PARAM")
        if child is not None:
            sw_generic_axis_param_value = ARObject._deserialize_by_tag(child, "SwGenericAxisParam")
            obj.sw_generic_axis_param = sw_generic_axis_param_value

        # Parse sw_record
        child = ARObject._find_child_element(element, "SW-RECORD")
        if child is not None:
            sw_record_value = child.text
            obj.sw_record = sw_record_value

        return obj



class SwRecordLayoutGroupBuilder:
    """Builder for SwRecordLayoutGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutGroup = SwRecordLayoutGroup()

    def build(self) -> SwRecordLayoutGroup:
        """Build and return SwRecordLayoutGroup object.

        Returns:
            SwRecordLayoutGroup instance
        """
        # TODO: Add validation
        return self._obj
