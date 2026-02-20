"""DiagnosticEnableConditionPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 251)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEnableConditionPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enable_condition: Optional[Any]
    swc_flat_service: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionPortMapping."""
        super().__init__()
        self.enable_condition: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnableConditionPortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnableConditionPortMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enable_condition
        if self.enable_condition is not None:
            serialized = ARObject._serialize_item(self.enable_condition, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_flat_service
        if self.swc_flat_service is not None:
            serialized = ARObject._serialize_item(self.swc_flat_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-FLAT-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_service
        if self.swc_service is not None:
            serialized = ARObject._serialize_item(self.swc_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionPortMapping":
        """Deserialize XML element to DiagnosticEnableConditionPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnableConditionPortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnableConditionPortMapping, cls).deserialize(element)

        # Parse enable_condition
        child = ARObject._find_child_element(element, "ENABLE-CONDITION")
        if child is not None:
            enable_condition_value = child.text
            obj.enable_condition = enable_condition_value

        # Parse swc_flat_service
        child = ARObject._find_child_element(element, "SWC-FLAT-SERVICE")
        if child is not None:
            swc_flat_service_value = child.text
            obj.swc_flat_service = swc_flat_service_value

        # Parse swc_service
        child = ARObject._find_child_element(element, "SWC-SERVICE")
        if child is not None:
            swc_service_value = child.text
            obj.swc_service = swc_service_value

        return obj



class DiagnosticEnableConditionPortMappingBuilder:
    """Builder for DiagnosticEnableConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionPortMapping = DiagnosticEnableConditionPortMapping()

    def build(self) -> DiagnosticEnableConditionPortMapping:
        """Build and return DiagnosticEnableConditionPortMapping object.

        Returns:
            DiagnosticEnableConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
