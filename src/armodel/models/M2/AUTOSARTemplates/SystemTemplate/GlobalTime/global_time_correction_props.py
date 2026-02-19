"""GlobalTimeCorrectionProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 862)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class GlobalTimeCorrectionProps(ARObject):
    """AUTOSAR GlobalTimeCorrectionProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    offset_correction: Optional[TimeValue]
    rate_correction: Optional[TimeValue]
    rate_corrections: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize GlobalTimeCorrectionProps."""
        super().__init__()
        self.offset_correction: Optional[TimeValue] = None
        self.rate_correction: Optional[TimeValue] = None
        self.rate_corrections: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCorrectionProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize offset_correction
        if self.offset_correction is not None:
            serialized = ARObject._serialize_item(self.offset_correction, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_correction
        if self.rate_correction is not None:
            serialized = ARObject._serialize_item(self.rate_correction, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_corrections
        if self.rate_corrections is not None:
            serialized = ARObject._serialize_item(self.rate_corrections, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTIONS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCorrectionProps":
        """Deserialize XML element to GlobalTimeCorrectionProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCorrectionProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse offset_correction
        child = ARObject._find_child_element(element, "OFFSET-CORRECTION")
        if child is not None:
            offset_correction_value = child.text
            obj.offset_correction = offset_correction_value

        # Parse rate_correction
        child = ARObject._find_child_element(element, "RATE-CORRECTION")
        if child is not None:
            rate_correction_value = child.text
            obj.rate_correction = rate_correction_value

        # Parse rate_corrections
        child = ARObject._find_child_element(element, "RATE-CORRECTIONS")
        if child is not None:
            rate_corrections_value = child.text
            obj.rate_corrections = rate_corrections_value

        return obj



class GlobalTimeCorrectionPropsBuilder:
    """Builder for GlobalTimeCorrectionProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCorrectionProps = GlobalTimeCorrectionProps()

    def build(self) -> GlobalTimeCorrectionProps:
        """Build and return GlobalTimeCorrectionProps object.

        Returns:
            GlobalTimeCorrectionProps instance
        """
        # TODO: Add validation
        return self._obj
