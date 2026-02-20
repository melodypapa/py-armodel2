"""DiagnosticIoControlNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 248)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 781)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
    DiagnosticValueNeeds,
)


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticIoControlNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    current_value: Optional[DiagnosticValueNeeds]
    freeze_current: Optional[Boolean]
    reset_to_default: Optional[Boolean]
    short_term: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticIoControlNeeds."""
        super().__init__()
        self.current_value: Optional[DiagnosticValueNeeds] = None
        self.freeze_current: Optional[Boolean] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIoControlNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIoControlNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize current_value
        if self.current_value is not None:
            serialized = ARObject._serialize_item(self.current_value, "DiagnosticValueNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CURRENT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freeze_current
        if self.freeze_current is not None:
            serialized = ARObject._serialize_item(self.freeze_current, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FREEZE-CURRENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reset_to_default
        if self.reset_to_default is not None:
            serialized = ARObject._serialize_item(self.reset_to_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESET-TO-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_term
        if self.short_term is not None:
            serialized = ARObject._serialize_item(self.short_term, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-TERM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIoControlNeeds":
        """Deserialize XML element to DiagnosticIoControlNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIoControlNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIoControlNeeds, cls).deserialize(element)

        # Parse current_value
        child = ARObject._find_child_element(element, "CURRENT-VALUE")
        if child is not None:
            current_value_value = ARObject._deserialize_by_tag(child, "DiagnosticValueNeeds")
            obj.current_value = current_value_value

        # Parse freeze_current
        child = ARObject._find_child_element(element, "FREEZE-CURRENT")
        if child is not None:
            freeze_current_value = child.text
            obj.freeze_current = freeze_current_value

        # Parse reset_to_default
        child = ARObject._find_child_element(element, "RESET-TO-DEFAULT")
        if child is not None:
            reset_to_default_value = child.text
            obj.reset_to_default = reset_to_default_value

        # Parse short_term
        child = ARObject._find_child_element(element, "SHORT-TERM")
        if child is not None:
            short_term_value = child.text
            obj.short_term = short_term_value

        return obj



class DiagnosticIoControlNeedsBuilder:
    """Builder for DiagnosticIoControlNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIoControlNeeds = DiagnosticIoControlNeeds()

    def build(self) -> DiagnosticIoControlNeeds:
        """Build and return DiagnosticIoControlNeeds object.

        Returns:
            DiagnosticIoControlNeeds instance
        """
        # TODO: Add validation
        return self._obj
