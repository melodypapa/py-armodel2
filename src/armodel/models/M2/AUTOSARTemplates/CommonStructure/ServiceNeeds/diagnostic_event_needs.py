"""DiagnosticEventNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 258)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 756)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    deferring_fid_refs: list[ARRef]
    diag_event_debounce: Optional[Any]
    inhibiting_fid_ref: Optional[ARRef]
    inhibiting_refs: list[ARRef]
    prestored: Optional[Boolean]
    uses_monitor: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticEventNeeds."""
        super().__init__()
        self.deferring_fid_refs: list[ARRef] = []
        self.diag_event_debounce: Optional[Any] = None
        self.inhibiting_fid_ref: Optional[ARRef] = None
        self.inhibiting_refs: list[ARRef] = []
        self.prestored: Optional[Boolean] = None
        self.uses_monitor: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize deferring_fid_refs (list to container "DEFERRING-FID-REFS")
        if self.deferring_fid_refs:
            wrapper = ET.Element("DEFERRING-FID-REFS")
            for item in self.deferring_fid_refs:
                serialized = ARObject._serialize_item(item, "FunctionInhibitionNeeds")
                if serialized is not None:
                    child_elem = ET.Element("DEFERRING-FID-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize diag_event_debounce
        if self.diag_event_debounce is not None:
            serialized = ARObject._serialize_item(self.diag_event_debounce, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-EVENT-DEBOUNCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibiting_fid_ref
        if self.inhibiting_fid_ref is not None:
            serialized = ARObject._serialize_item(self.inhibiting_fid_ref, "FunctionInhibitionNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INHIBITING-FID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibiting_refs (list to container "INHIBITING-REFS")
        if self.inhibiting_refs:
            wrapper = ET.Element("INHIBITING-REFS")
            for item in self.inhibiting_refs:
                serialized = ARObject._serialize_item(item, "FunctionInhibitionNeeds")
                if serialized is not None:
                    child_elem = ET.Element("INHIBITING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize prestored
        if self.prestored is not None:
            serialized = ARObject._serialize_item(self.prestored, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRESTORED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_monitor
        if self.uses_monitor is not None:
            serialized = ARObject._serialize_item(self.uses_monitor, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-MONITOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventNeeds":
        """Deserialize XML element to DiagnosticEventNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventNeeds, cls).deserialize(element)

        # Parse deferring_fid_refs (list from container "DEFERRING-FID-REFS")
        obj.deferring_fid_refs = []
        container = ARObject._find_child_element(element, "DEFERRING-FID-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.deferring_fid_refs.append(child_value)

        # Parse diag_event_debounce
        child = ARObject._find_child_element(element, "DIAG-EVENT-DEBOUNCE")
        if child is not None:
            diag_event_debounce_value = child.text
            obj.diag_event_debounce = diag_event_debounce_value

        # Parse inhibiting_fid_ref
        child = ARObject._find_child_element(element, "INHIBITING-FID-REF")
        if child is not None:
            inhibiting_fid_ref_value = ARRef.deserialize(child)
            obj.inhibiting_fid_ref = inhibiting_fid_ref_value

        # Parse inhibiting_refs (list from container "INHIBITING-REFS")
        obj.inhibiting_refs = []
        container = ARObject._find_child_element(element, "INHIBITING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.inhibiting_refs.append(child_value)

        # Parse prestored
        child = ARObject._find_child_element(element, "PRESTORED")
        if child is not None:
            prestored_value = child.text
            obj.prestored = prestored_value

        # Parse uses_monitor
        child = ARObject._find_child_element(element, "USES-MONITOR")
        if child is not None:
            uses_monitor_value = child.text
            obj.uses_monitor = uses_monitor_value

        return obj



class DiagnosticEventNeedsBuilder:
    """Builder for DiagnosticEventNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventNeeds = DiagnosticEventNeeds()

    def build(self) -> DiagnosticEventNeeds:
        """Build and return DiagnosticEventNeeds object.

        Returns:
            DiagnosticEventNeeds instance
        """
        # TODO: Add validation
        return self._obj
