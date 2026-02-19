"""EndToEndTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 808)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EndToEndTransformationISignalProps(ARObject):
    """AUTOSAR EndToEndTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    max_data_length: Optional[PositiveInteger]
    min_data_length: Optional[PositiveInteger]
    source_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EndToEndTransformationISignalProps."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.max_data_length: Optional[PositiveInteger] = None
        self.min_data_length: Optional[PositiveInteger] = None
        self.source_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndTransformationISignalProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize data_length
        if self.data_length is not None:
            serialized = ARObject._serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_data_length
        if self.max_data_length is not None:
            serialized = ARObject._serialize_item(self.max_data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_data_length
        if self.min_data_length is not None:
            serialized = ARObject._serialize_item(self.min_data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_id
        if self.source_id is not None:
            serialized = ARObject._serialize_item(self.source_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationISignalProps":
        """Deserialize XML element to EndToEndTransformationISignalProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndTransformationISignalProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_length
        child = ARObject._find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse max_data_length
        child = ARObject._find_child_element(element, "MAX-DATA-LENGTH")
        if child is not None:
            max_data_length_value = child.text
            obj.max_data_length = max_data_length_value

        # Parse min_data_length
        child = ARObject._find_child_element(element, "MIN-DATA-LENGTH")
        if child is not None:
            min_data_length_value = child.text
            obj.min_data_length = min_data_length_value

        # Parse source_id
        child = ARObject._find_child_element(element, "SOURCE-ID")
        if child is not None:
            source_id_value = child.text
            obj.source_id = source_id_value

        return obj



class EndToEndTransformationISignalPropsBuilder:
    """Builder for EndToEndTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndTransformationISignalProps = EndToEndTransformationISignalProps()

    def build(self) -> EndToEndTransformationISignalProps:
        """Build and return EndToEndTransformationISignalProps object.

        Returns:
            EndToEndTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
