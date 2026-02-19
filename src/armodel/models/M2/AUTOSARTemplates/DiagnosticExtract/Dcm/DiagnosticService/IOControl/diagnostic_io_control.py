"""DiagnosticIOControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)


class DiagnosticIOControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticIOControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    control_enables: list[Any]
    data_identifier_identifier: Optional[DiagnosticDataIdentifier]
    freeze_current: Optional[Boolean]
    io_control_class: Optional[DiagnosticIOControl]
    reset_to_default: Optional[Boolean]
    short_term: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticIOControl."""
        super().__init__()
        self.control_enables: list[Any] = []
        self.data_identifier_identifier: Optional[DiagnosticDataIdentifier] = None
        self.freeze_current: Optional[Boolean] = None
        self.io_control_class: Optional[DiagnosticIOControl] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIOControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIOControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize control_enables (list to container "CONTROL-ENABLES")
        if self.control_enables:
            wrapper = ET.Element("CONTROL-ENABLES")
            for item in self.control_enables:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_identifier_identifier
        if self.data_identifier_identifier is not None:
            serialized = ARObject._serialize_item(self.data_identifier_identifier, "DiagnosticDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-IDENTIFIER-IDENTIFIER")
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

        # Serialize io_control_class
        if self.io_control_class is not None:
            serialized = ARObject._serialize_item(self.io_control_class, "DiagnosticIOControl")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IO-CONTROL-CLASS")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticIOControl":
        """Deserialize XML element to DiagnosticIOControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIOControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIOControl, cls).deserialize(element)

        # Parse control_enables (list from container "CONTROL-ENABLES")
        obj.control_enables = []
        container = ARObject._find_child_element(element, "CONTROL-ENABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_enables.append(child_value)

        # Parse data_identifier_identifier
        child = ARObject._find_child_element(element, "DATA-IDENTIFIER-IDENTIFIER")
        if child is not None:
            data_identifier_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.data_identifier_identifier = data_identifier_identifier_value

        # Parse freeze_current
        child = ARObject._find_child_element(element, "FREEZE-CURRENT")
        if child is not None:
            freeze_current_value = child.text
            obj.freeze_current = freeze_current_value

        # Parse io_control_class
        child = ARObject._find_child_element(element, "IO-CONTROL-CLASS")
        if child is not None:
            io_control_class_value = ARObject._deserialize_by_tag(child, "DiagnosticIOControl")
            obj.io_control_class = io_control_class_value

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



class DiagnosticIOControlBuilder:
    """Builder for DiagnosticIOControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIOControl = DiagnosticIOControl()

    def build(self) -> DiagnosticIOControl:
        """Build and return DiagnosticIOControl object.

        Returns:
            DiagnosticIOControl instance
        """
        # TODO: Add validation
        return self._obj
