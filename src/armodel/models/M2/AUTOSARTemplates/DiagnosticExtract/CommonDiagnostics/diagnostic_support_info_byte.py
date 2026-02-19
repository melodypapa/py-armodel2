"""DiagnosticSupportInfoByte AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticSupportInfoByte(ARObject):
    """AUTOSAR DiagnosticSupportInfoByte."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    position: Optional[PositiveInteger]
    size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticSupportInfoByte."""
        super().__init__()
        self.position: Optional[PositiveInteger] = None
        self.size: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSupportInfoByte to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize position
        if self.position is not None:
            serialized = ARObject._serialize_item(self.position, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = ARObject._serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSupportInfoByte":
        """Deserialize XML element to DiagnosticSupportInfoByte object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSupportInfoByte object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse position
        child = ARObject._find_child_element(element, "POSITION")
        if child is not None:
            position_value = child.text
            obj.position = position_value

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        return obj



class DiagnosticSupportInfoByteBuilder:
    """Builder for DiagnosticSupportInfoByte."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSupportInfoByte = DiagnosticSupportInfoByte()

    def build(self) -> DiagnosticSupportInfoByte:
        """Build and return DiagnosticSupportInfoByte object.

        Returns:
            DiagnosticSupportInfoByte instance
        """
        # TODO: Add validation
        return self._obj
