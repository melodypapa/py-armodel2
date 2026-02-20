"""DiagnosticMemoryIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access: Optional[DiagnosticAccessPermission]
    id: Optional[PositiveInteger]
    memory_high: Optional[String]
    memory_low: Optional[String]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryIdentifier."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.id: Optional[PositiveInteger] = None
        self.memory_high: Optional[String] = None
        self.memory_low: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access
        if self.access is not None:
            serialized = ARObject._serialize_item(self.access, "DiagnosticAccessPermission")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize id
        if self.id is not None:
            serialized = ARObject._serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize memory_high
        if self.memory_high is not None:
            serialized = ARObject._serialize_item(self.memory_high, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-HIGH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize memory_low
        if self.memory_low is not None:
            serialized = ARObject._serialize_item(self.memory_low, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-LOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryIdentifier":
        """Deserialize XML element to DiagnosticMemoryIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryIdentifier, cls).deserialize(element)

        # Parse access
        child = ARObject._find_child_element(element, "ACCESS")
        if child is not None:
            access_value = ARObject._deserialize_by_tag(child, "DiagnosticAccessPermission")
            obj.access = access_value

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse memory_high
        child = ARObject._find_child_element(element, "MEMORY-HIGH")
        if child is not None:
            memory_high_value = child.text
            obj.memory_high = memory_high_value

        # Parse memory_low
        child = ARObject._find_child_element(element, "MEMORY-LOW")
        if child is not None:
            memory_low_value = child.text
            obj.memory_low = memory_low_value

        return obj



class DiagnosticMemoryIdentifierBuilder:
    """Builder for DiagnosticMemoryIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryIdentifier = DiagnosticMemoryIdentifier()

    def build(self) -> DiagnosticMemoryIdentifier:
        """Build and return DiagnosticMemoryIdentifier object.

        Returns:
            DiagnosticMemoryIdentifier instance
        """
        # TODO: Add validation
        return self._obj
