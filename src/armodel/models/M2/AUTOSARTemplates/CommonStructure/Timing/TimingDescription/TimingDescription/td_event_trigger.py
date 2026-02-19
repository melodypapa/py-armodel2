"""TDEventTrigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import (
    TDEventTriggerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TDEventTrigger(TDEventVfbPort):
    """AUTOSAR TDEventTrigger."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    td_event_trigger_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventTrigger."""
        super().__init__()
        self.td_event_trigger_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventTrigger to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventTrigger, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize td_event_trigger_ref
        if self.td_event_trigger_ref is not None:
            serialized = ARObject._serialize_item(self.td_event_trigger_ref, "TDEventTriggerTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TRIGGER")
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
    def deserialize(cls, element: ET.Element) -> "TDEventTrigger":
        """Deserialize XML element to TDEventTrigger object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventTrigger object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventTrigger, cls).deserialize(element)

        # Parse td_event_trigger_ref
        child = ARObject._find_child_element(element, "TD-EVENT-TRIGGER")
        if child is not None:
            td_event_trigger_ref_value = TDEventTriggerTypeEnum.deserialize(child)
            obj.td_event_trigger_ref = td_event_trigger_ref_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



class TDEventTriggerBuilder:
    """Builder for TDEventTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTrigger = TDEventTrigger()

    def build(self) -> TDEventTrigger:
        """Build and return TDEventTrigger object.

        Returns:
            TDEventTrigger instance
        """
        # TODO: Add validation
        return self._obj
