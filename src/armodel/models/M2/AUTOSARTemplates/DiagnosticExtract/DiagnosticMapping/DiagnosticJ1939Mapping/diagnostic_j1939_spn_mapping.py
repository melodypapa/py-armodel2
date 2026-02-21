"""DiagnosticJ1939SpnMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 267)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticJ1939SpnMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sending_node_refs: list[ARRef]
    spn_ref: Optional[ARRef]
    system_signal_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SpnMapping."""
        super().__init__()
        self.sending_node_refs: list[ARRef] = []
        self.spn_ref: Optional[ARRef] = None
        self.system_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939SpnMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939SpnMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sending_node_refs (list to container "SENDING-NODE-REFS")
        if self.sending_node_refs:
            wrapper = ET.Element("SENDING-NODE-REFS")
            for item in self.sending_node_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticJ1939Node")
                if serialized is not None:
                    child_elem = ET.Element("SENDING-NODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize spn_ref
        if self.spn_ref is not None:
            serialized = SerializationHelper.serialize_item(self.spn_ref, "DiagnosticJ1939Spn")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal_ref
        if self.system_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SpnMapping":
        """Deserialize XML element to DiagnosticJ1939SpnMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939SpnMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939SpnMapping, cls).deserialize(element)

        # Parse sending_node_refs (list from container "SENDING-NODE-REFS")
        obj.sending_node_refs = []
        container = SerializationHelper.find_child_element(element, "SENDING-NODE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sending_node_refs.append(child_value)

        # Parse spn_ref
        child = SerializationHelper.find_child_element(element, "SPN-REF")
        if child is not None:
            spn_ref_value = ARRef.deserialize(child)
            obj.spn_ref = spn_ref_value

        # Parse system_signal_ref
        child = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REF")
        if child is not None:
            system_signal_ref_value = ARRef.deserialize(child)
            obj.system_signal_ref = system_signal_ref_value

        return obj



class DiagnosticJ1939SpnMappingBuilder:
    """Builder for DiagnosticJ1939SpnMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SpnMapping = DiagnosticJ1939SpnMapping()

    def build(self) -> DiagnosticJ1939SpnMapping:
        """Build and return DiagnosticJ1939SpnMapping object.

        Returns:
            DiagnosticJ1939SpnMapping instance
        """
        # TODO: Add validation
        return self._obj
