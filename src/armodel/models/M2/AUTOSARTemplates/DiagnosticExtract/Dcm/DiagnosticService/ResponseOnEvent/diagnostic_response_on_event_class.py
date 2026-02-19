"""DiagnosticResponseOnEventClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticResponseOnEventClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of: Optional[PositiveInteger]
    max_num: Optional[PositiveInteger]
    max_supported: Optional[PositiveInteger]
    response_on: Optional[TimeValue]
    store_event: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEventClass."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.max_num: Optional[PositiveInteger] = None
        self.max_supported: Optional[PositiveInteger] = None
        self.response_on: Optional[TimeValue] = None
        self.store_event: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticResponseOnEventClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticResponseOnEventClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = ARObject._serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_num
        if self.max_num is not None:
            serialized = ARObject._serialize_item(self.max_num, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_supported
        if self.max_supported is not None:
            serialized = ARObject._serialize_item(self.max_supported, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SUPPORTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_on
        if self.response_on is not None:
            serialized = ARObject._serialize_item(self.response_on, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_event
        if self.store_event is not None:
            serialized = ARObject._serialize_item(self.store_event, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticResponseOnEventClass":
        """Deserialize XML element to DiagnosticResponseOnEventClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticResponseOnEventClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticResponseOnEventClass, cls).deserialize(element)

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse max_num
        child = ARObject._find_child_element(element, "MAX-NUM")
        if child is not None:
            max_num_value = child.text
            obj.max_num = max_num_value

        # Parse max_supported
        child = ARObject._find_child_element(element, "MAX-SUPPORTED")
        if child is not None:
            max_supported_value = child.text
            obj.max_supported = max_supported_value

        # Parse response_on
        child = ARObject._find_child_element(element, "RESPONSE-ON")
        if child is not None:
            response_on_value = child.text
            obj.response_on = response_on_value

        # Parse store_event
        child = ARObject._find_child_element(element, "STORE-EVENT")
        if child is not None:
            store_event_value = child.text
            obj.store_event = store_event_value

        return obj



class DiagnosticResponseOnEventClassBuilder:
    """Builder for DiagnosticResponseOnEventClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEventClass = DiagnosticResponseOnEventClass()

    def build(self) -> DiagnosticResponseOnEventClass:
        """Build and return DiagnosticResponseOnEventClass object.

        Returns:
            DiagnosticResponseOnEventClass instance
        """
        # TODO: Add validation
        return self._obj
