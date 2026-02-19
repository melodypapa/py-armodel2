"""DiagnosticPeriodicRate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticPeriodicRate(ARObject):
    """AUTOSAR DiagnosticPeriodicRate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    periodic_rate: Optional[DiagnosticPeriodicRate]
    def __init__(self) -> None:
        """Initialize DiagnosticPeriodicRate."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.periodic_rate: Optional[DiagnosticPeriodicRate] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticPeriodicRate to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize period
        if self.period is not None:
            serialized = ARObject._serialize_item(self.period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize periodic_rate
        if self.periodic_rate is not None:
            serialized = ARObject._serialize_item(self.periodic_rate, "DiagnosticPeriodicRate")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIODIC-RATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticPeriodicRate":
        """Deserialize XML element to DiagnosticPeriodicRate object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticPeriodicRate object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        # Parse periodic_rate
        child = ARObject._find_child_element(element, "PERIODIC-RATE")
        if child is not None:
            periodic_rate_value = ARObject._deserialize_by_tag(child, "DiagnosticPeriodicRate")
            obj.periodic_rate = periodic_rate_value

        return obj



class DiagnosticPeriodicRateBuilder:
    """Builder for DiagnosticPeriodicRate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPeriodicRate = DiagnosticPeriodicRate()

    def build(self) -> DiagnosticPeriodicRate:
        """Build and return DiagnosticPeriodicRate object.

        Returns:
            DiagnosticPeriodicRate instance
        """
        # TODO: Add validation
        return self._obj
