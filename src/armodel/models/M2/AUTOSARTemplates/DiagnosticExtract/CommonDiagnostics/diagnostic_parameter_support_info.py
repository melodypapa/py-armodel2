"""DiagnosticParameterSupportInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticParameterSupportInfo(ARObject):
    """AUTOSAR DiagnosticParameterSupportInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    support_info_bit: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterSupportInfo."""
        super().__init__()
        self.support_info_bit: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterSupportInfo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize support_info_bit
        if self.support_info_bit is not None:
            serialized = SerializationHelper.serialize_item(self.support_info_bit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-INFO-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterSupportInfo":
        """Deserialize XML element to DiagnosticParameterSupportInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterSupportInfo object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse support_info_bit
        child = SerializationHelper.find_child_element(element, "SUPPORT-INFO-BIT")
        if child is not None:
            support_info_bit_value = child.text
            obj.support_info_bit = support_info_bit_value

        return obj



class DiagnosticParameterSupportInfoBuilder:
    """Builder for DiagnosticParameterSupportInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterSupportInfo = DiagnosticParameterSupportInfo()

    def build(self) -> DiagnosticParameterSupportInfo:
        """Build and return DiagnosticParameterSupportInfo object.

        Returns:
            DiagnosticParameterSupportInfo instance
        """
        # TODO: Add validation
        return self._obj
