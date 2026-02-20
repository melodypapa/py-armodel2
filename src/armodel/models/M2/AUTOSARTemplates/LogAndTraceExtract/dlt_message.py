"""DltMessage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 12)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_argument import (
    DltArgument,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.privacy_level import (
    PrivacyLevel,
)


class DltMessage(Identifiable):
    """AUTOSAR DltMessage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dlt_arguments: list[DltArgument]
    message_id: Optional[PositiveInteger]
    message_line: Optional[PositiveInteger]
    message_source: Optional[String]
    message_type_info: Optional[String]
    privacy_level: Optional[PrivacyLevel]
    def __init__(self) -> None:
        """Initialize DltMessage."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.message_id: Optional[PositiveInteger] = None
        self.message_line: Optional[PositiveInteger] = None
        self.message_source: Optional[String] = None
        self.message_type_info: Optional[String] = None
        self.privacy_level: Optional[PrivacyLevel] = None

    def serialize(self) -> ET.Element:
        """Serialize DltMessage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltMessage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dlt_arguments (list to container "DLT-ARGUMENTS")
        if self.dlt_arguments:
            wrapper = ET.Element("DLT-ARGUMENTS")
            for item in self.dlt_arguments:
                serialized = ARObject._serialize_item(item, "DltArgument")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize message_id
        if self.message_id is not None:
            serialized = ARObject._serialize_item(self.message_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_line
        if self.message_line is not None:
            serialized = ARObject._serialize_item(self.message_line, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-LINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_source
        if self.message_source is not None:
            serialized = ARObject._serialize_item(self.message_source, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_type_info
        if self.message_type_info is not None:
            serialized = ARObject._serialize_item(self.message_type_info, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-TYPE-INFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize privacy_level
        if self.privacy_level is not None:
            serialized = ARObject._serialize_item(self.privacy_level, "PrivacyLevel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIVACY-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltMessage":
        """Deserialize XML element to DltMessage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltMessage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltMessage, cls).deserialize(element)

        # Parse dlt_arguments (list from container "DLT-ARGUMENTS")
        obj.dlt_arguments = []
        container = ARObject._find_child_element(element, "DLT-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_arguments.append(child_value)

        # Parse message_id
        child = ARObject._find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        # Parse message_line
        child = ARObject._find_child_element(element, "MESSAGE-LINE")
        if child is not None:
            message_line_value = child.text
            obj.message_line = message_line_value

        # Parse message_source
        child = ARObject._find_child_element(element, "MESSAGE-SOURCE")
        if child is not None:
            message_source_value = child.text
            obj.message_source = message_source_value

        # Parse message_type_info
        child = ARObject._find_child_element(element, "MESSAGE-TYPE-INFO")
        if child is not None:
            message_type_info_value = child.text
            obj.message_type_info = message_type_info_value

        # Parse privacy_level
        child = ARObject._find_child_element(element, "PRIVACY-LEVEL")
        if child is not None:
            privacy_level_value = ARObject._deserialize_by_tag(child, "PrivacyLevel")
            obj.privacy_level = privacy_level_value

        return obj



class DltMessageBuilder:
    """Builder for DltMessage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltMessage = DltMessage()

    def build(self) -> DltMessage:
        """Build and return DltMessage object.

        Returns:
            DltMessage instance
        """
        # TODO: Add validation
        return self._obj
