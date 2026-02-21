"""SwRecordLayoutV AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwRecordLayoutV(ARObject):
    """AUTOSAR SwRecordLayoutV."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_type_ref: Optional[ARRef]
    desc: Optional[MultiLanguageOverviewParagraph]
    short_label: Optional[Identifier]
    sw_generic_axis_param_ref: Optional[ARRef]
    sw_record: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize SwRecordLayoutV."""
        super().__init__()
        self.base_type_ref: Optional[ARRef] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param_ref: Optional[ARRef] = None
        self.sw_record: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutV to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize base_type_ref
        if self.base_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_ref, "SwBaseType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
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

        # Serialize sw_generic_axis_param_ref
        if self.sw_generic_axis_param_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_generic_axis_param_ref, "SwGenericAxisParam")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS-PARAM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record
        if self.sw_record is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record, "NameToken")
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
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutV":
        """Deserialize XML element to SwRecordLayoutV object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutV object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_type_ref
        child = SerializationHelper.find_child_element(element, "BASE-TYPE-REF")
        if child is not None:
            base_type_ref_value = ARRef.deserialize(child)
            obj.base_type_ref = base_type_ref_value

        # Parse desc
        child = SerializationHelper.find_child_element(element, "DESC")
        if child is not None:
            desc_value = SerializationHelper.deserialize_with_type(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse sw_generic_axis_param_ref
        child = SerializationHelper.find_child_element(element, "SW-GENERIC-AXIS-PARAM-REF")
        if child is not None:
            sw_generic_axis_param_ref_value = ARRef.deserialize(child)
            obj.sw_generic_axis_param_ref = sw_generic_axis_param_ref_value

        # Parse sw_record
        child = SerializationHelper.find_child_element(element, "SW-RECORD")
        if child is not None:
            sw_record_value = child.text
            obj.sw_record = sw_record_value

        return obj



class SwRecordLayoutVBuilder:
    """Builder for SwRecordLayoutV."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutV = SwRecordLayoutV()

    def build(self) -> SwRecordLayoutV:
        """Build and return SwRecordLayoutV object.

        Returns:
            SwRecordLayoutV instance
        """
        # TODO: Add validation
        return self._obj
