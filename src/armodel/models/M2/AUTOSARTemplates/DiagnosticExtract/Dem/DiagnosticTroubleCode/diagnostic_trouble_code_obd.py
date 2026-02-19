"""DiagnosticTroubleCodeObd AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)


class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeObd."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consider_pto: Optional[Boolean]
    dtc_props_props: Optional[DiagnosticTroubleCode]
    event_readiness: Optional[EventObdReadinessGroup]
    obd_dtc_value: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeObd."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.obd_dtc_value: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTroubleCodeObd to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTroubleCodeObd, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consider_pto
        if self.consider_pto is not None:
            serialized = ARObject._serialize_item(self.consider_pto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONSIDER-PTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dtc_props_props
        if self.dtc_props_props is not None:
            serialized = ARObject._serialize_item(self.dtc_props_props, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-PROPS-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_readiness
        if self.event_readiness is not None:
            serialized = ARObject._serialize_item(self.event_readiness, "EventObdReadinessGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-READINESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize obd_dtc_value
        if self.obd_dtc_value is not None:
            serialized = ARObject._serialize_item(self.obd_dtc_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-DTC-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeObd":
        """Deserialize XML element to DiagnosticTroubleCodeObd object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTroubleCodeObd object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTroubleCodeObd, cls).deserialize(element)

        # Parse consider_pto
        child = ARObject._find_child_element(element, "CONSIDER-PTO")
        if child is not None:
            consider_pto_value = child.text
            obj.consider_pto = consider_pto_value

        # Parse dtc_props_props
        child = ARObject._find_child_element(element, "DTC-PROPS-PROPS")
        if child is not None:
            dtc_props_props_value = ARObject._deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.dtc_props_props = dtc_props_props_value

        # Parse event_readiness
        child = ARObject._find_child_element(element, "EVENT-READINESS")
        if child is not None:
            event_readiness_value = ARObject._deserialize_by_tag(child, "EventObdReadinessGroup")
            obj.event_readiness = event_readiness_value

        # Parse obd_dtc_value
        child = ARObject._find_child_element(element, "OBD-DTC-VALUE")
        if child is not None:
            obd_dtc_value_value = child.text
            obj.obd_dtc_value = obd_dtc_value_value

        return obj



class DiagnosticTroubleCodeObdBuilder:
    """Builder for DiagnosticTroubleCodeObd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeObd = DiagnosticTroubleCodeObd()

    def build(self) -> DiagnosticTroubleCodeObd:
        """Build and return DiagnosticTroubleCodeObd object.

        Returns:
            DiagnosticTroubleCodeObd instance
        """
        # TODO: Add validation
        return self._obj
