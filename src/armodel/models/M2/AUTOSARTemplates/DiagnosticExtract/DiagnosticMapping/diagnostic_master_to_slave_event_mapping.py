"""DiagnosticMasterToSlaveEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 256)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticMasterToSlaveEventMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    master_event_ref: Optional[ARRef]
    slave_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticMasterToSlaveEventMapping."""
        super().__init__()
        self.master_event_ref: Optional[ARRef] = None
        self.slave_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMasterToSlaveEventMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMasterToSlaveEventMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize master_event_ref
        if self.master_event_ref is not None:
            serialized = ARObject._serialize_item(self.master_event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASTER-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slave_event_ref
        if self.slave_event_ref is not None:
            serialized = ARObject._serialize_item(self.slave_event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLAVE-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMasterToSlaveEventMapping":
        """Deserialize XML element to DiagnosticMasterToSlaveEventMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMasterToSlaveEventMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMasterToSlaveEventMapping, cls).deserialize(element)

        # Parse master_event_ref
        child = ARObject._find_child_element(element, "MASTER-EVENT-REF")
        if child is not None:
            master_event_ref_value = ARRef.deserialize(child)
            obj.master_event_ref = master_event_ref_value

        # Parse slave_event_ref
        child = ARObject._find_child_element(element, "SLAVE-EVENT-REF")
        if child is not None:
            slave_event_ref_value = ARRef.deserialize(child)
            obj.slave_event_ref = slave_event_ref_value

        return obj



class DiagnosticMasterToSlaveEventMappingBuilder:
    """Builder for DiagnosticMasterToSlaveEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMasterToSlaveEventMapping = DiagnosticMasterToSlaveEventMapping()

    def build(self) -> DiagnosticMasterToSlaveEventMapping:
        """Build and return DiagnosticMasterToSlaveEventMapping object.

        Returns:
            DiagnosticMasterToSlaveEventMapping instance
        """
        # TODO: Add validation
        return self._obj
