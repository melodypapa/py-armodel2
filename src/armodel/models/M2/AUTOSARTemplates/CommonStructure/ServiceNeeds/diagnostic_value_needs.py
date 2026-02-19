"""DiagnosticValueNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 245)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 114)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticProcessingStyleEnum,
    DiagnosticValueAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticValueNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    diagnostic_value_access: Optional[DiagnosticValueAccessEnum]
    fixed_length: Optional[Boolean]
    processing_style: Optional[DiagnosticProcessingStyleEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticValueNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.diagnostic_value_access: Optional[DiagnosticValueAccessEnum] = None
        self.fixed_length: Optional[Boolean] = None
        self.processing_style: Optional[DiagnosticProcessingStyleEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticValueNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticValueNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_length
        if self.data_length is not None:
            serialized = ARObject._serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_value_access
        if self.diagnostic_value_access is not None:
            serialized = ARObject._serialize_item(self.diagnostic_value_access, "DiagnosticValueAccessEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-VALUE-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fixed_length
        if self.fixed_length is not None:
            serialized = ARObject._serialize_item(self.fixed_length, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIXED-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processing_style
        if self.processing_style is not None:
            serialized = ARObject._serialize_item(self.processing_style, "DiagnosticProcessingStyleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-STYLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticValueNeeds":
        """Deserialize XML element to DiagnosticValueNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticValueNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticValueNeeds, cls).deserialize(element)

        # Parse data_length
        child = ARObject._find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse diagnostic_value_access
        child = ARObject._find_child_element(element, "DIAGNOSTIC-VALUE-ACCESS")
        if child is not None:
            diagnostic_value_access_value = DiagnosticValueAccessEnum.deserialize(child)
            obj.diagnostic_value_access = diagnostic_value_access_value

        # Parse fixed_length
        child = ARObject._find_child_element(element, "FIXED-LENGTH")
        if child is not None:
            fixed_length_value = child.text
            obj.fixed_length = fixed_length_value

        # Parse processing_style
        child = ARObject._find_child_element(element, "PROCESSING-STYLE")
        if child is not None:
            processing_style_value = DiagnosticProcessingStyleEnum.deserialize(child)
            obj.processing_style = processing_style_value

        return obj



class DiagnosticValueNeedsBuilder:
    """Builder for DiagnosticValueNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticValueNeeds = DiagnosticValueNeeds()

    def build(self) -> DiagnosticValueNeeds:
        """Build and return DiagnosticValueNeeds object.

        Returns:
            DiagnosticValueNeeds instance
        """
        # TODO: Add validation
        return self._obj
