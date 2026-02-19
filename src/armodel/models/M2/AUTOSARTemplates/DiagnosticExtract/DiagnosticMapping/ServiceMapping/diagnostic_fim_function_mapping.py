"""DiagnosticFimFunctionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticFimFunctionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mapped_bsw: Optional[Any]
    mapped_flat_swc: Optional[Any]
    mapped: Optional[Any]
    mapped_swc: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFimFunctionMapping."""
        super().__init__()
        self.mapped_bsw: Optional[Any] = None
        self.mapped_flat_swc: Optional[Any] = None
        self.mapped: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimFunctionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimFunctionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mapped_bsw
        if self.mapped_bsw is not None:
            serialized = ARObject._serialize_item(self.mapped_bsw, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-BSW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_flat_swc
        if self.mapped_flat_swc is not None:
            serialized = ARObject._serialize_item(self.mapped_flat_swc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-FLAT-SWC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped
        if self.mapped is not None:
            serialized = ARObject._serialize_item(self.mapped, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_swc
        if self.mapped_swc is not None:
            serialized = ARObject._serialize_item(self.mapped_swc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-SWC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimFunctionMapping":
        """Deserialize XML element to DiagnosticFimFunctionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimFunctionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimFunctionMapping, cls).deserialize(element)

        # Parse mapped_bsw
        child = ARObject._find_child_element(element, "MAPPED-BSW")
        if child is not None:
            mapped_bsw_value = child.text
            obj.mapped_bsw = mapped_bsw_value

        # Parse mapped_flat_swc
        child = ARObject._find_child_element(element, "MAPPED-FLAT-SWC")
        if child is not None:
            mapped_flat_swc_value = child.text
            obj.mapped_flat_swc = mapped_flat_swc_value

        # Parse mapped
        child = ARObject._find_child_element(element, "MAPPED")
        if child is not None:
            mapped_value = child.text
            obj.mapped = mapped_value

        # Parse mapped_swc
        child = ARObject._find_child_element(element, "MAPPED-SWC")
        if child is not None:
            mapped_swc_value = child.text
            obj.mapped_swc = mapped_swc_value

        return obj



class DiagnosticFimFunctionMappingBuilder:
    """Builder for DiagnosticFimFunctionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimFunctionMapping = DiagnosticFimFunctionMapping()

    def build(self) -> DiagnosticFimFunctionMapping:
        """Build and return DiagnosticFimFunctionMapping object.

        Returns:
            DiagnosticFimFunctionMapping instance
        """
        # TODO: Add validation
        return self._obj
