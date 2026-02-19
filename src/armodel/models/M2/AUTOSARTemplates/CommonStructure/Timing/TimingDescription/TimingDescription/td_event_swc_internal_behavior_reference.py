"""TDEventSwcInternalBehaviorReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehaviorReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    referenced_td_event_swc: Optional[TDEventSwc]
    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehaviorReference."""
        super().__init__()
        self.referenced_td_event_swc: Optional[TDEventSwc] = None
    def serialize(self) -> ET.Element:
        """Serialize TDEventSwcInternalBehaviorReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventSwcInternalBehaviorReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize referenced_td_event_swc
        if self.referenced_td_event_swc is not None:
            serialized = ARObject._serialize_item(self.referenced_td_event_swc, "TDEventSwc")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCED-TD-EVENT-SWC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwcInternalBehaviorReference":
        """Deserialize XML element to TDEventSwcInternalBehaviorReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventSwcInternalBehaviorReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventSwcInternalBehaviorReference, cls).deserialize(element)

        # Parse referenced_td_event_swc
        child = ARObject._find_child_element(element, "REFERENCED-TD-EVENT-SWC")
        if child is not None:
            referenced_td_event_swc_value = ARObject._deserialize_by_tag(child, "TDEventSwc")
            obj.referenced_td_event_swc = referenced_td_event_swc_value

        return obj



class TDEventSwcInternalBehaviorReferenceBuilder:
    """Builder for TDEventSwcInternalBehaviorReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwcInternalBehaviorReference = TDEventSwcInternalBehaviorReference()

    def build(self) -> TDEventSwcInternalBehaviorReference:
        """Build and return TDEventSwcInternalBehaviorReference object.

        Returns:
            TDEventSwcInternalBehaviorReference instance
        """
        # TODO: Add validation
        return self._obj
