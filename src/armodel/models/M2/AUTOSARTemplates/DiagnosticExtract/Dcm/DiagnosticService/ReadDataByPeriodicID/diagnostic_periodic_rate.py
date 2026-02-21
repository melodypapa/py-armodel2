"""DiagnosticPeriodicRate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticPeriodicRate, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize period
        if self.period is not None:
            serialized = SerializationHelper.serialize_item(self.period, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.periodic_rate, "DiagnosticPeriodicRate")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticPeriodicRate, cls).deserialize(element)

        # Parse period
        child = SerializationHelper.find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        # Parse periodic_rate
        child = SerializationHelper.find_child_element(element, "PERIODIC-RATE")
        if child is not None:
            periodic_rate_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticPeriodicRate")
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
