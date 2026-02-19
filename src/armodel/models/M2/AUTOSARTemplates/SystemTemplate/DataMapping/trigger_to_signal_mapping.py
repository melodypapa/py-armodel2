"""TriggerToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 249)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerToSignalMapping(DataMapping):
    """AUTOSAR TriggerToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    system_signal: Optional[SystemSignal]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerToSignalMapping."""
        super().__init__()
        self.system_signal: Optional[SystemSignal] = None
        self.trigger_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize TriggerToSignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TriggerToSignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize system_signal
        if self.system_signal is not None:
            serialized = ARObject._serialize_item(self.system_signal, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = ARObject._serialize_item(self.trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerToSignalMapping":
        """Deserialize XML element to TriggerToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerToSignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TriggerToSignalMapping, cls).deserialize(element)

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



class TriggerToSignalMappingBuilder:
    """Builder for TriggerToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerToSignalMapping = TriggerToSignalMapping()

    def build(self) -> TriggerToSignalMapping:
        """Build and return TriggerToSignalMapping object.

        Returns:
            TriggerToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
